from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request    
import pyexcel
url = "https://www.apple.com/itunes/charts/songs"

#1. Download web page
html = urlopen(url).read().decode('utf-8')

#2. Extract ROI (Regiom of interest)
soup = BeautifulSoup(html, "html.parser")
ul = soup.find("section", "section chart-grid")
li_list = ul.find_all("li")

top_song = []
for li in li_list:
    h3 = li.h3
    h4 = li.h4

    new_dict = {
    "Names" : h3.string,
    "Artists":  h4.string
    }
    top_song.append(new_dict)
    
    
    song_name = h3.string + " " + h4.string
   
pyexcel.save_as(records = top_song, dest_file_name = "topsong.xlsx")

