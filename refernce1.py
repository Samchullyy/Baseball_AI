import glob
import json
from bs4 import BeautifulSoup

def main():
    data = []
    for filename in glob.iglob('*.html'):
        with open(filename) as f:
            soup = BeautifulSoup(f)

            title = soup.find("span", id="btAsinTitle")
            data.append({
                "title":  title.get_text(),
                "author": title.find_next("a", href=True).get_text(),
                "isbn":   soup.find('b', text='ISBN-10:').next_sibling,
                "weight": soup.find('b', text='Shipping Weight:').next_sibling,
                "price":  soup.findAll('span', {"class":'bb_price'})
            })

    with open("my_output.json", "w") as outf:
        json.dump(data, outf)

main()