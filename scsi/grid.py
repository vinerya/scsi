import math
from .node import Node
from .utils import haversine_distance

class Grid:
    def __init__(self, levels=3):
        """
        Initialize the grid with a specified number of levels.

        :param levels: Number of hierarchical levels.
        """
        self.levels = levels
        self.nodes = {}
        self.build_grid()

    def build_grid(self):
        """
        Build the spherical grid using a simple latitude-longitude grid for simplicity.
        For production use, replace with an icosahedron-based tessellation for uniform cells.
        """
        node_id = 0
        lat_step = 180 / (2 ** self.levels)
        lon_step = 360 / (2 ** self.levels)
        for lat in range(-90, 90, int(lat_step)):
            for lon in range(-180, 180, int(lon_step)):
                coordinates = (lat + lat_step / 2, lon + lon_step / 2)
                node = Node(node_id, coordinates, self.levels)
                self.nodes[node_id] = node
                node_id += 1

        # Establish adjacency (naive implementation)
        for node in self.nodes.values():
            for other_node in self.nodes.values():
                if node.id != other_node.id:
                    distance = haversine_distance(node.coordinates, other_node.coordinates)
                    # Consider nodes within a certain distance as adjacent (simplified)
                    if distance < max(lat_step, lon_step):
                        node.add_adjacent_node(other_node)

    def find_node(self, latitude, longitude, level=None):
        """
        Find the node corresponding to the given coordinates and level.

        :param latitude: Latitude in degrees.
        :param longitude: Longitude in degrees.
        :param level: Level in the hierarchical grid.
        :return: Node object or None.
        """
        if level is None:
            level = self.levels
        min_distance = float('inf')
        closest_node = None
        for node in self.nodes.values():
            if node.level == level:
                distance = haversine_distance((latitude, longitude), node.coordinates)
                if distance < min_distance:
                    min_distance = distance
                    closest_node = node
        return closest_node

    def add_data_point(self, latitude, longitude, data):
        """
        Add data to the grid at the specified coordinates.

        :param latitude: Latitude in degrees.
        :param longitude: Longitude in degrees.
        :param data: Data to be stored.
        """
        node = self.find_node(latitude, longitude)
        if node:
            node.data = data

    def point_query(self, latitude, longitude):
        """
        Retrieve data at a specific point.

        :param latitude: Latitude in degrees.
        :param longitude: Longitude in degrees.
        :return: Data at the specified point.
        """
        node = self.find_node(latitude, longitude)
        if node:
            return node.data
        else:
            return None

    def range_query(self, center_lat, center_lon, radius):
        """
        Retrieve all data within a certain radius.

        :param center_lat: Center latitude.
        :param center_lon: Center longitude.
        :param radius: Radius in kilometers.
        :return: List of node data within the radius.
        """
        result = []
        for node in self.nodes.values():
            distance = haversine_distance((center_lat, center_lon), node.coordinates)
            if distance <= radius:
                result.append(node.data)
        return result
