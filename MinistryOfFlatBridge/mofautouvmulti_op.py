import bpy
import os
import subprocess
import time

class MOFUVMULTI_OT_Operator(bpy.types.Operator):
	bl_idname = "view3d.mofmulti_autouv"
	bl_label = "Auto UV object"
	bl_description = "Auto UV a single object"

	def execute(self, context):
		addonPath = bpy.utils.user_resource('SCRIPTS', "addons")
		mof_path = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\UnWrapConsole3.exe')
		base_file = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\autoUVbase.obj')
		result_file = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\autoUVresult.obj')
		command = r'"{}"'.format(mof_path) + ' ' + r'"{}"'.format(base_file) + ' ' + r'"{}"'.format(result_file)
		selected_obj = bpy.context.selected_objects
		active_obj = bpy.context.active_object
		for BaseObject in selected_obj:
			bpy.ops.object.select_all(action='DESELECT')
			BaseObject.select_set(True)
			bpy.context.view_layer.objects.active = BaseObject
			if BaseObject.type == 'MESH':
				print("------------ Export Selected To Obj ------------")
				BaseObject = bpy.context.selected_objects[0]
				bpy.ops.export_scene.obj(filepath=base_file, check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj", use_selection=True, use_animation=False, use_mesh_modifiers=False, use_edges=True, use_smooth_groups=True, use_smooth_groups_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=False, group_by_object=False, group_by_material=False, keep_vertex_order=True, global_scale=1, path_mode='AUTO')
				print("------------ Generate UVs ------------")
				while not os.path.exists(base_file):
					time.sleep(1)
				if os.path.isfile(base_file):
					print(os.popen(command).read())
				else:
					raise ValueError("%s isn't a file!" % base_file)
				print("------------ Reimport Selected Obj ------------")
				while not os.path.exists(result_file):
					time.sleep(1)
				if os.path.isfile(result_file):
					bpy.ops.import_scene.obj(filepath=result_file, filter_glob="*.obj", use_edges=True, use_smooth_groups=True, use_split_objects=False, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=False, split_mode='OFF', global_clight_size=0.0, axis_forward='-Z', axis_up='Y')
				else:
					raise ValueError("%s isn't a file!" % result_file)
				print("------------ Transfer UVs ------------")
				time.sleep(1)
				BaseObject.select_set(True)
				TempObject = bpy.context.selected_objects[1]
				TempObject.select_set(True)
				bpy.context.view_layer.objects.active = TempObject
				bpy.ops.object.join_uvs()
				print("UVs have been transferred!")
				print("------------ Delete Temporary Obj ------------")
				BaseObject.select_set(False)
				bpy.ops.object.delete()
				# os.remove(base_file)
				# os.remove(result_file)
				print("Temporary objects have been deleted")
		
		# Select again objects
		for j in selected_obj:
			j.select_set(True)
			
		bpy.context.view_layer.objects.active = active_obj

		return {'FINISHED'}		