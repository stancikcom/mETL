
# -*- coding: utf-8 -*-

"""
mETLapp is a Python tool for do ETL processes with easy config.
Copyright (C) 2013, Bence Faludi (b.faludi@mito.hu)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, <see http://www.gnu.org/licenses/>.
"""

import metl.transform.base

class SubTransform( metl.transform.base.Transform ):

    init = ['number']

    # void
    def __init__( self, number, *args, **kwargs ):

        self.number     = number
        super( SubTransform, self ).__init__( *args, **kwargs )

    # Field
    def transform( self, field ):

        value = field.getValue()
        if value is None:
            return field

        field.setValue( value - self.number )
        return field