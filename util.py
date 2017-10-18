# -*- coding: utf-8 -*-

import datetime
import calendar
import utm
import six


def datetime_to_unix_epoch(timestamp):
    """Converts datetime instance to UNIX epoch time
    """
    return calendar.timegm(timestamp.timetuple())


def parse_timestamp(timestamp):
    """New datetime object parse from a string (timestamp)
    """
    return datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")


def utm_to_gps(utm_coordinate, zone=33, zone_letter='N'):
    """
    Converts UTM coordinate to GPS lat, lon.

    Defaults to zone number 33 (Norway) and letter 'N'.
    """
    return utm.to_latlon(utm_coordinate[0], utm_coordinate[1], zone, zone_letter)
