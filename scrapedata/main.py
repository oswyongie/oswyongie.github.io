import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://www.republika.co.id/"
page = requests.get(URL) #mengunduh halaman

soup = BeautifulSoup(page.content, "html.parser") #mengambil kode html


data = []

for obj in soup.find_all("div",class_ = "caption"): 
    temp_tglTerbit = obj.find("div", class_ = 'date')
    temp_Judul = obj.find("h3")
    if temp_Judul != None and temp_tglTerbit != None:
        temp_tglTerbit = temp_tglTerbit.text

        temp_kategori = temp_tglTerbit[0:temp_tglTerbit.find(' -')]
        temp_kategori = temp_kategori.strip()

        temp_tglTerbit = temp_tglTerbit[temp_tglTerbit.find('- ')+2:]
        temp_tglTerbit = temp_tglTerbit.strip()

        temp_Judul = temp_Judul.find("span")
        temp_Judul = temp_Judul.text

        data.append({"judul": temp_Judul, "kategori" : temp_kategori, "waktu_publikasi": temp_tglTerbit,
                     "waktu_scrape": datetime.now().strftime('%a %d %b %Y, %H:%M')})
        
f=open('C:\\Users\\nadia\\OneDrive - Politeknik Negeri Bandung\\sem 2\\proyek\\w4\\oswyongie.github.io\\scrapedata\\headline.json','w')
jdumps=json.dumps(data)
print(data)
f.writelines(jdumps)
f.close()