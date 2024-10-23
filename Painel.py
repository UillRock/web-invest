import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.graph_objects as go

#Define the layout of the page
st.set_page_config(
    page_title="Painel",
    page_icon="🤑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the sections of the page
st.sidebar.header("")

# Define the title of the page
#st.title("Meus Aportes")

col_aporte, col_espaco = st.columns([1,5], gap='large', vertical_alignment='top')

# coluna de aporte
with col_aporte:
    # Define the contribution form
    st.write("## Aportes")
    aporte = st.number_input("Quanto você vai aportar?", min_value=0.0)


col_tabela, col_dashboard = st.columns([0.5,0.5], gap='large', vertical_alignment='top')

with col_tabela:

    # Define the data table
    df = pd.DataFrame({
        "CÓDIGO": ["HGLG11"],
        "NOME": ["ITAUSA"],
        "% REAL": [38.78],
        "% IDEAL": [25.00],
        "R$ REAL": [190.00],
        "R$ IDEAL": [122.50],
        "QTD": [1],
        "APORTE": [0.00]
    })

    # Delete the first column
    #df = df.drop(df.columns[0], axis=1)

    # Increase the table size
    pd.set_option('display.max_colwidth', 200)

    
    # Define the calculation function
    def calcular_aporte(aporte, df):
        """Calculates the contribution for each asset.

        Args:
            aporte: The amount of the contribution.
            df: The DataFrame of assets.

        Returns:
            The DataFrame of assets with the calculated contribution.
        """

        # Calculate the contribution for each asset
        df["APORTE"] = (df["% REAL"] / 100) * aporte

        return df

    #Define the calculate button
    calcular = st.button("Calcular")

    # If the calculate button is clicked, calculate the contribution and update the table
    if calcular:
        df = calcular_aporte(aporte, df)
    #st.dataframe(df)

    # Define the table of assets
    st.write("## Meus Ativos")
    st.dataframe(df)
    st.table(df)


with col_dashboard:
    st.header("")
    # Create the pie chart
    fig, ax = plt.subplots(figsize=(3, 3))


    # Create the legend patches
    patches = [
    mpatches.Patch(color="#66b3ff", label="Ações"),
    mpatches.Patch(color="#ffcc99", label="FIIS"),
    mpatches.Patch(color="#ff6666", label="Renda Fixa")
    ]

    # Add the legend to the chart
    plt.legend(handles=patches, loc="best", bbox_to_anchor=(1.0, 1.0), title="")   

    # Dados para o gráfico de pizza
    labels = ["Ações", "FIIS", "Renda Fixa"]
    sizes = [38.78, 25, 40.82] 
    colors = ["#66b3ff", "#ffcc99", "#ff6666"]  # Example colors, customize as needed

    # Create the pie chart with transparent background
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90, pctdistance=0.60, 
        wedgeprops={"edgecolor": "black", "linewidth": 1, "antialiased": True})

    # Set the aspect ratio to make the pie chart circular
    ax.axis("auto")

    # Add a title to the chart
    ax.set_title("Minha Rodela - Ativos", fontsize=20)

    # Remove the white background
    fig.patch.set_alpha(0) 
    ax.set_facecolor("none")

    # Display the chart
    st.pyplot(fig)


# # Cria um dataframe de exemplo
# df1 = pd.DataFrame({
#     'Categoria': ['A', 'B', 'C',],
#     'Valor': [10, 20, 30]
# })

# # Cria um gráfico com interatividade
# chart = alt.Chart(df1).mark_bar().encode(
#     x='Categoria',
#     y='Valor',
#     tooltip=['Categoria', 'Valor']
# )

# # Adiciona a legenda ao gráfico
# chart = chart.configure_axis(
#     labelFontSize=14,
#     titleFontSize=16
# ).configure_legend(
#     labelFontSize=14,
#     titleFontSize=16
# )

# # Exibe o gráfico com interatividade
# st.altair_chart(chart, use_container_width=True)

