from scraper import Scraper
import re

def main():
    test_url = "http://olympus.realpython.org/profiles/poseidon"
    test_keyword = "title"

    #get html page
    scr = Scraper()
    html = scr.scrap_html(test_url)

    #find keyword
    keyword = test_keyword
    pattern = "<" + test_keyword + ".*?>.*?</" + test_keyword + ".*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    needed_part = match_results.group()
    needed_part = re.sub("<.*?>", "", needed_part) # Remove HTML tags

    print(needed_part)

if __name__ == "__main__":
    main()