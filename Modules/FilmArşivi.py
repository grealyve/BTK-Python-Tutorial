import requests
import json

class Movie:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "e8a9d5f82d78ca210c8076d648685c12"

    def search(self, key):
        response = requests.get(self.api_url+"search/movie?api_key="+self.api_key+"&query="+key+"&page=1")
        return response.json()

    def populer(self):
        response = requests.get(self.api_url+"movie/popular?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()

    def nowPlaying(self):
        response = requests.get(self.api_url+"movie/now_playing?api_key="+self.api_key+"&language=en-US&page=1")
        return response.json()

movie = Movie()

while True:
    secim = input("\n1- Search\n2- Popular Movies\n3- Now Playing\n4- Exit\nSeçiminiz: ")
    if secim == "4":
        break
    else:
        if secim == "1":
            key = input("Search for: ")
            movies = movie.search(key)
            for movie in movies["results"]:
                print(movie["title"])
        elif secim == "2":
            movies = movie.populer()
            for movie in movies["results"]:
                print(movie["title"])
        elif secim == "3":
            movies = movie.nowPlaying()
            for movie in movies["results"]:
                print(movie["title"])
        else:
            print("Yanlış seçim!")