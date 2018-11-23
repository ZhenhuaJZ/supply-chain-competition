import pandas as pd
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns

w1 = 'train_w1.csv'
w2 = 'train_w2.csv'
w3 = 'train_w3.csv'
w4 = 'train_w4.csv'
w5 = 'train_w5.csv'
t = 'test.csv'

week1 = pd.read_csv(w1)
week2 = pd.read_csv(w2)
week3 = pd.read_csv(w3)
week4 = pd.read_csv(w4)
week5 = pd.read_csv(w5)
test = pd.read_csv(t)

week1 = week1.assign(day = pd.to_datetime(week1['data_date'], format='%Y-%m-%d').dt.day)
week2 = week2.assign(day = pd.to_datetime(week2['data_date'], format='%Y-%m-%d').dt.day)
week3 = week3.assign(day = pd.to_datetime(week3['data_date'], format='%Y-%m-%d').dt.day)
week4 = week4.assign(day = pd.to_datetime(week4['data_date'], format='%Y-%m-%d').dt.day)
week5 = week5.assign(day = pd.to_datetime(week5['data_date'], format='%Y-%m-%d').dt.day)
test = test.assign(day = pd.to_datetime(test['data_date'], format='%Y-%m-%d').dt.day)

week1 = week1.assign(month = pd.to_datetime(week1['data_date'], format='%Y-%m-%d').dt.month)
week2 = week2.assign(month = pd.to_datetime(week2['data_date'], format='%Y-%m-%d').dt.month)
week3 = week3.assign(month = pd.to_datetime(week3['data_date'], format='%Y-%m-%d').dt.month)
week4 = week4.assign(month = pd.to_datetime(week4['data_date'], format='%Y-%m-%d').dt.month)
week5 = week5.assign(month = pd.to_datetime(week5['data_date'], format='%Y-%m-%d').dt.month)
test = test.assign(month = pd.to_datetime(test['data_date'], format='%Y-%m-%d').dt.month)

# week1[(week1['orginal_shop_price'] == 0) & (week1['goods_price'] > 0)]
# week1['orginal_shop_price'] = week1['goods_price']

# week2[(week2['orginal_shop_price'] == 0) & (week2['goods_price'] > 0)]
# week2['orginal_shop_price'] = week2['goods_price']

# week3[(week3['orginal_shop_price'] == 0) & (week3['goods_price'] > 0)]
# week3['orginal_shop_price'] = week3['goods_price']

# week4[(week4['orginal_shop_price'] == 0) & (week4['goods_price'] > 0)]
# week4['orginal_shop_price'] = week4['goods_price']

# week5[(week5['orginal_shop_price'] == 0) & (week5['goods_price'] > 0)]
# week5['orginal_shop_price'] = week5['goods_price']

# test[(test['orginal_shop_price'] == 0) & (test['goods_price'] > 0)]
# test['orginal_shop_price'] = test['goods_price']

dataset = '../raw_data/'

goodsale = os.path.join(dataset, 'goodsale.csv') #(7325028, 6)
goodsdaily = os.path.join(dataset, 'goodsdaily.csv') #(35201588, 7)
info = os.path.join(dataset, 'goodsinfo.csv') #(423452, 10)
promote_price = os.path.join(dataset, 'goods_promote_price.csv') #(24016430, 6)
sku_relation = os.path.join(dataset, 'goods_sku_relation.csv') #(3245170, 2)
marketing = os.path.join(dataset, 'marketing.csv') #(416)

# _goodsdaily = pd.read_csv(goodsdaily)
# week1 = pd.merge(week1, _goodsdaily, on=["data_date","goods_id"] , how = 'left')
# week2 = pd.merge(week2, _goodsdaily, on=["data_date","goods_id"] , how = 'left')
# week3 = pd.merge(week3, _goodsdaily, on=["data_date","goods_id"] , how = 'left')
# week4 = pd.merge(week4, _goodsdaily, on=["data_date","goods_id"] , how = 'left')
# week5 = pd.merge(week5, _goodsdaily, on=["data_date","goods_id"] , how = 'left')
# test = pd.merge(test, _goodsdaily, on=["data_date","goods_id"] , how = 'left')

# goodsinfo = pd.read_csv(info)
# week1 = pd.merge(week1, goodsinfo, on="goods_id", how = 'left')
# week2 = pd.merge(week2, goodsinfo, on="goods_id", how = 'left')
# week3 = pd.merge(week3, goodsinfo, on="goods_id", how = 'left')
# week4 = pd.merge(week4, goodsinfo, on="goods_id", how = 'left')
# week5 = pd.merge(week5, goodsinfo, on="goods_id", how = 'left')
# test = pd.merge(test, goodsinfo, on="goods_id", how = 'left')

_marketing = pd.read_csv(marketing)
week1 = pd.merge(week1, _marketing, on="data_date", how = 'left')
week2 = pd.merge(week2, _marketing, on="data_date", how = 'left')
week3 = pd.merge(week3, _marketing, on="data_date", how = 'left')
week4 = pd.merge(week4, _marketing, on="data_date", how = 'left')
week5 = pd.merge(week5, _marketing, on="data_date", how = 'left')
test = pd.merge(test, _marketing, on="data_date", how = 'left')

#fillna with 0
week1 = week1.fillna(0)
week2 = week2.fillna(0)
week3 = week3.fillna(0)
week4 = week4.fillna(0)
week5 = week5.fillna(0)
test = test.fillna(0)

# week1[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = week1[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)
# week2[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = week2[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)
# week3[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = week3[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)
# week4[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = week4[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)
# week5[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = week5[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)
# test[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']] = test[['goods_price', 'orginal_shop_price', 'goods_click', 'cart_click', 'favorites_click', 'sales_uv', 'onsale_days']].round().astype(int)

week1[['goods_price', 'orginal_shop_price']] = week1[['goods_price', 'orginal_shop_price']].round().astype(int)
week2[['goods_price', 'orginal_shop_price']] = week2[['goods_price', 'orginal_shop_price']].round().astype(int)
week3[['goods_price', 'orginal_shop_price']] = week3[['goods_price', 'orginal_shop_price']].round().astype(int)
week4[['goods_price', 'orginal_shop_price']] = week4[['goods_price', 'orginal_shop_price']].round().astype(int)
week5[['goods_price', 'orginal_shop_price']] = week5[['goods_price', 'orginal_shop_price']].round().astype(int)
test[['goods_price', 'orginal_shop_price']] = test[['goods_price', 'orginal_shop_price']].round().astype(int)

#replace -1 to 0
week1 = week1.replace(-1,0)
week2 = week2.replace(-1,0)
week3 = week3.replace(-1,0)
week4 = week4.replace(-1,0)
week5 = week5.replace(-1,0)
test = test.replace(-1,0)

week1.to_csv("train_w1_2.csv", index = None)
week2.to_csv("train_w2_2.csv", index = None)
week3.to_csv("train_w3_2.csv", index = None)
week4.to_csv("train_w4_2.csv", index = None)
week5.to_csv("train_w5_2.csv", index = None)
test.to_csv("test_2.csv", index = None)
