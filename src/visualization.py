import cv2
import matplotlib.pyplot as plt
import os
from src.config import SAVE_RESULT


def display_results(original_img, binary_mask, hair_removed_img, img_title, output_dir="results/"):
    """
    Displays and saves the original image, binary mask, and hair-removed image using matplotlib.

    Args:
        original_img (np.ndarray): The original input image.
        binary_mask (np.ndarray): The binary mask showing segmented hair.
        hair_removed_img (np.ndarray): The image after hair removal.
        img_title (str): The title of the image.
        output_dir (str): The output directory to save the image.
    """
    plt.figure(figsize=(12, 4))
    original_img_rgb = cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB)
    hair_removed_img_rgb = cv2.cvtColor(hair_removed_img, cv2.COLOR_BGR2RGB)
    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(original_img_rgb)
    plt.title('Original Image')
    plt.axis('off')

    # Hair mask (segmentation)
    plt.subplot(1, 3, 2)
    plt.imshow(binary_mask, cmap='gray')
    plt.title('Hair Mask')
    plt.axis('off')

    # Hairless image (after hair removal)
    plt.subplot(1, 3, 3)
    plt.imshow(hair_removed_img_rgb)
    plt.title('Hairless Image')
    plt.axis('off')

    plt.tight_layout()
    if SAVE_RESULT:
        plt.savefig(os.path.join(output_dir, img_title), bbox_inches='tight', dpi=300)
    plt.show()
