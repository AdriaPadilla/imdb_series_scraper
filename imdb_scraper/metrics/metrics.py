import numpy as np
import pandas as pd

first_diff = 0

def get_votes(data_n_of_votes_list, data_chapter_rating_list):
    # RESULT LISTS

    data_average_votes_list = []
    votes_diff_list = []
    percentile_difference_list = []
    percentile_average_list = []

    # Number of VOTES BASIC METRICS
    total_votes = sum(data_n_of_votes_list)
    average_votes = total_votes / len(data_n_of_votes_list)
    average_votes = round(average_votes, 3)
    data_average_votes_list.extend([average_votes] * len(data_n_of_votes_list))

    # Insert "0" in the first episode to avoid Error
    votes_diff_list.append(first_diff)
    percentile_difference_list.append(first_diff)

    # Numerical difference in nº of votes
    votes_diff_list.extend(np.diff(data_n_of_votes_list))

    # Percentual Difference in nº of votes
    for vote_diff, n_of_votes in zip(votes_diff_list[1:], data_n_of_votes_list[:-1]):
        percentile_difference = ((vote_diff / n_of_votes) * 100)
        percentile_difference = round(percentile_difference, 3)
        percentile_difference_list.append(percentile_difference)

    # Percentual desviation in nº of votes for each Episode from all seasons votes Average
    for average, n_of_votes in zip(data_average_votes_list, data_n_of_votes_list):
        difference = n_of_votes - average
        percentual_diff = (difference / average) * 100
        percentual_diff = round(percentual_diff, 3)
        percentile_average_list.append(percentual_diff)

    return data_average_votes_list, votes_diff_list, percentile_difference_list, percentile_average_list


# RATING METRICS
def get_ratings(data_chapter_rating_list):

    rating_difference_list = []
    percentile_raing_difference_list = []
    rating_desviation_from_average_list = []
    data_average_rating_list = []

    # APPEND A "0" In first episode to avoid errors
    rating_difference_list.append(first_diff)
    percentile_raing_difference_list.append(first_diff)

    # Total rating difference between Episodes
    rating_difference_list.extend(np.diff(data_chapter_rating_list))

    # Rating (stars) BASIC METRICS
    total_rating = sum(data_chapter_rating_list)
    average_rating = total_rating / len(data_chapter_rating_list)
    average_rating = round(average_rating, 3)
    data_average_rating_list.extend([average_rating] * len(data_chapter_rating_list))

    # Percentual Difference in rating between Episodes
    for rating_dif, rating in zip(rating_difference_list[1:], data_chapter_rating_list[:-1]):
        rating_percentile_difference = ((rating_dif / rating) * 100)
        rating_percentile_difference = round(rating_percentile_difference, 3)
        percentile_raing_difference_list.append(rating_percentile_difference)

    # Percentual desviation in ratings for each Episode from all seasons rating Average
    for average, ratings in zip(data_average_rating_list, data_chapter_rating_list):
        difference = ratings - average
        percentual_diff = (difference / average) * 100
        percentual_diff = round(percentual_diff, 3)
        rating_desviation_from_average_list.append(percentual_diff)

    return data_average_rating_list, rating_difference_list, percentile_raing_difference_list, rating_desviation_from_average_list
