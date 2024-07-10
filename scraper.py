class Scraper:
    def __init__(self):
        pass

    def scrap_html(self):
        from urllib.request import urlopen
        url = "http://olympus.realpython.org/profiles/aphrodite"
        page = urlopen(url)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        print("parser work done")
        return html
    


