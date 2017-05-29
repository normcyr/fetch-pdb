#!/usr/bin/python3
import urllib.request

def downloading(filename):
    with open(filename) as pdb_list:
        for structure in pdb_list:
            pdb_url = base_url + structure[:4]
            out_file_name = structure[:4] + '.pdb'
            with urllib.request.urlopen(pdb_url) as response, open(out_file_name, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
                print('Downloading {} as {}.'.format(structure[:4], out_file_name))
    return(data)

if __name__ == '__main__':
    filename = 'pdblist'
    base_url = 'http://www.pdb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId='
    data = downloading(filename)
