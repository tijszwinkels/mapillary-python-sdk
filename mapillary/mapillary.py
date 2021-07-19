"""
mapillary.mapillary
~~~~~~~~~~~~~~~~~~~

This module implements the basic functionalities
of the Mapillary Python SDK, a pythonic
implementation of the Mapillary API v4. For
more information, please check out
https://www.mapillary.com/developer/api-documentation/

:copyright: (c) 2021 ...
:license: See LICENSE for more details
"""

# Datetime
from datetime import datetime

# Local
from models.client import Client
from models.auth import auth

# Controllers
from controller.image import get_image_thumbnail_controller
import controller.feature as feature


def set_access_token(token: str):
    """A function allowing the user to set an access
    token for the session, which they can create at
    https://www.mapillary.com/dashboard/developers.
    Takes token as an argument and sets a global
    variable used by other functions making API requests.
    For more information what the details of authentication,
    please check out the blog post at Mapillary.
    https://blog.mapillary.com/update/2021/06/23/getting-started-with-the-new-mapillary-api-v4.html

    :param token: The token itself that would
    be set and accessed globally. Must be obtained
    :type token: str

    :return: None
    :rtype: None

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
    """

    Client.set_token(token)

    return {"Success": "Token set"}


@auth()
def get_image_close_to(latitude=-122.1504711, longitude=37.485073, **kwargs):
    """Function that takes a longitude, latitude as argument and outputs the near images. This
    makes an API call with the token set in set_access_token and returns a JSON object.

    :param longitude: The longitude
    :type longitude: float or double

    :param latitude: The latitude
    :type latitude: float or double

    :param kwargs.fields: A list of options, either as ['all'], or a list of fields.
    See https://www.mapillary.com/developer/api-documentation/, under 'Fields' for more insight.
    :type kwargs.fields: list

    :param kwargs.radius: The radius of the images obtained from a center center
    :type kwargs.radius: float or int or double

    :param kwargs.image_type: The tile image_type to be obtained, either as 'flat', 'pano' (panoramic),
    or 'both'. See https://www.mapillary.com/developer/api-documentation/ under 'image_type Tiles'
    for more information
    :type kwargs.image_type: str

    :param kwargs.min_date: The min date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.min_date: str

    :param kwargs.max_date: The max date. Format from 'YYYY', to 'YYYY-MM-DDTHH:MM:SS'
    :type kwargs.max_date: str

    :param kwargs.org_id: The organization id, ID of the organization this image (or sets of
    images) belong to. It can be absent. Thus, default is -1 (None)
    :type kwargs.org_id: int

    :return: GeoJSON
    :rtype: dict

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('CLIENT_TOKEN_HERE')
        >>> mly.get_image_close_to(longitude=31, latitude=30)
        {'type': 'FeatureCollection', 'features': [{'type': 'Feature',
        'geometry': {'type': 'Point', 'coordinates': [30.9912246465683,
        29.99794091267283]}, 'properties': {'captured_at': 1621008070596,
        'compass_angle': 322.56726074219, 'id': 499412381300321, 'is_pano':
        False, 'sequence_id': '94afmyyhq85xd9bi8p44ve'}} ...
    """

    # ! Currently blocked by PR "[Config API] Documentation Fixes, Bug Removal, Functions For
    # ! Retrieving Field Lists #38"
    # The below will throw an error because of a missing parameter that this branch has,
    # but has been fixed in #38

    return image.get_image_close_to_controller(
        latitude=latitude,
        longitude=longitude,
        kwargs=kwargs,
    )


