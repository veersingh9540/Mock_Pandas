import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
  DF = sales.groupby('product_id')['sale_date'].agg([ 'min', 'max']).reset_index()
  DF = DF[(DF['min']>= '2019-01-01')&(DF['max']<= '2019-03-31')]

  result = pd.merge(DF, product, on= ['product_id'], how= 'left')

  return result[['product_id', 'product_name']]

    