"""find the data in the website tables"""
from statistics import NormalDist
from collections import OrderedDict
from typing import OrderedDict
from bs4 import BeautifulSoup
import requests

def find_Moves(website:str):
        text = requests.get(website).text
        soup = BeautifulSoup(text, features='lxml')
        tables = soup.findAll("table", {"class":"cargoDynamicTable display"})
        normal_moves_row_caption = tables[0].find("thead").findAll("th")
        normal_moves = tables[0].find("tbody").findAll("td")

        print(len(normal_moves))
        print(len(normal_moves_row_caption))
        print(normal_moves_row_caption)
        breakpoint()
        """
        special_moves_row_caption = tables[1].find("thead").find("tr")
        special_moves = tables[1].find("tbody").findAll("tr")
        
        overdrive_moves_row_caption = tables[2].find("thead").find("tr")
        overdrive_moves = tables[2].find("tbody").findAll("tr")
        
        other_moves_row_caption = tables[3].find("thead").find("tr")
        other_moves = tables[3].find("tbody").findAll("tr")
        """
        test = get_dictionary_from_keys(normal_moves_row_caption[1:])
        breakpoint()
        print(test.keys())
        return test


def get_dictionary_from_keys(uncleaned_html):
    my_dic = OrderedDict()
    for key in uncleaned_html:
        breakpoint()
        my_dic.setdefault(key.contents[0], "")

    return my_dic

