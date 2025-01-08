## AUTHOR: WILLIAM PONCZAK
## DATE: 1/8/25
## VERSION: 1.0

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#All courses
data = []

# Make the GET request

base_url = requests.get("https://catalog.jmu.edu/content.php?catoid=54&catoid=54&navoid=2887&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D=1#acalog_template_course_filter")
# Print the result of the request
print(base_url)

# Parse the HTML
soup = BeautifulSoup(base_url.content, 'html.parser')

pagination = soup.find_all('aria-label')
print(pagination)



# while True:
   


#     break

















# # Find all of the 'tr' tags:
# tds = soup.find_all('td')



# # Getting the title of the course
# for td in tds:
#     # Find all the tags with a
#     aTags = td.find_all('a')
#     for aTag in aTags:
#         # Get all of the title attributes
#         title = aTag.get('title')

#         #Some titles were None or not course names. Only and all course names have '.'
#         if (title != None):
#             if '.' in title:
#                 #print("Title: ", title.removesuffix('   opens a new window'))
#                 title_data = [title.removesuffix('   opens a new window')]
#                 data.append(title_data)


# with open('JMU_prerequisites.csv', "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# prereq_file_name = "JMU_prerequisites.csv"
# prereq_file_name_no_dupes = "JMU_prerequisites_no_dupes.csv"

# df = pd.read_csv(prereq_file_name, sep="\t or .")
# df.drop_duplicates(subset=None, inplace=True)
# df.to_csv(prereq_file_name_no_dupes, index=False)

# output_file = "JMU_Prereq"

# with open("JMU_prerequisites_no_dupes.csv", 'r') as infile, open(output_file, "w") as outfile:
#     for line in infile:
#         cleaned_line = line.strip()

#         if cleaned_line.startswith('"') and cleaned_line.endswith('"'):
#             cleaned_line = cleaned_line[1:-1]


#         if cleaned_line.startswith('""') and cleaned_line.endswith('""'):
#             cleaned_line = cleaned_line[2:-2]


#         outfile.write(cleaned_line + "\n")



    

# class prerequisites:


#     def __init__(self, courseID):
#         self.courseID = courseID

    
#     def find_prerequisites(courseID):
#         pass