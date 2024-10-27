import streamlit as st

#Define the layout of the page
st.set_page_config(
    page_title="Configuração",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Porcentagem Ideal:")

colunslide, colunporcent, colunspace = st.columns(spec=[1,1,1], gap='large', vertical_alignment='top')


with colunslide:
   st.markdown("#### Ações")
   acoes = st.slider("",min_value=0, max_value=100, key=0)
   st.markdown("#### Fills")
   fills = st.slider("",min_value=0, max_value=100, key=1)
   st.markdown("#### Stocks")
   stocks = st.slider("",min_value=0, max_value=100, key=2)
   st.markdown("#### Criptomoedas")
   cripto = st.slider("",min_value=0, max_value=100, key=3)
   st.markdown("#### Renda Fixa")
   renda_fixa = st.slider("",min_value=0, max_value=100, key=4) 


with colunporcent:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"### {acoes}%")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"### {fills}%")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"### {stocks}%")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"### {cripto}%")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.markdown(f"### {renda_fixa}%")