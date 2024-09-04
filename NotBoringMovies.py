import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
  DF = cinema[(cinema['id']%2 !=0) & (cinema['description']!= 'boring')]
  DF = DF.sort_values('rating', ascending= False)
  return DF