@auth()
def get_image_looking_at(
    coordinates_looker,
    coordinates_at,
    fields=["all"],
    radius=200,
    image_type="pano",
    date=datetime.today().strftime("%Y-%m-%d"),
    org_id=-1,
):
    """Function that takes two sets of latitude and
    longitude, where the 2nd set is the "looking at"
    location from 1st set's perspective
    argument and outputs the near images. This
    makes an API call with the token set in
    set_access_token and returns a JSON object.

    :param coordinates_looker: The coordinate sets from
    where a certain point is being looked at, it has
    length 2, index@0 is lat, index@1 is long
    :type coordinates_looker: list

    :param coordinates_at: The coordinate sets to
    where a certain point is being looked at, it has
    length 2, index@0 is lat, index@1 is long
    :type coordinates_at: list

    :param fields: A list of options, either as 'all',
    or individually accounted lists of fields. For more
    details about the fields themselves, please take a
    look at
    https://www.mapillary.com/developer/api-documentation/,
    under 'Fields'. Geometry must always be included in
    the fields, even in indvidual
    :type fields: list

    :param radius: The radius of the images obtained
    from a center center
    :type radius: float or int or double

    :param coverge: The tile image_type to be obtained,
    either as 'flat', 'pano' (panoramic), or 'both'.
    For more information, please take a look at
    https://www.mapillary.com/developer/api-documentation/
    under 'image_type Tiles'
    :type image_type: str

    :param date: The date to filter to, if needed.
    The date format currently is 'YYYY-MM-DD', or '%Y-%m-%d'
    :type date: datetime

    :param org_id: The organization id, ID of the
    organization this image (or sets of images) belong
    to. It can be absent. Thus, default is -1 (None)
    :type org_id: int

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how the function works
    """

    # * `coordinates_looker` and `coordinates_at`
    # * can be the same or different

    # ? It may be useful to have the function
    # ? exclude images that are too close to the
    # ? looking at longitude, latitude, as if
    # ? within 3 meters, as the returned photo may
    # ? be too close to be useful. 10+ meters may be
    # ? best

    # TODO: This functions needs implementation

    return None


@auth()
def get_detections_from_key(key):
    """Extracting all the detections within an image using an image key

    :param key: The image key as the argument
    :type key: int

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_detections_for_feature_from_key(feature_key):
    """Extracting all detections made for a map feature key

    :param feature_key: A map feature key as the argument
    :type feature_key: str # ? To check if valid

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def image_thumbnail(image_id, resolution=1024) -> str:
    """Gets the thumbnails of images from the API

    :param image_id: Image key as the argument

    :param resolution: Option for the thumbnail size, with available resolutions:
    256, 1024, and 2048

    :return: A URL for the thumbnail
    :rtype: str

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.image_thumbnail(
        ...     image_id='IMAGE_ID_HERE', resolution='DESIRED_RESOLUTION'
        ... )
    """
    return image.get_image_thumbnail_controller(image_id, resolution=resolution)


