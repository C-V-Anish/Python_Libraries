import requests
from bs4 import BeautifulSoup
import time

print("Enter a skill you are unfamiliar with.")
no_skill = input('>')
print(f'Filtering out {no_skill}....')

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=django&txtLocation=Bengaluru%2F+Bangalore&cboWorkExp1=0').text
    #print(html_text)

    soup = BeautifulSoup(html_text,'lxml')

    jobs = soup.find_all('li',class_ = 'clearfix job-bx wht-shd-bx')
    for job in jobs:
        published_date = soup.find('span',class_='sim-posted').span.text
        if '1' in published_date:
            company_name = job.find('h3',class_= 'joblist-comp-name').text.replace(' ','')
            skills = job.find('span',class_= 'srp-skills').text.replace(' ','')
            job_page = job.header.h2.a['href']
            if no_skill not in skills:
            #print(skills)
                print(f"Job Company:{company_name.strip()}")
                print(f"Job Skills:{skills.strip()}")
                print(f"Job Page:{job_page}")

                print(" ")

if __name__ == '__main__':
    while True:
        find_job()
        min=10
        print(f"Waiting {min} minutes....")
        time.sleep(min*60)



    