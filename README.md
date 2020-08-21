# messagehub [![Version][version-badge]][version-link] ![MIT License][license-badge]


messagehub: crypto and traditional financial data hub.    

include: 
bar data:  ohlcv for stock, crypto   
flash data: flash news of crypto symbols and stocks    
wallet data: blockchain labeling wallet 
transaction: blockchain  symbol large transactions 


### Install

```
$ pip install messagehub
```

In China：    
```
$ pip install messagehub -i https://pypi.tuna.tsinghua.edu.cn/simple
```
 

### Usage

```
import messagehub as mh

token = "getapitokens"
api = mh.api(token)

# get crypto btc ohlcv in binance
code = "btcusdt"
exchange = "binance"
asset = "spot"
df = mh.bar(code, exchange=exchange, asset=asset)

# get 5m crypto perpetual ohlcv in binance with ma 
code = "btcusdt"
exchange = "binance"
asset = "perpetual"
freq = "5m"
ma = [7, 25, 99]
df = mh.bar(code, exchange=exchange, freq=freq, asset=asset, ma=ma)

# get 1d crypto perpetual ohlcv in binance with ma and time start end 
code = "btcusdt"
exchange = "binance"
asset = "perpetual"
freq = "1d"
ma = [7, 25, 99]
start = '20200201'
end = '20200802'
df = mh.bar(code, exchange=exchange, freq=freq, asset=asset, ma=ma, start_date=start, end_date=end)

# get flash data 
query = ""  
source_name = ""   # support jinse/bishijie/huoxing 
df = mh.flash(query, source_name)

# get wallet data 
owner = "binance"
blockchain = "bitcoin"
symbol = "btc"
df = mh.wallet(owner, blockchain, symbol)

# get large transactions
owner = ""      # binance , huobi ,
blockchain = "bitcoin"
symbol = "btc"
df = mh.transaction(owner, blockchain, symbol)


```


### License

[MIT](https://github.com/chaininout/messagehub/blob/master/LICENSE)


[version-badge]:   https://raw.githubusercontent.com/chaininout/messagehub/master/version-0.1-brightgreen.svg
[version-link]:    https://pypi.org/project/messagehub/
[license-badge]:   https://raw.githubusercontent.com/chaininout/messagehub/master/license.svg