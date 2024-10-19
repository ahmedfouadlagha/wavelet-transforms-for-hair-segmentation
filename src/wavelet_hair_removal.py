import cv2
import numpy as np
import pywt
from src.config import DECOMPOSITION_LEVELS, WAVELET_TYPE, CLOSING_DISK_SIZE
# from src.image_processing import load_image


def wavelet_transform(gray_img, wavelet=WAVELET_TYPE, levels=DECOMPOSITION_LEVELS):
    """Performs the wavelet transform on the grayscale image."""
    coeffs = pywt.wavedec2(gray_img, wavelet, level=levels, mode='periodization')
    return coeffs

def apply_threshold(cA, threshold_factor=1.5):
    """Applies thresholding on the approximation coefficients."""
    threshold_value = np.median(cA) * threshold_factor
    cA_thresh = np.where(cA > threshold_value, cA, 0)
    # cA_thresh = pywt.threshold(cA, threshold_value, mode='soft')
    return cA_thresh

def reconstruct_image(coeffs_thresh, wavelet=WAVELET_TYPE):
    """Reconstructs the image from the thresholded wavelet coefficients."""
    img_reconstructed = pywt.waverec2(coeffs_thresh, wavelet, mode='periodization')
    return cv2.convertScaleAbs(img_reconstructed)  # Normalize to 8-bit

def otsu_thresholding(img):
    """Applies Otsu's thresholding to obtain a binary mask."""
    _, binary_mask = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary_mask

def inpaint_image(original_img, mask):
    """Removes hair from the image by inpainting using the binary mask."""
    return cv2.inpaint(original_img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

def wavelet_segmentation(image, wavelet=WAVELET_TYPE, levels=DECOMPOSITION_LEVELS, threshold_factor=1.5):
    """
    Performs wavelet-based segmentation on a hair dermoscopy image.

    Args:
        image (numpy.ndarray): Input grayscale image (2D array).
        wavelet (str): Wavelet basis to use.
        levels (int): Number of decomposition levels for wavelet transform.
        threshold_factor (float): Factor for thresholding approximation coefficients (default: 1.5).

    Returns:
        tuple: (binary_mask, hair_removed_image)
               - binary_mask: The segmented binary image (hair regions).
               - hair_removed_image: The image with hair removed.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply histogram equalization
    # gray = cv2.equalizeHist(gray)

    # Preprocessing: Apply Gaussian Blur and CLAHE for contrast enhancement
    smoothed_img = cv2.GaussianBlur(gray, (5, 5), 0)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_gray = clahe.apply(smoothed_img)

    # Wavelet decomposition
    coeffs = pywt.wavedec2(enhanced_gray, wavelet, level=levels, mode='periodization')
    cA = coeffs[0]  # Approximation coefficients

    # Apply thresholding
    threshold_value = np.median(cA) * threshold_factor
    cA_thresh = np.where(cA > threshold_value, cA, 0) # cA_thresh = pywt.threshold(cA, threshold_value, mode='soft')

    # Replace with thresholded coefficients
    coeffs_thresh = [cA_thresh] + list(coeffs[1:])

    # Reconstruct the image from the thresholded coefficients
    img_reconstructed = pywt.waverec2(coeffs_thresh, wavelet, mode='periodization')
    img_reconstructed_8u = cv2.convertScaleAbs(img_reconstructed)

    # Post-processing: Otsu's thresholding + Morphological closing
    _, hair_mask = cv2.threshold(img_reconstructed_8u, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # kernel = np.ones((CLOSING_DISK_SIZE, CLOSING_DISK_SIZE), np.uint8)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (CLOSING_DISK_SIZE, CLOSING_DISK_SIZE))
    binary_mask = cv2.morphologyEx(hair_mask, cv2.MORPH_CLOSE, kernel)

    # Inpainting to remove hair
    hair_removed_img = cv2.inpaint(image, binary_mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    return binary_mask, hair_removed_img
