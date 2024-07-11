#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Nandana santhosh
# DATE CREATED:  28.06.2024                                
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Import necessary modules
import time
import os
from print_functions_for_lab_checks import *
from get_input_args import *
from get_pet_labels import *
from classify_images import *
from adjust_results4_isadog import *
from calculates_results_stats import *
from print_results import *

def main():
    # Measure total program runtime by collecting start time
    start_time = time.time()

    # Define get_input_args function within the file get_input_args.py
    # This function retrieves command line arguments from the user
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg
    # This function checks if the command line arguments are valid
    check_command_line_arguments(in_arg)

    # Define get_pet_labels function within the file get_pet_labels.py
    # This function creates a dictionary of pet labels from the pet images directory
    results = get_pet_labels(in_arg.dir)

    # Function that checks Pet Images in the results Dictionary using results
    # This function checks if the pet images are correctly labeled
    check_creating_pet_image_labels(results)

    # Define classify_images function within the file classify_images.py
    # This function classifies the pet images using a pre-trained CNN model
    classify_images(in_arg.dir, results, in_arg.arch)

    # Function that checks Results Dictionary using results
    # This function checks if the classification results are correct
    check_classifying_images(results)

    # Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    # This function adjusts the classification results for is-a-dog labels
    adjust_results4_isadog(results, in_arg.dogfile)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    # This function checks if the is-a-dog labels are correctly adjusted
    check_classifying_labels_as_dogs(results)

    # Define calculates_results_stats function within the file calculates_results_stats.py
    # This function calculates statistics from the classification results
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    # This function checks if the statistics are correctly calculated
    check_calculating_results(results, results_stats)

    # Define print_results function within the file print_results.py
    # This function prints the classification results and statistics
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time.time()

    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )

if __name__ == "__main__":
    main()