# -*- coding: utf-8 -*-
import json
import logging
from urllib import urlencode

from django.conf import settings

import requests

logger = logging.getLogger(__name__)


class GoogleApiException(Exception):
    pass


class GoogleResponse(object):
    OK = "OK"
    OVER_QUERY_LIMIT = "OVER_QUERY_LIMIT"


def geolocation(address):
    """
    Retrieve the geographical location of given ``address``.

    :param address: A string representing the address.
    :return: Parsed JSON response object.
    """
    logger.debug("Geo-locating address")

    qs = {"key": settings.GOOGLE_API_KEY, "sensor": "false", "address": address}
    logger.debug(qs)
    response = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json?{0}".format(urlencode(qs))
    )
    logger.debug(response)

    # Example Google Geolocation service response::
    #
    #     {
    #        "results" : [
    #           {
    #              "address_components" : [
    #                 {
    #                    "long_name" : "1017 BZ",
    #                    "short_name" : "1017 BZ",
    #                    "types" : [ "postal_code" ]
    #                 },
    #                 {
    #                    "long_name" : "Centrum",
    #                    "short_name" : "Centrum",
    #                    "types" : [ "sublocality", "political" ]
    #                 },
    #                 {
    #                    "long_name" : "Amsterdam",
    #                    "short_name" : "Amsterdam",
    #                    "types" : [ "locality", "political" ]
    #                 }
    #              ],
    #              "formatted_address" : "1017 BZ Amsterdam, Nederland",
    #              "geometry" : {
    #                 "bounds" : {
    #                    "northeast" : {
    #                       "lat" : 52.3737272,
    #                       "lng" : 4.9006637
    #                    },
    #                    "southwest" : {
    #                       "lat" : 52.3624514,
    #                       "lng" : 4.885587
    #                    }
    #                 },
    #                 "location" : {
    #                    "lat" : 52.366725,
    #                    "lng" : 4.8878735
    #                 },
    #                 "location_type" : "APPROXIMATE",
    #                 "viewport" : {
    #                    "northeast" : {
    #                       "lat" : 52.368362,
    #                       "lng" : 4.889595100000001
    #                    },
    #                    "southwest" : {
    #                       "lat" : 52.3655774,
    #                       "lng" : 4.8860647
    #                    }
    #                 }
    #              },
    #              "types" : [ "postal_code" ]
    #           }
    #        ],
    #        "status" : "OK"
    #     }

    if response.status_code != 200:
        raise GoogleApiException(response.content)

    result = json.loads(response.content)
    if result["status"] != GoogleResponse.OK:
        raise GoogleApiException(response.content)

    location = result["results"][0]["geometry"]["location"]
    logger.debug(
        "Geolocation success: {0} / {1}".format(location["lat"], location["lng"])
    )
    return (location["lat"], location["lng"])
