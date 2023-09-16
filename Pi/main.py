import datetime
import os
import time
import sys

from google.cloud import storage
from picamera2 import Picamera2, Preview


storage_client = storage.Client(project="thermal-loop-399213")
bucket = storage_client.bucket("htn2023_pi")

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(
    main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores"
)
picam2.configure(camera_config)
picam2.start()

while True:
    now = datetime.datetime.now().isoformat().replace(" ", "_")
    filename = f"{now}.jpg"
    picam2.capture_file(filename)

    blob = bucket.blob(filename)
    blob.upload_from_filename(filename, if_generation_match=0)

    os.remove(filename)
    time.sleep(30)
