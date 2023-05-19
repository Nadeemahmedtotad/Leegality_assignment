class ParkingLot:
    
    def __init__(self):
        self.levelA = [i for i in range(1, 21)]
        self.levelB = [i for i in range(21, 41)]
        self.parking_details = {}

    def assign_spot(self, vehicle_number):
        
        if len(self.levelA):
            spot = self.levelA.pop(0)
            self.parking_details[vehicle_number] = {"level": "A", "spot": spot}
            print("Parking allotted in level : A spot : {}".format(spot))
            
        elif len(self.levelB):
            spot = self.levelB.pop(0)
            self.parking_details[vehicle_number] = {"level": "B", "spot": spot}
            print("Parking allotted in level : B spot : {}".format(spot))
            
        else:
            print("No parking slots available")
            
        print("")

    def retrieve_parking_spot(self, vehicle_number):
        
        if vehicle_number in self.parking_details:
            return self.parking_details[vehicle_number]
        return None


parking = ParkingLot()


def display_menu():
    print("To assign a parking spot, enter 1")
    print("To retrieve the parking spot, enter 2")
    print("To exit, enter any other key\n")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
    
        if choice == "1":
            vehicle_number = input("\nEnter Vehicle Number: ")
            parking.assign_spot(vehicle_number)
            
        elif choice == "2":
            vehicle_number = input("\nEnter Vehicle Number: ")
            parking_details = parking.retrieve_parking_spot(vehicle_number)
            if parking_details is not None:
                print("{}\n".format(parking_details))
            else:
                print("\nNo vehicle parked with this number\n")
                
        else:
            break

        
if __name__ == "__main__":
    main()
