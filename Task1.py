#Q1. Write a function in python to sum up a given set of numbers other than itself Input: An array of n integers nums, Output: An array output such that output[i] is equal to the sum of all the elements of nums except nums[i]. For example, given [1,2,3,4], return [9,8,7,6].

def int_list(colVals):   #list is passed to the function
	arr=[]
	for n in range(len(colVals)):
		array_a=[]
		global array_a
		array_a[0:len(colVals)] = colVals
		del array_a[n]
		arr.append(sum(array_a))
	return arr
int_list([1,2,3,4])