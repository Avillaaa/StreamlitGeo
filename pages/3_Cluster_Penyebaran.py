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
desa = "indonesia_villages_border.geojson"
df = pd.read_csv(cities)
df["JENIS BPJS"] = df["JENIS BPJS"].fillna("Tidak Diketahui").astype(str)
df["TANGGAL REGISTRASI"] = pd.to_datetime(df["TANGGAL REGISTRASI"], errors="coerce")


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
    selected_regions = st.multiselect("Pilih JENIS BPJS:", jenisbpjs, default=jenisbpjs)

    # Filter data berdasarkan pilihan multiple selection
    filtered_df = filtered_df[filtered_df["JENIS BPJS"].isin(selected_regions)]

    min_date = filtered_df["TANGGAL REGISTRASI"].min()
    max_date = filtered_df["TANGGAL REGISTRASI"].max()
    start_date, end_date = st.date_input(
        "Pilih rentang tanggal registrasi:",
        [min_date, max_date],
        min_value=min_date,
        max_value=max_date,
    )
    
    # Filter data berdasarkan rentang tanggal
    filtered_df = filtered_df[
        (filtered_df["TANGGAL REGISTRASI"] >= pd.Timestamp(start_date)) &
        (filtered_df["TANGGAL REGISTRASI"] <= pd.Timestamp(end_date))
    ]


with col1:

    m = leafmap.Map(center=[40, -100], zoom=4)

    m.add_geojson(regions, layer_name="Provinsi Indonesia")
    m.add_geojson(desa, layer_name="Desa Indonesia")
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
