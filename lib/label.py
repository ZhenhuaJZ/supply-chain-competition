import pandas as pd
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

w1 = "window1.csv"
w2 = "window2.csv"
w3 = "window3.csv"
w4 = "window4.csv"
w5 = "window5.csv"
w6 = "window6.csv"
w7 = "window7.csv"
w8 = "window8.csv"
test = "test.csv"

dataset = '../raw_data'
goodsale = os.path.join(dataset, 'goodsale.csv') #(7325028, 6)

def merge_label(window, week_label):
    window = pd.read_csv(window)
    df = pd.merge(window, week_label, on="sku_id")
    return df

def main():

    df = pd.read_csv(goodsale)

    label1 = df[(df.data_date >= '2017-09-15') & (df.data_date <= '2017-10-19')][['data_date', 'sku_id', 'goods_num']]
    label2 = df[(df.data_date >= '2017-09-22') & (df.data_date <= '2017-10-26')][['data_date', 'sku_id', 'goods_num']]
    label3 = df[(df.data_date >= '2017-09-29') & (df.data_date <= '2017-11-02')][['data_date', 'sku_id', 'goods_num']]
    label4 = df[(df.data_date >= '2017-10-06') & (df.data_date <= '2017-11-09')][['data_date', 'sku_id', 'goods_num']]
    label5 = df[(df.data_date >= '2017-12-04') & (df.data_date <= '2018-01-07')][['data_date', 'sku_id', 'goods_num']]
    label6 = df[(df.data_date >= '2017-12-11') & (df.data_date <= '2018-01-14')][['data_date', 'sku_id', 'goods_num']]
    label7 = df[(df.data_date >= '2017-12-18') & (df.data_date <= '2018-01-21')][['data_date', 'sku_id', 'goods_num']]
    label8 = df[(df.data_date >= '2017-12-25') & (df.data_date <= '2018-01-28')][['data_date', 'sku_id', 'goods_num']]

    l1_w1 = label1[(label1.data_date >= '2017-09-15') & (label1.data_date <= '2017-09-21')]
    l1_w2 = label1[(label1.data_date >= '2017-09-22') & (label1.data_date <= '2017-09-28')]
    l1_w3 = label1[(label1.data_date >= '2017-09-29') & (label1.data_date <= '2017-10-05')]
    l1_w4 = label1[(label1.data_date >= '2017-10-06') & (label1.data_date <= '2017-10-12')]
    l1_w5 = label1[(label1.data_date >= '2017-10-13') & (label1.data_date <= '2017-10-19')]

    l2_w1 = label2[(label2.data_date >= '2017-09-22') & (label2.data_date <= '2017-09-28')]
    l2_w2 = label2[(label2.data_date >= '2017-09-29') & (label2.data_date <= '2017-10-05')]
    l2_w3 = label2[(label2.data_date >= '2017-10-06') & (label2.data_date <= '2017-10-12')]
    l2_w4 = label2[(label2.data_date >= '2017-10-13') & (label2.data_date <= '2017-10-19')]
    l2_w5 = label2[(label2.data_date >= '2017-10-20') & (label2.data_date <= '2017-10-26')]

    l3_w1 = label3[(label3.data_date >= '2017-09-29') & (label3.data_date <= '2017-10-05')]
    l3_w2 = label3[(label3.data_date >= '2017-10-06') & (label3.data_date <= '2017-10-12')]
    l3_w3 = label3[(label3.data_date >= '2017-10-13') & (label3.data_date <= '2017-10-19')]
    l3_w4 = label3[(label3.data_date >= '2017-10-20') & (label3.data_date <= '2017-10-26')]
    l3_w5 = label3[(label3.data_date >= '2017-10-27') & (label3.data_date <= '2017-11-02')]

    l4_w1 = label4[(label4.data_date >= '2017-10-06') & (label4.data_date <= '2017-10-12')]
    l4_w2 = label4[(label4.data_date >= '2017-10-13') & (label4.data_date <= '2017-10-19')]
    l4_w3 = label4[(label4.data_date >= '2017-10-20') & (label4.data_date <= '2017-10-26')]
    l4_w4 = label4[(label4.data_date >= '2017-10-27') & (label4.data_date <= '2017-11-02')]
    l4_w5 = label4[(label4.data_date >= '2017-11-03') & (label4.data_date <= '2017-11-09')]

    l5_w1 = label5[(label5.data_date >= '2017-12-04') & (label5.data_date <= '2017-12-10')]
    l5_w2 = label5[(label5.data_date >= '2017-12-11') & (label5.data_date <= '2017-12-17')]
    l5_w3 = label5[(label5.data_date >= '2017-12-18') & (label5.data_date <= '2017-12-24')]
    l5_w4 = label5[(label5.data_date >= '2017-12-25') & (label5.data_date <= '2017-12-31')]
    l5_w5 = label5[(label5.data_date >= '2018-01-01') & (label5.data_date <= '2018-01-07')]

    l6_w1 = label6[(label6.data_date >= '2017-12-11') & (label6.data_date <= '2017-12-17')]
    l6_w2 = label6[(label6.data_date >= '2017-12-18') & (label6.data_date <= '2017-12-24')]
    l6_w3 = label6[(label6.data_date >= '2017-12-25') & (label6.data_date <= '2017-12-31')]
    l6_w4 = label6[(label6.data_date >= '2018-01-01') & (label6.data_date <= '2018-01-07')]
    l6_w5 = label6[(label6.data_date >= '2018-01-08') & (label6.data_date <= '2018-01-14')]

    l7_w1 = label7[(label7.data_date >= '2017-12-18') & (label7.data_date <= '2017-12-24')]
    l7_w2 = label7[(label7.data_date >= '2017-12-25') & (label7.data_date <= '2017-12-31')]
    l7_w3 = label7[(label7.data_date >= '2018-01-01') & (label7.data_date <= '2018-01-07')]
    l7_w4 = label7[(label7.data_date >= '2018-01-08') & (label7.data_date <= '2018-01-14')]
    l7_w5 = label7[(label7.data_date >= '2018-01-15') & (label7.data_date <= '2018-01-21')]

    l8_w1 = label8[(label8.data_date >= '2017-12-25') & (label8.data_date <= '2017-12-31')]
    l8_w2 = label8[(label8.data_date >= '2018-01-01') & (label8.data_date <= '2018-01-07')]
    l8_w3 = label8[(label8.data_date >= '2018-01-08') & (label8.data_date <= '2018-01-14')]
    l8_w4 = label8[(label8.data_date >= '2018-01-15') & (label8.data_date <= '2018-01-21')]
    l8_w5 = label8[(label8.data_date >= '2018-01-22') & (label8.data_date <= '2018-01-28')]

    _l1_w1 = l1_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l1_w2 = l1_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l1_w3 = l1_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l1_w4 = l1_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l1_w5 = l1_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l2_w1 = l2_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l2_w2 = l2_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l2_w3 = l2_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l2_w4 = l2_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l2_w5 = l2_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l3_w1 = l3_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l3_w2 = l3_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l3_w3 = l3_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l3_w4 = l3_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l3_w5 = l3_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l4_w1 = l4_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l4_w2 = l4_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l4_w3 = l4_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l4_w4 = l4_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l4_w5 = l4_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l5_w1 = l5_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l5_w2 = l5_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l5_w3 = l5_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l5_w4 = l5_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l5_w5 = l5_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l6_w1 = l6_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l6_w2 = l6_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l6_w3 = l6_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l6_w4 = l6_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l6_w5 = l6_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l7_w1 = l7_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l7_w2 = l7_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l7_w3 = l7_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l7_w4 = l7_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l7_w5 = l7_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

    _l8_w1 = l8_w1.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l8_w2 = l8_w2.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l8_w3 = l8_w3.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l8_w4 = l8_w4.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})
    _l8_w5 = l8_w5.groupby(["sku_id"], as_index=False)["goods_num"].sum().rename(columns={'goods_num': 'label'})

