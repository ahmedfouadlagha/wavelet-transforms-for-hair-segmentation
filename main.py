from src import wavelet_segmentation, display_results, load_random_images
from src.config import DATASET_PATH
# from src.image_processing import load_image

if __name__ == "__main__":
    # image_path = './data/dermoscopy_image.png'
    # img = load_image(image_path)
    # binary_mask, hair_removed_img = wavelet_segmentation(img)
    # display_results(img, binary_mask, hair_removed_img, 'hair_removal_result.jpg')

    random_images = load_random_images(DATASET_PATH, num_samples=3)
    for img, img_file in random_images:
        binary_mask, hair_removed_img = wavelet_segmentation(img)
        display_results(img, binary_mask, hair_removed_img, img_file)

