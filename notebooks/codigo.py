
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from statsmodels.stats.proportion import proportions_ztest
import math as math
from scipy import stats
import importlib
import project_functions

importlib.reload(project_functions)
from project_functions import *

df_pt1 = pd.read_csv('../raw_data/df_final_web_data_pt_1.txt')
df_pt2 = pd.read_csv('..//raw_data/df_final_web_data_pt_2.txt')
df_users = pd.read_csv('../raw_data/df_final_demo.txt')
df_exp =pd.read_csv('../raw_data/df_final_experiment_clients.txt')

# cleaning the columns : changing the columns headers to correct format
# for more information about this function --> cf project_functions.py notebook
clean_my_columns = project_functions.clean_my_columns

clean_my_columns(df_exp)
clean_my_columns(df_users)
clean_my_columns(df_pt1)
clean_my_columns(df_pt2)

df_users.info()
df_exp.info()
df_pt1.info()
df_pt2.info()

display(df_exp)
df_exp.shape

display(df_users)
df_users.shape

display(df_pt1.head())
df_pt1.shape

# Combining df_pt_1 and df_pt_2:
df_footprint=pd.concat([df_pt1,df_pt2])

#Now we take a overview about the concatenated table
display(df_footprint.head())

print(f"shape of pt1: {df_pt1.shape}")
print(f"shape of pt2: {df_pt2.shape}")
print(f"shape of the concat: {df_footprint.shape}")

# Number of clients
df_footprint['client_id'].nunique()

df_users['client_id'].nunique()

df_exp['client_id'].nunique()

df_clients = df_users.merge(df_exp, on='client_id', how='left')

df_clients = df_clients.reset_index(drop=True)

display(df_clients)
df_clients.shape

find_duplicates(df_clients)

missing_clients_data = df_clients.isnull().sum()
print(missing_clients_data)

df_clients_nd_nn = df_clients.dropna()

print(df_clients_nd_nn)

df_clients_nd_nn.shape

df_clients_nd_nn['client_id'].nunique()

display(df_clients_nd_nn['clnt_tenure_yr'])
print(f"Valor mínimo: {df_clients_nd_nn['clnt_tenure_yr'].min()}")
print(f"Valor máximo: {df_clients_nd_nn['clnt_tenure_yr'].max()}")

df_clients_nd_nn['clnt_tenure_yr'] = df_clients_nd_nn['clnt_tenure_yr'].astype(int)

df_clients_nd_nn['clnt_tenure_yr'].unique()

display(df_clients_nd_nn['clnt_tenure_mnth'])
print(f"Valor mínimo: {df_clients_nd_nn['clnt_tenure_mnth'].min()}")
print(f"Valor máximo: {df_clients_nd_nn['clnt_tenure_mnth'].max()}")

df_clients_nd_nn['clnt_tenure_mnth'] = df_clients_nd_nn['clnt_tenure_mnth'].astype(int)

df_clients_nd_nn['clnt_tenure_mnth'].unique()

