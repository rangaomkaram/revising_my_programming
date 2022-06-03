# Http Requests
from urllib import response
import requests
from bs4 import BeautifulSoup
import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

now = datetime.datetime.now()

# email content placeholder

content = ' '

# extracting Hacker News Stories

def extract_news(url):
    print('Extracting Hacker News Stories...')
    cnt = " "
    cnt += ('<b>HN Top Stories : <b>\n '+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content,'html.praser')
    for i,tag in enumerate(soup.find_all('td',attrs={'class':'title',}))

