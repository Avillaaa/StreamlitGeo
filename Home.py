import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

# Customize the sidebar
markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

# Customize page title
st.title("Dashboard sederhana penyebaran data pasien rawat jalan")
st.subheader("Halaman Utama")
st.write("""
        Sebuah Aplikasi Sederhana berbasis Python menggunakan library Streamlit untuk melihat penyebaran pasien rajal melalui geocoding.
        """)
st.image("foto igd.jpg", caption="Foto IGD RS An-Nisa", use_column_width=True)
