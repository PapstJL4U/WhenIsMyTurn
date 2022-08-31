"""find the data in the website tables"""
from bs4 import BeautifulSoup

def find_Moves(website:str)->list[str]:
    with open(website) as fp:
        soup = BeautifulSoup(fp)