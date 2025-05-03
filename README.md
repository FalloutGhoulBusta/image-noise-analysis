# Image Noise Analysis

Python scripts for analyzing and comparing noise levels in digital images.

## Features

- Estimate noise levels in images
- Compare noise between different resolution images (2K vs 4K)
- Visualize noise patterns
- Side-by-side comparison of images with noise metrics

## Requirements

- Python 3.x
- Required packages:
  - Pillow (PIL)
  - NumPy
  - OpenCV
  - Matplotlib

## Usage

1. Place your image files in the same directory as the scripts
2. Update the image paths in the scripts
3. Run the scripts:
   ```
   python compare_two_images_noise.py
   ```

## Scripts

- `compare_two_images_noise.py`: Compares noise between 2K and 4K images
- `image_noise_generator.py`: Generates noise analysis for a single image
- `image_noise_estimater.py`: Estimates noise levels in images
