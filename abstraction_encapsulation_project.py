from turtle import title


class Car:
    def __init__(self):
        self.carandrent = {'Mehran': 300, 'Bolan': 500, 'City': 700, 'Civic': 1000}


    def displaycar(self):
        print("Following is the rent for available cars:")
        print(f"Mehran has a rent of: PKR {self.carandrent['Mehran']}")
        print(f"Bolan has a rent of: PKR {self.carandrent['Bolan']}")
        print(f"City has a rent of: PKR {self.carandrent['City']}")
        print(f"Civic has a rent of: PKR {self.carandrent['Civic']}")
        

    def cal_rent(self, carname, nbrofdays):
        return self.carandrent[carname] *nbrofdays
        

car = Car()
while True:
    print("Enter 1 to show available cars and rent details.")
    print("Enter 2 to rent a car.")
    print("Enter 3 to exit.")
    userchoice=int(input())
    if userchoice is 1:
        car.displaycar()

    elif userchoice is 2:
        carname=input("Enter the name of the car you want to rent:")
        
        nbrofdays=int(input("Enter the number of days you want to rent:"))
        rent=car.cal_rent(carname, nbrofdays)
        print(f"Your rent of {carname} for {nbrofdays} days is {rent} PKR.")
        print("Thank You!")
    elif userchoice is 3:
        quit()
 