# Comprobamos si hay filas donde los meses son mayores o iguales a 12 pero no coinciden con los años
df_inconsistencias = df_clients_nd_nn[(df_clients_nd_nn['clnt_tenure_mnth'] >= 12) & (df_clients_nd_nn['clnt_tenure_yr'] != df_clients_nd_nn['clnt_tenure_mnth'] // 12)]

# Mostrar filas con inconsistencias
print(df_inconsistencias)

df_inconsistencias.shape

df_clients_nd_nn_in = df_clients_nd_nn.drop(df_inconsistencias.index)

display(df_clients_nd_nn_in['clnt_age'])
print(f"Valor mínimo: {df_clients_nd_nn_in['clnt_age'].min()}")
print(f"Valor máximo: {df_clients_nd_nn_in['clnt_age'].max()}")

df_clients_nd_nn_in['clnt_age'] = df_clients_nd_nn_in['clnt_age'].round()

df_clients_nd_nn_in['clnt_age'] = df_clients_nd_nn_in['clnt_age'].astype(int)

# Supongamos que tu DataFrame tiene una columna llamada 'edad'
df_clients_nd_nn_in['clnt_age'].value_counts().sort_index().plot(kind='bar', figsize=(10,6))

# Añadir título y etiquetas
plt.title("Client's age distribution")
plt.xlabel('Age')
plt.ylabel('Clients')

# Mostrar el gráfico
plt.show()

unique_genders = df_clients_nd_nn_in['gendr'].unique()
count_genders = df_clients_nd_nn_in['gendr'].value_counts()
print("\nValores únicos en la columna 'gendr':")
print(unique_genders)
print(count_genders)

df_clients_nd_nn_in['gendr'] = df_clients_nd_nn_in['gendr'].replace('X', 'U')

display(df_clients_nd_nn_in['num_accts'])
print(f"Valor mínimo: {df_clients_nd_nn_in['num_accts'].min()}")
print(f"Valor máximo: {df_clients_nd_nn_in['num_accts'].max()}")

df_clients_nd_nn_in['num_accts'].unique()

df_clients_nd_nn_in['num_accts'] = df_clients_nd_nn_in['num_accts'].astype(int)

df_clients_nd_nn_in['num_accts'].value_counts()

display(df_clients_nd_nn_in['bal'])
print(f"Valor mínimo: {df_clients_nd_nn_in['bal'].min()}")
print(f"Valor máximo: {df_clients_nd_nn_in['bal'].max()}")

display(df_clients_nd_nn_in['calls_6_mnth'])
print(f"Valor mínimo: {df_clients_nd_nn_in['calls_6_mnth'].min()}")
print(f"Valor máximo: {df_clients_nd_nn_in['calls_6_mnth'].max()}")

df_clients_nd_nn_in['calls_6_mnth'].value_counts()

df_clients_nd_nn_in['calls_6_mnth'] = df_clients_nd_nn_in['calls_6_mnth'].astype(int)

display(df_clients_nd_nn_in['logons_6_mnth'])
print(f"Valor mínimo: {df_clients_nd_nn_in['logons_6_mnth'].min()}")
print(f"Valor máximo: {df_clients_nd_nn_in['logons_6_mnth'].max()}")

df_clients_nd_nn_in['logons_6_mnth'].value_counts()

df_clients_nd_nn_in['logons_6_mnth'] = df_clients_nd_nn_in['logons_6_mnth'].astype(int)

df_clients_nd_nn_in = df_clients_nd_nn_in.reset_index(drop=True)

# Let's check how many duplicated rows there are.
duplicates = df_footprint.duplicated(keep=False)
df_duplicates = df_footprint[duplicates]

print(df_duplicates)

# Deleting all duplicates
df_footprint_nd = df_footprint.drop_duplicates(keep=False)

print(df_footprint_nd)

#create list of client_ids: 
clients_list = list(df_clients_nd_nn_in['client_id'])
clients_list

#creating new dataframe with footprints only with clients from clients list
df_sample_fp = df_footprint_nd.loc[df_footprint_nd['client_id'].isin(clients_list)]

df_sample_fp.shape

df_sample_fp = df_sample_fp.reset_index(drop=True)

missing_data = df_sample_fp.isnull().sum()
print(missing_data)

has_nan = df_sample_fp.isna().any().any()

if has_nan:
    print("El DataFrame contiene valores NaN.")
else:
    print("El DataFrame no contiene valores NaN.")

df_sample_fp = df_sample_fp.drop(['visitor_id', 'visit_id'], axis=1)

df_sample_fp

# Convertir la columna date_time a tipo datetime
df_sample_fp['date_time'] = pd.to_datetime(df_sample_fp['date_time'])

# Transformar el DataFrame usando pivot
df_pivot = df_sample_fp.pivot_table(index='client_id', columns='process_step', values='date_time', aggfunc='min')
# Mostrar el DataFrame transformado
print(df_pivot)

ordered_columns = ['start', 'step_1', 'step_2', 'step_3', 'confirm']
df_pivot = df_pivot[ordered_columns]

# Mostrar el DataFrame transformado y ordenado
print(df_pivot)

df_pivot = df_pivot.reset_index()

#creating new dataframe with footprints only with clients from clients list
df_pivot = df_pivot.loc[df_pivot['client_id'].isin(clients_list)]

df_pivot.shape

df_merged = pd.merge(df_pivot, df_clients_nd_nn_in[['client_id', 'variation']], on='client_id', how='left')

print(df_merged)

df_merged = df_merged.reset_index()

#PUNTO 3 EMPIEZA AQUÍ

























