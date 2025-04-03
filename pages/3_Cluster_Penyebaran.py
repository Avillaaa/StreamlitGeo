import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Cluster Penyebaran")


col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenStreetMap")
cities = "./geocoding.csv"
regions = "prov 37.geojson"
df = pd.read_csv(cities)

with col2:

    basemap = st.selectbox("Pilih basemap:", options, index)
    search_query = st.text_input("Cari berdasarkan NO RM:")
    if search_query:
        filtered_df = df[df["NO RM"].astype(str).str.contains(search_query, case=False, na=False)]
        if filtered_df.empty:
            st.warning("Tidak ada data yang cocok dengan pencarian.")
        else:
            st.success(f"Ditemukan {len(filtered_df)} hasil yang cocok.")
    else:
        filtered_df = df

    # Menambahkan dropdown filter
    jenisbpjs = filtered_df["JENIS BPJS"].unique()  # Ganti "JENIS BPJS" dengan nama kolom yang ingin difilter
    selected_region = st.selectbox("Pilih JENIS BPJS:", jenisbpjs)

    filtered_df = filtered_df[filtered_df["JENIS BPJS"] == selected_region]


with col1:

    m = leafmap.Map(center=[40, -100], zoom=4)

    m.add_geojson(regions, layer_name="Provinsi Indonesia")
    m.add_points_from_xy(
        filtered_df,
        x="Longitude",
        y="Latitude",
        icon_names=["gear", "map", "leaf", "globe"],
        spin=True,
        add_legend=True,
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)
