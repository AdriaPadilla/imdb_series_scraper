# IMDB Series Scraper And Statistics #

[![Anaconda-Server Badge](https://img.shields.io/pypi/v/imdb_scraper.svg)](https://pypi.org/project/imdb_scraper/)

## 1. ¿What's this about? ##

imdb_scraper is a tool build with Python to grab, collect, dowload and explore data from TV serie's and metrics from IMDB. Since IMDB don't have any official API or access method to his data, we use "scraping methods", consisting on read the html code and extract the information we want. 

![Spotixplore graph image](https://raw.githubusercontent.com/AdriaPadilla/imdb_series_scraper/master/imdb_series_scraper/img/graph.jpg)

## 2. ¿What kind of data this tool collect? ##

For each serie, you will get:
- All the episodes, from all seassons, listed by "air date".
- All episode names, and position in each season.
- User's Rating for each episode (IMDB uses "stars", from 1 to 10). 
- Volume of user's votes for each episode
- Metrics:
  - Median rating for each serie.
  - Median volume of votes for each serie.
  - Absolute difference between episode's rating and the inmediately previous episode.
  - Percentual difference between episode's rating and inmediatly previous episode.
  - Absolute difference between episode's vote volume and the inmediately previous episode. 
  - Percentual difference between episode's vote volume and inmediatly previous episode.
  - Episode rating deviation from median.
  - Episode vote volume deviation from median.

## 3. Usage Instructions ##
  
### 3.1. Installation ###

**Option 1:Pip install**

```Terminal
...$: pip install imdb_scraper
````

**Option 2: Hardcode**

Step 1: Clone this repository in your pc
```bash
...$: git clone https://github.com/AdriaPadilla/imdb_scraper.git 
```
Step 2: Access the main folder
```
...$: cd imdb_scraper 
```
Step 3: Execute install
```
...$: /imdb_scraper/python3 setup.py install
```

### 3.2. Command instructions ###

imdb_scraper works with "argparse". To start a capture you'll need a IMDB serie's ID, or a list of them, f.e.:
- This is the url for "The Walking Dead" in IMDB: ***https://www.imdb.com/title/tt1520211/***
                                                                            
- The Serie ID equals to **tt1520211**

In your terminal:
```bash
...$: Python3 -m imdb_scraper.main --ID tt1520211
```
This will capture all episodes from "The Walking Dead" serie.

The same with a list of series:
```bash
...$: Python3 -m imdb_scraper.main --ID tt1520211 anotherID anotherID anotherID
```
Just place the IDs with an spacebar, there's no limitations. The time of execution will increase if you demand a big bunch of series. For big captures, I'll recomend to fragment the capture. 

### 3.3. The Output ###

At the end of the process, you'll obtain a single .xslx format file with all the metrics and data. This file will include all series you demand to capture.

### 3.4. Things for the future ###

- [x] Basic data, metrics and statistics.
- [ ] Functionality to scrape films. <- Working on it.
- [ ] Add more Metrics and Statistics.
- [ ] Add option to output 1 .xlsx file for each serie when capture a list.
