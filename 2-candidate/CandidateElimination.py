import pandas as pd
import numpy as np
data = pd.read_csv('train.csv')
concept = np.array(data)[:,:-1]
target = np.array(data)[:,-1]

def train(concept,target):
    specific_h = concept[0].copy()
    general_h=[['?' for x in range(len(specific_h))] for x in range(len(specific_h))]
    
    for i,h in enumerate(concept):
        if target[i] == 'yes':
            for x in range(len(specific_h)):
                if(h[x] != specific_h[x]):
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        else:
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x]='?'
                    
        print(f"Iteration[{i+1}]")
        print("Specific: ", specific_h)
        print("General: ", general_h)
        print("\n\n")
    
    general_h =[general_h[i] for i, val in enumerate(general_h) 
    								if val!= ['?' for x in range(len(specific_h))]]
    return specific_h, general_h

specific , general = train(concept,target)
print("Final hypothesis: ")
print("Specific hypothesis: ", specific)
print("General hypothses: ", general)