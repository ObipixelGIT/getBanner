# -*- coding: utf-8 -*-
# Author : Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 08 November 2022


import subprocess
from prettytable import PrettyTable

# Ask the user for the website URL
url = input("Enter the website URL: ")

try:
    # Perform a banner grab using curl
    output = subprocess.check_output(['curl', '-I', url]).decode('utf-8')
    
    # Split the output into lines
    lines = output.strip().split('\n')

    # Create a table to display the banner information
    table = PrettyTable(['Header', 'Value'])

    # Add each header and its value to the table
    for line in lines:
        if line.startswith('HTTP/'):
            # The first line contains the HTTP status code and message
            table.add_row(['Status', line.split(' ', 2)[2]])
        elif ':' in line:
            # Other lines contain headers and their values
            header, value = line.split(':', 1)
            table.add_row([header.strip(), value.strip()])

    # Display the table
    print(table)

except subprocess.CalledProcessError as e:
    print(f"Error: {e}. Please check your URL and try again.")
    
except Exception as e:
    print(f"Error: {e}. Please try again later.")
