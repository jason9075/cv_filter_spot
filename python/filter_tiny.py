import glob
import os
import cv2
import shutil


def main():
    paths = glob.glob(os.path.join("photo", "**", "*.jpg"))
    for path in paths:
        img = cv2.imread(path)
        h, w, _ = img.shape

        if 120 < h and 120 < w:
            filename = path.split("/")[-1]
            shutil.copy(path, os.path.join("python", "size_correct", filename))


if __name__ == "__main__":
    main()
