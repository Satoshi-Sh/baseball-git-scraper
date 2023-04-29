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
full_pacific = pd.concat([pacific,new_pacific]).reset_index(drop=True)

# remove duplicates
full_central.drop_duplicates(subset=['順位', 'チーム名', '試合', '勝利', '敗戦', '引分', '勝率', '勝差', '残試合', '得点', '失点',
       '本塁打', '盗塁', '打率', '防御率', '失策'],inplace=True)
full_pacific.drop_duplicates(subset=['順位', 'チーム名', '試合', '勝利', '敗戦', '引分', '勝率', '勝差', '残試合', '得点', '失点',
       '本塁打', '盗塁', '打率', '防御率', '失策'],inplace=True)


full_central.to_csv('./data/central.csv',index=False)
full_pacific.to_csv('./data/pacifics.csv',index=False)