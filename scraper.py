from urllib.request import urlopen


class Scraper:
    def __init__(self):
        pass


    def scrap_html(self):
        url = "http://olympus.realpython.org/profiles/aphrodite"
        # print(check_url(url))
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print("parser work done")
        return html
    
    def scrap_html(self, url):
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print("parser work done")
        return html
    


