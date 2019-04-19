import os


PROJECT_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

LOG_PATH = os.path.join(PROJECT_ROOT_PATH, 'logs')

SYNTH_IMAGES_PATH = os.path.join(PROJECT_ROOT_PATH, 'synthetic_images')

OVERLAY_IMAGE_PATH = os.path.join(SYNTH_IMAGES_PATH, 'overlay')