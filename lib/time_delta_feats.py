import pandas as pd
import os
import gc

dataset = '../raw_data'

goodsale = os.path.join(dataset, 'goodsale.csv') #(7325028, 6)
goodsdaily = os.path.join(dataset, 'goodsdaily.csv') #(35201588, 7)
info = os.path.join(dataset, 'goodsinfo.csv') #(423452, 10)
promote_price = os.path.join(dataset, 'goods_promote_price.csv') #(24016430, 6)
sku_relation = os.path.join(dataset, 'goods_sku_relation.csv') #(3245170, 2)
marketing = os.path.join(dataset, 'marketing.csv') #(416, 3)



def main():
    df = pd.read_csv(goodsdaily)
    df = df[df['data_date'] > '2017-04-30']
    print(df[['goods_id','sales_uv']])
    df['data_date'] = pd.to_datetime(df['data_date'], format='%Y-%m-%d')
    df = df.groupby([pd.Grouper(key='data_date', freq = '2d'), 'goods_id'] , as_index=False)['sales_uv'].sum()
    print(df)
if __name__ == '__main__':
    main()
