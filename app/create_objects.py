import bpy
from random import randint
from math import radians
import mathutils
import random

num_renderings = 20000

# Clear Screen
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete(use_global=False)

# Add main object to center of scene
bpy.ops.mesh.primitive_monkey_add(location=(0,0,0))

# Get and position camera
distance = 0.0
camera = bpy.data.objects["Camera"]
camera.location = (0.0, 0.0, distance)

bpy.ops.object.select_camera()
bpy.ops.transform.translate(value=(-2.38419e-007, -7.99027, 0), constraint_axis=(False, True, False), constraint_orientation='GIMBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
bpy.ops.transform.translate(value=(0, -0, 4.0), constraint_axis=(False, False, True), constraint_orientation='GIMBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)

object_name = "monkey"
file_path = "C:\\Users\\Chris\\workspaces\\synthetic_ai_blender\\synthetic_images\\"
image_prefix = "{}_".format(object_name)

bpy.data.scenes["Scene"].render.filepath = "{0}{1}0-0_0_0.png".format(file_path, image_prefix)
bpy.ops.render.render(write_still=True)

max_degree_delta = 5
main_object = bpy.data.objects['Suzanne']

original_a = main_object.rotation_euler[0]
original_b = main_object.rotation_euler[1]
original_c = main_object.rotation_euler[2]

for index in range(0, num_renderings):
    # Reset to original orienation
    main_object.rotation_euler[0] = original_a
    main_object.rotation_euler[1] = original_b
    main_object.rotation_euler[2] = original_c

    # Set to random orientation
    a = round(random.uniform(0, max_degree_delta), 2)
    b = round(random.uniform(0, max_degree_delta), 2)
    c = round(random.uniform(0, max_degree_delta), 2)

    main_object.rotation_euler[0] = radians(a)
    main_object.rotation_euler[1] = radians(b)
    main_object.rotation_euler[2] = radians(c)

    bpy.data.scenes["Scene"].render.filepath = "{0}{1}{2}-{3}_{4}_{5}.png".format(file_path, image_prefix, index, a, b, c)
    print("rendered: " + bpy.data.scenes["Scene"].render.filepath)
    bpy.ops.render.render(write_still = True)
