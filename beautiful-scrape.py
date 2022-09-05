from fileinput import close
import json
import requests
from bs4 import BeautifulSoup
import csv


# url = "https://www.eventbrite.com/d/malaysia--kuala-lumpur--85675181/all-events/"
url = "https://www.eventbrite.com/d/kenya--nairobi/all-events/"

# while True:
#     print('Page {}...'.format(page))
#     soup = BeautifulSoup(requests.get(url, params={'page': page}).content, 'html.parser')
#     b = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))

    # if not b:
    #     break

#     for item in b:
#         print([item['startDate'], item['name'], item['url'], item['offers']['highPrice'], item['location']['name']])

    # page += 1
page = 1
while True:
    with open("details.json", "w") as file_object:
    # with open("data.csv", "w",  encoding='utf-8') as file:
        # csv_file = csv.writer(file)
        # csv_file.writerow( ["Date", "Name", "Price", "Location", "url"] )
        for x in range(1, 20):
            soup = BeautifulSoup(requests.get(url, params={'page': page}).content, 'html.parser')
            b = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
            # print('b', b)
    
            if  len(b) != 0:
                for item in b:
                    finalImg = ''
                    if 'image' in item:
                        finalImg = item['image']
                    else:
                        finalImg = 'https://demofree.sirv.com/nope-not-here.jpg'

                    fData = [item['startDate'], 
                         item['endDate'], 
                         item['name'],
                         item['offers']['highPrice'],
                         item['url'],
                         {"image": finalImg},
                         item['location']['name'],
                         item['location']['address']['addressLocality'],
                         item['location']['address']['addressRegion'], 
                         item['location']['address']['streetAddress'],
                         item['location']['address']['postalCode'],
                         item['location']['geo']['latitude'],
                         item['location']['geo']['longitude'],
                         item['description']]
                    json.dump(item, file_object) 
                page += 1
            else:
                with close():
                    break
                

