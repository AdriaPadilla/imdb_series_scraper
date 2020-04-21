import pandas as pd
import imdb_scraper.scraper.scraper_loop as sc
import argparse
import datetime

# series = ["tt0182576", "tt0096697"]

time = datetime.datetime.now()


def main(series):
    df_all = pd.DataFrame()
    for serie in series:
        the_data_df = sc.crawler(serie)
        df_all = pd.concat([df_all, the_data_df], axis=0)
    # df_all.to_excel(output)
    return df_all

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Scrape series from IMDB')
    parser.add_argument('--id', type=str, nargs="+", help='serie id on IMDB')
    args = parser.parse_args()
    ids = args.id
    main(ids)
