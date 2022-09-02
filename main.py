"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
from glob import escape
import pprint as pp
from re import M
import website_fiddling as wf
import dustloop_links as dl
import pandas as pd
import numpy as np

def minus_on_Block(dataframe: pd.DataFrame, type:str="None", character:str="None")->int:
    """Count the moves that are minus on Block"""
    number_of_all_moves = len(dataframe.index.to_list())

    if "jack" in character.lower() or "happy" in character.lower(): #jacko/hc exception, because ofcourse there is one in html
        minus = dataframe.loc[dataframe['On-Block'].str.startswith("-")] #select moves that are negative or unknown
    else:
        minus = dataframe.loc[dataframe['onBlock'].str.startswith("-")] #select moves that are negative or unknown
    number_of_non_plus_mives = len(minus.index.to_list())
    percentage =  (number_of_non_plus_mives / number_of_all_moves)*100
    sentence = f"{round(percentage,2)}% of {character} {type} moves are negative on Block({number_of_non_plus_mives}/{number_of_all_moves})."
    return number_of_non_plus_mives, number_of_all_moves

def all()->None:
    #create an array to sum up moves of all characters
    super_data = np.array([ [0.0]*3 for i in range(5)])
    #create an array to only safe extrem cases, i.e character with the highest/lowest amount of moves -onBlock
    extremes = np.array([ [1.0]*4 for i in range(5)])
    
    maximum = "worst"
    for index,char in enumerate(dl.characters): 
        temp = np.array(single(char))
        extremes = find_min_or_max_minus_frames(index, maximum, extremes, temp)
        super_data = np.add(super_data,temp)
    for i in range(5):
        super_data[i][2] = round(super_data[i][0]/super_data[i][1],3) #evalute percentage per type and for the sum
    
    col = ['Moves Minus onBlock', 'All Moves', 'Percentage']
    types= ['Normals', 'Specials', 'Overdrives', 'Other', "Sum"]
    df = pd.DataFrame(super_data, index=types, columns=col)
    df.to_html(r"res/all.html")
    col.insert(0,"Character")
    extr = pd.DataFrame(extremes, index=types, columns=col)
    index_to_name = list(map(dl.name_by_index, extr["Character"]))
    remap = dict(zip(types, index_to_name))
    breakpoint()
    extr["Character"].update(pd.Series(remap))
    extr.to_html(r"res/"+maximum+"_extremes.html")

def single(dl_name:str)->list:
    """Get data for a single character"""

    name = dl_name.split("/")[-2] #get name of the character from website string
    normal, specials , overdrives, others = wf.find_Moves(dl_name) #get moves grouped by type
    data = [ [0.0]*3 for i in range(5)] # create 3x4 array to fill data

    #returns only negative moves or unknown onBlock moves
    data[0][0], data[0][1] = minus_on_Block(normal ,"Normals", name)
    data[1][0], data[1][1] = minus_on_Block(specials ,"Specials", name)
    data[2][0], data[2][1] = minus_on_Block(overdrives ,"Overdrives", name)
    data[3][0], data[3][1] = minus_on_Block(others ,"Other", name)
    
    data[4][0] = sum(col[0] for col in data) #sum of all negative moves
    data[4][1] = sum(col[1] for col in data) #sum of all moves

    for i in range(5):
        data[i][2] = round(data[i][0]/data[i][1],3) #evalute percentage per type and for the sum
    print(name+": Normals === Specials === Overdrives === Other")
    pp.pprint(data)
    
    return data

def find_min_or_max_minus_frames(name_index:int=0, char:str="+", extremes:np.array=None, new:np.array=None)->np.array:
    """returns the data with
    better (char:+) aka less % 
    or worse (char:-) aka more % minus frames"""
    #breakpoint()
    for i in range(5):
        #breakpoint()
        if char=="best":
            extremes[i][1:] = extremes[i][1:] if extremes[i][3]<new[i][2] else new[i][:]
            extremes[i][0] = extremes[i][0] if extremes[i][3]<new[i][2] else name_index
        elif char=="worst":
            extremes[i][1:] = extremes[i][1:] if extremes[i][3]>new[i][2] else new[i][:]
            extremes[i][0] = extremes[i][0] if extremes[i][3]>new[i][2] else name_index          
        else:
            print("'char' should be 'best' or 'worst'.")
            raise ValueError

    return extremes

if __name__ == "__main__":
        #single(dl.Ramlethal)
        all()