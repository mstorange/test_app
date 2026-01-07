import pandas as pd
import streamlit as st

st.title('Hier ist eine Testapp, welche Daten von Github nimmt und von allen Usern mit Link genutzt werden kann')


st.write('Wir laden zuerst ein einfaches JSON File rein, welches die BFS-Nummern und die entsprechenden Gemeindenamen enthält.')

url = "https://raw.githubusercontent.com/mstorange/test_app/blob/main/BFSNummern_reversed.json"
df = pd.read_json(r"C:\Users\ma.stutz\OneDrive - BYCN\2 Geodaten\0_Schweiz\BFSNummern_reversed.json")
# df.head(3)
st.table(df, border=True)


oben = st.number_input('Obere Grenze der BFS-Nummer', min_value=0, max_value=9999, value=20, step=1)
unten = st.number_input('Untere Grenze der BFS-Nummer', min_value=0, max_value=9999, value=10, step=1)

st.write(f'Die gefilterten Gemeinden mit BFS-Nummern zwischen {unten} und {oben} sind:')

df_filtered = df[(df['bfsnr'] < oben) & (df['bfsnr'] >= unten)]

st.table(df_filtered, border=True)