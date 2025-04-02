import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.title("Cluster Penyebaran")


# col1, col2 = st.columns([4, 1])
# options = list(leafmap.basemaps.keys())
# index = options.index("OpenStreetMap")

# with col2:

#     basemap = st.selectbox("Pilih basemap:", options, index)


# with col1:

#     m = leafmap.Map(center=[40, -100], zoom=4)
#     cities = "geocoding.csv"
#     regions = "prov 37.geojson"

#     m.add_geojson(regions, layer_name="Provinsi Indonesia")
#     m.add_points_from_xy(
#         cities,
#         x="Longitude",
#         y="Latitude",
#         icon_names=["gear", "map", "leaf", "globe"],
#         spin=True,
#         add_legend=True,
#     )
#     m.add_basemap(basemap)
#     m.to_streamlit(height=700)


row1_col1, row1_col2 = st.columns([3, 1])
width = None
height = 800
tiles = None

with row1_col2:

    checkbox = st.checkbox("Cari Quick Map Services (QMS)")
    keyword = st.text_input("Cari dengan kata kunci lalu enter:")
    empty = st.empty()

    if keyword:
        options = leafmap.search_xyz_services(keyword=keyword)
        if checkbox:
            options = options + leafmap.search_qms(keyword=keyword)

        tiles = empty.multiselect("Select XYZ tiles to add to the map:", options)

    with row1_col1:
        m = leafmap.Map()
        m = leafmap.Map(center=[40, -100], zoom=4)
        cities = "geocoding.csv"
        regions = "prov 37.geojson"

        m.add_geojson(regions, layer_name="Provinsi Indonesia")
        m.add_points_from_xy(
            cities,
            x="Longitude",
            y="Latitude",
            icon_names=["gear", "map", "leaf", "globe"],
            spin=True,
            add_legend=True,
        )

        if tiles is not None:
            for tile in tiles:
                m.add_xyz_service(tile)

        m.to_streamlit(width, height)
