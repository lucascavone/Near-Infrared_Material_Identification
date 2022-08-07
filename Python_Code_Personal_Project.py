from ast import literal_eval
import csv
import serial
import numpy as np
import math
import time

data_bank_average = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
average_list = []
ser = serial.Serial("/dev/cu.usbmodem1D11141", baudrate=9600, timeout=1)  # Sets port for serial communication


def updating_list():  # Data from 5 Arduino measurements appended to list data_bank_average
    counts = 0
    while counts != 5:
        ser.write(b'g')
        data = ser.readline().decode('ascii')
        split_data = data.split()
        material = split_data
        updated_material = []
        for m in material:
            updated_value = float(m)
            updated_material.append(updated_value)
        print(updated_material)

        for d in range(0, len(data_bank_average)):
            data_bank_average[d].append(updated_material[d])
        counts += 1
        time.sleep(0.2)
    return


def finding_average():  # Data from list data_bank_average averaged and appended to list average_list
    for d in range(0, len(data_bank_average)):
        average = 0
        for i in range(0, len(data_bank_average[d])):
            average += data_bank_average[d][i]
        average = average / len(data_bank_average[0])
        average = round(average, 2)
        average_list.append(average)
    return average_list


print('''
Welcome to the Material Identifier. What would you like to do?
> Add a material (1)
> Scan a material (2)
> See a list of the available materials (3)
> About the program (4)
> Terminate (0)
    ''')
while True:
    command = str(input("Enter command: "))
    if command == '1':  # Data from Arduino is averaged and appended to a CSV file
        add_data = input('Add data? (press "y") ').lower()
        if add_data == 'y':
            average_list = []
            data_bank_average = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
            updating_list()
            print(f'The data collected is: {finding_average()}')
            with open('Data_Bank.csv', 'r') as read_file:
                reader = csv.reader(read_file)
                with open('Data_Bank.csv', 'a') as write_file:
                    writer = csv.writer(write_file)
                    material_name = input('What material do you wish to add? ')
                    writer.writerow([material_name, average_list])
                for row in reader:
                    print(row)
    elif command == '2':  # Data from Arduino is averaged and compared to data in CSV file, closest match is outputted
        add_data = input('Get data? (press "y") ').lower()
        if add_data == 'y':
            average_list = []
            data_bank_average = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
            updating_list()
            finding_average()
            np.asarray(average_list)
            print(f'The data collected is: {average_list}')
            with open('Data_Bank.csv', 'r') as read_file:
                reader = csv.reader(read_file)
                next(reader)
                min_final_array = 1000000
                for row in reader:  # Euclidean distance calculation for every row in CSV file
                    final_array = 0
                    data_row = np.array(literal_eval(row[1]))
                    inter_array = (data_row - average_list)**2
                    for val in inter_array:
                        final_array += val
                    final_array = math.sqrt(final_array)
                    if final_array <= min_final_array:  # Row with smallest euclidean dist. is the identified material
                        min_final_array = final_array
                        material_name = row[0]
                        exp_values = 0
                        theo_values = 0
                        for dd in data_row:
                            exp_values += dd
                        for ddd in average_list:
                            theo_values += ddd
                        percentage_difference = (abs((theo_values - exp_values))/theo_values)*100
                        percentage_difference = round(percentage_difference, 2)
                print(f'The material was identified as {material_name} with a {percentage_difference} % deviation.')
    elif command == '3':  # Complete name fetch from CSV file
        print('Fetching data...')
        with open('Data_Bank.csv', 'r') as read_file:
            reader = csv.reader(read_file)
            for row in reader:
                print(row[0])
    elif command == '4':
        print('''
Luca Scavone created this Python program as part of his 
Secondary 5 Personal Project. The program scans materials 
using a NIR (near infrared) scanner and compares the 
results to a data bank in order to identify various types
of materials (plastic, wood, paper, etc.) 
            ''')
    elif command == '0':
        break
    elif command == '':
        continue
    else:
        print('Wrong Command. Try Again.')
        continue
