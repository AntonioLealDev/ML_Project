# Importing required libraries
import os

def generatate_negative_description_file(myObj):
    """Generates text file to locate negative files 

    Args:
      myObj: string containg the name of the object to be detected
    """
    # Open output file for writing
    with open("data\\" + myObj + "\\neg.txt", "w") as f:
        # Loop over all the filenames and write them on the file
        for filename in os.listdir("data\\" + myObj + "\\Negative"):
            f.write("negative/" + filename + "\n")

# Calling function
generatate_negative_description_file("Man")