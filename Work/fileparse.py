# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename:str, select:list=[], types:list=[], has_headers=False) -> list:
    '''
    Parse a CSV file into a list of records.
    '''
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        if has_headers:
            headers = next(rows)    # Read the files headers
            if not select:
                select = headers
            indices = [headers.index(colname) for colname in select]
            if types:
                try:
                    if len(select) == len(types):
                        return [{colname: func(row[indice]) for colname, indice, func in zip(select, indices, types)} for row in rows if len(row) > 0]
                    else:
                        print('The number of elements given for types is not correct.')
                        return None
                except ValueError as e:
                    print(f'There is a problem with the type of data: {e}') 
            else:
                return [{colname: row[indice] for colname, indice in zip(select, indices)} for row in rows if len(row) > 0]
        else:
            if types:
                return [tuple([func(val) for func, val in zip(types, row)]) for row in rows if len(row) > 0]
            else:
                return [tuple(row) for row in rows if len(row) > 0]
            
        