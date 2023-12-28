# Concept

I created theses scripts in order to scrapp documentation websites in order to merge all the data into one file and give it like a context for create GPT Builder specialized in specific technos.

## Setup

### First Step:

- Choose the website url you want to scrap


#### Second Step:

- Run `python scrap.py` in the terminal for getting all the route from the url you want. It will create a folder txt with all the links route


#### Third Step:

- Run `python scrapwebsiteDataSelenium.py` in the terminal for getting all the links you scrapped in nextjs_doc_links.txt. It will create a files with websites content for every link you scrapped in the step 2

#### Fourth Step:

- Run `python mergeFiles.py` in the terminal for merge all the files in one file.

