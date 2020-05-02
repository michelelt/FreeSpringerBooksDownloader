import os
import warnings
warnings.simplefilter(action='ignore')

import pandas as pd


class BookListFormatter:

    def __init__(self, books_db):
        self.books_db = books_db
        self.config = None
        self.b2d = None

    def parse_medium_selection(self, line):
        line = line.upper().lower().strip()
        key, value = [x for x in line.split('=')]
        if value == 'false': value=False
        elif value == 'true': value=True
        else:value=None

        return key, value

    def parse_keywords(self, line):
        line = line.upper().lower().strip()
        key, value = [x for x in line.split('=')]
        if ',' in value:
            value = value.split(',')
        return key, value

    def parse_download_fromat(self, line):
        line = line.upper().lower().strip()
        key, value = [x for x in line.split('=')]

        if len(value)==0:value=['pdf']
        if len(value)==1:value=[value]
        if ',' in value:
            value= value.split(',')

        out_value=[]
        for v in value:
            if v in ['epub', 'pdf']:
                out_value.append(v)

        value = list(set(out_value))
        return key, value


    def parse_config(self, config_file_path):
        fp=open(config_file_path, 'r')
        config_lines = fp.readlines()

        config={}
        for line in config_lines:
            if 'medium' in line:
                key, value = self.parse_medium_selection(line)
                config[key] = value
            elif 'keyword' in line:
                key, value = self.parse_keywords(line)
                config[key] = value
            elif 'formats' in line:
                key, value = self.parse_download_fromat(line)
                config[key] = value
            else:
                continue

        self.config = config
        return config


    def make_title(self, books_to_donwload):

        books_to_donwload.loc[:,'Year'] = books_to_donwload.Edition.str[-4:]

        books_to_donwload['DL_Title'] = books_to_donwload['Book Title'].str.replace(' ', '_')
        books_to_donwload['DL_Title'] = books_to_donwload['Year'] + '_' + books_to_donwload['DL_Title']
        books_to_donwload['DOI_A'] = books_to_donwload['DOI URL'].str.split('/').str[3]
        books_to_donwload['DOI_B'] = books_to_donwload['DOI URL'].str.split('/').str[4]
        books_to_donwload['OpenURL_old'] = books_to_donwload['OpenURL']

        books_to_donwload['OpenURL'] = 'https://link.springer.com/book/'+books_to_donwload['DOI_A']+'%2F'+books_to_donwload['DOI_B']

        return books_to_donwload


    def select_books_to_dl(self, config, ml_db=None):
        if os.path.isfile(str(config)):
            self.parse_config(config)

        if self.config['medium_selection'] == True:
            if isinstance(ml_db, pd.DataFrame):
                books_to_download = self.books_db[self.books_db['OpenURL'].isin(ml_db.link.tolist())]
                books_to_download = self.make_title(books_to_download)
            else:
                print ('Invalid Machine Learning database')
                return None

        ### Select books subsets by title_keywords OR topic Keywords
        elif self.config['medium_selection'] == False:
            books_to_download = self.books_db[
                (self.books_db['Subject Classification'].str.contains(config['keywords_in_topic'])) |
                (self.books_db['Book Title'].str.contains(config['keywords_in_title']))
            ]
            books_to_download = self.make_title(books_to_download)


        elif self.config['medium_selection'] == 'bulk':
            books_to_download = self.books_db
            books_to_download = self.make_title(books_to_download)

        else:
            books_to_download = None

        self.b2d = books_to_download
        return books_to_download


    def preare_list(self, output_path):

        out_list=[]
        if not isinstance(self.b2d, pd.DataFrame):
            print('Impossible create list')
            return out_list

        for dl_type in self.config['download_formats']:
            for index,row in self.b2d.iterrows():
                out_list.append(
                    dict(url=row['OpenURL'],
                         type=dl_type,
                         output_path=output_path+dl_type+'/',
                         title=row['DL_Title']+'.'+dl_type
                     )
                )

        return out_list























