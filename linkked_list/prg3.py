class Customer:
    def __init__(self,id,name,place,phoneum,email,location):
        self.id=id
        self.name=name
        self.place=place
        self.phoneum=phoneum
        self.email=email
        self.location=location
        self.next=None
        self.prev=None
s1=Customer(int(input("Enter id: ")),input("Enter name: "),input("Enter place: "),int(input("Enter phone number: ")),input("Enter email: "),input("Enter location: "  ))
s2=Customer(int(input("Enter id: ")),input("Enter name: "),input("Enter place: "),int(input("Enter phone number: ")),input("Enter email: "),input("Enter location: "  ))
s3=Customer(int(input("Enter id: ")),input("Enter name: "),input("Enter place: "),int(input("Enter phone number: ")),input("Enter email: "),input("Enter location: "  ))
s4=Customer(int(input("Enter id: ")),input("Enter name: "),input("Enter place: "),int(input("Enter phone number: ")),input("Enter email: "),input("Enter location: "  ))
s5=Customer(int(input("Enter id: ")),input("Enter name: "),input("Enter place: "),int(input("Enter phone number: ")),input("Enter email: "),input("Enter location: "  ))
s1.next=s2
s2.next=s3
s3.next=s4
s4.next=s5
cur=s1
while cur:
    print(cur)
    cur=cur.next
                                                                                                                                                