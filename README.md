# Automate_File_Transfer
Automate the process of transferring the files from an external FTP server to an internal network

## Given Prompt

You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

## Objectives

    - Use the ftplib library to connect to the external FTP server and list the files in the directory.

    - Use the os library to check for the existence of a local directory where the files will be stored.

    - Use a for loop to iterate through the files on the FTP server and download them to the local directory   using the ftplib.retrbinary() method.

    - Use the shutil library to move the files from the local directory to the internal network.

    - Use the schedule library to schedule the script to run daily at a specific time.

    - Use log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process.

## Quick start

1. Install project dependencies using the **setup.py** file provided
``` pip install -e . ```
2. Install project library dependencies using **requirements.txt**
``` pip install -r requirements.txt ```
3. Modify configuration files as your context needs, this files are found in **config/** directory
4. Modigy hour in which the main script **file_trasnfer.py** would execute daily, the default hour is 8:00AM of your local time

## Author

