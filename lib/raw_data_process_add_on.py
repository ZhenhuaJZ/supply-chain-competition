import pandas as pd
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns

w1 = 'train_w1_2.csv'
w2 = 'train_w2_2.csv'
w3 = 'train_w3_2.csv'
w4 = 'train_w4_2.csv'
w5 = 'train_w5_2.csv'
t = 'test_2.csv'

# week1 = pd.read_csv(w1)
# week2 = pd.read_csv(w2)
# week3 = pd.read_csv(w3)
# week4 = pd.read_csv(w4)
# week5 = pd.read_csv(w5)
# test = pd.read_csv(t)

dataset = '../raw_data'

goodsale = os.path.join(dataset, 'goodsale.csv') #(7325028, 6)
goodsdaily = os.path.join(dataset, 'goodsdaily.csv') #(35201588, 7)
info = os.path.join(dataset, 'goodsinfo.csv') #(423452, 10)
promote_price = os.path.join(dataset, 'goods_promote_price.csv') #(24016430, 6)
sku_relation = os.path.join(dataset, 'goods_sku_relation.csv') #(3245170, 2)
marketing = os.path.join(dataset, 'marketing.csv') #(416)

# _sku_relation = pd.read_csv(sku_relation)
# df_sku = _sku_relation.groupby(["goods_id"], as_index=False)["sku_id"].size().to_frame('sku_id_num')
# df_sku["goods_id"] = df_sku.index

# week1 = pd.merge(week1, df_sku, on="goods_id", how = 'left')
# week2 = pd.merge(week2, df_sku, on="goods_id", how = 'left')
# week3 = pd.merge(week3, df_sku, on="goods_id", how = 'left')
# week4 = pd.merge(week4, df_sku, on="goods_id", how = 'left')
# week5 = pd.merge(week5, df_sku, on="goods_id", how = 'left')
# test = pd.merge(test, df_sku, on="goods_id", how = 'left')

df = pd.read_csv(goodsale)
df = df[df['data_date'] > '2017-04-30']

df = df.assign(day = pd.to_datetime(df['data_date'], format='%Y-%m-%d').dt.day)
df = df.assign(month = pd.to_datetime(df['data_date'], format='%Y-%m-%d').dt.month)

#make the orignal shop price = goods_price
replace = df[(df['orginal_shop_price'] == 0) & (df['goods_price'] > 0)]['goods_price']
error_index = df[(df['orginal_shop_price'] == 0) & (df['goods_price'] > 0)].index.values
df.loc[error_index, 'orginal_shop_price'] = replace

_marketing = pd.read_csv(marketing)
df = pd.merge(df, _marketing, on="data_date", how = 'left')

df= df.fillna(0)
# df[['cat_level1_id', 'cat_level2_id', 'cat_level3_id', 'cat_level4_id', 'goods_season', 'brand_id']] = df[['cat_level1_id', 'cat_level2_id', 'cat_level3_id', 'cat_level4_id', 'goods_season', 'brand_id']].round().astype(int)
df[['goods_price', 'orginal_shop_price', 'marketing', 'plan']] = df[['goods_price', 'orginal_shop_price','marketing','plan']].round().astype(int)

# df = df.replace(-1,0).round()

df.to_csv("goodsale.csv", index = None)
