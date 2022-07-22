import requests
import tkinter as tk

def getnews():
    api_key = "613806a6a7e24a7ba2b67c3c44bd6b9d"
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + api_key
    news = requests.get(url).json()

    articles = news["articles"]
    my_articles = list()
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ", " + my_articles[i] + "\n"

    label.config(text = my_news)





canvas = tk.Tk()
canvas.geometry("1000x700")
canvas.title("Latest News")

button = tk.Button(canvas, font=24, text="Reload", command = getnews)
button.pack(pady = 20)

label = tk.Label(canvas, font =15, justify = "left")
label.pack(pady =40)

getnews()

canvas.mainloop()
