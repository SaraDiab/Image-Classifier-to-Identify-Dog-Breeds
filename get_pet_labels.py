#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER:Sarah Emad Diab
# DATE CREATED: June 13                                    
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
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    ## Retrieve the filenames from folder pet_images/
    filename_list = listdir(image_dir)

    ## Creates empty dictionary named results_dic
    results_dic = dict()
    ## Determines number of items in dictionary
    items_in_dic = len(results_dic)
    print("\nEmpty Dictionary results_dic - n items=", items_in_dic)

    ## Adds new key-value pairs to dictionary ONLY when key doesn't already exist. This dictionary's value is
    ## a List that contains only one item - the pet image label
     # Process each filename to create the pet image labels
    prepare_result_dict_using_filename_as_key_and_petname_as_value(filename_list, results_dic)
    return results_dic

def prepare_result_dict_using_filename_as_key_and_petname_as_value(filename_list, results_dic):
    """
    Prepare the results dictionary using the filename as the key and the pet name as the value.

    Args:
        filename_list (list): A list of filenames.
        results_dic (dict): A dictionary to store the results as {filename: [pet_name]}.
    Returns:
        None

    """
    for filename in filename_list:
        pet_name = prepare_pet_name(filename)
        if filename in results_dic:
            continue
        results_dic[filename] = [pet_name]

def prepare_pet_name(filename):
    """
    Prepare the pet name from a given filename.
    Args:
        filename (str): The filename which is used to extract the pet name from.
    Returns:
        str: The pet name after modification.
    """
    filename_lowercase = filename.lower()
    words = filename_lowercase.split("_")
    pet_name = " ".join(word.strip() for word in words if word.isalpha())
    return pet_name
