class Order():
    filledqty = 0
    isAcked = False
    isOpen = True
    isRejected = False

    def __init__(self,id, side, ticker, orderqty, price):
        self.id = id
        self.ticker = ticker
        self.orderqty = int(orderqty)
        self.side = side
        self.price = price

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6}"\
                .format(self.id, self.ticker, self.orderqty, self.side,\
                self.price, self.isAcked,self.filledqty )

    def procExcutionReport(self, reportdict):
        reportType = reportdict["type"]
        if reportType == "ACK":
            self.isAcked = True
        if reportType == "FILL":
            self.fill(reportdict["filled_shares"])
        if reportType == "REJ":
            self.reject()

    def reject(self):
        self.isRejected = True
        self.isOpen = False

    def acked(self):
        self.acked = True

    def fill(self, fillqty):
        fillqty = int(fillqty)
        self.filledqty += fillqty
        if self.orderqty == self.filledqty:
            self.isOpen = False


