from google_play_scraper import app
import pandas as pd
import numpy as np


result = app(
    'com.duolingo',
    lang='pt', # defaults to 'en'
    country='br' # defaults to 'us'
)

from google_play_scraper import Sort, reviews_all

result_all_5 = reviews_all(
    'com.duolingo',
    sleep_milliseconds=2000, # defaults to 0
    lang='pt', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=5
)

result_all_4 = reviews_all(
    'com.duolingo',
    sleep_milliseconds=2000, # defaults to 0
    lang='pt', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=4
)

result_all_3 = reviews_all(
    'com.duolingo',
    sleep_milliseconds=2000, # defaults to 0
    lang='pt', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=3
)

result_all_2 = reviews_all(
    'com.duolingo',
    sleep_milliseconds=2000, # defaults to 0
    lang='pt', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=2
)

result_all_1 = reviews_all(
    'com.duolingo',
    sleep_milliseconds=2000, # defaults to 0
    lang='pt', # defaults to 'en'
    country='br', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    filter_score_with=1
)

result_table_5 = pd.DataFrame(result_all_5)
result_table_4 = pd.DataFrame(result_all_4)
result_table_3 = pd.DataFrame(result_all_3)
result_table_2 = pd.DataFrame(result_all_2)
result_table_1 = pd.DataFrame(result_all_1)

result_table = pd.concat([result_table_1, result_table_2, result_table_3, result_table_4, result_table_5])

result_table = result_table[['score', 'content', 'at']]
result_content = result_table[['score', 'content']]

at = np.datetime_as_string(result_table['at'], unit='h')
at = pd.DataFrame(
    data=at
)
at['year'] = at[0].str.split('-').str[0]

result = result_content.merge(at, right_index=True, left_index=True, how='inner')

result.drop(0, axis=1, inplace=True)

result.to_excel('duolingo_data.xlsx') # arquivo final com os dados das reviews do app Duolingo