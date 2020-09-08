import requests
from bs4 import BeautifulSoup

def scrapeHallmark():
    website_url = requests.get('https://en.wikipedia.org/wiki/List_of_Hallmark_Channel_Original_Movies').text
    soup = BeautifulSoup(website_url, 'lxml')
    tables = soup.find_all('table', class_='sortable')
    
    for table in tables:
        titles = table.find_all('tr')
        for title in titles:
            print(title.contents[3].i)
            #print(title.contents[3].a)
            # write a text stripper that slices at > and ends at <
    
        




if __name__ == "__main__":
    scrapeHallmark()
