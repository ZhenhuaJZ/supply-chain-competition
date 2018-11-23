import pandas as pd
import os
import gc
from tqdm import tqdm

def feats_selection(df_path, i):
    df = pd.read_csv(df_path)
    df = df.drop(['cat_level5_id','cat_level6_id','cat_level7_id'],axis = 1)
    df = df.loc[:, ~df.columns.str.endswith("_35")]
    df = df.loc[:, ~df.columns.str.endswith("_28")]
    df = df.loc[:, ~df.columns.str.endswith("_21")]
    df = df.fillna(0)
    if i == 6 :
        df.to_csv("20_10/test{}.csv".format(i), index = None)
    elif i >6: 
        df.to_csv("20_10/validation{}.csv".format(i), index = None)
    else:
        df.to_csv("20_10/train{}.csv".format(i), index = None)
def main():

    orign_ver = 0
    wk1 = "train_dataset1.csv"
    wk2 = "train_dataset2.csv"
    wk3 = "train_dataset3.csv"
    wk4 = "train_dataset4.csv"
    wk5 = "train_dataset5.csv"
    test = 'feature_test.csv'

    val1 = "val1.csv"
    val2 = "val2.csv"
    val3 = "val3.csv"
    val4 = "val4.csv"
    val5 = "val5.csv"

    i = 0
    arg = [wk1, wk2, wk3, wk4, wk5, test, val1, val2, val3, val4, val5]
    for df_path in tqdm(arg):
        i +=1
        feats_selection(df_path, i) #cat_level1_id

if __name__ == '__main__':
    main()
