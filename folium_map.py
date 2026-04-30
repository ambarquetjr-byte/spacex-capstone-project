import folium

launch_sites = {
    "CCAFS LC-40": [28.562302, -80.577356],
    "CCAFS SLC-40": [28.563197, -80.576820],
    "KSC LC-39A": [28.573255, -80.646895],
    "VAFB SLC-4E": [34.632834, -120.610745],
}

site_map = folium.Map(location=[29.5597, -95.0831], zoom_start=4)

for site, coordinates in launch_sites.items():
    folium.Marker(
        location=coordinates,
        popup=site,
        icon=folium.Icon(color="blue", icon="rocket", prefix="fa")
    ).add_to(site_map)

site_map.save("spacex_launch_sites_map.html")

print("Map saved as spacex_launch_sites_map.html")