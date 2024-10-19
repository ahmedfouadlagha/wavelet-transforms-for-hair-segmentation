import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_PATH = os.path.join(BASE_DIR, 'data', 'GAD-VAE-HairRemoval-Dataset', 'test', 'hair_occluded')

SAVE_RESULT = True

# Wavelet
WAVELET_TYPE = 'db4'
DECOMPOSITION_LEVELS = 5  # Number of decomposition levels for WT
CLOSING_DISK_SIZE = 3  # Size of the disk for morphological closing

