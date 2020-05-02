import requests
import os

class Downloader:
    def __init__(self):
        pass



    def download(self, book):



        url=book['url']
        out_type = book['type']
        outpath=book['output_path']
        title=book['title']

        if out_type == 'pdf':
            new_url = url.replace('book', 'content/pdf')
            new_url = new_url+'.pdf'
        if out_type == 'epub':
            new_url = url.replace('book', 'download/epub')
            new_url = new_url+'.epub'

        print('Download of ' + title[0:15] + '... .' + out_type, 'started.')
        myfile = requests.get(new_url)
        if myfile.status_code == 200:

            open(outpath+title, 'wb').write(myfile.content)
            print(title[0:15]+'... .'+out_type, 'Properly Downloaded!')
            print()
        else:
            print(title[0:15]+'... .'+out_type, 'NOT Downloaded!')
            print('http return code:', myfile.status_code )
            print()
