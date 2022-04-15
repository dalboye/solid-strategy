import cv2
import os
from pathlib import Path
from typing import Callable, Any


def high_smoothed_cartoonify(color_image: str):
    print("High Smoothed Cartoonify function is running")
    return cv2.stylization(color_image, sigma_s=150, sigma_r=0.25)

def low_smoothed_cartoonify(color_image: str):
    print("Low Smoothed Cartoonify function is running")
    return cv2.stylization(color_image, sigma_s=60, sigma_r=0.5)

def experimental_cartoonify(color_image: str):
    print("Experimental Cartoonify function is running")
    return cv2.stylization(color_image, sigma_s=200, sigma_r=1.5)

def no_cartoonify(color_image: str):
    print("No Cartoonify function is running")
    return color_image

cartoonify_selection_dict = {
    "0": no_cartoonify,
    "1": high_smoothed_cartoonify,
    "2": low_smoothed_cartoonify,
    "3": experimental_cartoonify,
}

class Cartonify:
    def __init__(self, directory_name: str, image_name: str):
        self.image_name = image_name
        self.directory_name = directory_name
        self.color_image = None
        
    def cartonify(self, cartoonify_strategy: Callable[[str], Any]):
        try:
            self.color_image = cv2.imread(f"{self.directory_name}{self.image_name}")
        except:
            print("There is something wrong with the image file.")
            return
        
        cv2.imshow('cartoon', cartoonify_strategy(self.color_image))
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    #image_name = input("Please enter the name of the image file that you want to process: ")
    #image_directory = input("Please enter the directory that may contain the image: ")

    image_name = "kus.jpeg"
    image_directory = "/Users/lg48np/Projects/dp-examples/easy_cartonify/pictures/"

    os.chdir(Path(image_directory))
    cartoon_style_selection = input("This script currently has 2 sytles. Please type 1, 2, or 3 ")
    
    cartonify = Cartonify(image_directory, image_name)
    if cartoon_style_selection in cartoonify_selection_dict.keys():
        cartonify.cartonify(cartoonify_selection_dict[cartoon_style_selection])
    else:
        cartonify.cartonify(cartoonify_selection_dict["0"])
