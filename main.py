"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
import website_fiddling as wf
import dustloop_links as dl
import pandas as pd

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
    data = [[0]*3]*4

    for char in dl.characters:
        name = char.split("/")[-2]
        normal, specials , overdrives, others = wf.find_Moves(char)
        data[0][0], data[0][1] = minus_on_Block(normal ,"Normals", name)
        data[1][0], data[1][1] = minus_on_Block(specials ,"Specials", name)
        data[2][0], data[2][1] = minus_on_Block(overdrives ,"Overdrives", name)
        data[3][0], data[3][1] = minus_on_Block(others ,"Other", name)
        breakpoint()

def single(dl_name:str)->None:
        
    name = dl_name.split("/")[-2]
    normal, specials , overdrives, others = wf.find_Moves(dl_name)
    data = [[0]*3]*4
    breakpoint()
    data[0][0], data[0][1] = minus_on_Block(normal ,"Normals", name)
    data[1][0], data[1][1] = minus_on_Block(specials ,"Specials", name)
    data[2][0], data[2][1] = minus_on_Block(overdrives ,"Overdrives", name)
    data[3][0], data[3][1] = minus_on_Block(others ,"Other", name)
    breakpoint()
    print()

if __name__ == "__main__":
        single(dl.Jack_O)