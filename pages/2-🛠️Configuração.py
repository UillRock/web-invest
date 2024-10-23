import streamlit as st

#Define the layout of the page
st.set_page_config(
    page_title="Configuração",
    page_icon="🛠️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Configurações")

colun1, colun2, colun3 = st.columns(spec=[0.3,1,1], gap='large', vertical_alignment='top')


with colun1:
    # Adicionar espaçamento entre os elementos
    st.write("")
    st.write("## FIIs")


with colun2:

    slider = st.slider("", min_value=0, max_value=100)


with colun3:
    st.write("")
    st.markdown(f"## {slider}%")