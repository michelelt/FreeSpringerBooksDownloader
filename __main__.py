import sys
sys.path.append('.')
from Classes.BookListFormatter import BookListFormatter
from Classes.Downloader import Downloader
import os
import pandas as pd

if __name__== '__main__':
    data_path = './Data/'
    config_path = './config.txt'
    output_path = './Downloads/'

    if not os.path.isdir(output_path + 'pdf/'): os.mkdir(output_path+'pdf')
    if not os.path.isdir(output_path + 'epub/'): os.mkdir(output_path + 'epub')

    books_db = pd.read_excel(data_path+'BooksDB.xlsx')
    ml_books_db = pd.read_csv(data_path+'MLBooksDB.csv', sep=';')
    
    bcl = BookListFormatter(books_db)
    config = bcl.parse_config(config_path)
    books_to_download = bcl.select_books_to_dl(config_path, ml_books_db)
    list_b2d = bcl.preare_list(output_path)
    
    downloader = Downloader()
    for book in list_b2d:
        downloader.download(book)



