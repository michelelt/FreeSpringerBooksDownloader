# Springer's books downloader

## Intro
During the covid-19 lockdown, Springer released for free more than 400 books both in .pdf and .epub format
This tool automatically download those books.
https://www.springernature.com/gp/librarians/news-events/all-news-articles/industry-news-initiatives/free-access-to-textbooks-for-institutions-affected-by-coronaviru/17855960


## Setup
You have to properly fill the config.txt file
- medium_selection: [True,False,bulk]
    - True: the list of downloaded booking refers more on an Machine Learning subsection selected by Medium (https://towardsdatascience.com/springer-has-released-65-machine-learning-and-data-books-for-free-961f8181f189)
    - False: the books selection done according following parameters
    - bulk: downloads all the bookings (14GB)

- keywords_in_title:
    -if medium_selection is False, all the books containing the list of keywords separated by coma are selected

- keywords_in_topic:
    if medium_selection is False, all the books containing the list of keywords separated by coma are selected

-download_formats: [pdf, epub]
    -can be selected both

## Run
    python3 __main__.py

## Thanks
    inspired by https://github.com/alexgand/springer_free_books/blob/master/README.MD

