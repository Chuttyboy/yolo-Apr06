import pandas as pd
import _json
import csv
import json

cam_details =  pd.read_csv('output.txt', sep=r'(?:,\s*|^)(?:\d+: \d+x\d+|Done[^)]+\)\s*)',
                 header=None, engine='python', names=(None, 'a', 'b', 'date')).iloc[:, 1:]


cam_details.to_json('file1.json', orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)




               