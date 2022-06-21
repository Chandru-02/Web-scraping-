#importing python libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime
import pandas as pd
import csv


def laptop_price():

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

# uploading the prodeuct's URL form the flipkart website!....
    url="https://www.flipkart.com/acer-aspire-7-core-i5-10th-gen-8-gb-512-gb-ssd-windows-10-home-4-graphics-nvidia-geforce-gtx-1650-a715-75g-50ta-a715-75g-41g-a715-75g-52aa-gaming-laptop/p/itm365d5a348ad9c?pid=COMG2KBG2K4GFFF7&lid=LSTCOMG2KBG2K4GFFF75TIZXH&marketplace=FLIPKART&q=acer+aspire+7&store=4rr%2Ftz1&spotlightTagId=BestvalueId_4rr%2Ftz1&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_2_9_na_na_ps&fm=search-autosuggest&iid=02220cb8-60a5-421b-bb4d-f5386102a2ff.COMG2KBG2K4GFFF7.SEARCH&ppt=sp&ppn=sp&ssid=8j7un4sq3k0000001654590960689&qH=8b5d26a924ee876e"



    page = requests.get(url,headers=headers)                       #requesting the UL form the website....
    soup1=BeautifulSoup(page.content, "html.parser")               # Getting the html content form the web page ....
    soup2=BeautifulSoup(soup1.prettify(), "html.parser")           # making the html content in a good manner.....

# scrapingthe required data fromthe web site!!!!!!!!
    name = soup2.find('span',attrs={'class':'B_NuCI'}).get_text()                # Name of the product..
    price=soup2.find('div',attrs={'class':'_30jeq3 _16Jk6d'}).get_text()         # Price of the Product......
    originalprice=soup2.find('div',attrs={'class':'_3I9_wc _2p6lqe'}).get_text()
    ratings=soup2.find('div',attrs={'class':'_3LWZlK'}).get_text()              # Ratings of the product......
    reviews=soup2.find('span',attrs={'class':'_2_R_DZ'}).get_text()             # Total Ratings and Reviews.......
    rateing=ratings.lstrip()
    review=reviews.strip()
    review=review.split()
    if "Ratings" in review:
        review.remove("Ratings")
    if "Reviews" in review:
        review.remove("Reviews")
    review =" ".join(review)



 # removing the new line comment....!!!!!!
    name_separation=list(map(str,name.split()))
    Name=" ".join(name_separation)
    a=list(map(str,originalprice.split()))


# Removing the dollar symbol before the price....!!!!!
    Price=price.strip()[1:]
    OriginalPrice =a[1:]
    OriginalPrice=OriginalPrice[0]
    print(OriginalPrice)


    Date=datetime.date.today()                                               #Importing daily date.......

# Code for finding day for the date.....!!!!!!
    Year,Month,Day=str(Date).split("-")
    year,month,day=int(Year), int(Month),int(Day)
    if month<3:
        month+=12
        year-=1
    result = ((day + (int((13 * (month - 2)) / 5)) + year + (int(year / 4)) - (int(year / 100)) - (int(year / 400))) % 7)+2

    week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    Day=week_days[result%7]


    header = ["Name","Price","MRP", "Date", "Day", "Ratings", "Reviews& ratings"]



# To store the values in desired list........!!!!!!!!!

    data=[Name, Price,OriginalPrice, Date, Day, rateing, review]
    with open('flipkartwebscrap.csv', 'a+', newline="", encoding="UTF8") as f:
        writer=csv.writer(f)
        writer.writerow(data)
while True:
    laptop_price()
    time.sleep(2)                  # For every two seconds the data's are scraped from the website
