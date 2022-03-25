def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump - mpg*fuel_left <= 0
    
    
print(zero_fuel(62, 24, 3))