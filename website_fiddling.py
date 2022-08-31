"""find the data in the website tables"""
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp)