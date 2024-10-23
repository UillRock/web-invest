import streamlit as st
import matplotlib.pyplot as plt

# Define the layout of the page
st.set_page_config(
    page_title="Ativos",
    page_icon="〽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.header("Pagina de Ativos")

# Dados para o gráfico de pizza
labels = ['Ações', 'FIIS', 'Renda Fixa']
sizes = [38.8, 20.4, 40.8]
colors = ['lightskyblue', 'navajowhite', 'salmon']

# Criar o gráfico de pizza
fig, ax = plt.subplots()
patches, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Adicionar a legenda
ax.legend(patches, labels, loc="upper right", bbox_to_anchor=(1.5, 0.7), title="")

# Remove the white background
fig.patch.set_alpha(0) 
ax.set_facecolor("none")

# Exibir o gráfico no Streamlit
st.pyplot(fig)