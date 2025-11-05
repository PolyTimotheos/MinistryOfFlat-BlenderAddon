import bpy
import os
import subprocess
import time

# PropertyGroup for storing properties
class MOFUV_Properties(bpy.types.PropertyGroup):
	useNormals: bpy.props.BoolProperty(
		name="Use Normals",
		description="Use Normals",
		default=False
	)

	separateHardEdges: bpy.props.BoolProperty(
		name="Separate Hard Edges",
		description="Separate Hard Edges",
		default=False
	)

	overlapMirrored: bpy.props.BoolProperty(
		name="Overlap mirrored parts",
		description="Overlap mirrored parts",
		default=False
	)

	overlapIdentical: bpy.props.BoolProperty(
		name="Overlap identical parts",
		description="Overlap identical parts",
		default=False
	)

	keepSourceUVObject: bpy.props.BoolProperty(
		name="Keep Auto UV Object",
		description="Keep Auto UV Object",
		default=False
	)

	seamDirection: bpy.props.FloatVectorProperty(
		name="Seam Direction",
		description="Seam Direction",
		default=(0.0, 0.0, 0.0),
		size=3
	)

	showDebugProperties: bpy.props.BoolProperty(
		name="Show Debug Properties",
		description="Show Debug Properties",
		default=False
	)

	# Debug properties
	supressValidationDebug: bpy.props.BoolProperty(
		name="Supress Validation Debug",
		description="Supress Validation Debug",
		default=False
	)

	quadDebug: bpy.props.BoolProperty(
		name="Quads",
		description="Searches the model for triangle pairs that make good quads. Improves the use of patches.",
		default=True
	)

	vertexWeldDebug: bpy.props.BoolProperty(
		name="Vertex Weld",
		description="Welds vertices that are close together.",
		default=True
	)

	flatDebug: bpy.props.BoolProperty(
		name="Flat Soft surface",
		description="Description: Detects flat areas of soft surfaces in order to minimize their distortion.",
		default=True
	)

	coneDebug: bpy.props.BoolProperty(
		name="Cones",
		description="Searches the model for sharp Cones.",
		default=True
	)

	coneRatioDebug: bpy.props.FloatProperty(
		name="Cone Ratio",
		description="Ratio of the cone angle.",
		default=0.5
	)

	gridsDebug: bpy.props.BoolProperty(
		name="Grids",
		description="Searches the model for grids of quads.",
		default=True
	)

	stripsDebug: bpy.props.BoolProperty(
		name="Strips",
		description="Searches the model for strips of quads.",
		default=True
	)

	patchesDebug: bpy.props.BoolProperty(
		name="Patches",
		description="Searches the model for patches of quads.",
		default=True
	)

	planesDebug: bpy.props.BoolProperty(
		name="Planes",
		description="Detect planes",
		default=True
	)

	flatnessDebug: bpy.props.FloatProperty(
		name="Minimum Flatness",
		description="Minimum normal dot product between two flat polygons.",
		default=0.9
	)

	mergeDebug: bpy.props.BoolProperty(
		name="Merge",
		description="Merges polygons using unfolding",
		default=True
	)

	mergeLimitDebug: bpy.props.FloatProperty(
		name="Merge Limit",
		description="Limit the angle between polygons to merge.",
		default=0.0
	)

	preSmoothDebug: bpy.props.BoolProperty(
		name="Pre Smooth",
		description="Soften the mesh before atempting to cut and project.",
		default=True
	)

	softUnfoldDebug: bpy.props.BoolProperty(
		name="Soft Unfold",
		description="Atempt to unfold soft surfaces.",
		default=True
	)

	tubesDebug: bpy.props.BoolProperty(
		name="Tubes",
		description="Find tube shaped geometry and unwrap it using cylindrical projection.",
		default=True
	)

	junctionsDebug: bpy.props.BoolProperty(
		name="Junctions",
		description="Find and handle Junctions between tubes.",
		default=True
	)

	extraDebug: bpy.props.BoolProperty(
		name="Extra ordinary Point",
		description="Using vertices not sharded by 4 quads as starting points for cutting.",
		default=False
	)

	angleBasedFlatteningDebug: bpy.props.BoolProperty(
		name="Angle Based Flattening",
		description="sing angle based flattening to handle smooth surfaces.",
		default=True
	)

	smoothDebug: bpy.props.BoolProperty(
		name="Smooth",
		description="Cut and project smooth surfaces.",
		default=True
	)

	repairSmoothDebug : bpy.props.BoolProperty(
		name="Repair Smooth",
		description="Attaches small islands to larger islands on smooth surfaces.",
		default=True
	)

	repairDebug: bpy.props.BoolProperty(
		name="Repair",
		description="Repair edges to make then straight.",
		default=True
	)

	squaresDebug: bpy.props.BoolProperty(
		name="Squares",
		description="Finds various individual polygons that have right angles.",
		default=True
	)

	relaxDebug: bpy.props.BoolProperty(
		name="Relax",
		description="Relax all smooth polygons to minimize distortion.",
		default=True
	)

	relaxIterationDebug: bpy.props.IntProperty(
		name="Relaxation Iterations",
		description="The number of iteration loops when relaxing.",
		default=50
	)

	expandDebug: bpy.props.FloatProperty(
		name="Expand",
		description="The amount to expand the UV islands.",
		default=0.25
	)

	cutDebug: bpy.props.BoolProperty(
		name="Cut",
		description="Cut",
		default=True
	)

	stretchDebug: bpy.props.BoolProperty(
		name="Stretch",
		description="Stretch",
		default=True
	)

	matchDebug: bpy.props.BoolProperty(
		name="Match",
		description="Match",
		default=True
	)

	packingDebug: bpy.props.BoolProperty(
		name="Packing",
		description="Packing",
		default=True
	)

	rasteriationResolutionDebug: bpy.props.IntProperty(
		name="Rasteriation Resolution",
		description="The resolution of the rasterization.",
		default=64
	)

	packingIterationsDebug: bpy.props.IntProperty(
		name="Packing Iterations",
		description="The number of iterations when packing.",
		default=4
	)

	scaleToFitDebug: bpy.props.FloatProperty(
		name="Scale To Fit",
		description="Scale To Fit",
		default=0.500000
	)

	validateDebug: bpy.props.BoolProperty(
		name="Validate",
		description="Validate",
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
		layout.prop(mofuv_props, 'keepSourceUVObject')
		layout.prop(mofuv_props, 'overlapMirrored')
		layout.prop(mofuv_props, 'overlapIdentical')
		layout.prop(mofuv_props, 'seamDirection')

		# Operator button
		layout.operator("view3d.mofmulti_autouv", text="AutoUV")
		layout.prop(mofuv_props, 'showDebugProperties')

		# Debug properties
		if mofuv_props.showDebugProperties:
			layout.prop(mofuv_props, 'supressValidationDebug')
			layout.prop(mofuv_props, 'quadDebug')
			layout.prop(mofuv_props, 'vertexWeldDebug')
			layout.prop(mofuv_props, 'flatDebug')
			layout.prop(mofuv_props, 'coneDebug')
			layout.prop(mofuv_props, 'coneRatioDebug')
			layout.prop(mofuv_props, 'gridsDebug')
			layout.prop(mofuv_props, 'stripsDebug')
			layout.prop(mofuv_props, 'patchesDebug')
			layout.prop(mofuv_props, 'planesDebug')
			layout.prop(mofuv_props, 'flatnessDebug')
			layout.prop(mofuv_props, 'mergeDebug')
			layout.prop(mofuv_props, 'mergeLimitDebug')
			layout.prop(mofuv_props, 'preSmoothDebug')
			layout.prop(mofuv_props, 'softUnfoldDebug')
			layout.prop(mofuv_props, 'tubesDebug')
			layout.prop(mofuv_props, 'junctionsDebug')
			layout.prop(mofuv_props, 'extraDebug')
			layout.prop(mofuv_props, 'angleBasedFlatteningDebug')
			layout.prop(mofuv_props, 'smoothDebug')
			layout.prop(mofuv_props, 'repairSmoothDebug')
			layout.prop(mofuv_props, 'repairDebug')
			layout.prop(mofuv_props, 'squaresDebug')
			layout.prop(mofuv_props, 'relaxDebug')
			layout.prop(mofuv_props, 'relaxIterationDebug')
			layout.prop(mofuv_props, 'expandDebug')
			layout.prop(mofuv_props, 'cutDebug')
			layout.prop(mofuv_props, 'stretchDebug')
			layout.prop(mofuv_props, 'matchDebug')
			layout.prop(mofuv_props, 'packingDebug')
			layout.prop(mofuv_props, 'rasteriationResolutionDebug')
			layout.prop(mofuv_props, 'packingIterationsDebug')
			layout.prop(mofuv_props, 'scaleToFitDebug')
			layout.prop(mofuv_props, 'validateDebug')


		




