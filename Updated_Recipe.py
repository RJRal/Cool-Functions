

# This is a fun function to print an updated recipe! Mamas_cake list the ingredients of an old cake recipe. I want to update this recipe by adding some more ingredients. The function Updated_Recipie would join the old and new lists without repetition 

import numpy as np 

def Updated_Recipie(old_list, new_list):
 
	common_ingredient=list()

	for i in range(len(old_list)):
		for j in range(len(new_list)):
			if old_list[i]==new_list[j]:
				common_ingredient.append(old_list[i])

	new_list_minus_common_ingredient=list()

	for jj in range(len(new_list)):
		for kk in range(len(common_ingredient)):
			if new_list[jj]!=common_ingredient[kk]:
				new_list_minus_common_ingredient.append(new_list[jj])

	updated_list=new_list_minus_common_ingredient+old_list 

	return(print('For the updated recipie you need the following ingredients: '),updated_list)
	
	

Mamas_cake=['sugar','butter','flower','cinnamon','apple']   

additional_yumminess=['milk','butter','cream'] 

Updated_Recipie(Mamas_cake, additional_yumminess)

