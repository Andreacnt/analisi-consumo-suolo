# 10 COMANDI PYTHON (PANDAS) PER DATA ANALYST
# Apri questo file in VS Code, seleziona una riga e premi Shift+Enter
# Oppure esegui tutto: tasto destro > Run Python File in Terminal

import pandas as pd

print("=== 1. CARICARE E GUARDARE ===")
df = pd.read_csv('dati.csv')          # carica CSV
df.head()                              # prime 5 righe
df.shape                               # (righe, colonne)
df.columns                             # elenco colonne
df.dtypes                              # tipo di ogni colonna

print("=== 2. ESPLORARE ===")
df.info()                              # tipo + valori non nulli
df.describe()                          # media, std, min, max, quartili
df['regione'].value_counts()           # conta frequenze
df['regione'].nunique()                # quanti valori unici

print("=== 3. FILTRARE ===")
df[df['regione'] == 'Lombardia']                       # una condizione
df[(df['anno'] >= 2020) & (df['stock_pct'] > 10)]      # due condizioni
df[df['comune'].str.contains('Milano')]                 # testo contiene

print("=== 4. SELEZIONARE COLONNE ===")
df[['comune', 'stock_pct']]                              # solo queste
df.drop(columns=['colonna_inutile'], inplace=True)      # rimuovi colonna

print("=== 5. RAGGRUPPARE (groupby) ===")
df.groupby('regione')['stock_pct'].mean()                                    # media per gruppo
df.groupby('regione').agg(
    media=('stock_pct', 'mean'),
    massimo=('stock_pct', 'max'),
    comuni=('comune', 'nunique')
).reset_index()                                                                # più metriche

print("=== 6. ORDINARE ===")
df.sort_values('stock_pct', ascending=False)              # decrescente
df.sort_values(['regione', 'stock_pct'], ascending=[True, False])  # multi-colonna

print("=== 7. CREARE NUOVE COLONNE ===")
df['anno_fine'] = 2024                                    # valore fisso
df['stock_perc_su_media'] = df['stock_pct'] / df['stock_pct'].mean()  # da altre colonne

print("=== 8. UNIRE DUE DATASET ===")
pd.merge(df1, df2, on='codice_comune', how='left')       # come SQL JOIN
pd.concat([df1, df2], axis=0)                              # impila righe

print("=== 9. GRAFICO VELOCE ===")
df.groupby('anno')['incremento_netto_ha'].sum().plot(kind='line')   # linea
df.groupby('regione')['stock_pct'].mean().plot(kind='bar')          # barre
df['stock_pct'].hist(bins=30)                                        # istogramma

print("=== 10. SALVARE ===")
df.to_csv('output.csv', index=False)                       # CSV
df.to_parquet('output.parquet', index=False)               # Parquet (più veloce)
