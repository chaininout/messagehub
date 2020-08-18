import unittest
import messagehub as mh
import sys
import traceback


class MessageHubTest(unittest.TestCase):

    def test_v(self):
        print(mh.__version__)

    def test_token(self):
        # use api token
        token = "7194f650afe74aedb7a2a1e5ceba95da76dc15453ea3e44de0f1171aac913347"
        api = mh.api(token)
        print(api)

    def test_get_bar(self):
        print("message hub test")
        code = "600123"
        ret = mh.bar(code)
        print("============")
        print(ret)

    def test_get_c_bar(self):
        print("message hub test")
        code = "BTC"
        exchange = "okex"
        asset = "spot"
        ret = mh.bar(code, exchange=exchange, asset=asset)
        print("============")
        print(ret)

    def test_get_f_bar(self):
        print("message hub test")
        code = "btcusdt"
        exchange = "binance"
        asset = "perpetual"
        freq = "5m"
        ma = [7, 25, 99]
        ret = mh.bar(code, exchange=exchange, freq=freq, asset=asset, ma=ma)
        print("============")
        if ret is not None:
            print(ret.head(5))
            df = ret.head(5)
            df.to_csv('btcusdt.csv', index=None)

    def test_get_f_bar_ts(self):
        print("message hub test")
        code = "btcusdt"
        exchange = "binance"
        asset = "perpetual"
        freq = "1d"
        ma = [7, 25, 99]
        start = '20200201'
        end = '20200802'
        ret = mh.bar(code, exchange=exchange, freq=freq, asset=asset, ma=ma, start_date=start, end_date=end)
        print("============")
        print(ret.head(5))
        # df = ret.head(5)
        ret.to_csv('btcusdt_start_end.csv', index=None)

    def test_getall_type(self):
        ASSET_STOCK = "stock"
        ASSET_INDEX = "index"
        ASSET_SPOT = "spot"
        ASSET_DELIVERY = "delivery"
        ASSET_PERPETUAL = "perpetual"
        ASSET_OPTION = "option"
        ASSET_ETF = "etf"

        timeframes = {
            '1m': '1m',
            '5m': '5m',
            '30m': '30m',
            '1h': '1h',
            '4h': '4h',
            '1d': '1d',
            '1w': '1w',
            '1M': '1M',
        }

        assets = [ASSET_STOCK, ASSET_INDEX, ASSET_SPOT, ASSET_DELIVERY, ASSET_PERPETUAL, ASSET_OPTION, ASSET_ETF]
        timeframes = timeframes.keys()
        numbers = []
        for a in assets:
            for t in timeframes:
                pair = "{}_{}".format(a, t)
                code = "BTC/USDT"
                exchange = "okex"
                ret = mh.bar(code, exchange=exchange, asset=a, freq=t)
                print(ret)
                numbers.append(pair)
        print(numbers)
        print("len pair: {}".format(len(numbers)))

    def test_get_flash(self):
        print("message hub test flash")
        query = ""
        source_name = ""
        # source_name = "jinse"
        ret = mh.flash(query, source_name)
        print("============")
        print(ret.head(5))
        # df = ret.head(5)
        ret.to_csv('flash.csv', index=None)

    def test_get_wallet(self):
        print("get wallet")
        owner = "binance"
        blockchain = "bitcoin"
        symbol = "btc"
        ret = mh.wallet(owner, blockchain, symbol)
        print(ret.head(5))
        ret.to_csv('wallet.csv', index=None)

    def test_get_transaction(self):
        print("get transaction")
        owner = ""  # binance , huobi ,
        blockchain = "bitcoin"
        symbol = "btc"
        ret = mh.transaction(owner, blockchain, symbol)
        if ret is not None:
            print(ret.head(5))
            ret.to_csv('transaction.csv', index=None)

    def test_get_defi(self):
        print("get defi")
        contract_address = "0x06d6d9c4c9eadcb0319b46b7cd05358915bda97a"
        ret = mh.defi(contract_address)
        print(ret.head(5))
        ret.to_csv('defi.csv', index=None)

    def test_get_nocheck(self):
        print("get nocheck -----------")
        owner = "binance"
        blockchain = "bitcoin"
        symbol = "btc"
        ret = mh.wallet(owner, blockchain, symbol)
        print(ret)
