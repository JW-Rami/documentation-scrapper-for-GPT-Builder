import requests
from bs4 import BeautifulSoup

def scrape_nextjs_docs(base_url, file_name):
    with open(file_name, 'w') as file:
        response = requests.get(base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            for link in links:
                href = link['href']
                if href.startswith('/docs'):
                    full_url = f"{base_url.rstrip('/')}{href}"
                    print(full_url, file=file)
        else:
            print('Failed to retrieve the documentation')

base_url = 'https://nextjs.org/'
file_name = 'website_doc_links.txt'
scrape_nextjs_docs(base_url, file_name)
