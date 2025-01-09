## AUTHOR: WILLIAM PONCZAK
## DATE: 1/8/25
## VERSION: 2.1

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

def find_prerequisites(courseID):
    pass

def get_next_page_url():
    count += 1
    insert = str(count)
    result = f"https://catalog.jmu.edu/content.php?catoid=54&catoid=54&navoid=2887&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={insert}#acalog_template_course_filter"
    return result

#Update method to use pandas
def update_CSV(from_filename, to_filename):
    with open(from_filename, 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE)
        writer.writerows(data)

    df = pd.read_csv(from_filename, sep="\t or .")
    df.drop_duplicates(subset=None, inplace=True)
    df.to_csv(to_filename, index=False)       

def extract_course_title(tds):
    titles = []
    # Getting the title of the course
    for td in tds:
        # Find all the tags with a
        aTags = td.find_all('a')
        for aTag in aTags:
            # Get all of the title attributes
            title = aTag.get('title')
            if title:
                titles.append(title)
    return titles
        
def get_href():
    pass

def get_courseID():
    pass

def append_title_to_data(title):
    #Some titles were None or not course names. Only and all course names have '.'
    if (title != None):
        if '.' in title:
            #print("Title: ", title.removesuffix('   opens a new window'))
            title_data = [title.removesuffix('   opens a new window')]
            data.append(title_data)
