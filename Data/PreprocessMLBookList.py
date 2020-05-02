'''
keep the link of ML files
'''


with open('MLBooksDB_raw.csv', 'r') as fp: lines = fp.readlines()
fout = open('MLBooksDB.csv', 'w')
fout.write('title;authors;link\n')
for index,line in enumerate(lines):
    if 'http' in line:
        fout.write('%s;%s;%s\n' %(
            lines[index-2].strip(), lines[index-1].strip(), lines[index].strip())
            )

fout.close()
fp.close()

