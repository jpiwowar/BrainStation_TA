from bs4 import BeautifulSoup
import gdown 
import re
import requests
import sys 

page_url=''
try:
    page_url = sys.argv[1]
except IndexError:
    print('No URL provided')

page_req=''
print(f'attempting to access {page_url} ')
try:
    page_req=requests.get(page_url, verify=False) # verify=False for demo only
except requests.exceptions.RequestException as e:
    print(f'Error accessing {page_url}:\n {e}')

tomato_basil=BeautifulSoup(page_req.content, features='lxml')

link_filter=re.compile('google.com')
string_filter=re.compile('\S+') #small hack to skip "invisible" links

for anchor in tomato_basil("a", href=link_filter, string=string_filter):
    download_link=anchor.get('href')\
        .replace('file/d/','uc?id=')\
        .replace('/view?usp=sharing','')
    gdown.download(download_link)