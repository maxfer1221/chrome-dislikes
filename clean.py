import numpy as np
import pandas as pd
import os

for dirname, _, filenames in os.walk('data'):
    # read all relevant tables
    datasets = [pd.read_csv(f"data/{f}") for f in filenames if f.endswith('csv')]

# join tables
df = pd.concat(datasets)

# remove duplicate videos across regions
df.drop_duplicates(subset=['video_id'], inplace=True)

# remove videos with disabled comments (necessary for model)
df.drop(df[df['comments_disabled']].index, inplace=True)
df.drop(df[df['ratings_disabled']].index, inplace=True)


# save file
df.to_csv('data_c/joined_all.csv', index=False)
