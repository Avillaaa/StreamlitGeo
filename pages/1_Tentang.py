import streamlit as st
st.title("Tentang Aplikasi")

    # Company Values Section
st.subheader("Tujuan Aplikasi ini")
st.write("""
        - Melihat Penyebaran Pasien Rawat Jalan.
        - Membantu Pengambilan Keputusan.
        """)

    # Services Offered
st.subheader("Menu Navigasi")
st.write("""
        - **Tentang:** Memuat Informasi terkait Aplikasi dan Pembuat Aplikasi.
        - **Cluster Penyebaran:** Menampilkan cluster penyebaran.
        - **Heatmap:** Menampilkan peta sebaran pasien rawat jalan.
        """)

    # Contact Information
st.subheader("Hubungi Kami")
st.write("""
        Email: avillaalif13@gmail.com  
        Phone: +62 87804675210  
        Address: Cibodas, Kota Tangerang, Banten.
        """)

    # Footer
st.markdown("""
        ---
        ### Follow Us:
        [LinkedIn](https://www.linkedin.com/in/muhammad-avilla-701ba6324?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) | [Instagram](https://www.instagram.com/avillalif?igsh=czVzcnJxY2QzZ2M0)
        """)
