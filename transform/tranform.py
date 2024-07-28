import pandas as pd

def data_frame(file_path):
    # Carregar os dados do arquivo Excel
    df = pd.read_html(file_path, skiprows=11, header=[0, 2])
    df = df[0].dropna(how='all')
    return df

def new_dataframe(dataframe):
    # Identificar as disciplinas disponíveis no DataFrame
    available_columns = dataframe.columns.tolist()
        
    # Identificar e manter apenas as colunas relevantes ('Nome', 'Sit', 'M', 'F', 'AC', 'Total')
    colunas_relevantes = []
    
    for col in available_columns:
        if col[1] in ['Nome', 'Sit', 'M', 'F', 'AC', 'TF', 'Fre(%)', 'FT An.', 'Fre.An(%)']:
            colunas_relevantes.append(col)            
     
    # Selecionar as colunas específicas para o novo DataFrame
    new_df = dataframe[colunas_relevantes]
    
    return new_df


def disciplinas(dataframe):
    # Identificar as disciplinas disponíveis no DataFrame
    available_columns = dataframe.columns.tolist()    
    dis = []
    for col in available_columns:
        if col[1] in ['M', 'F', 'AC','TF', 'FRE(%)', 'FT AN.', 'FRE.AN(%)']:
            dis.append(col[0])    
    disciplinas_unicas = list(set(dis))  
    return disciplinas_unicas


def transformer(data):    
    dataframe = data_frame(data)
    new_df = new_dataframe(dataframe)
    #new_df.to_csv('output.csv') # Caso necessidade de salvar um csv
    return new_df

# # Teste de funções
# if __name__ == '__main__':
#     data = 'input.xls'
#     df = transformer(data)  
#     # me = metric(df)
#     # print(me)
#     disci = disciplinas(df)  
#     print(disci)
#     #print(disci)
    


