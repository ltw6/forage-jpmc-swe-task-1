import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    price = []
    stock = [quote['stock'] for quote in quotes]
    top_asks = [quote['top_ask'] for quote in quotes]
    ask_price = ([top_ask['price'] for top_ask in top_asks])
    top_bids = [quote['top_bid'] for quote in quotes]
    bid_price = [top_bid['price'] for top_bid in top_bids]
    for i in range(0, len(bid_price)):
      tempPrice = (bid_price[i]+ask_price[i]) / 2
      price.append(tempPrice)
    return stock, price


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    price = []
    stock = [quote['stock'] for quote in quotes]
    top_asks = [quote['top_ask'] for quote in quotes]
    ask_price = ([top_ask['price'] for top_ask in top_asks])
    top_bids = [quote['top_bid'] for quote in quotes]
    bid_price = [top_bid['price'] for top_bid in top_bids]
    for i in range(0, len(bid_price)):
      tempPrice = (bid_price[i]+ask_price[i]) / 2
      price.append(tempPrice)
    if price[1] == 0:
      return
    return price[0] / price[1]

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
