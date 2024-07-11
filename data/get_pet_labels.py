#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nandana Santhosh
# DATE CREATED: 6.6.24                              
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os
from os import listdir


def get_pet_labels(image_dir: str) -> dict:
    """
    Creates a dictionary of pet labels based on the filenames of the image files.

    Parameters:
    image_dir (str): The full path to the folder of images to be classified.

    Returns:
    dict: A dictionary with the image filename as the key and a list containing
          the pet image label as the value.
    """
    filename_list = os.listdir(image_dir)
    results_dic = {}

    for filename in filename_list:
        if not filename.startswith('.'):
            pet_name = ' '.join(word for word in filename.lower().split('_') if word.isalpha()).strip()
            results_dic[filename] = [pet_name]

    print("\nPrinting all key-value pairs in dictionary results_dic:")
    for key, value in results_dic.items():
        print(f"filename = {key}, pet label = {value[0]}")

    return results_dic