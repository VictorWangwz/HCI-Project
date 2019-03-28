__author__ = ' Zhen Wang'

import requests
import pandas as pd
import os
from xlrd import open_workbook

url = "http://localhost:8000/videos/"
file_path = "/Users/zhenwang/Desktop/cpen541/projects/verbs.xlsx"


def create_videos():
    wb = open_workbook(file_path)
    for sheet in wb.sheets():

        number_of_rows = sheet.nrows

        items = {}

        rows = []
        log = []
        for row in range(1, number_of_rows):
            values = []
            for col in range(3):
                value = (sheet.cell(row, col).value)
                try:
                    value = str(int(value))
                except ValueError:
                    pass
                finally:
                    values.append(value)
            if len(values) is not 0:

                data = {
                    "name": values[1],
                    "category": values[0],
                    "url": values[2],
                    "key": values[1]
                }
                r = requests.post(url, data=data)
                if(r.status_code is not 201):
                    log.append({
                        "data": data,
                        "status_code":r.status_code
                    })
            # items[row + 1] = values

        print(log)

create_videos()