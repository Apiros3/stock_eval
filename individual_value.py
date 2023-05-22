import requests
from bs4 import BeautifulSoup

def get_vals(id):
    print(f"obtaining stock value for #{id}...")

    with open(f'dataset/value-{id}.csv', 'w') as f:
        for j in range(4) :
            url = f"https://kabutan.jp/stock/kabuka?code={id}&ashi=day&page={j+1}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content,'html.parser')
            value = soup.find_all('tr')
            # value = soup.find_all()
            # value = value[10] + value[12:]
            search = ["time","td","td","td","td","last"]
            # f.write(str(value))

            start = 12
            if (j == 0) :
                start = 11
                value[11] = value[10]
            # print(start)
            for data in value[start:41]:
                tmp = data
                for i in search : 
                    if (i == "last") : 
                        tmp = tmp.findNext('td').findNext('td').findNext('td')
                    else :
                        tmp = tmp.findNext(i)
                    f.write(f"{str(tmp.contents[0].strip())}, ")
                f.write("\n")
            print(f"{25*(j+1)}%...")

        

    print("done!")
