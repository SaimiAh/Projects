class student:
    uni="IUB"
    def __init__(self, name, depart):
        self.name=name
        self.depart=depart
        print(f"His name is {name},and student of department {depart}.")

student1=student("Saim", "CS")
student2=student("Adeel", "BBA")
print(student1.name)
print(student1.uni)
print(student2.depart)
print(student2.uni)
print(student.__init__)