# Week 3 - Task 1: Neural Network for Image Classification

## Overview

This project focuses on building a Convolutional Neural Network (CNN) for image classification using TensorFlow and Keras.

The model was trained on the MNIST Handwritten Digits Dataset to classify images of handwritten digits from 0 to 9.

## Dataset

**Dataset:** MNIST Handwritten Digits Dataset

- 60,000 training images
- 10,000 test images
- Image size: 28 × 28 pixels
- 10 classes: 0–9
- Grayscale images

The dataset was loaded using the TensorFlow/Keras built-in MNIST dataset loader.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Google Colab

## CNN Workflow

The project follows this workflow:

1. Load the MNIST dataset
2. Preprocess and normalize image data
3. Reshape images for CNN input
4. Build a Convolutional Neural Network
5. Train the model using training data
6. Validate the model during training
7. Plot training and validation accuracy
8. Plot training and validation loss
9. Evaluate the model on the test dataset
10. Generate predictions on sample images

## Model Architecture

The CNN consists of:

- Convolutional Layer
- Max Pooling Layer
- Convolutional Layer
- Max Pooling Layer
- Flatten Layer
- Dense Layer
- Output Layer with 10 classes

## Model Performance

**Final Test Accuracy: 98.75%**

The model achieved a test accuracy of **98.75%** on the MNIST test dataset.

## Training and Validation Curves

Training and validation accuracy and loss curves were plotted to observe the model's learning performance and check for possible overfitting.

## Sample Predictions

The trained CNN was tested on sample MNIST images. The notebook displays the actual labels and predicted labels for comparison.

## Files

- `MNIST_CNN_Image_Classification.ipynb` - Complete CNN implementation and results
- `README.md` - Project documentation
