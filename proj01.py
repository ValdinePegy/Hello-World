# Prjoect01

# Purpose: Prompt the user to enter a floating-point value for distance in rod
# Print the value
# Convert the value to other values in Meters, Feet, Miles and Furlongs
# Print the final values for the converted value


rod = input ( "Input rods: ")
rod_float = float(rod)
print ('You input', rod_float ,'rods.')
print()     
print('Conversions')
meters_per_rod_float = 5.0292
furlongs_per_rod_float = 1/40 
mile_per_rod_float = 5.0292/1609.34 
foot_per_rod_float= 5.0292/0.3048

Meters = round(rod_float * meters_per_rod_float,3)
Feet = round(rod_float * foot_per_rod_float,3)
m = rod_float * mile_per_rod_float # m is mile with values not rounded up
Miles = round(rod_float * mile_per_rod_float,3)
Furlongs = round(rod_float * furlongs_per_rod_float,3)

print('Meters:', Meters)
print('Feet: ', Feet)
print('Miles:', Miles)
print('Furlongs:', Furlongs)

Minutes = round(( 60 * m)/3.1,3) 
print('Minutes to walk', rod_float, 'rods:', Minutes)
