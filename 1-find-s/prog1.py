import numpy as np
import pandas as pd

data = pd.read_csv('finds.csv')

def train(concepts, target):
	for i,val in enumerate(target):
		if val=='Yes':
			specific_h = concepts[i]
			
	for i,h in enumerate(concepts):
			if target[i] == 'Yes':
				for x in range(len(specific_h)):
					if h[x] != specific_h[x]:
						specific_h[x] = '?'
	
	return specific_h

concepts = np.array(data.iloc[:,0:-1])
target = np.array(data.iloc[:,-1])

print(train(concepts,target))