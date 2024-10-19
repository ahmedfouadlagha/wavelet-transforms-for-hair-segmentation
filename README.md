# Hair Removal from Dermoscopy Images
![hair_removal_result.png](results%2Fhair_removal_result.jpg)
## Overview

This project aims to remove hair occlusions from dermoscopy images using wavelet transforms and image processing techniques. The goal is to enhance the visibility of skin lesions by segmenting and eliminating hair from the images.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Dataset](#dataset)
- [Usage](#usage)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Features

- **Wavelet Transform**: Utilizes the Discrete Wavelet Transform (DWT) for effective hair segmentation.
- **Adaptive Thresholding**: Implements adaptive thresholding techniques for accurate hair mask generation.
- **Morphological Operations**: Cleans up the segmented hair mask using morphological operations.
- **Visualization**: Displays original, segmented, and hairless images for easy comparison.

## Requirements

To run this project, you will need the following libraries:

- Python 3.x
- OpenCV
- NumPy
- PyWavelets
- Matplotlib

You can install the required packages using pip:

```bash
pip install opencv-python numpy pywavelets matplotlib
```
## Dataset
The dataset used in this project is the GAD-VAE Hair Removal Dataset, which contains dermoscopy 
images with hair occlusions. You can download the dataset from [this link](https://www.kaggle.com/datasets/bardoudalal/gad-vae-hairremovaldataset).

## Directory Structure
```
project/
│
├── data/
│   └── GAD-VAE-HairRemoval-Dataset/
│       └── test/
│           └── hair_occluded/
│               ├── ISIC_0024314.jpg
│               ├── ISIC_0024315.jpg
│               └── ...
│
├── results/
│   └── hair_removal_result.jpg/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── image_processing.py
│   ├── wavelet_hair_removal.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Usage
Clone the repository:
```
git clone https://github.com/ahmedfouadlagha/wavelet_hair_removal.git
cd wavelet_hair_removal
```
Install the required dependencies:

```bsh
pip install -r requirements.txt
```
Run the main script to process the images:

```bsh
python main.py
```

The processed images will be displayed, showing the original, hair mask, and hairless images.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Thanks to the author of the GAD-VAE Hair Removal Dataset **Prof. D. BARDOU**.<br>
Special thanks to the maintainers of the libraries used in this project.