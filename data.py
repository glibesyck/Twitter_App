import requests
from hidden import oauth
import json
import folium
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from geopy.exc import GeocoderUnavailable

geolocator = Nominatim(user_agent='smth')
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
base_url = 'https://api.twitter.com/'

def get_information(name_of_user:str) -> dict:
    '''
    Return the user's friends' locations and nicknames as tuples in list.
    '''
    list_of_users = []
    search_headers = {
    'Authorization': 'Bearer {}'.format(oauth())
    }
    search_params = {
    'screen_name': f'@{name_of_user}'
    }
    search_url = '{}1.1/friends/list.json'.format(base_url)
    response = requests.get(search_url, headers=search_headers, params=search_params)
    json_response = response.json(encoding='utf-8')
    for user in json_response['users']:
        list_of_users.append((user['screen_name'], user['location']))
    return list_of_users

def geocoding(users:list):
    '''
    Return a list of (user_name, lat, lng).
    '''
    list_of_users = []
    locations = []
    for user in users:
        try:
            location = geolocator.geocode(user[1])
            if location:
                latitude = location.latitude
                longitude = location.longitude
                while (latitude, longitude) in locations: #avoid exact locations
                    latitude += 0.01
                    latitude += 0.01
                locations.append((latitude, longitude))
                list_of_users.append((user[0], latitude, longitude))
        except GeocoderUnavailable:
            pass
    return list_of_users

def generating_map(users:list):
    '''
    Generates a map with users' nicknames.
    '''
    map = folium.Map(zoom_start=1)
    fg_friends = folium.FeatureGroup(name='Friends')
    for user in users:
        fg_friends.add_child(folium.Marker(location=[user[1], user[2]], 
        popup=user[0], icon=folium.Icon()))
    map.add_child(fg_friends)
    map.save('templates/friends.html')
