class Computer:
    def __init__(self):
        self.name="Atik"
        self.age=18

    def update(self):
        self.age=30

c1=Computer()
c2=Computer()

c1.name='ISlAM'
c1.age='21'
if c1==c2:
    print("Theyu are same age")

c1.update

print(c1.name)
print(c2.name)