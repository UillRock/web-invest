import streamlit as st
import matplotlib.pyplot as plt

# Define the layout of the page
st.set_page_config(
    page_title="Ativos",
    page_icon="〽️",
    layout="wide",
    initial_sidebar_state="expanded"
)

coluntext, coluntextspace = st.columns([4,1])
colunimput, colunspace = st.columns([1,3])
coluntab, colundash = st.columns([2,1], gap='large', vertical_alignment='top')


with coluntext:
    # Define os títulos
    st.write("### Calculadora de Rebalanceamento de Carteira")

with colunimput:
    # Define os inputs
    current_equity = st.number_input("Patrimônio atual (R$)", value=1115.28, step=0.01)
    contribution = st.number_input("Valor aporte (R$)", value=533.22, step=0.01)


with coluntab:
    # Define a tabela de ativos e seus percentuais ideais
    assets = {
        "Ações": {"current": 29.83, "ideal": 25.0},
        "Stocks": {"current": 19.19, "ideal": 20.0},
        "ETFs": {"current": 0.0, "ideal": 5.0},
        "Flls": {"current": 28.25, "ideal": 25.0},
        "Renda Fixa": {"current": 17.2, "ideal": 25.0},
        "Criptomoedas": {"current": 5.55, "ideal": 5.0},
    }

    # Calcula o valor a ser alocado em cada ativo
    allocations = {}
    for asset, percentages in assets.items():
        target_value = (percentages["ideal"] / 100) * (current_equity + contribution)
        current_value = (percentages["current"] / 100) * current_equity
        allocations[asset] = target_value - current_value

    # Mostra os resultados em uma tabela
    st.write("### Recomendações de Alocação:")
    st.table({
        "ATIVO": list(assets.keys()),
        "% ATUAL": [f"{p['current']:.2f}%" for p in assets.values()],
        "% IDEAL": [f"{p['ideal']:.2f}%" for p in assets.values()],
        "QUANTO COLOCAR (R$)": [f"R$ {allocations[a]:.2f}" for a in assets.keys()],
    })


# st.header("Pagina de Ativos")

# # Dados para o gráfico de pizza
# labels = ['Ações', 'FIIS', 'Renda Fixa']
# sizes = [38.8, 20.4, 40.8]
# colors = ['lightskyblue', 'navajowhite', 'salmon']

# # Criar o gráfico de pizza
# fig, ax = plt.subplots()
# patches, texts, autotexts = ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# # Adicionar a legenda
# ax.legend(patches, labels, loc="upper right", bbox_to_anchor=(1.5, 0.7), title="")

# # Remove the white background
# fig.patch.set_alpha(0) 
# ax.set_facecolor("none")

# # Exibir o gráfico no Streamlit
# st.pyplot(fig)