@auth()
def get_images_in_bbox(bbox, **filters):
    """Gets a complete list of all images within a BBox

    :param bbox: Bounding box coordinates, length 4
    :type bbox: list

    :param **filters: Contains filter arguments for
    date, pano/flat. Such is 'date', 'is_pano',
    'is_flat', 'is_both'
    :type **filters: dict

    :return: Output is a GeoJSON object. Could do the
    same for sequences and leave as an option to return
    either image (point) or sequences (line). Sequences
    would NOT be cut at BBox boundary, would select all
    sequences which are partially or entirely in BBox
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return {"Message": "Hello, World!"}


@auth()
def map_feature_points_in_bbox(
    bbox: dict, filter_values: list = None, **filters: dict
) -> str:
    """Extracts map feature points within a bounding box (bbox)

    :param bbox: bbox coordinates as the argument
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param filter_values: a list of filter values supported by the API.
    example: ['object--support--utility-pole', 'object--street-light']
    :type filter_values: list

    :param **filters: kwarg filters to be applied on the resulted GeoJSON
    Chronological filters:
    - existed_after: checks if a feature existed after a certain date depending on the time it 
    was first seen at.
    - existed_before: filters out the features that existed after a given date
    :type **filters: dict

    :return: GeoJSON Object
    :rtype: <class 'dict'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.map_feature_points_in_bbox(
        ...     bbox={
        ...         'west': 'BOUNDARY_FROM_WEST',
        ...         'south': 'BOUNDARY_FROM_SOUTH',
        ...         'east': 'BOUNDARY_FROM_EAST',
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...     },
        ...     filter_values=['object--support--utility-pole', 'object--street-light'],
        ...     existed_after='2015-01-01',
        ...     existed_before='2015-01-02'
        ... )
    """

    return feature.get_map_features_in_bbox_controller(
        bbox=bbox, filters=filters, filter_values=filter_values, layer="points"
    )


@auth()
def traffic_signs_in_bbox(
    bbox: dict, filter_values: list = None, **filters: dict
) -> str:
    """Extracts traffic signs within a bounding box (bbox)

    :param bbox: bbox coordinates as the argument
    example: {
        'west': 'BOUNDARY_FROM_WEST',
        'south': 'BOUNDARY_FROM_SOUTH',
        'east': 'BOUNDARY_FROM_EAST',
        'north': 'BOUNDARY_FROM_NORTH'
    }
    :type bbox: dict

    :param filter_values: a list of filter values supported by the API,
    example: ['regulatory--advisory-maximum-speed-limit--g1', 'regulatory--atvs-permitted--g1']
    :type filter_values: list

    :param **filters: kwarg filters to be applied on the resulted GeoJSON
    Chronological filters:
    - existed_after: checks if a feature existed after a certain date depending on the time it 
    was first seen at.
    - existed_before: filters out the features that existed after a given date
    :type **filters: dict

    :return: GeoJSON Object
    :rtype: <class 'dict'>

    Usage::
        >>> import mapillary as mly
        >>> mly.set_access_token('MLY|XXX')
        >>> mly.traffic_signs_in_bbox(
        ...    bbox={
        ...         'west': 'BOUNDARY_FROM_WEST', 
        ...         'south': 'BOUNDARY_FROM_SOUTH', 
        ...         'east': 'BOUNDARY_FROM_EAST', 
        ...         'north': 'BOUNDARY_FROM_NORTH'
        ...    },
        ...    filter_values=[
        ...        'regulatory--advisory-maximum-speed-limit--g1',
        ...        'regulatory--atvs-permitted--g1'
        ...    ],
        ...    existed_after='2016-01-01',
        ...    existed_before='2016-01-02'
        ... )
    """

    return feature.get_map_features_in_bbox_controller(
        bbox=bbox, filters=filters, filter_values=filter_values, layer="traffic_signs"
    )


@auth()
def get_all_images_in_a_shape(geoJSON, **filters):
    """Extracts all images within a shape

    :param geoJSON: Bbox coordinates as the argument
    :type geoJSON: list

    :param **filters: Contains filter arguments
    for date, pano/flat. Such is 'date', 'is_pano',
    'is_flat', 'is_both'
    :type **filters: dict

    :return: # ? Not sure, need to ask Chris
    :rtype: # ? Not sure, need to ask Chris

    Usage::
        # TODO: Write code here to display how the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_all_map_features_in_shape(geoJSON, **filters):
    """Extracts all images within a shape

    :param geoJSON: Bbox coordinates as the argument
    :type geoJSON: list

    :param **filters: Contains filter arguments
    for date, pano/flat. Such is 'date', 'is_pano',
    'is_flat', 'is_both'
    :type **filters: dict

    :return: # ? Not sure, need to ask Chris
    :rtype: # ? Not sure, need to ask Chris

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_feature_from_map_feature_key(map_feature_key, fields):
    """Gets features for the given map_key argument

    :param map_feature_key: The map feature key to
    extract features
    :type map_feature_key: int

    :param fields: The fields to include. Geometry is
    always included in the request
    :type fields: list

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def get_feature_from_image_feature_key(image_feature_key):
    """Gets features for the given map_key argument

    :param image_feature_key: The image feature key to
    extract features
    :type image_feature_key: int

    :param fields: The fields to include. Geometry is
    always included in the request
    :type fields: list

    :return: JSON
    :rtype: <class 'dict'>

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def save_to_csv(
    csv_data,
    file_path,
):
    """This function saves the csv data locally with the extension .csv

    :param csv_data: The CSV data to be stored
    :type csv_data: CSV Object

    :param file_path: The path to save the data to
    :type file_path: str

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None


@auth()
def save_as_geojson(
    geojson_data,
    file_path,
):
    """This function saves the geojson data locally with the extension .geojson

    :param geojson_data: The GeoJSON data to be stored
    :type geojson_data: GeoJSON Object

    :param file_path: The path to save the data to
    :type file_path: str

    :return: None
    :rtype: None

    Usage::
        # TODO: Write code here to display how
        # TODO: the function works
    """

    # TODO: This functions needs implementation

    return None
