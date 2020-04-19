import requests
from bs4 import  BeautifulSoup

def scrape(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    ratings = soup.find_all('div', class_="ipl-rating-star small")
    chap_names = soup.find_all('a', itemprop="name")
    season_n = soup.find_all('h3', itemprop="name")[1]
    serial_name_string = soup.find_all('h3', itemprop="name")[0]
    serial_name = serial_name_string.find('a', itemprop="url").text
    air_dates = soup.find_all('div', class_="airdate")

    chapt_name_list = []
    season_list = []
    chapter_rating_list = []
    n_of_votes_list = []
    air_date_list = []
    serial_name_list = []
    index_list = []

    for rating, chapter, air_date  in zip(ratings, chap_names, air_dates):
        chapter_rating = float(rating.find('span', class_="ipl-rating-star__rating").text)
        total_votes = int(rating.find('span', class_="ipl-rating-star__total-votes").text.strip("(").strip(")").replace(",", ""))
        release_date = air_date.text.strip("\n").strip().lstrip()
        title = chapter.text
        season = int(season_n.text.split()[-1])

        # Append to lists
        serial_name_list.append(serial_name)
        chapt_name_list.append(title)
        season_list.append(season)
        chapter_rating_list.append(chapter_rating)
        n_of_votes_list.append(total_votes)
        air_date_list.append(release_date)

        # Index Num for each Episode
        index = chapt_name_list.index(title)
        index = index + 1
        index_list.append(index)

        print(serial_name + " [" + "season: " + str(season) + "] " + " [" + str(index) + "] " + "On Air Date: " + release_date + "  |  " +  "Title: ", title)


    return chapt_name_list, season_list, chapter_rating_list, n_of_votes_list, air_date_list, serial_name_list, index_list