#############################################################################################################
    # #all data
    # windows = [w1, w2, w3, w4, w5, w6, w7, w8] #8 windows
    # week1 = [_l1_w1, _l2_w1, _l3_w1, _l4_w1, _l5_w1, _l6_w1, _l7_w1, _l8_w1] #  week1 label
    # week2 = [_l1_w2, _l2_w2, _l3_w2, _l4_w2, _l5_w2, _l6_w2, _l7_w2, _l8_w2] #  week2 label
    # week3 = [_l1_w3, _l2_w3, _l3_w3, _l4_w3, _l5_w3, _l6_w3, _l7_w3, _l8_w3] #  week3 label
    # week4 = [_l1_w4, _l2_w4, _l3_w4, _l4_w4, _l5_w4, _l6_w4, _l7_w4, _l8_w4] #  week4 label
    # week5 = [_l1_w5, _l2_w5, _l3_w5, _l4_w5, _l5_w5, _l6_w5, _l7_w5, _l8_w5] #  week5 label
    # five_weeks = [week1, week2, week3, week4, week5]

    # #all data
    # i = 0
    # for weeks in tqdm(five_weeks):
    #     i+=1
    #     week_stack = []
    #     for window, week in zip(windows, weeks):
    #         _week = merge_label(window, week)
    #         week_stack.append(_week)
    #     _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
    #     _week.to_csv('../weeks/all/train_w{}.csv'.format(i), index = None)

