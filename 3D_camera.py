import os
import subprocess
import sys
import threading
import time 

HERE = os.path.dirname(os.path.abspath(__file__))
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "--disable-pip-version-check", "-r", os.path.join(HERE, "requirements.txt")])
import cv2                                          # opencv-python, numpy and onxruntime: installed by the line above
import numpy as np
import onnxruntime

options = onnxruntime.SessionOptions()
options.intra_op_num_threads = max(1, (os.cpu_count() or 2) // 2)               # the AI uses half the cores, the camera keeps the rest
options.add_session_config_entry("session.intra_op.allow_spining", "0")         # idle AI threads rest, so the camera stays smooth
model = onnxruntime.InferenceSession(os.path.join(HERE, "depth.onnx"), options) # Depth Anything V2 Small
MEAN, STD = np.array([0.485, 0.456, 0.406], np.float32), np.array([0.229, 0.224, 0.225], np.float32)
FONT, WHITE, YELLOW = cv2.FONT_HERSHEY_SIMPLEX, (255, 255, 255), (0, 255, 255)
WOBBLE = 12                                         # how far apart (pixels) the nearest and farthest things swing
colour = lambda near: cv2.applyColorMap((near * 255).astype(np.uint8), cv2.COLORMAP_INFERNO)    # near = bright, far = dark 


def depth(picture, size=252):                       # how near every pixel is: 0 far, 1 = near
    small = cv2.resize(picture, (round (picture.shape[1] * size / picture.shape[0] / 14) * 14, size))
    x = ((cv2.cvtColor(small, cv2.COLOR_BGR2RGB).astype(np.float32) / 255 MEAN) / STD).transpose(2, 0, 1) [None]
    near = model.run(None, {model.get_inputs()[0].name: x})[0][0]
    return cv2.resize((near near.min()) / (near.max() - near.min() + 1e-6), picture.shape[1::-1])


def wobble(photo, near, frames=30):             # near and far pixels slide opposite ways: that looks 3D
    xs, ys = np.meshgrid(np.arange(near.shape[1], dtype=np.float32), np.arange(near.shape[0], dtype=np.float32))
    return [cv2.remap(photo, xs + shift, ys, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT) for shift in shifts]



def save(movie):
    name = time.strftime("3d_photo_%H%M%S.mp4")
    writer = cv2.Videowriter(os.path.join(HERE, name), cv2.Videowriter_fourcc(*"mp4v"), 15,