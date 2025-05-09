import streamlit as st

st.title("Calculadora 3D")

gramos = st.number_input("Peso en gramos", min_value=1)

if st.button("Calcular costo"):
    costo = gramos * 15 * 2
    st.success(f"Costo estimado: ${costo}")

if st.button("Calcular precio"):
    precio = gramos * 15 * 2 * 5
    st.success(f"Precio sugerido: ${precio}")
