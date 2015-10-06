import math;
import random;

# a Python program that implements a quicksort algorithm using list comprehension
def quicksort(lst): # senza duplicati
	if(len(lst) <= 1):
		return lst;
	pivot = math.floor(random.random() * len(lst));
	
	temp_list = lst[0:pivot]+lst[pivot+1:];
	smaller = [x for x in temp_list if x <= lst[pivot]];
	larger = [x for x in temp_list if x >= lst[pivot]];
	return quicksort(smaller) + [lst[pivot]] + quicksort(larger);
		
	
lista = [3, 2, 5, 1, 23];
print("Input list: ", lista);
print("-------------------------------------------------------------------------------------");
print("Output list: ", quicksort(lista));