from fileinput import close
import json
import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.eventbrite.com/d/kenya--nairobi/all-events/"

page = 1
while True:
    with open("data.csv", "w",  encoding='utf-8') as file:
        csv_file = csv.writer(file)
        csv_file.writerow( ["StartDate", "EndDate", "Name", "Price" , "URL", "Image", "Location", "Location", "Region", "Street", "postalCode", "Latitude", "Longitude", "Description"] )
        for x in range(1, 20):
            soup = BeautifulSoup(requests.get(url, params={'page': page}).content, 'html.parser')
            b = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
    
            if  len(b) != 0:
                for item in b:
                    finalImg = ''
                    if 'image' in item:
                        finalImg = item['image']
                    else:
                        finalImg = 'https://demofree.sirv.com/nope-not-here.jpg'

                    csv_file.writerow([
                         item['startDate'], 
                         item['endDate'], 
                         item['name'],
                         item['offers']['highPrice'],
                         item['url'],
                         finalImg,
                         item['location']['name'],
                         item['location']['address']['addressLocality'],
                         item['location']['address']['addressRegion'], 
                         item['location']['address']['streetAddress'],
                         item['location']['address']['postalCode'],
                         item['location']['geo']['latitude'],
                         item['location']['geo']['longitude'],
                         item['description']
                    ])
                page += 1
            else:
                with close():
                    break

