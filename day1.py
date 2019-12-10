import math

mass_list = []
fuel_total = 0
fuels = []

def calc_fuel(mass):
    fuel = math.floor((mass/3) - 2)
    return fuel

with open('day1innputs.txt', 'r') as f:
    for line in f:
        mass_list.append(int(line))

for mass in mass_list:
    fuel_req = calc_fuel(mass)
    fuel_total += fuel_req
    while fuel_req > 0:
        fuel_req = calc_fuel(fuel_req)
        if fuel_req > 0:
            fuel_total += fuel_req

print(fuel_total)