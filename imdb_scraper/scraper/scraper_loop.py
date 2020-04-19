import pandas as pd
import imdb_scraper.scraper.scraper_serie as sr
import imdb_scraper.metrics.metrics as mt

def crawler(serie):
    current_season = 1
    season_list = [0]
    data_chapt_name_list = []
    data_season_list = []
    data_chapter_rating_list = []
    data_n_of_votes_list = []
    data_air_date_list = []
    data_serial_name_list = []
    index_glob_list = []

    print("Gathering data")

    while current_season == (season_list[0] + 1):
        url = "https://www.imdb.com/title/{}/episodes?season={}".format(serie, current_season)
        chapt_name_list, season_list, chapter_rating_list, n_of_votes_list, air_date_list, serial_name_list, index_list = sr.scrape(url)
        current_season = current_season + 1

        try:
            if current_season == season_list[0] + 1:
                index_glob_list.extend(index_list)
                data_serial_name_list.extend(serial_name_list)
                data_chapt_name_list.extend(chapt_name_list)
                data_season_list.extend(season_list)
                data_chapter_rating_list.extend(chapter_rating_list)
                data_n_of_votes_list.extend(n_of_votes_list)
                data_air_date_list.extend(air_date_list)
        except IndexError:
            break

    print("Generating stadistics")

    ## VOTES METRICS ##
    data_average_votes_list, votes_diff_list, percentile_difference_list, percentile_average_list = mt.get_votes(data_n_of_votes_list, data_chapter_rating_list)

    ## RATING METRICS ##
    data_average_rating_list , rating_difference_list, percentile_raing_difference_list, rating_desviation_from_average_list = mt.get_ratings(data_chapter_rating_list)

    print("Creating Dataframe")

    ## CREATE DATAFRAME ##
    df = pd.DataFrame({

        # BASIC DATA AND INFO
        "serial_name": data_serial_name_list,
        "season": data_season_list,
        "index": index_glob_list,
        "Episode": data_chapt_name_list,
        "air": data_air_date_list,

        # RATING DATA AND METRICS

        "rating": data_chapter_rating_list,
        "average_rating": data_average_rating_list,
        "rating_variation_from_previous": rating_difference_list,
        "%_rating_variation_from_previous": percentile_raing_difference_list,
        "%_rating_desviation_from_av": rating_desviation_from_average_list,

        # VOTE DATA AND METRICS

        "n_of_votes": data_n_of_votes_list,
        "average_vote": data_average_votes_list,
        "votes_variation_from_previous": votes_diff_list,
        "%_votes_variation_from_previous": percentile_difference_list,
        "%_votes_desviation_from_av": percentile_average_list,
    })
    return df


