# Imports for relevant libraries
import json
from newsapi import NewsApiClient

class NewsStoriesClass:
    def __init__(self, json_file):
        self.api_key = ''
        self.api_client = None

        with open(json_file, 'r') as json_config:
            dict_config = json.load(json_config)
            self.api_key = dict_config["api-key"]
            self.country = dict_config["country"]
            self.language = dict_config["language"]
            self.category = dict_config["category"]
            self.right_sources = dict_config["right-sources"]
            self.left_sources = dict_config["left-sources"]
            self.center_sources = dict_config["center-sources"]

        self.api_client = NewsApiClient(api_key=self.api_key)

    def allSources(self):
        sources = self.api_client.get_sources()
        with open('source/backend/json/sources.json', 'w') as f:
            f.write(json.dumps(sources, indent=4, sort_keys=True))

    # TODO: Need bias and then all sources that correspond
    def topStories(self, source):
        authors = []
        titles = []
        descriptions = []
        urls = []
        images = []
        timeDate = []

        politics = self.api_client.get_top_headlines(sources=source)
        with open('source/backend/json/news.json', 'w') as f:
            f.write(json.dumps(politics, indent=4, sort_keys=True))

        for title in politics['articles']:
            titles.append(title['title'])
        print("titles: ", titles)

        for author in politics['articles']:
            authors.append(author['author'])
        print("authors: ", authors)

        for description in politics['articles']:
            descriptions.append(description['description'])
        print("descriptions: ", descriptions)

        for url in politics['articles']:
            urls.append(url['url'])
        print("urls: ", urls)

        for image in politics['articles']:
            images.append(image['urlToImage'])
        print("images: ", images)

        for published in politics['articles']:
            timeDate.append(published['publishedAt'])
        print("timeDate: ", timeDate)

        return titles, authors, descriptions, urls, images, timeDate


def main():
    newsInstance = NewsStoriesClass("source/backend/json/config.json")
    newsInstance.allSources()
    # newsInstance.everything()
    # newsInstance.topHeadlines()
    newsInstance.topStories("cnn")

# Program Entry Point
if __name__ == '__main__':
    main()
