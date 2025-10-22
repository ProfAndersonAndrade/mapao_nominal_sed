from transform.tranform import transformer, disciplinas
from transform.style import style_dataframe, style_metrics, style_common, style_media, footer
from transform.media import calcular_media_geral 
from animation.anima import animation
import pandas as pd
import streamlit as st
import time

# Título da aplicação
st.markdown('''
# Mapão Nominal Sala do Futuro
''')

# Upload do arquivo
arquivo = st.file_uploader(
    'Arraste ou faça o upload do seu arquivo:',
    type=['xls', 'xlsx'],
)
if arquivo:
    new_df = transformer(arquivo)  # Processamento dos dados do arquivo

    # Configuração da barra lateral
    with st.sidebar:
        with st.spinner("Carregando..."):
            time.sleep(2)  # Simula um carregamento

            # Obtenção e ordenação da lista de alunos
            alunos = new_df[[('Aluno', 'Nome'), ('Aluno', 'Sit')]].dropna()            
            alunos_df = new_df.sort_values(by=[('Aluno', 'Sit'), ('Aluno', 'Nome')])
            alunos_ordenados = alunos_df[('Aluno', 'Nome')].tolist()
            aluno_selecionado = st.selectbox("Selecione um aluno", alunos_ordenados)  # Seleção do aluno
            
        # Exibição de animação na barra lateral
        for _ in range(30):
            st.sidebar.write('')
        animation('https://lottie.host/4001cd1a-e4c0-47ac-a788-bba60042ec11/aJUAJq3Udo.json')
            
    # Exibir as notas do aluno selecionado
    if aluno_selecionado:
        # Filtrar os dados para o aluno selecionado
        notas_aluno = new_df[new_df[('Aluno', 'Nome')] == aluno_selecionado]
                
        # Obtenção das disciplinas, excluindo 'Total'
        materias = sorted(disciplinas(new_df))
        materias.remove('Total')
        
        # Preparação dos DataFrames para notas e métricas
        nota_formatada = pd.DataFrame(index=materias, columns=['M', 'F', 'AC'])                
        metricas = pd.DataFrame(index=materias, columns=['TF','Fre(%)','FT An.','Fre.An(%)'])
                
        # Preenchimento das notas para cada disciplina
        for disci in materias:
            nota_formatada.loc[disci] = [
                pd.to_numeric(notas_aluno.get((disci, 'M'), pd.Series([0])).iloc[0], errors='coerce'),
                pd.to_numeric(notas_aluno.get((disci, 'F'), pd.Series([0])).iloc[0], errors='coerce'),
                pd.to_numeric(notas_aluno.get((disci, 'AC'), pd.Series([0])).iloc[0], errors='coerce')
            ]
        nota_formatada.fillna(0, inplace=True)  # Preenchimento de NaN com 0

        # Extração de métricas específicas
        total_faltas = notas_aluno[('Total', 'TF')].values[0]
        freq_bim = notas_aluno[('Total', 'Fre(%)')].values[0]
        faltas_anuais = notas_aluno[('Total', 'FT An.')].values[0]
        freq_anual = notas_aluno[('Total', 'Fre.An(%)')].values[0]
        media_geral = calcular_media_geral(nota_formatada)  # Cálculo da média geral das notas

        # Estilização do DataFrame de notas
        styled_df = style_dataframe(nota_formatada)
            
        # Layout de colunas para exibição de dados
        col1, col2 = st.columns([6, 4])
    
        # Exibição das notas formatadas
        col1.write(styled_df.to_html(), unsafe_allow_html=True)
        
        # Exibição de métricas na segunda coluna
        with col2:
            st.markdown('#### Faltas')
            st.markdown(style_common(int(total_faltas)), unsafe_allow_html=True)
            st.markdown('#### Freq. Bim(%)')
            st.markdown(style_metrics(freq_bim), unsafe_allow_html=True)
            st.markdown('#### Faltas Anuais')
            st.markdown(style_common(int(faltas_anuais)) , unsafe_allow_html=True)
            st.markdown('#### Freq. Anual(%)')
            st.markdown(style_metrics(freq_anual), unsafe_allow_html=True)
            st.markdown('#### Média Notas')
            st.markdown(style_media(media_geral), unsafe_allow_html=True)

# Adiciona o rodapé personalizado
st.markdown(footer(), unsafe_allow_html=True)

