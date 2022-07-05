# Material Identification Through Near-Infrared Spectroscopy

This project was the main focus of my Grade 11 Personal Project. My goal was to apply near-infrared spectroscopy to the recycling industry as an efficient and reliable way to identify and sort plastics. Hundreds of different types of plastics exist but cannot be recycled together. Before the recycling process begins, plastic waste has to be sorted manually.

Using a near-infrared spectrometer, I analyzed the reflective properties of 20 different objects at 18 different wavelengths between 410 and 940nm. Data collected through the spectrometer using an Arduino was transferred to a python program for analysis. I made use of the [SparkFun Triad Spectroscopy Sensor (AS7265x)](https://github.com/sparkfun/SparkFun_AS7265x_Arduino_Library) and their open source Arduino library. 

The python code has two main functions:

- A data collection function takes in data from the spectrometer and adds it to a CSV file used as a databank.
- A material identifier function takes in spectrometer data from an unknown material and compares it to data found in the databank. The program calculates the euclidean distance between the colleected data and the various materials already stored in the databank to determine which material is likely to be the unknown object. 

During experimentation, nearly every material scanned by the spectrometer was correctly identified except highly transparent and heterogeneous materials where reflectivity can vary quite significantly. My experimentation during this project was primarily to demonstrate proof-of-concept and to establish near-infrared spectroscopy as a viable technology for recycling and material identification. While some near-infrared technology already exists in a handful of recycling plants, the use of an affordable, small-scale spectrometer has viable applications in private and public spheres as a means to quickly identify unnkown materials.

I hope to shed light on a relatively unknown technology with huge potential to solve the plastic pollution crisis and to revolutionize the recycling industry. For further analysis and improvements, please refer to my research paper included in the files.

_Luca Scavone_
