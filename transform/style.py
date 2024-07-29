import requests

# Separar o style em cada parte da tabela para aplicar o lambda
def style_dataframe(df):

    return df.style.apply(lambda y: ['background-color: #ffffff' for i in y], axis=1).set_table_styles(
        [{
            'selector': 'th',
            'props': [
                ('background-color', '#f0f0f0'),
                ('color', '#01579b'),
                ('font-family', 'Arial, sans-serif'),
                ('font-size', '18px'),
                ('text-align', 'center'),
                ('width', 'auto'),  # Ajusta a largura da tabela
                ('height', 'auto'),
            ]
        }, 
        {
            'selector': 'td',
            'props': [
                ('color', '#000000'),
                ('font-family', 'Arial, sans-serif'),
                ('font-size', '16px'),
                ('text-align', 'center'),
                
            ]
        },
        {
            'selector': 'td, th',
            'props': [
                ('border', '2px solid #cfd8dc')
            ]
        }]
    ).apply(lambda x: ['background-color: cyan' if (x.M >= 5) 
                          else ('background-color: pink' if (x.M < 5) else '') 
                          for i in x], axis=1, subset='M')


def style_metrics(value):
    font_size = '30px'  # Defina o tamanho da fonte desejado
    if value >= 85:
        return f'<p style="color: green; font-size: {font_size};"><strong>{value}</strong></p>'
    elif value >= 75:
        return f'<p style="color: orange; font-size: {font_size};"><strong>{value}</strong></p>'
    else:
        return f'<p style="color: red; font-size: {font_size};"><strong>{value}</strong></p>'

def style_media(value):
    font_size = '35px'  # Defina o tamanho da fonte desejado
    if value >= 5:
        return f'<p style="color: blue; font-size: {font_size};"><strong>{value:.2f}</strong></p>'    
    else:
        return f'<p style="color: red; font-size: {font_size};"><strong>{value:.2f}</strong></p>'


def style_common(value):
    font_size = '30px'  # Defina o tamanho da fonte desejado
    return f'<p style="color: black; font-size: {font_size};"><strong>{value}</strong></p>'

def footer():
    return  '''
            <style>
            footer {
                visibility: hidden;
            }

            .footer-custom {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                color: #000;
                text-align: center;
                padding: 5px;
                font-size: 10px;
            }

            .footer-custom img {
                width: 16px; /* Ajuste o tamanho conforme necessário */
                margin-right: 5px;
                vertical-align: middle;
            }

            .footer-custom a {
                color: #0366d6;
                text-decoration: none;
            }

            .footer-custom a:hover {
                text-decoration: underline;
            }
            </style>

            <div class="footer-custom">
                <a href="https://opensource.org/licenses/MIT" target="_blank">MIT License</a></p>
                <p>Este aplicativo é destinado apenas à visualização e não armazena ou salva dados de terceiros.
                  Todos os dados são processados localmente e temporariamente para fins de exibição.</p>
                <p style="text-align:center;">By Prof. Anderson | 
                <a href="https://github.com/ProfAndersonAndrade" target="_blank">
                    <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" alt="GitHub Logo">
                </a> 
                <a href="mailto:andersonandrades@prof.educacao.sp.gov.br">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="Gmail Logo">
                </a>
                </p>
            </div>
            '''


    
