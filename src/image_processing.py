import os
import cv2
import random


def load_image(image_path):
    """Loads an image from the specified path."""
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Image not found at path: {image_path}")
    return img

def convert_to_grayscale(img):
    """Converts the input image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def load_random_images(dataset_path, num_samples=3):
    """Loads a random selection of images from the dataset."""
    image_files = [f for f in os.listdir(dataset_path) if os.path.isfile(os.path.join(dataset_path, f))]
    random_samples = random.sample(image_files, num_samples)

    images = []
    for img_file in random_samples:
        img_path = os.path.join(dataset_path, img_file)
        img = cv2.imread(img_path)
        if img is not None:
            images.append((img, img_file))
    return images

def histogram_equalization(gray_img):
    """
    Enhances contrast by applying histogram equalization.
    """
    return cv2.equalizeHist(gray_img)
