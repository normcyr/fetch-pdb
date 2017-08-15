#!/usr/bin/python3
from urllib.request import urlopen
from re import match, compile

def downloading(pdbList):

    with open(pdbList) as myList:

        for structure in myList:

            if match(pdbPattern, structure):

                pdbUrl = baseUrl + structure[:4]
                outFileName = structure[:4] + '.pdb'

                with urlopen(pdbUrl) as response, open(outFileName, 'wb') as outFile:

                    data = response.read()
                    outFile.write(data)
                    print('Downloading {} as {}.'.format(structure[:4], outFileName))

    return(data)

if __name__ == '__main__':

    pdbList = 'pdblist'
    pdbPattern = compile('\d.{3}')
    baseUrl = 'http://www.pdb.org/pdb/download/downloadFile.do?fileFormat=pdb&compression=NO&structureId='
    data = downloading(pdbList)
