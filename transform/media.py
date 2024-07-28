import pandas as pd

def calcular_media_geral(df):
    medias = pd.to_numeric(df['M'], errors='coerce').mean()
    return medias

# Futura implementação
# def alunos_abaixo_da_media(df, media_minima=5):
#     alunos_baixo = df[df['M'] < media_minima]
#     return alunos_abaixo


