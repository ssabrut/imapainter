import cv2
import sys
import base64
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO

sys.path.append('C:/Users/micha/OneDrive/Documents/JupyterProjects/personal/imapainter/site')
from utils import utils

def resize_img(content_img, style_img):
  content_img = cv2.resize(cv2.imread(content_img), (512, 512))
  style_img = cv2.resize(cv2.imread(style_img), (512, 512))
  return content_img, style_img

def image_to_tensor(content_img, style_img):
  content_img = tf.image.convert_image_dtype(content_img, tf.float32)
  style_img = tf.image.convert_image_dtype(style_img, tf.float32)
  return content_img, style_img

def get_target(content_img, style_img, weights='model/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5'):
  model = utils.load_pre_trained_model(weights)
  content_target = model(np.array([content_img * 255]))[0]
  style_target = model(np.array([style_img * 255]))[1]
  return model, (content_target, style_target)

def normalize_img(content_img):
  content_img = tf.image.convert_image_dtype(content_img, tf.float32)
  content_img = tf.Variable([content_img])
  return content_img

def finalize(content_img):
  content_img = content_img * 255
  content_img = np.array(content_img, dtype=np.uint8)
  if np.ndim(content_img) > 3:
    assert content_img.shape[0] == 1
    content_img = content_img[0]
  content_img = Image.fromarray(content_img)
  
  return content_img

def encode_img(content_img):
  buffered = BytesIO()
  content_img.save(buffered, format='PNG')
  return base64.b64encode(buffered.getvalue()).decode('utf-8')