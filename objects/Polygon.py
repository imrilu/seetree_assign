from shapely.geometry import shape


class Polygon:
    """
    A Class representing a polygon object as given in input data
    """

    feature_fields = ['properties', 'geometry']
    properties_fields = ['createdAt', 'farmID', 'id', 'index', 'zoneID']

    def __init__(self, feature):
        """
        Constructor for class Polygon, parsing raw feature and validating fields
        :param feature: feature data from geojson file
        """
        if not all(field in feature.keys() for field in Polygon.feature_fields) \
                or not all(field in feature['properties'].keys() for field in Polygon.properties_fields):
            raise Exception("Polygon feature invalid")
        self.geometry = shape(feature['geometry'])
        self.createdAt = feature['properties']['createdAt']
        self.farmID = feature['properties']['farmID']
        self.id = feature['properties']['id']
        self.index = feature['properties']['index']
        self.zondID = feature['properties']['zoneID']
        self.images = {}

    def dict_repr(self):
        """
        Function to return a dictionary representation of the current object
        :return: Dictionary representing obj
        """
        images = []
        for image in self.images.values():
            images.append(image.dict_repr())
        return {"createdAt": self.createdAt,
                "farmID": self.farmID,
                "id": self.id,
                "index": self.index,
                "zoneID": self.zondID,
                "images": images}
