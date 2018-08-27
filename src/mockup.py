import webbrowser
from top_stories import *
from tkinter import *
from urllib.request import *
from PIL import ImageTk, Image
import io


class MockUp:
    def __init__(self, master):

        self.bias = "Independent"

        self.master = master
        self.label = Label(master, text="Bias: Independent", bg="white", justify=CENTER)
        self.label.pack()

        self.scale = Scale(master, from_=-60, to=60, orient=HORIZONTAL, bg="white", length=500,
                           tickinterval=20, command=self.Bias)
        self.scale.pack()

        self.pop = Button(master, text="Top Stories", command=self.Populate)
        self.pop.pack()

    def Bias(self, arg):
        if self.scale.get() == 0:
            self.label.config(text="Bias: Independent")
            self.bias = "Independent"
        if self.scale.get() >= 20:
            self.label.config(text="Bias: Moderate Republican")
            self.bias = "Moderate Republican"
        if self.scale.get() >= 40:
            self.label.config(text="Bias: Republican")
            self.bias = "Republican"
        if self.scale.get() >= 60:
            self.label.config(text="Bias: Far Right")
            self.bias = "Far Right"
        if self.scale.get() <= -20:
            self.label.config(text="Bias: Moderate Democrat")
            self.bias = "Moderate Democrat"
        if self.scale.get() <= -40:
            self.label.config(text="Bias: Democrat")
            self.bias = "Democrat"
        if self.scale.get() <= -60:
            self.label.config(text="Bias: Far Left")
            self.bias = "Far Left"

    def Populate(self):
        authors = []
        titles = []
        descriptions = []
        urls = []
        images = []
        timeDate = []
        newsAPI = NewsApiClient(api_key='803ed7b8cbbf4e9b8b315641f2124c69')
        if self.bias == 'Independent':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'associated-press')
        if self.bias == 'Moderate Republican':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'the-wall-street-journal')
        if self.bias == 'Republican"':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'fox-news')
        if self.bias == 'Far Right':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'breitbart-news')
        if self.bias == 'Moderate Democrat':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'bbc-news')
        if self.bias == 'Democrat':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'cnn')
        if self.bias == 'Far Left':
            titles, authors, descriptions, urls, images, timeDate = topStories(newsAPI, 'the-huffington-post')

        for results in range(len(titles)):
            label = Label(self.master, text=titles[results], bg='white', font='Arial 14 bold')
            label.pack()

            label = Label(self.master, text="Author(s): " + authors[results] + " Published: " + timeDate[results], bg='white')
            label.pack()

            if images[results] is not '':
                image_url = images[results]
                image_read = requests.get(image_url)
                image_data = Image.open(io.BytesIO(image_read.content))
                image_data = image_data.resize((500, 250), Image.ANTIALIAS)
                photo = ImageTk.PhotoImage(image_data)
                image = Label(self.master, image=photo, bg="white")
                image.image = photo
                image.pack()

            body = Label(self.master, text=descriptions[results], wraplength=300, bg='white', justify=CENTER)
            body.pack()

            link = Label(self.master, text=urls[results], bg='white', fg='blue', cursor='hand2')
            link.pack()
            link.bind('<Button-1>', self.Hyperlink)

    def Hyperlink(self, url):
        #print(url.widget.cget("text"))
        webbrowser.open(url.widget.cget("text"))

def main():
    root = Tk()
    root.title("Confirmation Bias")
    root.geometry("700x500")
    root.resizable(width=True, height=True)
    root.configure(background="white")
    GUI = MockUp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