#############################################################################################################

    # #train
    # windows = [w1, w2, w3, w4, w5, w6, w7] #7 windows
    # week1 = [_l1_w1, _l2_w1, _l3_w1, _l4_w1, _l5_w1, _l6_w1, _l7_w1] #  week1 label
    # week2 = [_l1_w2, _l2_w2, _l3_w2, _l4_w2, _l5_w2, _l6_w2, _l7_w2] #  week2 label
    # week3 = [_l1_w3, _l2_w3, _l3_w3, _l4_w3, _l5_w3, _l6_w3, _l7_w3] #  week3 label
    # week4 = [_l1_w4, _l2_w4, _l3_w4, _l4_w4, _l5_w4, _l6_w4, _l7_w4] #  week4 label
    # week5 = [_l1_w5, _l2_w5, _l3_w5, _l4_w5, _l5_w5, _l6_w5, _l7_w5] #  week5 label
    # five_weeks = [week1, week2, week3, week4, week5]

    # #train
    # i = 0
    # for weeks in tqdm(five_weeks):
    #     i+=1
    #     week_stack = []
    #     for window, week in zip(windows, weeks):
    #         _week = merge_label(window, week)
    #         week_stack.append(_week)
    #     _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
    #     _week.to_csv('../weeks/train/train_w{}.csv'.format(i), index = None)

    # windows = [w8] #7 windows
    # val_week1 = [_l8_w1] #  week1 label
    # val_week2 = [_l8_w2] #  week2 label
    # val_week3 = [_l8_w3] #  week3 label
    # val_week4 = [_l8_w4] #  week4 label
    # val_week5 = [_l8_w5] #  week5 label
    # val_five_weeks = [val_week1, val_week2, val_week3, val_week4, val_week5]

    # #validation 
    # i = 0
    # for weeks in tqdm(val_five_weeks):
    #     i+=1
    #     week_stack = []
    #     for window, week in zip(windows, weeks):
    #         _week = merge_label(window, week)
    #         week_stack.append(_week)
    #     _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
    #     _week.to_csv('../weeks/val/val_w{}.csv'.format(i), index = None)
#############################################################################################################


    #train A
    windows = [w1, w2, w3, w4] #7 windows  w5, w6, w7
    week1 = [_l1_w1, _l2_w1, _l3_w1, _l4_w1] #  week1 label , _l5_w1, _l6_w1, _l7_w1
    week2 = [_l1_w2, _l2_w2, _l3_w2, _l4_w2] #  week2 label , _l5_w2, _l6_w2, _l7_w2
    week3 = [_l1_w3, _l2_w3, _l3_w3, _l4_w3] #  week3 label , _l5_w3, _l6_w3, _l7_w3
    week4 = [_l1_w4, _l2_w4, _l3_w4, _l4_w4] #  week4 label , _l5_w4, _l6_w4, _l7_w4
    week5 = [_l1_w5, _l2_w5, _l3_w5, _l4_w5] #  week5 label , _l5_w5, _l6_w5, _l7_w5
    five_weeks = [week1, week2, week3, week4, week5]

    i = 0
    for weeks in tqdm(five_weeks):
        i+=1
        week_stack = []
        for window, week in zip(windows, weeks):
            _week = merge_label(window, week)
            week_stack.append(_week)
        _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
        _week.to_csv('../weeks/A/train_w{}_a.csv'.format(i), index = None)

    #train B
    windows = [w5, w6, w7, w8] #7 windows  
    week1 = [_l5_w1, _l6_w1, _l7_w1, _l8_w1] #  week1 label 
    week2 = [_l5_w2, _l6_w2, _l7_w2, _l8_w2] #  week2 label 
    week3 = [_l5_w3, _l6_w3, _l7_w3, _l8_w3] #  week3 label 
    week4 = [_l5_w4, _l6_w4, _l7_w4, _l8_w4] #  week4 label
    week5 = [_l5_w5, _l6_w5, _l7_w5, _l8_w5] #  week5 label 
    five_weeks = [week1, week2, week3, week4, week5]

    i = 0
    for weeks in tqdm(five_weeks):
        i+=1
        week_stack = []
        for window, week in zip(windows, weeks):
            _week = merge_label(window, week)
            week_stack.append(_week)
        _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
        _week.to_csv('../weeks/B/train_w{}_b.csv'.format(i), index = None)

    # windows = [w8] #7 windows
    # val_week1 = [_l8_w1] #  week1 label
    # val_week2 = [_l8_w2] #  week2 label
    # val_week3 = [_l8_w3] #  week3 label
    # val_week4 = [_l8_w4] #  week4 label
    # val_week5 = [_l8_w5] #  week5 label
    # val_five_weeks = [val_week1, val_week2, val_week3, val_week4, val_week5]

    # #validation 
    # i = 0
    # for weeks in tqdm(val_five_weeks):
    #     i+=1
    #     week_stack = []
    #     for window, week in zip(windows, weeks):
    #         _week = merge_label(window, week)
    #         week_stack.append(_week)
    #     _week = pd.concat(week_stack, ignore_index=True).drop_duplicates().reset_index(drop=True)
    #     _week.to_csv('../weeks/val/val_w{}.csv'.format(i), index = None)
        
if __name__ == '__main__':
    main()
