# Springer's books downloader

## Intro
During the covid-19 lockdowns the Springer released a for free books both in .pdf and .epub format
This tool automatically download these books
https://group.springernature.com/gp/group/media/press-releases/freely-accessible-textbook-initiative-for-educators-and-students/17858180?utm_medium=social&utm_content=organic&utm_source=facebook&utm_campaign=SpringerNature_&sf232256230=1
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

