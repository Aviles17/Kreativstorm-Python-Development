from config.credentials import FTP_SERVER, FTP_USER, FTP_PASSWORD, FTP_PORT
from config.file_repo_config import LOCAL, INTERNAL_NETWORK
import logging as log
from scripts.utility_functions import connect_to_ftp_server, list_directory, create_local_dir, manage_files_directory, move_files, read_files_to_transfer
import schedule
import time

def file_transfer(pth_files_transfer: str):
    # Connect to the FTP server and create the local directory
    connector = connect_to_ftp_server(FTP_SERVER, FTP_USER, FTP_PASSWORD, FTP_PORT)
    create_local_dir(LOCAL)
    # List the parent directory and copy the corresponding files and directories
    list_directory(connector, '/')
    files_to_transfer = read_files_to_transfer(pth_files_transfer)
    if files_to_transfer != [] and files_to_transfer is not None:
        try:
            manage_files_directory(connector, LOCAL, files_to_transfer)
            move_files(LOCAL, INTERNAL_NETWORK)
        except IOError as e:
            log.error(f'Error managing files and directories: {e}')
        except Exception as e:
            log.error(f'An unexpected error has ocurred: {e}')
    

if __name__ == '__main__':
    #Configure the log file
    log.basicConfig(filename='file_transfer.log', level=log.INFO, format= '%(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filemode='w')
    #Schedule the job to run every day at a specific time (8 AM)
    schedule.every().day.at("8:00").do(file_transfer, "config\\files_to_transfer.json")
    while True:
        schedule.run_pending()
        time.sleep(1)
    