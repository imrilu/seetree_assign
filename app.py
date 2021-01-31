from flask import Flask, jsonify
from data_handler import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def app_help():
    """
    Basic endpoint to check service and get initial usage information
    :return: json with information about the API
    """
    return jsonify("Welcome to SeeTree home assignment.",
                   "This API is used to load and retrieve image and polygon data.",
                   "This API can also answer which images contained in what polygon and vice-versa.")


@app.route('/load_images', methods=['GET'])
def request_load_images():
    """
    An endpoint to load the images from files and parse them into memory.
    will also check if it can calculate image-polygon relations.
    :return: approve message
    """
    load_images()
    check_can_calculate_relations()
    return jsonify("Images loaded successfully")


@app.route('/load_polygons', methods=['GET'])
def request_load_polygons():
    """
    An endpoint to load the polygons from files and parse them into memory.
    will also check if it can calculate image-polygon relations.
    :return: approve message
    """
    load_polygons()
    check_can_calculate_relations()
    return jsonify("Polygons loaded successfully")


@app.route('/get_polygon/<image_name>', methods=['GET'])
def request_get_polygon(image_name):
    """
    An endpoint to retrieve the polygon containing the image with name 'image_name'.
    :param image_name: the name of the image the polygon should contain
    :return: A json representation of the polygon, or a message saying "Not found"
    """
    if image_name in images and images[image_name].polygon:
        return jsonify(images[image_name].polygon.dict_repr())
    return jsonify("Not found")


@app.route('/get_images/<index1>/<index2>', methods=['GET'])
def request_get_images(index1, index2):
    """
    An endpoint to retrieve all the images contained in the polygon with index 'index1/index2'.
    :param index1: first half of polygon's index
    :param index2: second half of polygon's index
    :return: A json representation all the images containing in the polygon, or a message saying "Not found"
    """
    index = index1 + "/" + index2
    if index in polygons:
        polygon_imgs = []
        for image in polygons[index].images.values():
            polygon_imgs.append(image.dict_repr())
        return jsonify(polygon_imgs)
    return jsonify("Not found")


@app.route('/get_all_polygons', methods=['GET'])
def get_all_polygons():
    """
    An endpoint to retrieve all the polygon's index for which they contain at least 1 image
    :return: A json containing a list of polygon index
    """
    poly_list = []
    for polygon in polygons.values():
        if polygon.images:
            poly_list.append(polygon.index)
    return jsonify(poly_list)


if __name__ == "__main__":
    app.run(host='localhost', debug=True)
