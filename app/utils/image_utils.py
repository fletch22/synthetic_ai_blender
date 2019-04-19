import os

from app import overlay
from app.config import config
from app.services import file_services
import logging


def overlay_images(origin_image_path, images_dir_path):
    file_paths = file_services.walk_dir(images_dir_path)
    file_paths.remove(origin_image_path)

    file_services.empty_dir(config.OVERLAY_IMAGE_PATH)

    _, pitch_origin, yaw_origin, roll_origin = extract_image_info(origin_image_path)

    output_path_list = []
    for fp in file_paths:
        overlay_filename = create_overlay_filename(fp, pitch_origin, yaw_origin, roll_origin)
        output_path = os.path.join(config.OVERLAY_IMAGE_PATH, overlay_filename)
        overlay.run(origin_image_path, fp, output_path)
        output_path_list.append(output_path)
        break

    return output_path_list


def create_overlay_filename(target_file_path, yaw_origin, pitch_origin, roll_origin):
    file_index_id, pitch_target, yaw_target, roll_target = extract_image_info(target_file_path)

    return f"output_{file_index_id}-{pitch_target - pitch_origin}_{yaw_target - yaw_origin}_{roll_target - roll_origin}.png"


def extract_image_info(file_path):
    filename, _ = os.path.splitext(os.path.basename(file_path))

    left, right = filename.split('-')
    file_index_id = left.split('_')[1]

    pitch, yaw, roll = right.split('_')

    return file_index_id, float(pitch), float(yaw), float(roll)
