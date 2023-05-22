import requests
from bs4 import BeautifulSoup

def get_vals():
    print("obtaining general stock values...")

    with open('dataset/value-list.csv', 'w') as f:

        for i in range(5) :
            url = f""
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')
            value = soup.find_all('tr', {"class": "tr2"})
            # f.write(str(value))     

            for stock in value :
                tmp = stock.findNext('a')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('a')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('div')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('div')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('div')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('span').findNext('span')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('span').findNext('span')
                f.write(f"{str(tmp.contents[0])}, ")
                tmp = tmp.findNext('div')
                f.write(f"{str(tmp.contents[0])}, ")
                
                f.write("\n")   



    print("done!")
