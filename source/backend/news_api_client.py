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
            print(self.api_key)

        # https://www.reddit.com/r/webdev/comments/a5hdkk/how_should_i_handle_having_api_keys_in_my_app/ebmtcdl?utm_source=share&utm_medium=web2x
        # https://stackoverflow.com/questions/44342276/how-to-push-code-to-github-hiding-the-api-keys
        # https://pypi.org/project/python-dotenv/
        self.api_client = NewsApiClient(api_key=self.api_key)


    # TODO: Need bias and then all sources that correspond
    def topStories(self, source):
        authors = []
        titles = []
        descriptions = []
        urls = []
        images = []
        timeDate = []

        politics = self.api_client.get_top_headlines(sources=source)
        politicsDump = json.dumps(politics)
        parseList = json.loads(politicsDump)
        with open('news.json', 'w') as f:
            f.write(json.dumps(politics, indent=4, sort_keys=True))
        return
        #print(parseList)

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
    storyInstance = NewsStoriesClass("config.json")
    storyInstance.topStories("cnn")

# Program Entry Point
if __name__ == '__main__':
    main()
