import pandas as pd

df = pd.read_csv('train.csv')

spe_df = df.loc[df['EnjoySport'].str.upper()=='YES'] #'Yes' case
gene_df = df.loc[df['EnjoySport'].str.upper()=='NO'] #'No' case

# remove the result column from dataset
spe_df = spe_df.iloc[:,:-1]
gene_df = gene_df.iloc[:,:-1]

base = spe_df.iloc[0] # 1st set of value of 'Yes' case

print(spe_df,gene_df,base, sep='\n\n')

for x in range(1,len(spe_df)):
    base = base.where(spe_df.iloc[x]==base,other='?')

print('Specific :- \n',base.values)

'''
# Elimination of Candidate
for x in range(len(gene_df)):
    base = base.where(base!=gene_df.iloc[x] , other='?')

print('Final General :-')

for i,x in enumerate(base):
    if x !='?':
        l = ['?']*len(base)
        l[i] = x
        print(l)

'''