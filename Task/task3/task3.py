import pandas as pd
import folium
from folium import Choropleth, GeoJsonTooltip

data = pd.read_csv("election_data.csv")
data_2022 = data[data['year'] == 2022].copy()


data_2022['pct_turnout'] = data_2022['TotalVoteTurnout'] / data_2022['ActiveRegisteredVoters'] * 100


geo_json = 'counties_VA.json'


VA_CENTER = [37.5407, -77.4360]


m = folium.Map(VA_CENTER, zoom_start=7, tiles=None)
data_2022['locality'] = data_2022['locality'].str.title()


choropleth = Choropleth(
    geo_data=geo_json,
    data=data_2022,
    columns=['locality', 'pct_turnout'],
    key_on='feature.properties.NAME',  
    fill_color='YlGnBu',
    legend_name='Voter Turnout Percentage in Virginia (2022)',
    bins=8
).add_to(m)


tooltip = GeoJsonTooltip(
    fields=['NAME'],  
    aliases=['Locality:'],
    style=('background-color:grey;color:white;font-size:medium;padding-left:0px')
)
tooltip.add_to(choropleth.geojson)


m.save('map.html')

m

print(data_2022['locality'].unique())