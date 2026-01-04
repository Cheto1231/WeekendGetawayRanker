Weekend Getaway Ranker
Weekend Getaway Ranker is a Python project that recommends the top weekend destinations from a given source city in India. The recommendations are based on distance, rating, and popularity of must-see places.
Features
Input a source city and get ranked weekend destinations.
Combines distance, user ratings, and popularity for scoring.
Easy-to-use Python script using Pandas.
Works with a simple CSV dataset of Indian must-see places.
Dataset
The project uses a CSV dataset (travel_dataset.csv) with the following columns:
Column
Description
Place
Name of the tourist spot
City
City where the place is located
State
State of the place
Latitude
Latitude coordinate for distance calculation
Longitude
Longitude coordinate for distance calculation
Rating
Average user rating (1–5)
Popularity
Popularity score (number of visitors/reviews)
You can customize the dataset by adding more cities or destinations.
Installation
Clone the repository:

Bash
git clone https://github.com/yourusername/WeekendGetawayRanker.git
cd WeekendGetawayRanker
Install dependencies:

Bash
pip install -r requirements.txt
Usage
Run the script using Python:

Bash

python weekend_getaway_ranker.py
The script will print the top weekend getaways for the sample cities (Delhi, Mumbai, Bangalore).
You can also modify the list of cities in the script or call the function directly:
Python

from weekend_getaway_ranker import rank_weekend_getaways

rank_weekend_getaways("Chennai", top_n=5)
Example Output

Top weekend getaways from Delhi:
        Place      City        State  Distance_km  Rating  Popularity     Score
0   Agra Fort       Agra  Uttar Pradesh     203.45     4.7        950  0.9321
1  Jaipur Palace    Jaipur        Rajasthan     270.12     4.6        870  0.8903
2  Neemrana Fort  Neemrana        Rajasthan     120.34     4.5        800  0.8652
Technologies Used
Python 3.x
Pandas
How It Works
The script reads the travel dataset.
Calculates the distance between the source city and all other destinations using the Haversine formula.
Normalizes Rating, Popularity, and Distance.
Computes a combined score:
Copy code

Score = 0.4 * Rating_norm + 0.4 * Popularity_norm + 0.2 * Distance_norm
Ranks the destinations and outputs the top N weekend getaways.
