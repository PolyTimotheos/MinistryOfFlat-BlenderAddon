# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "MinistryOfFlatBridge",
    "author" : "Tim Mayer",
    "wiki_url": "https://github.com/",
    "description" : "This script exports the current mesh to the auto-uv program 'Ministry of Flat' and then reimports and applies the result. Go to http://www.ministryofflat.com/ for a liscence, it's really an incredible tool",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 4),
	"location": "3D View > Toolbox",
	"category": "Object"
}

# from . import auto_load

import bpy

# from . mofautouv_op import MOFUV_OT_Operator
from . mofautouvmulti_op import MOFUVMULTI_OT_Operator
from . mofautouv_panel import MOFUV_PT_Panel

classes = (MOFUVMULTI_OT_Operator, MOFUV_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
