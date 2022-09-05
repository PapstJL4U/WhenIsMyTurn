"""add all kinds of methods to safe data for use in other pys"""
import pandas as pd

def save(name:str="None", type:str="csv", df:pd.DataFrame=None)->None:
    """save data as either html or csv"""
    if type=="csv":
        df.to_csv(r"csv/"+name+".csv", index=False)
    elif type=="html":
        df.to_html(r"html/"+name+".html")
    elif type=="custom":
        folder = name.split("-")[0]
        na = name.split("-")[-1]
        df.to_csv(folder+r"/"+na+".csv")
    else:
        df.to_clipboard()