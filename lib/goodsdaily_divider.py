import pandas as pd
import os
import gc
import matplotlib.pyplot as plt
import seaborn as sns

dataset = ''

goodsale = os.path.join(dataset, 'goodsale.csv') #(7325028, 6)
goodsdaily = os.path.join(dataset, 'goodsdaily.csv') #(35201588, 7)
info = os.path.join(dataset, 'goodsinfo.csv') #(423452, 10)
promote_price = os.path.join(dataset, 'goods_promote_price.csv') #(24016430, 6)
sku_relation = os.path.join(dataset, 'goods_sku_relation.csv') #(3245170, 2)
marketing = os.path.join(dataset, 'marketing.csv') #(416, 3)

df = pd.read_csv(goodsale)
# df = df[df['data_date'] > '2017-04-30']

w1 = df[(df.data_date >= '2017-05-03') & (df.data_date <= '2017-07-31')]
w2 = df[(df.data_date >= '2017-05-10') & (df.data_date <= '2017-08-07')]
w3 = df[(df.data_date >= '2017-05-17') & (df.data_date <= '2017-08-14')]
w4 = df[(df.data_date >= '2017-05-24') & (df.data_date <= '2017-08-21')]
w5 = df[(df.data_date >= '2017-08-01') & (df.data_date <= '2017-10-19')]
w6 = df[(df.data_date >= '2017-08-08') & (df.data_date <= '2017-10-26')]
w7 = df[(df.data_date >= '2017-08-15') & (df.data_date <= '2017-11-02')]
w8 = df[(df.data_date >= '2017-08-22') & (df.data_date <= '2017-11-09')]
test = df[(df.data_date >= '2017-12-17') & (df.data_date <= '2018-03-16')]

w1.to_csv("window1_daily.csv", index = None)
w2.to_csv("window2_daily.csv", index = None)
w3.to_csv("window3_daily.csv", index = None)
w4.to_csv("window4_daily.csv", index = None)
w5.to_csv("window5_daily.csv", index = None)
w6.to_csv("window6_daily.csv", index = None)
w7.to_csv("window7_daily.csv", index = None)
w8.to_csv("window8_daily.csv", index = None)
test.to_csv("test_daily.csv", index = None)

# w1.to_csv("window1_sale.csv", index = None)
# w2.to_csv("window2_sale.csv", index = None)
# w3.to_csv("window3_sale.csv", index = None)
# w4.to_csv("window4_sale.csv", index = None)
# w5.to_csv("window5_sale.csv", index = None)
# w6.to_csv("window6_sale.csv", index = None)
# w7.to_csv("window7_sale.csv", index = None)
# w8.to_csv("window8_sale.csv", index = None)
# test.to_csv("test_sale.csv", index = None)


