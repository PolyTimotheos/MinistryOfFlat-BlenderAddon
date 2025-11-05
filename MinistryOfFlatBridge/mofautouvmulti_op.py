import bpy
import os
import subprocess
import time
from .mofautouv_panel import MOFUV_Properties

class MOFUVMULTI_OT_Operator(bpy.types.Operator):
    bl_idname = "view3d.mofmulti_autouv"
    bl_label = "Auto UV object"
    bl_description = "Auto UV a single object"

    def execute(self, context):
        #Set To Object Mode
        bpy.ops.object.mode_set(mode='OBJECT')

        #Get Properties
        mofuv_props = context.scene.mofuv_props
        useNormals = mofuv_props.useNormals
        separateHardEdges = mofuv_props.separateHardEdges
        keepAutoUVObject = mofuv_props.keepSourceUVObject


        # Ministry of Flat Settings
        resolution = ' -RESOLUTION 1024'
        normalCommand = ' -NORMALS FALSE'
        seperateHardEdgesCommand = ' -SEPARATE FALSE'
        aspectCommand = ' -ASPECT 1.0'
        udimsCommand = ' -UDIMS 1'
        overlapIdenticalCommand = ' -OVERLAP FALSE'
        mirrorCommand = ' -MIRROR FALSE'
        worldscaleCommand = ' -WORLDSCALE FALSE'
        texDensityCommand = ' -DENSITY 1024'
        seamDirectionCommand = ' -CENTER 0 0 0'
        # experimentalCommand = ' -EXPERIMENTAL FALSE'

        if useNormals:
            normalCommand = ' -NORMALS TRUE'

        if separateHardEdges:
            seperateHardEdgesCommand = ' -SEPARATE TRUE'

        if mofuv_props.overlapIdentical:
            overlapIdenticalCommand = ' -OVERLAP TRUE'

        if mofuv_props.overlapMirrored:
            mirrorCommand = ' -MIRROR TRUE'

        if mofuv_props.seamDirection != (0.0, 0.0, 0.0):
            seamDirectionCommand = ' -CENTER ' + str(mofuv_props.seamDirection[0]) + ' ' + str(mofuv_props.seamDirection[1]) + ' ' + str(mofuv_props.seamDirection[2])

        # Ministry of Flat Debug Settings
        supressValidationDebug = ' -SUPRESS FALSE'
        quadDebug = ' -QUAD TRUE'
        weldDebug = ' -WELD TRUE'
        flatDebug = ' -FLAT TRUE'
        coneDebug = ' -CONE TRUE'
        coneRatioDebug = ' -CONERATIO 0.500000'
        gridsDebug = ' -GRIDS TRUE'
        stripsDebug = ' -STRIP TRUE'
        patchesDebug = ' -PATCH TRUE'
        planesDebug = ' -PLANES TRUE'
        flatnessDebug = ' -FLATT 0.900000'
        mergeDebug = ' -MERGE TRUE'
        mergeLimitDebug = ' -MERGELIMIT 0.000000'
        preSmoothDebug = ' -PRESMOOTH TRUE'
        softUnfoldDebug = ' -SOFTUNFOLD TRUE'
        tubesDebug = ' -TUBES TRUE'
        junctionsDebug = ' -JUNCTIONSDEBUG TRUE'
        extraDebug = ' -EXTRADEBUG FALSE'
        angleBasedFlatteningDebug = ' -ABF TRUE'
        smoothDebug = ' -SMOOTH TRUE'
        repairSmoothDebug = ' -REPAIRSMOOTH TRUE'
        repairDebug = ' -REPAIR TRUE'
        squareDebug = ' -SQUARE TRUE'
        relaxDebug = ' -RELAX TRUE'
        relaxIterationDebug = ' -RELAX_ITERATIONS 50'
        expandDebug = ' -EXPAND 0.250000'
        cutDebug = ' -CUTDEBUG TRUE'
        stretchDebug = ' -STRETCH TRUE'
        matchDebug = ' -MATCH TRUE'
        packingDebug = ' -PACKING TRUE'
        rasteriationResolutionDebug = ' -RASTERIZATION 64'
        packingIterationsDebug = ' -PACKING_ITERATIONS 4'
        scaleToFitDebug = ' -SCALETOFIT 0.500000'
        validateDebug = ' -VALIDATE FALSE'

        if mofuv_props.supressValidationDebug:
            supressValidationDebug = ' -SUPRESS TRUE'
        
        if not mofuv_props.quadDebug:
            quadDebug = ' -QUAD FALSE'

        if not mofuv_props.vertexWeldDebug:
            weldDebug = ' -WELD FALSE'
        
        if not mofuv_props.flatDebug:
            flatDebug = ' -FLAT FALSE'
    
        if not mofuv_props.coneDebug:
            coneDebug = ' -CONE FALSE'

        if mofuv_props.coneRatioDebug != 0.5:
            coneRatioDebug = ' -CONERATIO ' + str(mofuv_props.coneRatioDebug)
        
        if not mofuv_props.gridsDebug:
            gridsDebug = ' -GRIDS FALSE'

        if not mofuv_props.stripsDebug:
            stripsDebug = ' -STRIP FALSE'

        if not mofuv_props.patchesDebug:
            patchesDebug = ' -PATCH FALSE'

        if not mofuv_props.planesDebug:
            planesDebug = ' -PLANES FALSE'

        if mofuv_props.flatnessDebug != 0.9:
            flatnessDebug = ' -FLATT ' + str(mofuv_props.flatnessDebug)

        if not mofuv_props.mergeDebug:
            mergeDebug = ' -MERGE FALSE'
        
        if mofuv_props.mergeLimitDebug != 0.0:
            mergeLimitDebug = ' -MERGELIMIT ' + str(mofuv_props.mergeLimitDebug)

        if not mofuv_props.preSmoothDebug:
            preSmoothDebug = ' -PRESMOOTH FALSE'

        if not mofuv_props.softUnfoldDebug:
            softUnfoldDebug = ' -SOFTUNFOLD FALSE'

        if not mofuv_props.tubesDebug:
            tubesDebug = ' -TUBES FALSE'

        if not mofuv_props.junctionsDebug:
            junctionsDebug = ' -JUNCTIONSDEBUG FALSE'

        if mofuv_props.extraDebug:
            extraDebug = ' -EXTRADEBUG TRUE'

        if not mofuv_props.angleBasedFlatteningDebug:
            angleBasedFlatteningDebug = ' -ABF FALSE'

        if not mofuv_props.smoothDebug:
            smoothDebug = ' -SMOOTH FALSE'

        if not mofuv_props.repairSmoothDebug:
            repairSmoothDebug = ' -REPAIRSMOOTH FALSE'

        if not mofuv_props.repairDebug:
            repairDebug = ' -REPAIR FALSE'

        if not mofuv_props.squaresDebug:
            squareDebug = ' -SQUARE FALSE'

        if not mofuv_props.relaxDebug:
            relaxDebug = ' -RELAX FALSE'

        if mofuv_props.relaxIterationDebug != 50:
            relaxIterationDebug = ' -RELAX_ITERATIONS ' + str(mofuv_props.relaxIterationDebug)

        if mofuv_props.expandDebug != 0.25:
            expandDebug = ' -EXPAND ' + str(mofuv_props.expandDebug)

        if not mofuv_props.cutDebug:
            cutDebug = ' -CUTDEBUG FALSE'

        if not mofuv_props.stretchDebug:
            stretchDebug = ' -STRETCH FALSE'

        if not mofuv_props.matchDebug:
            matchDebug = ' -MATCH FALSE'

        if not mofuv_props.packingDebug:
            packingDebug = ' -PACKING FALSE'

        if mofuv_props.rasteriationResolutionDebug != 64:
            rasteriationResolutionDebug = ' -RASTERIZATION ' + str(mofuv_props.rasteriationResolutionDebug)

        if mofuv_props.packingIterationsDebug != 4:
            packingIterationsDebug = ' -PACKING_ITERATIONS ' + str(mofuv_props.packingIterationsDebug)

        if mofuv_props.scaleToFitDebug != 0.5:
            scaleToFitDebug = ' -SCALETOFIT ' + str(mofuv_props.scaleToFitDebug)

        if mofuv_props.validateDebug:
            validateDebug = ' -VALIDATE TRUE'

        debugCommands = supressValidationDebug + quadDebug + weldDebug + flatDebug + coneDebug + coneRatioDebug + gridsDebug + stripsDebug + patchesDebug + planesDebug + flatnessDebug + mergeDebug + mergeLimitDebug + preSmoothDebug + softUnfoldDebug + tubesDebug + junctionsDebug + extraDebug + angleBasedFlatteningDebug + smoothDebug + repairSmoothDebug + repairDebug + squareDebug + relaxDebug + relaxIterationDebug + expandDebug + cutDebug + stretchDebug + matchDebug + packingDebug + rasteriationResolutionDebug + packingIterationsDebug + scaleToFitDebug + validateDebug



        #Set Paths
        if (3, 00, 0) <= bpy.app.version:
            addonPath = bpy.utils.user_resource('SCRIPTS', path="addons")
        else:
            addonPath = bpy.utils.user_resource('SCRIPTS', "addons")
        mof_path = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\UnWrapConsole3.exe')
        base_file = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\autoUVbase.obj')
        result_file = os.path.join(addonPath, 'MinistryOfFlatBridge\\mof\\autoUVresult.obj')
        command = r'"{}"'.format(mof_path) + ' ' + r'"{}"'.format(base_file) + ' ' + r'"{}"'.format(result_file) + resolution + normalCommand +  seperateHardEdgesCommand + aspectCommand + udimsCommand + overlapIdenticalCommand + mirrorCommand + worldscaleCommand + texDensityCommand + seamDirectionCommand + debugCommands

        print("Auto UV process command = ", command)

        #Execute
        selected_obj = bpy.context.selected_objects
        active_obj = bpy.context.active_object
        amountofobjects = len(selected_obj)
        index = 0
        scale = 100
        unscale = 0.01
        for BaseObject in selected_obj:
            bpy.ops.object.select_all(action='DESELECT')
            BaseObject.select_set(True)
            bpy.context.view_layer.objects.active = BaseObject
            if BaseObject.type == 'MESH':
                print("------------ Export Selected To Obj ------------")
                bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=0.00271427, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='ACTIVE', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True, properties=False)
                # BaseObject = bpy.context.selected_objects[0]
                if bpy.app.version >= (4, 00, 0):
                    bpy.ops.wm.obj_export(filepath=base_file, check_existing=False, forward_axis='NEGATIVE_Z', up_axis='Y', filter_glob="*.obj", export_selected_objects=True, export_animation=False, apply_modifiers=False, export_smooth_groups=True, smooth_group_bitflags=False, export_normals=True, export_colors=True, export_uv=True, export_materials=True, export_pbr_extensions=True, export_triangulated_mesh=False, export_curves_as_nurbs=False, export_vertex_groups=False, export_object_groups=False, export_material_groups=False, global_scale=1, path_mode='AUTO')
                    # bpy.ops.wm.obj_export(filepath=base_file, check_existing=False, forward_axis='NEGATIVE_Z', up_axis='Y', filter_glob="*.obj", export_selected_objects=True, export_animation=False, apply_modifiers=False, export_smooth_groups=False, smooth_group_bitflags=False, export_normals=True, export_colors=True, export_uv=True, export_materials=True, export_pbr_extensions=True, export_triangulated_mesh=False, export_curves_as_nurbs=False, export_vertex_groups=False, export_object_groups=False, export_material_groups=False, global_scale=1, path_mode='AUTO')
                    # bpy.ops.wm.obj_export(filepath=base_file)
                # if bpy.app.version < (4, 00, 0):
                #     bpy.ops.export_scene.obj(filepath=base_file, check_existing=False, axis_forward='-Z', axis_up='Y', filter_glob="*.obj", use_selection=True, use_animation=False, use_mesh_modifiers=False, use_edges=True, use_smooth_groups=True, smooth_group_bitflags=False, use_normals=True, use_uvs=True, use_materials=True, use_triangles=False, use_nurbs=False, use_vertex_groups=False, use_blen_objects=False, group_by_object=False, group_by_material=False, keep_vertex_order=True, global_scale=1, path_mode='AUTO')
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
                    if bpy.app.version >= (4, 00, 0):
                        bpy.ops.wm.obj_import(filepath=result_file, filter_glob="*.obj", use_split_objects=True, use_split_groups=False, import_vertex_groups=False, validate_meshes=True, forward_axis='NEGATIVE_Z', up_axis='Y')
                        # bpy.ops.wm.obj_import(filepath=result_file)
                    # if (3, 00, 0) <= bpy.app.version:
                    # 	bpy.ops.import_scene.obj(filepath=result_file, filter_glob="*.obj", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=False, split_mode='ON', global_clamp_size=0.0, axis_forward='-Z', axis_up='Y')
                    # if bpy.app.version < (4, 00, 0):
                    #     bpy.ops.import_scene.obj(filepath=result_file, filter_glob="*.obj", use_edges=True, use_smooth_groups=True, use_split_objects=True, use_split_groups=False, use_groups_as_vgroups=False, use_image_search=False, split_mode='ON', global_clight_size=0.0, axis_forward='-Z', axis_up ='Y')
                else:
                    raise ValueError("%s isn't a file!" % result_file)
                print("------------ Transfer UVs ------------")
                time.sleep(1)
                # Reorder Faces and Vertices to match
                BaseObject.select_set(True)
                TempObject = bpy.context.selected_objects[1]
                TempObject.select_set(True)
                BaseObject.select_set(False)
                bpy.context.view_layer.objects.active = TempObject
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True, properties=False)
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.sort_elements(type='VIEW_ZAXIS', elements={'VERT', 'EDGE', 'FACE'})
                bpy.ops.object.mode_set(mode='OBJECT')
                TempObject.select_set(False)
                BaseObject.select_set(True)
                bpy.ops.object.mode_set(mode='EDIT')
                bpy.ops.mesh.select_all(action='SELECT')
                bpy.ops.mesh.sort_elements(type='VIEW_ZAXIS', elements={'VERT', 'EDGE', 'FACE'})
                bpy.ops.object.mode_set(mode='OBJECT')

                TempObject.select_set(True)
                BaseObject.select_set(True)
                bpy.context.view_layer.objects.active = TempObject

                # Add the Data Transfer Modifier
                data_transfer_mod = BaseObject.modifiers.new(name="DataTransfer", type='DATA_TRANSFER')
                data_transfer_mod.loop_mapping = 'TOPOLOGY'
                data_transfer_mod.poly_mapping = 'TOPOLOGY'
                data_transfer_mod.object = TempObject
                # Enable loop data transfer (for UVs)
                data_transfer_mod.use_loop_data = True
                data_transfer_mod.data_types_loops = {'UV'}
                data_transfer_mod.layers_uv_select_dst = 'INDEX'
                # data_transfer_mod.layers_uv_select_dst = 'INDEX'
                # Apply the modifier
                bpy.context.view_layer.objects.active = BaseObject
                if not keepAutoUVObject:
                    bpy.ops.object.modifier_apply(modifier=data_transfer_mod.name)
                print("UVs have been transferred!")
                print("------------ Delete Temporary Obj ------------")
                BaseObject.select_set(False)
                if not keepAutoUVObject:
                    bpy.ops.object.delete()

                BaseObject.select_set(True)
                bpy.ops.transform.resize(value=(unscale, unscale, unscale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=0.00271427, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_elements={'INCREMENT'}, use_snap_project=False, snap_target='ACTIVE', use_snap_self=True, use_snap_edit=True, use_snap_nonedit=True, use_snap_selectable=False, release_confirm=True)
                bpy.ops.object.transform_apply(location=False, rotation=True, scale=True, properties=False)

                if index == amountofobjects - 1:
                    BaseObject.select_set(True)
                    bpy.context.view_layer.objects.active = BaseObject
                    bpy.ops.object.mode_set(mode='EDIT')
                    bpy.ops.mesh.select_all(action='SELECT')
                # os.remove(base_file)
                # os.remove(result_file)
                print("Temporary objects have been deleted")
            index += 1
        # Select again objects
        for j in selected_obj:
            j.select_set(True)
            
        bpy.context.view_layer.objects.active = active_obj

        return {'FINISHED'}		