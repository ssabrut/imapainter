# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:31:20 2022

@author: micha
"""

import tensorflow as tf
from tensorflow.keras import Model

def gram_matrix(tensor):
    """
    
    Get the gram matrix from the i and j product (Gij)
    
    Parameters
    ----------
    tensor : Output tensor from each style layer output.

    Returns
    -------
    gram matrix : Tensor where gram matrix divided by i and j dot product.
    
    """
    
    result = tf.linalg.einsum('bijc,bijd->bcd', tensor, tensor) # equation pattern from gram matrix with batches
    gram_matrix = tf.expand_dims(result, axis=0) # add batches to outer layer
    input_shape = tf.shape(tensor) # get the shape of input tensor
    i_dot_j = tf.cast(input_shape[1] * input_shape[2], tf.float32) # convert the dot product to tf float32
    return gram_matrix / i_dot_j

def load_pre_trained_model(weights=None):
    """

    Create the pre trained model

    Parameters
    ----------
    weights : Path to local weights.

    Returns
    -------
    model : Keras class Model loaded with pre trained model.

    """
    
    vgg = tf.keras.applications.VGG19(include_top=False, weights=weights) # initialize pre trained model
    vgg.load_weights(weights) # load the pre trained model weights
    vgg.trainable = False
    content_layers = ['block4_conv2'] # select the layer for content layer
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1', 'block4_conv1', 'block5_conv1'] # select the layer for style layer
    content_output = vgg.get_layer(content_layers[0]).output # get the content layer output
    style_output = [vgg.get_layer(style_layer).output for style_layer in style_layers] # get all the style layer output
    gram_style_output = [gram_matrix(output) for output in style_output] # get the gram matrix for all output style layer
    model = Model([vgg.input], [content_output, gram_style_output])
    return model

def loss_object(style_outputs, content_outputs, style_target, content_target):
    """
    
    Calculate the total loss object from the content and style image
    
    Parameters
    ----------
    style_outputs : G from the equation.
    content_outputs : F from the equation.
    style_target : A from the equation.
    content_target : P from the equation.

    Returns
    -------
    total_loss : The compute from the content_loss * content_weight plus style_loss * style_weight.

    """
    
    style_weight = 1e-2 # alpha from the loss total equation
    content_weight = 1e-1 # beta from the loss total equation
    content_loss = tf.reduce_mean((content_outputs - content_target) ** 2)
    style_loss = tf.add_n([tf.reduce_mean((output - target) ** 2) for output, target in zip(style_outputs, style_target)])
    total_loss = content_weight * content_loss + style_weight * style_loss
    return total_loss
    
def train_step(image, epoch, style_target, content_target, optimizer, model, start):
    """
    
    Train the style transfer model

    Parameters
    ----------
    image : The image array.
    epoch : Current iteration.

    Returns
    -------
    None.

    """
    
    with tf.GradientTape() as tape:
        output = model(image * 255) # convert to original range 0 to 255
        loss = loss_object(output[1], output[0], style_target, content_target)
    gradient = tape.gradient(loss, image) # calculate the gradient for backprop
    optimizer.apply_gradients([(gradient, image)]) # optimize the gradient and to backprop through image
    image.assign(tf.clip_by_value(image, clip_value_min=0.0, clip_value_max=1.0)) # to clip image pixel between 0 to 1
    
    if epoch % 100 == 0:
        tf.print(f'Epoch {epoch} : Loss = {loss}')