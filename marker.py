import cv2
import numpy as np

def apply_watermark(input_image_path, watermark_image_path, output_image_path, position):
    base_image = cv2.imread(input_image_path)
    watermark = cv2.imread(watermark_image_path, cv2.IMREAD_UNCHANGED)

    if watermark.shape[2] != 4:
        raise ValueError("Watermark image must have an alpha channel (4 channels).")

    base_h, base_w = base_image.shape[:2]
    wm_h, wm_w = watermark.shape[:2]

    if wm_w > base_w or wm_h > base_h:
        scaling_factor = 0.05
        new_wm_w = int(wm_w * scaling_factor)
        new_wm_h = int(wm_h * scaling_factor)
        watermark = cv2.resize(watermark, (new_wm_w, new_wm_h), interpolation = cv2.INTER_AREA)
        wm_h, wm_w = watermark.shape[:2]

    if position == 'center':
        x = (base_w - wm_w) // 2
        y = (base_h - wm_h) // 2
    elif position == 'bottom_right':
        x = base_w - wm_w
        y = base_h - wm_h - 50
    elif position == 'top_left':
        x = 0
        y = 0
    elif position == 'top_right':
        x = base_w - wm_w
        y = 0
    elif position == 'bottom_left':
        x = 0
        y = base_h - wm_h - 50
    else:
        raise ValueError("Invalid position argument. Use 'center', 'bottom_right', 'top_left', 'top_right', or 'bottom_left'.")
    
    wm_bgr = watermark[:, :, :3]
    wm_alpha = watermark[:, :, 3] / 255.0
    inv_alpha = 1.0 - wm_alpha
    roi = base_image[y:y+wm_h, x:x+wm_w]
    for c in range(0, 3):
        roi[:, :, c] = (wm_alpha * wm_bgr[:, :, c] + inv_alpha * roi[:, :, c])

    base_image[y:y+wm_h, x:x+wm_w] = roi


    cv2.imwrite(output_image_path, base_image)

apply_watermark('path to your input image', 'path to your watermark image (png only)', 'output.jpg', 'bottom_right') #position can be changed to 'center', 'top_left', 'top_right', 'bottom_left'
