"""find the +onBlock moves in GG Strive and find the percentage for normals and specials
    to do so we need to scrap dustloop.com for each characters moves and do some math
"""
import website_fiddling as wf
import dustloop_links as dl
import pandas as pd

def minus_on_Block(dataframe: pd.DataFrame, type:str="Normals")->None:
    """Count the moves that are minus on Block"""
    breakpoint()
    minus = dataframe.loc[dataframe['onBlock'].replace(to_replace="-", value=1).astype('int32') < 0]
    minus.to_html("minus.html")

if __name__ == "__main__":
    normal, _, _,_ = wf.find_Moves(dl.I_No)
    minus_on_Block(normal)