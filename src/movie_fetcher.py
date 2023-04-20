# import requests
# import re
# import csv
# from bs4 import BeautifulSoup


# def main():
#     Downloading imdb top 250 movie's data
#     url = 'http://www.imdb.com/chart/top'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'lxml')

#     movies = soup.select('td.titleColumn')
#     links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
#     crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
#     ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
#     votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

#     create a empty list for storing
#     movie information
#     list = []

#     Iterating over movies to extract
#     each movie's details
#     for index in range(0, len(movies)):
#         Separating movie into: 'place',
#         'title', 'year'
#         movie_string = movies[index].get_text()
#         movie = (' '.join(movie_string.split()).replace('.', ''))
#         movie_title = movie[len(str(index)) + 1:-7]
#         year = re.search('\((.*?)\)', movie_string).group(1)
#         place = movie[:len(str(index)) - (len(movie))]

#         data = {"movie_title": movie_title,
#                 "year": year,
#                 "place": place,
#                 "star_cast": crew[index],
#                 "rating": ratings[index],
#                 "vote": votes[index],
#                 "link": links[index],
#                 "preference_key": index % 4 + 1}
#         list.append(data)

#     fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
#     with open("movie_results.csv", "w", newline="") as file:
#         writer = csv.DictWriter(file, fieldnames=fields)
#         writer.writeheader()
#         for movie in list:
#             writer.writerow({**movie})


# if __name__ == '__main__':
#     main()
import requests
import re
import csv
from bs4 import BeautifulSoup


class IMDBScraper:
    def __init__(self, url):
        self.url = url
        self.movies = []

    def fetch_data(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        return soup

    def parse_data(self, soup):
        movies = soup.select('td.titleColumn')
        links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
        crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
        ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
        votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

        for index in range(len(movies)):
            movie_string = movies[index].get_text()
            movie = (' '.join(movie_string.split()).replace('.', ''))
            movie_title = movie[len(str(index)) + 1:-7]
            year = re.search('\((.*?)\)', movie_string).group(1)
            place = movie[:len(str(index)) - (len(movie))]

            data = {"movie_title": movie_title,
                    "year": year,
                    "place": place,
                    "star_cast": crew[index],
                    "rating": ratings[index],
                    "vote": votes[index],
                    "link": links[index],
                    "preference_key": index % 4 + 1}
            self.movies.append(data)

    def save_to_csv(self, filename):
        fields = ["preference_key", "movie_title", "star_cast", "rating", "year", "place", "vote", "link"]
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            for movie in self.movies:
                writer.writerow(movie)

    def scrape(self):
        soup = self.fetch_data()
        self.parse_data(soup)


def main():
    imdb_scraper = IMDBScraper('http://www.imdb.com/chart/top')
    imdb_scraper.scrape()
    imdb_scraper.save_to_csv("movie_results.csv")


if __name__ == '__main__':
    main()
