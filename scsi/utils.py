import math

def latlon_to_cartesian(latitude, longitude):
    """
    Convert latitude and longitude to Cartesian coordinates.

    :param latitude: Latitude in degrees.
    :param longitude: Longitude in degrees.
    :return: Tuple of (x, y, z).
    """
    lat_rad = math.radians(latitude)
    lon_rad = math.radians(longitude)
    x = math.cos(lat_rad) * math.cos(lon_rad)
    y = math.cos(lat_rad) * math.sin(lon_rad)
    z = math.sin(lat_rad)
    return x, y, z

def haversine_distance(coord1, coord2):
    """
    Calculate the Haversine distance between two points on the Earth.

    :param coord1: Tuple of (latitude, longitude).
    :param coord2: Tuple of (latitude, longitude).
    :return: Distance in kilometers.
    """
    R = 6371.0  # Earth radius in kilometers
    lat1_rad = math.radians(coord1[0])
    lon1_rad = math.radians(coord1[1])
    lat2_rad = math.radians(coord2[0])
    lon2_rad = math.radians(coord2[1])

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance
