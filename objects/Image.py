from shapely.geometry import Point


class Image:
    """
    A Class representing an image object as given in input data
    """

    def __init__(self, row):
        """
        Constructor for class Image, parsing raw feature and validating fields
        :param feature: feature data from geojson file
        """
        img_row = row.rstrip('\n')
        img_row = img_row.split(",")
        if len(img_row) != 7:
            raise Exception("Img row invalid")
        self.name = img_row[0]
        self.point = Point((float(img_row[2]), float(img_row[1])))
        self.z = img_row[3]
        self.yaw = img_row[4]
        self.pitch = img_row[5]
        self.roll = img_row[6]
        self.polygon = None

    def dict_repr(self):
        """
        Function to return a dictionary representation of the current object
        :return: Dictionary representing obj
        """
        return {"name": self.name,
                "point": [self.point.x, self.point.y],
                "z": self.z,
                "yaw": self.yaw,
                "pitch": self.pitch,
                "roll": self.roll,
                "polygon index": self.polygon.index if self.polygon else None}
