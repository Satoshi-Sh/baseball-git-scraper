import pandas as pd

# read data

central = pd.read_csv('./data/central.csv',index_col=False)
pacific = pd.read_csv('./data/pacific.csv',index_col=False)

url = 'https://baseball.yahoo.co.jp/npb/standings/'
encoding = 'utf-8'
tables = pd.read_html(url,encoding=encoding)

new_central = tables[0]
new_pacific = tables[1]

from datetime import datetime
new_central['date']= datetime.today()
new_pacific['date']= datetime.today()

## combine old and new 
full_central = pd.concat([central,new_central]).reset_index(drop=True)
# Sometimes number is not updated yet
full_central = full_central.drop(full_central[full_central['打率'] == '-'].index)
full_central['打率'] = full_central['打率'].astype(float)
full_central = full_central.drop(full_central[full_central['防御率'] == '-'].index)
full_central['防御率'] = full_central['防御率'].astype(float)

full_pacific = pd.concat([pacific,new_pacific]).reset_index(drop=True)
# Sometimes number is not updated yet
full_pacific = full_pacific.drop(full_pacific[full_pacific['打率'] == '-'].index)
full_pacific['打率'] = full_pacific['打率'].astype(float)
full_pacific = full_pacific.drop(full_pacific[full_pacific['防御率'] == '-'].index)
full_pacific['防御率'] = full_pacific['防御率'].astype(float)

# remove duplicates
full_central.drop_duplicates(subset=['順位', 'チーム名', '試合', '勝利', '敗戦', '引分', '勝率', '勝差', '残試合', '得点', '失点',
       '本塁打', '盗塁', '打率', '防御率', '失策'],inplace=True)
full_pacific.drop_duplicates(subset=['順位', 'チーム名', '試合', '勝利', '敗戦', '引分', '勝率', '勝差', '残試合', '得点', '失点',
       '本塁打', '盗塁', '打率', '防御率', '失策'],inplace=True)


full_central.to_csv('./data/central.csv',index=False)
full_pacific.to_csv('./data/pacific.csv',index=False)