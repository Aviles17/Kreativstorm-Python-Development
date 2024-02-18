''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''
from config.credentials import FTP_SERVER, FTP_USER, FTP_PASSWORD, FTP_PORT
import logging as log
from scripts.utility_functions import connect_to_ftp_server, list_parent_directories, create_local_dir, manage_files_directory

if __name__ == '__main__':
    #Configure the log file
    log.basicConfig(filename='file_transfer.log', level=log.INFO, format= '%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode='w')
    # Connect to the FTP server and create the local directory
    connector = connect_to_ftp_server(FTP_SERVER, FTP_USER, FTP_PASSWORD, FTP_PORT)
    create_local_dir('data\\LOCAL_REPO')
    # List the parent directory and copy the corresponding files and directories
    list_parent_directories(connector, '/')
    try:
        comp = manage_files_directory(connector, 'data\\LOCAL_REPO', ['HEADER.html', 'robots.txt', 'about'])
    except IOError as e:
        log.error(f'Error managing files and directories: {e}')
    except Exception as e:
        log.error(f'An unexpected error has ocurred: {e}')
    