Script that parses in sequential order:
 1. orders file containing orders that went out to the exchange.
 2. recieved messages file that contain different messages (ACK, FILL, REJ) on the orders contained in orders file

Report on the following:
1. all unacked orders
2. all rejected orders
3. all open orders

TODO: Process cancel order and also replace orders.
