#Import necessary modules
import requests
from bs4 import BeautifulSoup
import array as arr
import json

#Iterate pages 
for pgno in range(21,31):
    
    # print("page no" + str(pgno))
    
    url = "https://swadesii.com/collections/skin-and-personal-care?page=" + str(pgno)

    web = requests.get(url)

    soup = BeautifulSoup(web.content, "html.parser")

    product_cards = soup.find_all("product-card")

    for l in product_cards:

        img = l.find_all("img")
        
        main = l.find_all("main")
        main_a = main[0].find("a")
        a_link = "https://swadesii.com" + main_a.get('href')
        pagecontent = requests.get(a_link)
        content_soup = BeautifulSoup(pagecontent.content, "html.parser")
        description_element = content_soup.find(attrs={'class':'product-description-desktop'})
        product_dscription = str(description_element.text)
        
        main_price = main[0].find("price-item")

        # print(img[0].get("data-srcset"))
        # print(main_a.text)
        # print(main_price.text)

        datastr = main_a.text+"~"+main_price.text+"~"+img[0].get("data-srcset")+"~"+product_dscription.replace("\n", "\t")

        print(datastr)
