from random import random

def make_random(number_of_elements, range_of_random):
  i = 0
  number_array = []
  for num in range(0, number_of_elements):
    this_num = random() * range_of_random
    this_num = int(this_num)
    number_array.append(this_num)
  return number_array

def square_list(number_list):
  squared_list = [i * i for i in number_list]
  return squared_list

random20 = make_random(20, 49)
print("\n")
print("Numbers:", random20)
print("\n")
print("Squared List:", square_list(random20))