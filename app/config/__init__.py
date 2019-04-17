import sys
import os
import logging
from app.config import config

log_path = os.path.join(config.LOG_PATH, 'synth_ai_blender.log')

logging.basicConfig(filename=log_path,level=logging.INFO)

root = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)