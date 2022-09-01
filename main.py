"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
import website_fiddling as wf
import dustloop_links as dl
import pandas as pd

def minus_on_Block(dataframe: pd.DataFrame, type:str="Normals", character:str="Gabriel")->str:
    """Count the moves that are minus on Block"""
    number_of_all_moves = len(dataframe.index)
    minus = dataframe.loc[dataframe['onBlock'].str.startswith("-")] #select moves that are negative or unknown
    number_of_non_plus_mives = len(minus.index)
    percentage =  (number_of_non_plus_mives / number_of_all_moves)*100
    return f"{round(percentage,2)}% of {character} {type} moves are negative on Block({number_of_non_plus_mives}/{number_of_all_moves})."
def all():
    for char in dl.characters:
        name = char.split("/")[-2]
        normal, specials , overdrives, others = wf.find_Moves(char)
        print(minus_on_Block(normal ,"Normals", name))
        print(minus_on_Block(specials ,"Specials", name))
        print(minus_on_Block(overdrives ,"Overdrives", name))
        print(minus_on_Block(others ,"Other", name))

if __name__ == "__main__":
        normal, specials , overdrives, others = wf.find_Moves(dl.Jack_O)
        print(minus_on_Block(normal ,"Normals", name))
        print(minus_on_Block(specials ,"Specials", name))
        print(minus_on_Block(overdrives ,"Overdrives", name))
        print(minus_on_Block(others ,"Other", name))