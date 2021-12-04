#Number of cars
cars = 100
#How many people we can fit per car
space_in_a_car = 4.0
#How many drivers
drivers = 30
#How many people need rides
passengers = 90
#How many free cars there are
cars_not_driven = cars - drivers
#How many cars are being driven
cars_driven = drivers
#Total number of people we can fit in the cars available
carpool_capacity = cars_driven * space_in_a_car
#How many people should be in each car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We have to put about", average_passengers_per_car, "in each car.")
