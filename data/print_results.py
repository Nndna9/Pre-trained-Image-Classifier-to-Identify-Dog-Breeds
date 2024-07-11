#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Nandana Santhosh
# DATE CREATED:7.7.24
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    """
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    print(f"N Images: {results_stats_dic['n_images']}")
    print(f"N Dog Images: {results_stats_dic['n_dogs_img']}")
    print(f"N Not-Dog Images: {results_stats_dic['n_notdogs_img']}")

    print("\nSummary Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith("p"):
            print(f"{key}: {value}")

    if print_incorrect_dogs and results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']:
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key, value in results_dic.items():
            if value[3] + value[4] == 1:
                print(f"Pet Label: {value[0]}\nClassifier Label: {value[1]}")

    if print_incorrect_breed and results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']:
        print("\nINCORRECT Dog Breed Assignment:")
        for key, value in results_dic.items():
            if sum(value[3:]) == 1 and value[2] == 0:
                print(f"Real: {value[0]:>26}   Classifier: {value[1]:>30}")
            elif sum(value[3:]) == 2 and value[2] == 0:
                print(f"Real: {value[0]:>26}   Classifier: {value[1]:>30}")