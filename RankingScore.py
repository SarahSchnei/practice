###this is a sollution I developed at work to score and rank records for a project, I dummied the sensitive parts

import numpy as np
import pandas as pd


df = pd.read_csv('abc.csv')


df.head()
df.columns
df = df.drop(['ID_NUMBER.1'], axis=1)

df['Score'] = pd.np.where(df.SUMMARY.str.contains('orgname'), 'orgname', pd.np.where(df.SUMMARY.str.contains('xyz'), 'xyz', pd.np.where(df.SUMMARY.str.contains('building'), 'building', 'other')))

df.Score.value_counts()

df['orgname'] = pd.np.where(df.SUMMARY.str.contains('orgname'), '1', '0')
df['xyz'] = pd.np.where(df.SUMMARY.str.contains('xyz'), '1', '0')
df['building'] = pd.np.where(df.SUMMARY.str.contains('building'), '1', '0')
df['lab'] = pd.np.where(df.SUMMARY.str.contains('lab'), '1', '0')
df['COS'] = pd.np.where(df.SUMMARY.str.contains('COS'), '1', '0')
df['DAC'] = pd.np.where(df.SUMMARY.str.contains('DAC'), '1', '0')


def applyfunc(s):
    if s == 'RTG':
        return '3'
    elif s == 'DT':
        return '3'
    elif s == 'AIP?':
        return '2'
    elif s == 'NAP':
        return'1'
    return '0'





df['Seg'] = df['SEGMENT'].apply(applyfunc)




df.columns


df.shape


df.GOLDSeg.value_counts()




def sum_frame_by_column(frame, new_col_name, list_of_cols_to_sum):
    frame[new_col_name] = frame[list_of_cols_to_sum].astype(float).sum(axis=1)
    return(frame)


sum_frame_by_column(df, 'ratingscore', ['orgname', 'xyz', 'building', 'lab', 'COS', 'DAC', 'Seg'])

df.ratingscore.value_counts()

sorteddf = df.sort_values(by=['ratingscore', 'CONTACT_DATE'], ascending=False)

sorted_df = sorteddf.drop_duplicates(subset='SUMMARY', keep='first')

sorted_df.shape

sorted_df.head()

sorted_df.to_csv('new_score_ranked.csv')
