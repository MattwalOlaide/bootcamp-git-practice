#Lodash for python
def unique(l):
	'''
	This function generate a list of unique values from l
	'''
	new_list = []
	for item in l:
		if item not in new_list:
			new_list[len(new_list)]= item
	return new_list
	

def reverse(s):
	'''
	This function generates the reverse of s. s can be a string or a list. It returns the type given to it
	'''
	original_s = s
	s_length = len(original_s)
	new_obj = []
	for item in s:
	    
	    if len(new_obj) == 0:
	        new_obj.append(item)
	    else:
	        new_obj.insert(0,item)
	   
	return (new_obj)
	

def intersection(a,b):
	'''
	This function returns the intersection of a and b - A list of common elements between a and b
	'''
	
	interList = []
	for item1 in a:
		for item2 in b:
		    if item1 == item2:
    			interList.append(item1)
    			
	return  interList
	

def generate(steps):
	pass

def parse_csv(csv_string):
	'''
	This function parses a CSV string as a list. The specification demands that the first row of data represents the column names
	'''
	pass

def frequency(needle, haystack):
	'''
	This function returns the number of times needle appears in haystack
	'''
	num_of_needles = 0
	for item in haystack:
		if item == needle:
			num_of_needles += 1
	return num_of_needles
	

def sort(l):
	'''
	This function returns a sorted version of l
	'''

	pass
