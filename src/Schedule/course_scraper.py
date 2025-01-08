## AUTHOR: WILLIAM PONCZAK
## DATE: 1/8/25
## VERSION: 1.1

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv


# Make the GET request
base_url = requests.get("https://catalog.jmu.edu/content.php?catoid=54&catoid=54&navoid=2887&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter")

# Parse the HTML
soup = BeautifulSoup(base_url.content, 'html.parser')

# Find all of the 'td' tags:
tds = soup.find_all('td')



data = []
count = 1

def __init__(self, courseID, url):
    self.courseID = courseID
    self.url = url


def find_prerequisites(courseID):
    pass

def next_page():
    count += 1
    insert = str(count)
    result = f"https://catalog.jmu.edu/content.php?catoid=54&catoid=54&navoid=2887&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={insert}#acalog_template_course_filter"
    return result


def update_CSV():
    with open('JMU_Prerequisite_dataset.csv', 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        writer.writerows(data)

    df = pd.read_csv('JMU_Prerequisite_dataset.csv', sep="\t or .")
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv('JMU_Prereq_No_Dupes', index=False)       


def getTitle():
    # Getting the title of the course
    for td in tds:
        # Find all the tags with a
        aTags = td.find_all('a')
        for aTag in aTags:
            # Get all of the title attributes
            title = aTag.get('title')

            #Some titles were None or not course names. Only and all course names have '.'
            if (title != None):
                if '.' in title:
                    #print("Title: ", title.removesuffix('   opens a new window'))
                    title_data = [title.removesuffix('   opens a new window')]
                    data.append(title_data)
    

def get_href():
    pass


def get_courseID():
    pass
