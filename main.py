"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
from glob import escape
import pprint as pp
import website_fiddling as wf
import dustloop_links as dl
import pandas as pd
import numpy as np

def minus_on_Block(dataframe: pd.DataFrame, type:str="Normals", character:str="Gabriel")->int:
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

def all():
    super_data = np.array([ [0]*3 for i in range(5)])
    #breakpoint()
    for char in dl.characters: 
        temp = np.array(single(char))   
        super_data = np.add(super_data,temp)
    for i in range(5):
        super_data[i][2] = round(super_data[i][0]/super_data[i][1],2) #evalute percentage per type and for the sum
    
    #breakpoint()
    pp.pprint(super_data)

def single(dl_name:str)->list:
    """Get data for a single character"""

    name = dl_name.split("/")[-2] #get name of the character from website string
    normal, specials , overdrives, others = wf.find_Moves(dl_name) #get moves grouped by type
    data = [ [0]*3 for i in range(5)] # create 3x4 array to fill data

    #returns only negative moves or unknown onBlock moves
    data[0][0], data[0][1] = minus_on_Block(normal ,"Normals", name)
    data[1][0], data[1][1] = minus_on_Block(specials ,"Specials", name)
    data[2][0], data[2][1] = minus_on_Block(overdrives ,"Overdrives", name)
    data[3][0], data[3][1] = minus_on_Block(others ,"Other", name)
    
    data[4][0] = sum(col[0] for col in data) #sum of all negative moves
    data[4][1] = sum(col[1] for col in data) #sum of all moves

    for i in range(5):
        data[i][2] = round(data[i][0]/data[i][1],2) #evalute percentage per type and for the sum
    print(name+": Normals === Specials === Overdrives === Other")
    pp.pprint(data)
    
    return data

if __name__ == "__main__":
        #single(dl.Ramlethal)
        all()