import pandas as pd

df = pd.read_csv('finds.csv')

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