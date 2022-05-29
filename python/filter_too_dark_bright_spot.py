import cv2
import glob
import os
import numpy as np

MAX_THR = 50
MIN_THR = 205
KERNAL_SIZE = 3

SINGLE_FILE = "size_correct/d42647ed2b51eec390d691f3b3f0eb03.jpg"
# FILTER_PATH = os.path.join("too_dark", "*.jpg")
FILTER_PATH = os.path.join("size_correct", "*.jpg")


def calculate_percent(img_path):
    img = cv2.imread(img_path)
    h, w, _ = img.shape
    mask = np.zeros(img.shape[:2], dtype=np.uint8)

    # find too dark area
    max_value = np.amax(img, axis=2)
    mask[np.where(max_value < MAX_THR)] = 1

    # find too bright area
    min_value = np.amin(img, axis=2)
    mask[np.where(MIN_THR < min_value)] = 1

    # erode and dilate
    _, thresh = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
    kernel = np.ones((KERNAL_SIZE, KERNAL_SIZE), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

    # find max contour area
    cnts, _ = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    max_area = 0
    for c in cnts:
        c_area = cv2.contourArea(c)
        if max_area < c_area:
            max_area = c_area

    # calcuate too dark or too bright area of percent
    percent = max_area / (w * h)
    cv2.imwrite("mask.jpg", thresh)

    return percent


if __name__ == "__main__":
    # for img_path in glob.glob(FILTER_PATH):
    #     percent = calculate_percent(img_path)
    #     print(f"{percent}| {img_path}")

    print(calculate_percent(SINGLE_FILE))
