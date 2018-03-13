from orders import Order


class Reader():
    """
    Create reader that reads sent orders and recived messages
    override __iter__ and __next__ to turn object into an iterable to be
    looped over and dictionary of field returned
    """
    COMMA = ","
    def __init__(self, fname):
        self.linedicts = []
        fname = fname
        fhand = open(fname)
        rows = fhand.readlines()
        header = rows.pop(0)
        headerarr = header.split(self.COMMA)
        for line in rows:
             line = line.strip()
             #turn each line into dictionary
             currentdict = {}
             linefields = line.split(self.COMMA)
             for i,field in enumerate(linefields):
                  currentdict[headerarr[i].strip()]=field
             self.linedicts.append(currentdict)
    def __iter__(self):
        return self
    def __next__(self):
        if len(self.linedicts) > 0:
            return self.linedicts.pop(0)
        else:
            raise StopIteration

class OrdersParser():

   sentfile = "sent.txt"
   recievedfile = "recieved.txt"

   ordersdict = {}

   def __init__(self):
       self.processOrders()
       self.processRecieved()

   def processOrders(self):
       """
       process each line in orders text as dictory
       fields: id,ticker,side,shares,price
       store the order objects in dictonary with id as key
       """
       ordersreader = Reader(self.sentfile)
       for d in ordersreader:
           id     = d["id"]
           ticker = d["ticker"]
           side   = d["side"]
           shares = d["shares"]
           price  = d["price"]
           order = Order(id, side, ticker, shares, price)
           self.ordersdict[id] = order

   def processRecieved(self):
       """
       process each line in recieved text as dictory
       fields: id,type,filled_shares,filled_price
       retrieve orders object and set action accordingly
       """
       recievedreader = Reader(self.recievedfile)
       for d in recievedreader:
           id = d["id"]
           #get orders object as we expect object to be present as we processed orders file already
           order = self.ordersdict[id]
           order.procExcutionReport(d)

   def reportUnacked(self):
       for id in self.ordersdict:
         order = self.ordersdict[id]
         if not order.isAcked:
             print("orderID {} is unacked".format(order.id))
       print("")

   def reportRejected(self):
       for id in self.ordersdict:
         order = self.ordersdict[id]
         if  order.isRejected:
             print("orderID {} is rejected".format(order.id))
       print("")

   def reportOnOpen(self):
       for id in self.ordersdict:
         order = self.ordersdict[id]
         if  order.isOpen:
             print("orderID {} is open".format(order.id))
       print("")

if __name__ == "__main__":
    op = OrdersParser()
    op.reportUnacked()
    op.reportRejected()
    op.reportOnOpen()