import pandas as pd
import streamlit as st
import folium
from streamlit_folium import st_folium

st.title('Hier ist eine Testapp, welche Daten von Github nimmt und von allen Usern mit Link genutzt werden kann')


st.write('Wir laden zuerst ein einfaches JSON File rein, welches die BFS-Nummern und die entsprechenden Gemeindenamen enthält.')

url = "https://raw.githubusercontent.com/mstorange/test_app/main/BFSNummern_reversed.json"
df = pd.read_json(url)
# df.head(3)
# st.table(df, border=True)


oben = st.number_input('Obere Grenze der BFS-Nummer', min_value=0, max_value=9999, value=20, step=1)
unten = st.number_input('Untere Grenze der BFS-Nummer', min_value=0, max_value=9999, value=10, step=1)

st.write(f'Die gefilterten Gemeinden mit BFS-Nummern zwischen {unten} und {oben} sind:')

df_filtered = df[(df['bfsnr'] < oben) & (df['bfsnr'] >= unten)]


st.table(df_filtered, border=True)

st.subheader('Eine Foliumkarte:')

satellite = folium.TileLayer(
        tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr = 'Esri',
        name = 'Esri Satellite',
        overlay = False,
        control = True)

m = folium.Map(location=[47.04, 8.29], zoom_start=10, tiles=satellite, zoom_control=False)
folium.Marker([47.12, 8.45], popup='Schweiz').add_to(m)

st_data = st_folium(m, width = 700, height = 500)





