cars = 100
space_in_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passenger_per_car = int(passengers / cars_driven)

print("There are",cars ,"cars available")
print("There only", drivers, "drivers available")
print("there will be", cars_not_driven , "empty car")
print("we can transport ",carpool_capacity,"people today")
print(f"we have {passengers} passenger to carpool today")
print("we need to put abput", average_passenger_per_car, "in each car")