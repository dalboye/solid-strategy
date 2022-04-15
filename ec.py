import cv2
import os
from pathlib import Path


class Cartonify:
    def __init__(self, directory_name: str, image_name: str):
        self.image_name = image_name
        self.directory_name = directory_name
        self.color_image = None
        
    def cartonify(self, cartoon_style_selection: str):
        try:
            self.color_image = cv2.imread(f"{self.directory_name}{self.image_name}")
        except:
            print("There is something wrong with the image file.")
            return
        
        if (cartoon_style_selection == "1"):
            cartoon_image_style_1 = cv2.stylization(self.color_image, sigma_s=150, sigma_r=0.25) 
            cv2.imshow('cartoon_1', cartoon_image_style_1)
            cv2.waitKey()
            cv2.destroyAllWindows()
        elif (cartoon_style_selection == "2"):
            cartoon_image_style_2  = cv2.stylization(self.color_image, sigma_s=60, sigma_r=0.5) 
            cv2.imshow('cartoon_2', cartoon_image_style_2)
            cv2.waitKey()
            cv2.destroyAllWindows()
        else:
            print("Invalid selection.")

if __name__ == '__main__':
    #image_name = input("Please enter the name of the image file that you want to process: ")
    #image_directory = input("Please enter the directory that may contain the image: ")

    image_name = "kus.jpeg"
    image_directory = "pictures/"

    cartoon_style_selection = input("This script currently has 2 sytles. Please type 1 or 2. ")
    
    cartonify = Cartonify(image_directory, image_name)
    cartonify.cartonify(cartoon_style_selection)
