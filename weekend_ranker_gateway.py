import pandas as pd
from math import radians, cos, sin, asin, sqrt

# ------------------------------
# Function to calculate distance
# ------------------------------
def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # Convert decimal degrees to radians 
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Haversine formula 
    dlat = lat2 - lat1 
    dlon = lon2 - lon1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in km
    return c * r

# ------------------------------
# Load dataset
# ------------------------------
try:
    df = pd.read_csv("travel_dataset.csv")
except FileNotFoundError:
    print("Error: 'travel_dataset.csv' not found. Make sure the CSV is in the same folder.")
    exit()

# ------------------------------
# Ranking function
# ------------------------------
def rank_weekend_getaways(source_city, top_n=5):
    """
    Returns top N weekend getaways from the source city
    """
    # Get source city coordinates
    source = df[df['City'].str.lower() == source_city.lower()]
    if source.empty:
        return f"Source city '{source_city}' not found in dataset."

    src_lat = source.iloc[0]['Latitude']
    src_lon = source.iloc[0]['Longitude']

    # Calculate distance for all places
    df['Distance_km'] = df.apply(lambda row: haversine(src_lat, src_lon, row['Latitude'], row['Longitude']), axis=1)

    # Avoid recommending places in the same city
    df_filtered = df[df['City'].str.lower() != source_city.lower()]

    # Normalize Rating, Popularity, and Distance for scoring
    df_filtered['Rating_norm'] = df_filtered['Rating'] / df_filtered['Rating'].max()
    df_filtered['Popularity_norm'] = df_filtered['Popularity'] / df_filtered['Popularity'].max()
    df_filtered['Distance_norm'] = 1 - (df_filtered['Distance_km'] / df_filtered['Distance_km'].max())  # closer = higher score

    # Calculate combined score
    df_filtered['Score'] = (0.4 * df_filtered['Rating_norm'] +
                            0.4 * df_filtered['Popularity_norm'] +
                            0.2 * df_filtered['Distance_norm'])

    # Sort by score descending
    top_destinations = df_filtered.sort_values(by='Score', ascending=False).head(top_n)

    return top_destinations[['Place', 'City', 'State', 'Distance_km', 'Rating', 'Popularity', 'Score']]

# ------------------------------
# Sample run
# ------------------------------
if __name__ == "__main__":
    cities = ["Delhi", "Mumbai", "Bangalore"]
    for city in cities:
        print(f"\nTop weekend getaways from {city}:")
        print(rank_weekend_getaways(city))