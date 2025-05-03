from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

# === CONFIGURE FILE PATHS ===
image_2k_path = "your_2k_crop.jpg"  # Replace with path to cropped 2K image
image_4k_path = "your_4k_crop.jpg"  # Replace with path to cropped 4K image

# === LOAD IMAGES ===
img_2k = Image.open(image_2k_path).convert("L")
img_4k = Image.open(image_4k_path).convert("L")

img_2k_np = np.array(img_2k)
img_4k_np = np.array(img_4k)

# === NOISE ESTIMATION FUNCTION ===
def estimate_noise(image_gray):
    blurred = cv2.GaussianBlur(image_gray, (5, 5), 0)
    noise = image_gray.astype(np.float32) - blurred.astype(np.float32)
    return np.std(noise)

# === CALCULATE NOISE ===
noise_2k = estimate_noise(img_2k_np)
noise_4k = estimate_noise(img_4k_np)

# === DISPLAY RESULTS SIDE-BY-SIDE ===
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].imshow(img_2k_np, cmap='gray')
axs[0].set_title(f"2K Crop\nNoise Level: {noise_2k:.2f}")
axs[0].axis("off")

axs[1].imshow(img_4k_np, cmap='gray')
axs[1].set_title(f"4K Crop\nNoise Level: {noise_4k:.2f}")
axs[1].axis("off")

plt.tight_layout()
plt.show()
