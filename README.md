# ProfessorDoppleganger
ProfessorDoppleganger is a project that takes a picture of someone's face as input and finds the CMU professor that looks most similar to them. It uses the Microsoft Azure Face API.

# How to use it
Once you download the project, replace the Microsoft Azure subscription key with yours in the marked area in Image_properties.py. Then, run Testing.py from the command line with the file path to the input image as an argument. Note: You don't need the folder marked by ProfWebsite.

# How it works
The program sends a request to Microsoft Azure with the input image. Then it takes the results and compares it to all CMU professors and generates a score. It then returns the image of the professor with the highest score.
