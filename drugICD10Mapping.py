import pandas as pd

cuiSnomed = pd.read_csv(r"C:\Users\sgaox\Desktop\mapping\out1.csv") 
cuiSnomed = cuiSnomed.drop('Unnamed: 0', 1)


snomedICD10 = pd.read_csv(r"C:\Users\sgaox\Desktop\mapping\snomedICD10.csv") 
snomedICD10 = snomedICD10.drop_duplicates(keep = False)
snomedICD10 = snomedICD10.dropna(how = 'any')
snomedICD10["mapTarget"] = snomedICD10["mapTarget"].str.replace("\?", "")


cuiICD10 = cuiSnomed.merge(snomedICD10, on = 'snomed', how = 'left')
cuiICD10 = cuiICD10.dropna(how = 'any')
cuiICD10 = cuiICD10.rename(columns={'cui': 'umls_cui_from_meddra'})


drugBank = pd.read_csv(r"C:\Users\sgaox\Desktop\mapping\2.tsv.txt", sep='\t')
drugBank = drugBank.drop('Unnamed: 0', 1)
drugBank = drugBank[['drugbank_id','drugbank_name',
                     'side_effect_name','umls_cui_from_meddra']]


drugICD10 = drugBank.merge(cuiICD10, on = 'umls_cui_from_meddra', how = 'left')
drugICD10 = drugICD10.dropna(how = 'any')
drugICD10.to_csv(r'C:\Users\sgaox\Desktop\mapping\drugICD10.csv')