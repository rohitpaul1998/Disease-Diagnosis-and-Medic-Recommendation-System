# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Python Script for scrapping data from  Boston Magzines

#url="https://findmydoctor.mass.gov/"
# url="https://www.zocdoc.com/search?address=Boston%2C+MA&after_5pm=false&before_10am=false&city=Boston&day_filter=AnyDay&dr_specialty=132&filters=%7B%7D&gender=-1&insurance_carrier=&insurance_plan=-1&language=-1&latitude=42.3600825&locationType=placemark&longitude=-71.0588801&offset=0&ppsSelectionId=7ba98268-02aa-4cd1-98ce-d90bcce028c0&reason_visit=162&searchQueryGuid=1c1c1e6f-0afd-49ea-8198-536a2297279e&searchType=specialty&search_query=Allergist+%28Immunologist%29&sees_children=false&sort_type=Default&visitType=inPersonAndVirtualVisits"
#url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=0"
# url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=480"
#url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=442"
#url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=1222"
#url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=1014"
url="https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=540"
response=requests.get(url)
print(response.status_code)
print(url)
len(response.text)
page_contents = response.text

Soup=BeautifulSoup(page_contents,'html.parser')
def get_doctor_titles(Soup):
    selection_class = 'search-listing__title-link'
    doctor_title = Soup.find_all(attrs= {'class': selection_class})
    doctors_titles = []
    for d in doctor_title:
        doctors_titles.append(d.text.strip())
    return doctors_titles

def get_speciality_titles(Soup):
    selection_class1 = 'search-listing__specialty-link'
    speciality_title = Soup.find_all(attrs= {'class': selection_class1})
    specialities_titles = []
    for s in speciality_title:
        specialities_titles.append(s.text.strip())
    return specialities_titles

def get_locations(Soup):
    selection_class2 = 'search-listing__neighbourhood-link'
    location_title = Soup.find_all(attrs= {'class': selection_class2})
    locations = []
    for l in location_title:
        locations.append(l.text.strip())
    return locations

def get_topic_urls(Soup):
    topic_link_tags = Soup.find_all('a', {'class':"search-listing__title-link"})
    topic0_url =  topic_link_tags[0]['href']
    topic_urls = []
    for tag in topic_link_tags:
        topic_urls.append(tag['href'])
    return topic_urls


topics_dict = {
     'doctors': get_doctor_titles(Soup),
     'Specialities': get_speciality_titles(Soup),
     'Locations': get_locations(Soup),
     'Doctor_Urls': get_topic_urls(Soup),

}
#Writing data to csv

print(topics_dict)
topics_df = pd.DataFrame.from_dict(topics_dict)
print(topics_df)
topics_df.to_csv('doctorsdetails.csv')



















