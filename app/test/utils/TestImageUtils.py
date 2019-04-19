import os
from unittest import TestCase

from app.config import config
from app.utils import image_utils


class TestImageUtils(TestCase):

    def test_overlay(self):
        # Arrange
        origin_file_path = os.path.join(config.SYNTH_IMAGES_PATH, 'monkey_0-0_0_0.png')

        # Act
        combined_paths = image_utils.overlay_images(origin_file_path, config.SYNTH_IMAGES_PATH)

        # Assert
        assert(combined_paths is not None)
        assert(len(combined_paths) > 0)

    def test_extract_image_info(self):
        # Arrange
        file_path = 'C:\\Users\\Chris\\workspaces\\synthetic_ai_blender\\synthetic_images\\monkey_0-2.83_4.41_2.54.png'

        # Act
        file_index_id, pitch, yaw, roll = image_utils.extract_image_info(file_path)

        # Assert
        assert file_index_id == '0'
        assert pitch == 2.83
        assert yaw == 4.41
        assert roll == 2.54