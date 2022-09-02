"""find the data in the website tables"""
from statistics import NormalDist
from bs4 import BeautifulSoup
import pandas as pd
import requests

def find_Moves(website:str)->pd.DataFrame:
        """opens the full framedata website and finds normals, specials, overdrives and other moves"""

        try:
        #load website and find the 4 tables
            text = requests.get(website).text
        except:
            raise
        soup = BeautifulSoup(text, features='lxml')
        tables = soup.findAll("table", {"class":"cargoDynamicTable display"})
        
        #find the column names of normal moves
        normal_moves_row_caption = tables[0].find("thead").findAll("th")
        normal_data_frame = get_data_frame_from_list(normal_moves_row_caption[1:])
        
        #find the data of every move and fill the data in the dataframe
        normal_moves = tables[0].find("tbody").findAll("tr")
        normal_data_frame= fill_data_frame(normal_moves,normal_data_frame)

        #Do the same for the other tables
        special_moves_row_caption = tables[1].find("thead").findAll("th")
        special_data_frame = get_data_frame_from_list(special_moves_row_caption[1:])
        special_moves = tables[1].find("tbody").findAll("tr")
        special_data_frame= fill_data_frame(special_moves,special_data_frame)
        
        overdrive_moves_row_caption = tables[2].find("thead").findAll("th")
        overdrive_data_frame = get_data_frame_from_list(overdrive_moves_row_caption[1:])
        overdrive_moves = tables[2].find("tbody").findAll("tr")
        overdrive_data_frame= fill_data_frame(overdrive_moves,overdrive_data_frame)

        other_moves_row_caption = tables[3].find("thead").findAll("th")
        other_data_frame = get_data_frame_from_list(other_moves_row_caption[1:])
        other_moves = tables[3].find("tbody").findAll("tr")
        other_data_frame= fill_data_frame(other_moves,other_data_frame)
        
        name = website.split("/")[-2]
        try:
            save(name+"_normals", "csv", normal_data_frame)
            save(name+"_specials", "csv", special_data_frame)
            save(name+"_overdrives", "csv", overdrive_data_frame)
            save(name+"_others", "csv", other_data_frame)
        except Exception:
            print(Exception)
        return normal_data_frame, special_data_frame, overdrive_data_frame, other_data_frame

def get_data_frame_from_list(list: list[str])->pd.DataFrame:
    """build a list of column names and generate an empty dataframe"""
    col = []
    for entry in list:
        col.append(entry.contents[0])
    return pd.DataFrame(columns=col)

def fill_data_frame(list:list[str], df:pd.DataFrame)->pd.DataFrame:
    """use the list of moves (still in html) and fill the data frame with one move per row"""
    moves = []
    for row in list:
        move = []
        for i,value in enumerate(row.findAll("td")):
            if len(value) == 2:
                value = value[1]
            if len(value.contents)>0:
                if value.contents[0]=="~" or \
                    value.contents[0]=="N/A" or \
                    value.contents[0]=="NA" or \
                    value.contents[0]=="n/a":
                    move.append("var")
                else:
                    move.append(strip_wn(str(value.contents[0])))
            elif i>0:
                move.append("no data")
        moves.append(move)

    return pd.DataFrame(moves, columns=df.columns)

def strip_wn(value:str):
    return value.strip("\n").strip(" ").strip("\n").strip(" ")

def save(name:str="None", type:str="csv", df:pd.DataFrame=None)->None:
    if type=="csv":
        df.to_csv(r"csv/"+name+".csv", index=False)
    elif type=="html":
        df.to_html(r"html/"+name+".html")
    else:
        df.to_clipboard()
