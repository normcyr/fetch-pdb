#!/usr/bin/python3
from urllib.request import urlopen
from re import match, compile

def downloading(filename):

    with open(filename) as pdb_list:

        for structure in pdb_list:

            if match(pdbPattern, structure):

                pdb_url = base_url + structure[:4]
                out_file_name = structure[:4] + '.pdb'

                with urlopen(pdb_url) as response, open(out_file_name, 'wb') as out_file:

                    data = response.read()
                    out_file.write(data)
                    print('Downloading {} as {}.'.format(structure[:4], out_file_name))

    return(data)

if __name__ == '__main__':

    filename = 'pdblist'
    pdbPattern = compile('\d.{3}')
    base_url = 'http://www.pdb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId='
    data = downloading(filename)
