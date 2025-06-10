class duck:
    def fly(self):
        print("duck flying")
    def swim(self):
        print("duck swiming")
class swan:
    def fly(self):
        print("swan flying")
    def swim(self):
        print("swan swiming")
class person:
     def swim(self):
        print("swan swiming")
def display(obj):
        obj.fly()
        obj.swim()

d = duck()
s = swan()
p = person()
display(p)
    