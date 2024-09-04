import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
  DF= orders[(orders['order_date']>='2019-01-01') & (orders['order_date']<= '2019-12-31')]
  DF = DF.groupby('buyer_id')['order_date'].size().reset_index(name='orders_in_2019')
  users.rename(columns={'user_id': 'buyer_id'}, inplace = True)
  result = pd.merge(users, DF, on= ['buyer_id'], how= 'left')
  result['orders_in_2019'] = result['orders_in_2019'].fillna(0)
  return result[['buyer_id', 'join_date', 'orders_in_2019']]