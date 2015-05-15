# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyPlugin
                                 A QGIS plugin
 Demonstration of a QGIS Plugin
                             -------------------
        begin                : 2014-05-16
        copyright            : (C) 2014 by Joel Lawhead
        email                : jlawhead@geospatialpython.com
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

def classFactory(iface):
    # load MyPlugin class from file MyPlugin
    from myplugin import MyPlugin
    return MyPlugin(iface)
