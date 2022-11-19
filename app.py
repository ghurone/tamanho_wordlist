from code import byte_counter, byte_formatter

import streamlit as st
import numpy as np
import string

# Configurações da página
st.set_page_config(
   page_title="O tamanho de uma wordlist",
   page_icon="💾",
   layout="centered",
   initial_sidebar_state="collapsed"
)

can_run = True

st.title("O quão grande uma _wordlist_ pode ser?")

# Configurações
n = st.slider('Tamanho das palavras geradas', 1, 32, value=8)

col1, col2 = st.columns(2)  # Separa a tela em duas colunas

# WIDGETS DA PRIMEIRA COLUNA

col1.write('Quais caracteres farão parte?')

checksbox = np.array([col1.checkbox('Números', value=True),
                      col1.checkbox('Letras minúsculas'),
                      col1.checkbox('Letras maiúsculas'),
                      col1.checkbox(f'Caracteres especiais')])

if np.all(checksbox==False):
    can_run = False
    st.error('Selecione ao menos um conjunto de caracteres!') 
    # a mensagem de erro aparece nas duas colunas.

# WIDGETS DA SEGUNDA COLUNA

col2.write('Considerar as quebras de linha?')
break_line = col2.checkbox('Sim', value=True)

col2.write('Sistema de unidade')
unit = col2.radio('a', options=['SI', 'IEC'], label_visibility='collapsed')

# Resultado
if can_run:
    data = np.array([string.digits,
                     string.ascii_lowercase,
                     string.ascii_uppercase,
                     string.punctuation])
    
    chars = ''.join(data[checksbox])
    
    # tamanho dos arquivos em bytes
    tam = byte_counter(chars, word_length=n,break_line=break_line)
    # tamanho dos arquivos formatados para a unidade certa
    tam_format = byte_formatter(tam, unit=unit)
    
    st.write(f'## Tamanho do arquivo: {tam_format}')