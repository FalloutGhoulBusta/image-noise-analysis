# Image Noise Analysis

A Python-based toolkit for analyzing and comparing noise levels in digital images, specifically designed for comparing noise between different image resolutions.

## Overview

This project provides tools to:
- Quantitatively measure noise levels in digital images
- Compare noise characteristics between different resolution images (2K vs 4K)
- Visualize noise patterns through image processing techniques
- Generate side-by-side comparisons with noise metrics

## Features

- **Noise Estimation**: Uses Gaussian blur and difference calculation to estimate noise levels
- **Resolution Comparison**: Specialized for comparing noise between 2K and 4K images
- **Visualization**: Generates visual representations of noise patterns
- **Side-by-Side Comparison**: Displays both images with their noise metrics
- **Image Processing**: Utilizes advanced image processing techniques for accurate noise analysis

## Technical Details

The noise estimation algorithm works by:
1. Applying a Gaussian blur to reduce high-frequency noise
2. Calculating the difference between the original and blurred image
3. Measuring the standard deviation of the difference to quantify noise

## Requirements

- Python 3.x
- Required packages:
  - Pillow (PIL) - For image handling
  - NumPy - For numerical operations
  - OpenCV - For image processing
  - Matplotlib - For visualization

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/FalloutGhoulBusta/image-noise-analysis.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your image files in the same directory as the scripts
2. Update the image paths in the scripts to point to your images
3. Run the comparison script:
   ```bash
   python compare_two_images_noise.py
   ```

The script will:
- Load your images in grayscale
- Calculate noise levels for both images
- Generate a side-by-side comparison
- Display the results in a window

## Scripts

- `compare_two_images_noise.py`: Main script for comparing noise between 2K and 4K images
- `image_noise_generator.py`: Generates noise analysis for a single image
- `image_noise_estimater.py`: Core noise estimation functionality

## Author

Created by FalloutGhoulBusta

## Acknowledgments

- Uses OpenCV for image processing
- Utilizes NumPy for efficient numerical computations
- Leverages Matplotlib for visualization capabilities
