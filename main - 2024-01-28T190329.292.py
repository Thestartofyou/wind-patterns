import folium
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from folium.plugins import MarkerCluster

def add_wind_arrow(map_obj, lat, lon, u, v, length=0.1, color='red'):
    arrow = FancyArrowPatch(
        (lon, lat),
        (lon + length * u, lat + length * v),
        color=color,
        arrowstyle='->',
        mutation_scale=10
    )
    map_obj.add_child(arrow)

def plot_wind_map(wind_data):
    center_lat, center_lon = sum(wind_data['latitude']) / len(wind_data), sum(wind_data['longitude']) / len(wind_data)
    wind_map = folium.Map(location=[center_lat, center_lon], zoom_start=3)

    marker_cluster = MarkerCluster().add_to(wind_map)

    for index, row in wind_data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f'Wind: {row["u"]}, {row["v"]}',
        ).add_to(marker_cluster)

        add_wind_arrow(wind_map, row['latitude'], row['longitude'], row['u'], row['v'])

    return wind_map

if __name__ == "__main__":
    # Example wind data (replace this with your actual wind data)
    wind_data = {
        'latitude': [37.7749, 40.7128, 34.0522],  # Example latitude data
        'longitude': [-122.4194, -74.0060, -118.2437],  # Example longitude data
        'u': [1, -2, 0.5],  # Example u component (eastward wind)
        'v': [0, 1, -1],  # Example v component (northward wind)
    }

    wind_df = pd.DataFrame(wind_data)

    # Plot the wind map
    wind_map = plot_wind_map(wind_df)
    wind_map.save('wind_map.html')
