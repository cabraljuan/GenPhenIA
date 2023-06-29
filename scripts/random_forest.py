


# Libraries
import json
import pandas as pd



PATH = "E:/articulos/GenPhenIA/"




# Open real datasetes
with open(f'{PATH}data/real/bitgenia.json','r') as f:
    bitgenia = json.load(f)

with open(f'{PATH}data/real/clinvar.json','r') as f:
    clinvar = json.load(f)
    
# Open "gene-phenotype" dicts
with open(f'{PATH}data/simulated/gene_phenotype_dict.json','r') as f:
    gene_phenotype = json.load(f)

with open(f'{PATH}data/simulated/phenotype_gene_dict.json','r') as f:
    phenotype_gene = json.load(f)
  
# Subset dataframes (for now)


# Crear una lista de tuplas con la clave y los valores concatenados como strings
formatted_data = [(key, ', '.join(map(str, value))) for key, value in phenotype_gene.items()]

# Convertir la lista de tuplas a un DataFrame de pandas
gene_phenotype = pd.DataFrame(formatted_data, columns=['key_hp', 'gene_values'])

# Subset dataframe (for now)
gene_phenotype = gene_phenotype.sample(n=500, random_state=42)


# Separando la columna 'gen_values' en múltiples columnas
# y luego aplicando el one-hot encoding
genes = gene_phenotype['gene_values'].str.split(',').apply(set).apply(list)
one_hot = pd.get_dummies(genes.apply(pd.Series).stack()).sum(level=0)

# Uniendo las columnas key_hp y el one-hot encoding en un nuevo DataFrame
gene_phenotype = gene_phenotype[['key_hp']].join(one_hot)


# Objetive: assign genes from a patient with certain phenotypes
