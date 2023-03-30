# getBanner
Performs a banner grab for a given website.

## How this script works?
A banner grab is a technique used to gather information about a website's operating system, web server, and other details by inspecting the HTTP headers returned in response to a request. This is a Python 3 script that performs a banner grab for a given website.

## Requirements

Install your libraries:
```bash
pip3 install subprocess, prettytable
```
## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x getBanner.py
```
## Usage
```bash
sudo python3 getBanner.py
```

## Example script
```python
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

```

## Example output
```
Enter the website URL: https://www.microsoft.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0  1020    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
+----------------+-----------------------------------------------+
|     Header     |                     Value                     |
+----------------+-----------------------------------------------+
                        |
| accept-ranges  |                     bytes                     |
|  content-type  |                   text/html                   |
|      etag      | "6082151bd56ea922e1357f5896a90d0a:1425454794" |
| last-modified  |         Wed, 04 Mar 2015 07:39:54 GMT         |
|     server     |                AkamaiNetStorage               |
| content-length |                      1020                     |
|    expires     |         Thu, 30 Mar 2023 20:06:42 GMT         |
| cache-control  |         max-age=0, no-cache, no-store         |
|     pragma     |                    no-cache                   |
|      date      |         Thu, 30 Mar 2023 20:06:42 GMT         |
+----------------+-----------------------------------------------+
```

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.


