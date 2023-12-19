import bpy
import os
import subprocess
import time

# PropertyGroup for storing properties
class MOFUV_Properties(bpy.types.PropertyGroup):
	useNormals: bpy.props.BoolProperty(
		name="Use Normals",
		description="Use Normals",
		default=True
	)
	separateHardEdges: bpy.props.BoolProperty(
		name="Separate Hard Edges",
		description="Separate Hard Edges",
		default=False
	)

class MOFUV_PT_Panel(bpy.types.Panel):
	bl_idname = "MOFUV_PT_Panel"
	bl_label = "Auto UV Panel"
	bl_category = "AutoUV"
	bl_space_type = "VIEW_3D"
	bl_region_type = "UI"

	# def poll(self, context):
	# 	return (context.object is not None and (context.object.mode == 'OBJECT'	or context.mode == 'EDIT_ARMATURE'))

	def draw(self, context):
		layout = self.layout
		mofuv_props = context.scene.mofuv_props
		
		# Add properties to the panel
		layout.prop(mofuv_props, 'useNormals')
		layout.prop(mofuv_props, 'separateHardEdges')
		
		# Operator button
		layout.operator("view3d.mofmulti_autouv", text="AutoUV")



