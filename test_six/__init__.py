# -*- coding: utf-8 -*-
"""
/***************************************************************************
 test_six
                                 A QGIS plugin
 test six despt
                             -------------------
        begin                : 2015-05-15
        copyright            : (C) 2015 by zia
        email                : zia@
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
    """Load test_six class from file test_six.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .test_six import test_six
    return test_six(iface)
