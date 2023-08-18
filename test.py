import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/traj_UNI_CORR_500_01.txt", 
                 skiprows=4, 
                 sep="\t", 
                 names=["ID", "frames", "X", "Y", "Z"])
    
st.write("""
# Mi primera aplicación interactiva
Histograma sobre el eje X
""")

# Using "with" notation
with st.sidebar:
    # Titulo
    st.write("# Opciones")
    # slider
    div = st.slider('Número de bins:', 0, 130, 25)
    st.write("Bins=", div)

# Desplegamos un histograma con los datos del eje X
fig, ax = plt.subplots(figsize=(8, 3))
ax.hist(df["X"], bins=div)

# Desplegamos el gráfico
st.pyplot(fig)



