# Material Identification Through Near-Infrared Spectroscopy

This project was the main focus of my Grade 11 Personal Project. My goal was to apply near-infrared spectroscopy to the recycling industry as an efficient and reliable way to identify and sort plastics. Hundreds of different types of plastics exist but cannot be recycled together. Before the recycling process begins, plastic waste has to be sorted manually.

Using a near-infrared spectrometer, I analyzed the reflective properties of approximately 15 different plastic objects at 18 different wavelengths between 410nm and 940nm. Data collected through the spectrometer using an Arduino was transferred to a python program for analysis. The python code has two main functions:

- A data collection function takes in data from the spectrometer and adds it to a CSV file used as a databank.
- A material identifier function takes in spectrometer data from an unknown material and compares it to data found in the databank. The program calculates the euclidean distance between the colleected data and the various materials already stored in the databank to determine which material is likely to be the unknown object. 

