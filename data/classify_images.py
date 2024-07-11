#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Nandana santhosh 
# DATE CREATED: 6.7.2024                             
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Classify pet images using a CNN model and compare with pet labels.

    Args:
        images_dir (str): The path to the folder of images to be classified.
        results_dic (dict): A dictionary with image filenames as keys and lists as values.
        model (str): The CNN model architecture to use for classification.

    Returns:
        None
    """
    for key in results_dic:
        if images_dir:
            classified_image = classifier(f"{images_dir}/{key}", model)
        else:
            print("Error: images_dir is None")
            classified_image = ""

        classified_image = classified_image.lower().strip()

        pet_label = results_dic[key][0]
        if pet_label in classified_image:
            results_dic[key].extend([classified_image, 1])
        else:
            results_dic[key].extend([classified_image, 0])

    print(results_dic)