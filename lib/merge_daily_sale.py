import pandas as pd
import os
import gc
from tqdm import tqdm

def merge_daily_sale(daily_path, sale_path, i):
        df_d = pd.read_csv(daily_path)
        df_s = pd.read_csv(sale_path)
        df = pd.merge(df_s, df_d, on = ['data_date', 'goods_id'], how = 'left')
        df = df.fillna(0)
        df.loc[:, df.columns[3:]] = df.loc[:, df.columns[3:]].round().astype(int)

        if i == 9:
            df.to_csv('test.csv', index = None)
        else:
            df.to_csv('window{}.csv'.format(i), index = None)

def main():

    w1_d = "../goods_daily/window1_daily_1.csv"
    w2_d = "../goods_daily/window2_daily_1.csv"
    w3_d = "../goods_daily/window3_daily_1.csv"
    w4_d = "../goods_daily/window4_daily_1.csv"
    w5_d = "../goods_daily/window5_daily_1.csv"
    w6_d = "../goods_daily/window6_daily_1.csv"
    w7_d = "../goods_daily/window7_daily_1.csv"
    w8_d = "../goods_daily/window8_daily_1.csv"
    test_d = "../goods_daily/test_daily_1.csv"

    w1_s = "../goods_sale/window1_sale_1.csv"
    w2_s = "../goods_sale/window2_sale_1.csv"
    w3_s = "../goods_sale/window3_sale_1.csv"
    w4_s = "../goods_sale/window4_sale_1.csv"
    w5_s = "../goods_sale/window5_sale_1.csv"
    w6_s = "../goods_sale/window6_sale_1.csv"
    w7_s = "../goods_sale/window7_sale_1.csv"
    w8_s = "../goods_sale/window8_sale_1.csv"
    test_s = "../goods_sale/test_sale_1.csv"

    i = 0
    arg1 = [w1_d, w2_d, w3_d, w4_d, w5_d, w6_d, w7_d, w8_d, test_d]
    arg2 = [w1_s, w2_s, w3_s, w4_s, w5_s, w6_s, w7_s, w8_s, test_s]
    for df_d, df_s in tqdm(zip(arg1, arg2)):
        i+=1
        merge_daily_sale(df_d, df_s, i)


if __name__ == '__main__':
    main()
