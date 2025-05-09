import streamlit as st

# Mostrar el logo de TREDIX
st.image("logo.png", width=150)

# Título centrado con estilo
st.markdown(
    "<h1 style='text-align: center; color: #33CCCC;'>Calculadora 3D - TREDIX</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# Entrada de datos
gramos = st.number_input("🔧 Ingresá el peso del objeto en gramos", min_value=1)

# Botones en columnas
col1, col2 = st.columns(2)

with col1:
    if st.button("💰 Calcular costo"):
        costo = gramos * 15 * 2
        st.success(f"📦 Costo estimado: **${costo}**")

with col2:
    if st.button("🏷️ Calcular precio"):
        precio = gramos * 15 * 2 * 5
        st.success(f"🧾 Precio sugerido: **${precio}**")

# Footer opcional
st.markdown("---")
st.markdown(
    "<small style='text-align: center; display: block;'>Desarrollado por TREDIX - 2025</small>",
    unsafe_allow_html=True
)
