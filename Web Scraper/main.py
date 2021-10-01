from bs4 import BeautifulSoup
import requests
import mystocks




html_text = requests.get('https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/').text
soup = BeautifulSoup(html_text, 'lxml')
stocks = soup.find_all('span', class_ = 'tv-screener__description')

##used to get all the names in a container
top_10_stocks = []
count = 0
for stock in stocks:
    count = count + 1
    insertion = stock.text
    top_10_stocks.append(insertion)
    #print(insertion)
    if count == 10:
        
        break
     

count = 0
count2 = 0
values = soup.find_all('td',class_ = 'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big')

##used to put the prices in a container the data i needed was every 6th item
single_stock_price= []
for price in values:
   # print("A " +price.text)
  
    if count % 6 == 0:
       # print("B: "+ price.text)
        single_stock_price.append(price.text)
        count = 0
    if count2 == 55:
        break
    count = count + 1    
    count2 = count2 + 1



 
top_10_stocks_names = []
## was getting extra text in the name so I found a pattern to elminate the extra text and put that in a new conatainer
for str in top_10_stocks:
    x = (str[9:-1] + str[-1])
    top_10_stocks_names.append(x)
 
#print(top_10_stocks_names)

changes = soup.find_all('td', class_ = 'tv-data-table__cell tv-screener-table__cell tv-screener-table__cell--big tv-screener-table__cell--up')

count = 0 # to help put percents in the right container
count2 = 0 # to help get only the top 10 changes for both


percent_change = []
cost_change = []
for raises in changes:
    
   # percent_change.append(raises.text)
   
    
    if count % 2 == 0:
        percent_change.append(raises.text)
        count = 0
    else:
        cost_change.append(raises.text)

    if count2 == 19:
        break
    
    count = count + 1
    count2 = count2 + 1




#print(percent_change)
#print(cost_change)

#putting all top 10 info into objects

stock1 = mystocks.GainerStock(top_10_stocks_names[0],single_stock_price[0],percent_change[0],cost_change[0])
stock2 = mystocks.GainerStock(top_10_stocks_names[1],single_stock_price[1],percent_change[1],cost_change[1])
stock3 = mystocks.GainerStock(top_10_stocks_names[2],single_stock_price[2],percent_change[2],cost_change[2])
stock4 = mystocks.GainerStock(top_10_stocks_names[3],single_stock_price[3],percent_change[3],cost_change[3])
stock5 = mystocks.GainerStock(top_10_stocks_names[4],single_stock_price[4],percent_change[4],cost_change[4])
stock6 = mystocks.GainerStock(top_10_stocks_names[5],single_stock_price[5],percent_change[5],cost_change[5])
stock7 = mystocks.GainerStock(top_10_stocks_names[6],single_stock_price[6],percent_change[6],cost_change[6])
stock8 = mystocks.GainerStock(top_10_stocks_names[7],single_stock_price[7],percent_change[7],cost_change[7])
stock9 = mystocks.GainerStock(top_10_stocks_names[8],single_stock_price[8],percent_change[8],cost_change[8])
stock10 = mystocks.GainerStock(top_10_stocks_names[9],single_stock_price[9],percent_change[9],cost_change[9])


