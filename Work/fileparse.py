# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select=[], types:list=[], has_headers=True, delimiter =',', silence_errors=False) -> list:
    '''
    Parse a file into a list of records.
    '''
    try:
        some_object_iterator = iter(file)
        if select and not has_headers:
            raise RuntimeError('select argument requieres column headers')
        record = []
        rows = csv.reader(file, delimiter=delimiter)
        if has_headers:
            headers = next(rows)    # Read the files headers
            if not select:
                select = headers
            indices = [headers.index(colname) for colname in select]
            if types:
                if len(select) == len(types):
                    for rowno, row in enumerate(rows, start=1):
                        if len(row) > 0:
                            try:
                                record.append({colname: func(row[indice]) for colname, indice, func in zip(select, indices, types)})
                            except ValueError as e:
                                if not silence_errors:
                                    print(f'Could not convert {row}')
                                    print(f'Row: {rowno}: Reason {e}')
                    return record
                else:
                    print('The number of elements given for types is not correct.')
                    return None
            else:
                return [{colname: row[indice] for colname, indice in zip(select, indices)} for row in rows if len(row) > 0]
        else:
            if types:
                for rowno, row in enumerate(rows, start=1):
                    if len(row) > 0:
                        try:
                            record.append(tuple([func(val) for func, val in zip(types, row)]))
                        except ValueError as e:
                            if not silence_errors:
                                print(f'Could not convert {row}')
                                print(f'Row: {rowno}: Reason {e}') 
                return record
            else:
                return [tuple(row) for row in rows if len(row) > 0]
    except TypeError as te:
        print(f'{file} is not iterable.')
            
        