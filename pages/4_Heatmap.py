import streamlit as st
import leafmap.foliumap as leafmap
import pandas as pd

df = pd.read_csv("geocoding.csv")
df["value"] = 1  # Menambahkan kolom value dengan nilai default 1

temp_filepath = "temp_geocoding.csv"
df.to_csv(temp_filepath, index=False)

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Heatmap")
filepath = "temp_geocoding.csv"  # Ganti dengan path file CSV Anda


col1, col2 = st.columns([4, 1])
options = list(leafmap.basemaps.keys())
index = options.index("OpenTopoMap")

with col2:

    basemap = st.selectbox("Pilih basemap:", options, index)


with col1:

    m = leafmap.Map(center=[-7, 108], zoom=5)
    regions = "prov 37.geojson"
    m.add_geojson(regions, layer_name="Provinsi Indonesia")
    m.add_heatmap(
        filepath,
        latitude="Latitude",
        longitude="Longitude",
        value="value",
        name="Heat map",
        radius=20,
    )
    m.add_basemap(basemap)
    m.to_streamlit(height=700)