"""

label1 = df[(df.data_date >= '2017-09-15') & (df.data_date <= '2017-10-19')][['data_date', 'goods_id']]
label2 = df[(df.data_date >= '2017-09-22') & (df.data_date <= '2017-10-26')][['data_date', 'goods_id']]
label3 = df[(df.data_date >= '2017-09-29') & (df.data_date <= '2017-11-02')][['data_date', 'goods_id']]
label4 = df[(df.data_date >= '2017-10-06') & (df.data_date <= '2017-11-09')][['data_date', 'goods_id']]
label5 = df[(df.data_date >= '2017-12-04') & (df.data_date <= '2018-01-07')][['data_date', 'goods_id']]
label6 = df[(df.data_date >= '2017-12-11') & (df.data_date <= '2018-01-14')][['data_date', 'goods_id']]
label7 = df[(df.data_date >= '2017-12-18') & (df.data_date <= '2018-01-21')][['data_date', 'goods_id']]
label8 = df[(df.data_date >= '2017-12-25') & (df.data_date <= '2018-01-28')][['data_date', 'goods_id']]

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


_w1_w1 = pd.merge(w1,l1_w1,on="goods_id")
_w1_w2 = pd.merge(w1,l1_w2,on="goods_id")
_w1_w3 = pd.merge(w1,l1_w3,on="goods_id")
_w1_w4 = pd.merge(w1,l1_w4,on="goods_id")
_w1_w5 = pd.merge(w1,l1_w5,on="goods_id")

_w2_w1 = pd.merge(w2,l2_w1,on="goods_id")
_w2_w2 = pd.merge(w2,l2_w2,on="goods_id")
_w2_w3 = pd.merge(w2,l2_w3,on="goods_id")
_w2_w4 = pd.merge(w2,l2_w4,on="goods_id")
_w2_w5 = pd.merge(w2,l2_w5,on="goods_id")

_w3_w1 = pd.merge(w3,l3_w1,on="goods_id")
_w3_w2 = pd.merge(w3,l3_w2,on="goods_id")
_w3_w3 = pd.merge(w3,l3_w3,on="goods_id")
_w3_w4 = pd.merge(w3,l3_w4,on="goods_id")
_w3_w5 = pd.merge(w3,l3_w5,on="goods_id")

_w4_w1 = pd.merge(w4,l4_w1,on="goods_id")
_w4_w2 = pd.merge(w4,l4_w2,on="goods_id")
_w4_w3 = pd.merge(w4,l4_w3,on="goods_id")
_w4_w4 = pd.merge(w4,l4_w4,on="goods_id")
_w4_w5 = pd.merge(w4,l4_w5,on="goods_id")

_w5_w1 = pd.merge(w5,l5_w1,on="goods_id")
_w5_w2 = pd.merge(w5,l5_w2,on="goods_id")
_w5_w3 = pd.merge(w5,l5_w3,on="goods_id")
_w5_w4 = pd.merge(w5,l5_w4,on="goods_id")
_w5_w5 = pd.merge(w5,l5_w5,on="goods_id")

_w6_w1 = pd.merge(w6,l6_w1,on="goods_id")
_w6_w2 = pd.merge(w6,l6_w2,on="goods_id")
_w6_w3 = pd.merge(w6,l6_w3,on="goods_id")
_w6_w4 = pd.merge(w6,l6_w4,on="goods_id")
_w6_w5 = pd.merge(w6,l6_w5,on="goods_id")

_w7_w1 = pd.merge(w7,l7_w1,on="goods_id")
_w7_w2 = pd.merge(w7,l7_w2,on="goods_id")
_w7_w3 = pd.merge(w7,l7_w3,on="goods_id")
_w7_w4 = pd.merge(w7,l7_w4,on="goods_id")
_w7_w5 = pd.merge(w7,l7_w5,on="goods_id")

_w8_w1 = pd.merge(w8,l8_w1,on="goods_id")
_w8_w2 = pd.merge(w8,l8_w2,on="goods_id")
_w8_w3 = pd.merge(w8,l8_w3,on="goods_id")
_w8_w4 = pd.merge(w8,l8_w4,on="goods_id")
_w8_w5 = pd.merge(w8,l8_w5,on="goods_id")

week1 = pd.concat([_w1_w1, _w2_w1, _w3_w1, _w4_w1, _w5_w1, _w6_w1, _w7_w1, _w8_w1], ignore_index=True).drop_duplicates().reset_index(drop=True)
week2 = pd.concat([_w1_w2, _w2_w2, _w3_w2, _w4_w2, _w5_w2, _w6_w2, _w7_w2, _w8_w2], ignore_index=True).drop_duplicates().reset_index(drop=True)
week3 = pd.concat([_w1_w3, _w2_w3, _w3_w3, _w4_w3, _w5_w3, _w6_w3, _w7_w3, _w8_w3], ignore_index=True).drop_duplicates().reset_index(drop=True)
week4 = pd.concat([_w1_w4, _w2_w4, _w3_w4, _w4_w4, _w5_w4, _w6_w4, _w7_w4, _w8_w4], ignore_index=True).drop_duplicates().reset_index(drop=True)
week5 = pd.concat([_w1_w5, _w2_w5, _w3_w5, _w4_w5, _w5_w5, _w6_w5, _w7_w5, _w8_w5], ignore_index=True).drop_duplicates().reset_index(drop=True)

week1.to_csv('goodsdaily_w1.csv', index = None)
week2.to_csv('goodsdaily_w2.csv', index = None)
week3.to_csv('goodsdaily_w3.csv', index = None)
week4.to_csv('goodsdaily_w4.csv', index = None)
week5.to_csv('goodsdaily_w5.csv', index = None)
test.to_csv('goodsdaily_test.csv', index = None)
"""