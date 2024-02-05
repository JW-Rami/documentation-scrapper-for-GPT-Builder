from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

def scrape_content_and_save(url, driver):
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text(separator='\n', strip=True)
    return text

# Assurez-vous que le dossier 'data' existe
os.makedirs('data', exist_ok=True)

# Initialisez le WebDriver de Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Lisez les liens à partir du fichier et scrapez chaque page
with open('website_doc_links.txt', 'r') as links_file:
    for url in links_file:
        url = url.strip()  # Enlever les espaces blancs et les sauts de ligne
        content = scrape_content_and_save(url, driver)
        # Créer un nom de fichier basé sur l'URL ou un identifiant unique et enregistrez dans le dossier 'data'
        filename = os.path.join('data', url.split('/')[-1] + ".txt")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)

driver.quit()  # Fermez le navigateur après avoir terminé
