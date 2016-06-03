soupamd = BeautifulSoup(amd.content) 
products = []

for item in soupamd.select("div.listRow"):
    prodname = item.find("span", class_="name")
    adinfo = item.find("span", class_="additional")
    formfactor, grafisch, socket = item.find_all("span", class_="info")[:3]
    prijs = item.find("span", class_="price")
    products.append({
        'prodname': prodname.text.strip(),
        'adinfo': adinfo.text.strip(),
        'formfactor': formfactor.text.strip(),
        'grafisch': grafisch.text.strip(),
        'socket': socket.text.strip(),
        'prijs': prijs.text.strip(),
    })

with open("mobos.json", "w") as outfile:
    json.dump(products, outfile)