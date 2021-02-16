
### Project Overview
Welcome to the dog breed classifier project. This project uses Convolutional Neural Networks (CNNs)! In this project, you will learn how to build a pipeline to process real-world, user-supplied images. Given an image of a dog, your algorithm will identify an estimate of the canine’s breed. If supplied an image of a human, the code will identify the resembling dog breed.

### Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Acknowledgements](#ack)

### Requirements <a name="requirements"></a>
Python3 and the following libraries: 
* opencv-python
* h5py
* matplotlib
* numpy
* scipy
* tqdm
* scikit-learn
* keras
* tensorflow
* jupyterlabs


### File Descriptions <a name="files"></a>

Some important files used in the project include:
1. haarcascades/haarcascade_frontalface_alt.xml: Viola-Jones face detector provided by OpenCV.
2. saved_models/weights.best.InceptionV3.hdf5: Inception v3 model trained using transfer learning.
3. dog_app.ipynb: a notebook that explains the classifier code.
4. extract_bottleneck_features.py: functions to compute bottleneck features of image
5. images/: contains few random images

### Results <a name="results"></a>

1. saved_models/weights.best.from_scratch.hdf5
2. saved_models/weights.best.VGG16.hdf5
3. saved_models/weights.best.InceptionV3.hdf5

For more information, check the medium article: https://xscbsx.medium.com/how-to-identify-dog-breeds-using-cnn-204a36ec2e7a

### Acknowledgements <a name="ack"></a>
Thanks to Udacity's Data Science Nano Degree Program team!
