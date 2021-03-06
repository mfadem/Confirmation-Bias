"""
Project: Conformation Bias: The news you care about
File: top_stories.py
Author: Michael Fadem
Date: 5/26/19
Language: Python 3.7.3
Purpose: Call the NewsAPI and parse the returned JSON string for all relevant information
Restrictions: None
Steps:
    TODO
"""

# Imports for relevant libraries
import json
from newsapi import *  # NewsAPI key: 803ed7b8cbbf4e9b8b315641f2124c69


"""
Function: TopStories
Class: None
Author: Michael Fadem
Purpose: Page the NewsAPI and parse the JSON returned string 
Restrictions: None
Notes: None
"""
def topStories(newsAPI, source):
    authors = []
    titles = []
    descriptions = []
    urls = []
    images = []
    timeDate = []

    politics = newsAPI.get_top_headlines(sources=source)
    politicsDump = json.dumps(politics)
    parseList = json.loads(politicsDump)

    for title in parseList['articles']:
        #print(title['title'])
        titles.append(title['title'])
    #print(titles)

    for author in parseList['articles']:
        #print(author['author'])
        authors.append(author['author'])
    #print(authors)

    for description in parseList['articles']:
        #print(description['description'])
        descriptions.append(description['description'])
    #print(descriptions)

    for url in parseList['articles']:
        #print(url['url'])
        urls.append(url['url'])
    #print(urls)

    for image in parseList['articles']:
        #print(image['urlToImage'])
        images.append(image['urlToImage'])
    #print(images)

    for published in parseList['articles']:
        #print(published['publishedAt'])
        timeDate.append(published['publishedAt'])
    #print(timeDate)

    return titles, authors, descriptions, urls, images, timeDate


def main():
    newsAPI = NewsApiClient(api_key='803ed7b8cbbf4e9b8b315641f2124c69')
    topStories(newsAPI, 'cnn')

# Program Entry Point
if __name__ == '__main__':
    main()