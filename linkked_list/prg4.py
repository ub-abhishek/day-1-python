class Order:
    def __init__(self, id, date, price):
        self.id = id
        self.date = date
        self.price = price
        self.next = None
        self.prev = None
o1 = Order(int(input("Enter order id: ")), input("Enter order date: "), float(input("Enter order price: ")))
o2 = Order(int(input("Enter order id: ")), input("Enter order date: "), float(input("Enter order price: ")))
o3 = Order(int(input("Enter order id: ")), input("Enter order date: "), float(input("Enter order price: ")))
o1.next = o2
o2.prev = o1
o2.next = o3
o3.prev = o2
cur = o1
while cur:
    print(cur.id,cur.date,cur.price)
    cur = cur.next
o4 = Order(int(input("Enter order id: ")), input("Enter order date: "), float(input("Enter order price: ")))
o3.next = o4
o4.prev = o3
cur = o1
while cur:
    print(cur.id,cur.date,cur.price)
    cur = cur.next
    