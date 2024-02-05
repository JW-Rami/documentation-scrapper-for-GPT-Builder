### Setup

### Before begin install dependances:

- `pip install requests`
- `pip install beautifulsoup4`
- `pip install selenium`
- `pip install webdriver-manager`

##### First Step:

- Choose the website url you want to scrap


##### Second Step:

- Run `python scrap.py` in the terminal for getting all the route from the url you want. It will create a folder txt with all the links route


##### Third Step:

- Run `python scrapwebsiteDataSelenium.py` in the terminal for getting all the links you scrapped in nextjs_doc_links.txt. It will create a files for every link you scrapped in the step 2

##### Fourth Step:

- Run `python mergeFiles.py` in the terminal for merge all the files in one file.

