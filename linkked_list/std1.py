class Student:
    def __init__(self, name, roll_no,total):
        self.name = name
        self.roll_no = roll_no
        self.total = total
        self.next = None
    def std_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Total: {self.total}")
s1=Student("abhishek",7,54)
s2=Student("sachin",8,67)
s3=Student("rohit",9,89)
s4=Student("virat",10,90)
s5=Student("dhoni",11,78)
s1.next=s2
s2.next=s3
s3.next=s4
s4.next=s5
cur=s1
while cur:
    print(cur)
    cur=cur.next