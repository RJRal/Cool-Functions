
# This is a script to find a function that when given 2 arrays, the function returns a new array with the shared elements removed. I will call this function "function_unique"  

A=(1,2,3); B=(2,4) # we need to get c=(1,3,4)

def function_unique(a1,a2):

	list_a1=list()

	for i in range(len(a1)):
		count_a1=0.0
		for j in range(len(a2)):

			if a1[i]==a2[j]:
				count_a1 +=1.0 

		if count_a1==0.0:
			list_a1.append(a1[i])  #we are choosing the elements unique to a1

	list_a2=list()

	for i in range(len(a2)):
		count_a2=0.0
		for j in range(len(a1)):

			if a2[i]==a1[j]:
				count_a2 +=1.0

		if count_a2==0.0:
			list_a2.append(a2[i])  #we are choosing the elements unique to a1

	list_a1_a2=list_a1+list_a2
	return(list_a1_a2)


function_unique(A,B)








