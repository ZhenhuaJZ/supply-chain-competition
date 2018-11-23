import pandas as pd
import os
import gc
from tqdm import tqdm

def statics_feats_daily(key, target, version, i, df_path):
        df = pd.read_csv(df_path)
        df_mean = df.groupby(['{}'.format(key)], as_index=False)['{}'.format(target)].mean().rename(columns = {'{}'.format(target) : '{}_{}'.format(target, 'mean')})
        df_min = df.groupby(['{}'.format(key)], as_index=False)['{}'.format(target)].min().rename(columns = {'{}'.format(target) : '{}_{}'.format(target, 'min')})
        df_max = df.groupby(['{}'.format(key)], as_index=False)['{}'.format(target)].max().rename(columns = {'{}'.format(target) : '{}_{}'.format(target, 'max')})
        df_sum = df.groupby(['{}'.format(key)], as_index=False)['{}'.format(target)].sum().rename(columns = {'{}'.format(target) : '{}_{}'.format(target, 'sum')})
        df_count = df.groupby(['{}'.format(key)], as_index=False)['{}'.format(target)].size().to_frame('{}_{}'.format(target, 'count'))
        df_count['{}'.format(key)] = df_count.index

        df1 = pd.merge(df, df_mean, on = '{}'.format(key), how = 'left')
        df2 = pd.merge(df1, df_min, on = '{}'.format(key), how = 'left')
        df3 = pd.merge(df2, df_max, on = '{}'.format(key), how = 'left')
        df4 = pd.merge(df3, df_sum, on = '{}'.format(key), how = 'left')
        df5 = pd.merge(df4, df_count, on = '{}'.format(key), how = 'left')

        if i == 9:
            df5.to_csv('test_daily_{}.csv'.format(version), index = None)
        else:
            df5.to_csv('window{}_daily_{}.csv'.format(i, version), index = None)

def main():

    orign_ver = 1
    w1_d = "window1_daily_1.csv"
    w2_d = "window2_daily_1.csv"
    w3_d = "window3_daily_1.csv"
    w4_d = "window4_daily_1.csv"
    w5_d = "window5_daily_1.csv"
    w6_d = "window6_daily_1.csv"
    w7_d = "window7_daily_1.csv"
    w8_d = "window8_daily_1.csv"
    test_d = "test_daily_1.csv"

    i = 0
    arg = [w1_d, w2_d, w3_d, w4_d, w5_d, w6_d, w7_d, w8_d, test_d]
    for df_path in tqdm(arg):
        i+=1
        statics_feats_daily('goods_id', 'goods_click', orign_ver, i,df_path)



if __name__ == '__main__':
    main()
