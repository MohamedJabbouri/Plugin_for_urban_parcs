# -*- coding: utf-8 -*-
"""
/***************************************************************************
 UrbanParks
                                 A QGIS plugin
 to indices and calucaltion
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-11-26
        copyright            : (C) 2021 by moahmed
        email                : moha@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load UrbanParks class from file UrbanParks.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .urban_parks import UrbanParks
    return UrbanParks(iface)