import pandas as pd
import os
def get_moves_from_csv(website:str="None")->pd.DataFrame:
    """returns tha moves from locally sourced ingredients, ehm csv"""
    name = website.split("/")[-2]

    for file in os.listdir("csv"):
        if name.lower() in file.lower():
            f = os.path.join("csv", file)
            if "normals" in file.lower():
                normal_data_frame = pd.read_csv(f,dtype=str, sep=",")
            if "specials" in file.lower():
                special_data_frame = pd.read_csv(f,dtype=str, sep=",")
            if "overdrives" in file.lower():
                overdrive_data_frame = pd.read_csv(f,dtype=str, sep=",")
            if "others" in file.lower():
                other_data_frame = pd.read_csv(f,dtype=str, sep=",")
    
    return normal_data_frame, special_data_frame, overdrive_data_frame, other_data_frame

