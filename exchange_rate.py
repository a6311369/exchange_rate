import pandas as pd
from datetime import datetime
import sqlite3

#source
url="http://rate.bot.com.tw/xrt?Lang=zh-TW"

#讀取網頁
dfs=pd.read_html(url)
currency=dfs[0]
#檢查
type(currency)

#擷取需要的欄位
# currency_fix=currency.ix[:,0:5]
currency_fix=currency.iloc[:,0:5]

#自訂欄位名稱
currency_fix.columns=[u'幣別',u'現金匯率-本行買入',u'現金匯率-本行賣出',u'即期匯率-本行買入',u'即期匯率-本行賣出']

#清除幣別欄重複字元
currency_fix[u'幣別']=currency_fix[u'幣別'].str.extract('\((\w+)\)')

#檢查
print(currency_fix)

#存檔成excel
# currency_fix.to_excel('currency.xlsx')
#currency_fix.to_csv('currency.csv')

