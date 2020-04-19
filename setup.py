import setuptools


setuptools.setup(name='imdb_series_scraper',
      version="1.0.4",
      url = "https://github.com/AdriaPadilla/imdb_series_scraper/", 
      description='scrape IMDB series and create metrics for statistics',
      author='Adrian Padilla',
      author_email='adrian.padilla.m@gmail.com',
      packages=setuptools.find_packages(),
      install_requires=["numpy", "pandas", "requests", "beautifulsoup4", "openpyxl"],
      classifiers=[
       "Programming Language :: Python :: 3",
       "License :: OSI Approved :: MIT License",
       "Operating System :: OS Independent",
       ],
     )
