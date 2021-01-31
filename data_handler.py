import json
import threading
import os
from objects.Image import Image
from objects.Polygon import Polygon

images_path = ["data/Images metadata_1.csv", "data/Images metadata_2.csv", "data/Images metadata_1.csv"]
polygons_path = "data/polygons metadata.geojson"
dir_path = os.path.dirname(os.path.realpath(__file__))
images = {}
polygons = {}


def load_images():
    """
    Function to load all images from images_path files path list
    """
    for img_path in images_path:
        with open(os.path.join(dir_path, img_path)) as f:
            for row in f.readlines():
                image = Image(row)
                if image.name not in images:
                    images[image.name] = image


def load_polygons():
    """
    Function to load all polygons from polygons_path file path
    """
    with open(os.path.join(dir_path, polygons_path)) as f:
        gj = json.load(f)
        if gj['type'] != "FeatureCollection":
            print("error parsing geojson")
        features = gj['features']
        for feature in features:
            polygon = Polygon(feature)
            polygons[polygon.index] = polygon


def check_can_calculate_relations():
    """
    Function to check whether we can calculate the images-polygons relations in a separate thread.
    This can only be done once we've loaded both images and polygons
    :return: True if created a daemon thread calculating the relations, False otherwise.
    """
    if images and polygons:
        thread = threading.Thread(target=calculate_relations, args=())
        thread.daemon = True
        thread.start()
        return True
    return False


def calculate_relations():
    """
    Function to calculate for each image the polygon it contains in, and for each polygon which images are contained
    within it's shape geometry.
    :return:
    """
    for image in images.values():
        if not image.polygon:
            for polygon in polygons.values():
                if polygon.geometry.contains(image.point):
                    polygon.images[image.name] = image
                    image.polygon = polygon
