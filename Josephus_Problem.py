# k : constant, n : number of people

import numpy as np

def josephus(n, k): 
  
	if (n == 1): 
		return 1

	else:
		return (josephus(n - 1, k) + k-1) % n + 1


n_arr=np.arange(5,100)

k_arr=np.arange(2,10)

josephus_array=np.zeros((len(n_arr),len(k_arr)))

for nn in range(len(n_arr)): 
     n=n_arr[nn] 
     for kk in range(len(k_arr)): 
         k=k_arr[kk]           
         josephus_array[nn,kk]=josephus(n,k) 


# Visualize 

import matplotlib.pyplot as plt
import seaborn as sns

f, ax = plt.subplots(figsize=(10, 7))

cmap = sns.cubehelix_palette(light=1, as_cmap=True)

sns.heatmap(josephus_array, cmap=cmap)

plt.title("The Josephus Problem",size=16)

ax.set_xlim([k_arr[0],k_arr[-1]]) 

ax.set_ylim([n_arr[0],n_arr[-1]])

plt.show(block=False)

































