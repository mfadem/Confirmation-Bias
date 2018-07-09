from bs4 import *
import urllib
import urllib.request
import web_page
import re


def pull_top_stories_CNN():
    url = 'http://www.cnn.com/politics'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), "lxml")
    links = []
    pattern = re.compile(r'\"uri\":\"(.*?)\"')

    prettyHTML = open("prettyHTML.html", 'w+')
    prettyHTML = soup.prettify()
    prettyHTML.close()

    for script in soup.find_all("script", text=pattern):
        match = pattern.findall(script.text)
        if match:
            for i in range(len(match)):
                newURL = url[0:18]+match[i]
                links.append(newURL)
                #print(newURL)

    print(links)

def pull_top_stories_Fox():
    url = 'http://www.foxnews.com/politics.html'
    response = urllib.request.urlopen(url)
    soup = BeautifulSoup(response.read(), "lxml")
    trendingLinks = []

    for link in soup.find_all('a', {'data-omtr-intcmp': lambda L: L and L.startswith('trending')}, href=True):
        trendingLinks.append(link['href'])

    print(trendingLinks)

def main():
    pull_top_stories_CNN()
    pull_top_stories_Fox()
    #web_page.main()

if __name__ == '__main__':
    main()