"""find the data in the website tables"""
from statistics import NormalDist
from bs4 import BeautifulSoup
import pandas as pd
import requests

def find_Moves(website:str):
        text = requests.get(website).text
        soup = BeautifulSoup(text, features='lxml')
        tables = soup.findAll("table", {"class":"cargoDynamicTable display"})
        
        normal_moves_row_caption = tables[0].find("thead").findAll("th")
        normal_data_frame = get_data_frame_from_list(normal_moves_row_caption[1:])

        normal_moves = tables[0].find("tbody").findAll("tr")
        #row = normal_moves.findAll("td")
        breakpoint()
        fill_data_frame(normal_moves[1:],normal_data_frame)
        print(normal_data_frame.columns)
        breakpoint()
        """
        special_moves_row_caption = tables[1].find("thead").findAll("th")
        special_moves = tables[1].find("tbody").findAll("td")
        
        overdrive_moves_row_caption = tables[2].find("thead").findAll("th")
        overdrive_moves = tables[2].find("tbody").findAll("td")
        
        other_moves_row_caption = tables[3].find("thead").findAll("th")
        other_moves = tables[3].find("tbody").findAll("td")
        """
        #test = get_dictionary_from_keys(normal_moves_row_caption[1:])
        
        
        return None

def get_data_frame_from_list(list: list[str])->pd.DataFrame:
    
    col = []
    for entry in list:
        col.append(entry.contents[0])
    return pd.DataFrame(columns=col)

def fill_data_frame(list:list[str], df:pd.DataFrame):
    moves = []
    for entry in list:
        row = BeautifulSoup(entry, 'html.parser')
        for value in row.findAll("td"):
            print(value)
