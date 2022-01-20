import bpy

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

		row = layout.row()
		row.operator('view3d.mofmulti_autouv', text="AutoUV")
		# row1 = layout.row()
		# row1.operator('view3d.mofmulti_autouv', text="Multi AutoUV")