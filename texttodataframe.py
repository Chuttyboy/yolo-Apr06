import pandas as pd
import _json

cam_details =  pd.read_csv('output.txt', sep=r'(?:,\s*|^)(?:\d+: \d+x\d+|Done[^)]+\)\s*)',
                 header=None, engine='python', names=(None, 'a', 'b', 'date')).iloc[:, 1:]

print(cam_details)

# save_csv = cam_details.to_json('txttocsv.json',index = None)





               