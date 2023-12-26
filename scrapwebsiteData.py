import requests
from bs4 import BeautifulSoup

def scrape_content_and_save(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Ceci suppose que vous voulez tout le texte de la page. 
        # Vous devrez peut-être ajuster le sélecteur selon la structure du site.
        text = soup.get_text(separator='\n', strip=True)
        return text
    else:
        print(f"Failed to retrieve content from {url}")
        return ""

# Lisez les liens à partir du fichier et scrapez chaque page
with open('nextjs_doc_links.txt', 'r') as links_file:
    for url in links_file:
        url = url.strip()  # Enlever les espaces blancs et les sauts de ligne
        content = scrape_content_and_save(url)
        # Créer un nom de fichier basé sur l'URL ou un identifiant unique
        filename = url.split('/')[-1] + ".txt"
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
