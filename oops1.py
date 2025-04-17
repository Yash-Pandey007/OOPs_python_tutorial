class employee:
    def __init__(self):
        print("Started excecuting data")
        self.id = 123
        self.salary = 40000
        self.designation = "DevOp"
        print("Data has been excecuted")
    

    def travel(self,destination):
        print("this method was called manually")
        print(f"employee is traveling to {destination}")

sam = employee()

 # print(sam.salary)

# sam.travel("Mumbai")
print(type(sam))