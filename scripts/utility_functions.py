import os
import re
import logging as log
from ftplib import FTP, error_perm

def connect_to_ftp_server(server: str, user: str, password: str, port: int) -> FTP:
    ftp_conection = FTP(server)
    if user != '' and password != '' and port != -1:
        ftp_conection.login(user='username', passwd='password') # If the server requires a username and password
    else:
        if ftp_conection.login():
            log.info(f'Connected to {server}')
            return ftp_conection # Return the connection object for future use
        else:
            log.error(f'Failed to connect to {server}')
            raise ConnectionError(f'Failed to connect to {server}') 
    
    
def list_parent_directories(ftp_conection: FTP, remote_dir: str):
    try:
        ftp_conection.cwd(remote_dir)
        files = ftp_conection.retrlines('LIST')
        log.info(f'Directories in the parent directory: {files}')
    except error_perm as e:
        log.error(f'Failed change root directory to {remote_dir}. Error: {e}')
    finally:
        ftp_conection.cwd('/')


def download_files(ftp_conection: FTP, local_dir: str, file_path: str) -> bool:
    try:
        create_local_dir(local_dir)
        if local_dir_exists(local_dir):
            local_filepath = os.path.join(local_dir, os.path.basename(file_path))
            with open(local_filepath, 'wb') as file:
                ftp_conection.retrbinary('RETR ' + file_path, file.write)
                log.info(f'File {file_path} downloaded successfully')
        else:
            raise FileExistsError(f'The directory {local_dir} does not exist')
            
        return True
        
    except FileExistsError as e:
        log.error(f'Failed to access of create {local_dir}. Error: {e}')
        return False
    except error_perm as e:
        log.error(f'Failed to read FTP file {file_path}. Error: {e}')
        return False
    except Exception as e:
        log.error(f'An unexpected errror has ocurred. Error: {e}')
        return False

def download_directories(ftp_conection: FTP, local_dir: str, remote_dir: str) -> bool:
    try:
        create_local_dir(local_dir)
        log.info(f"Create directory: {remote_dir}")
        ftp_conection.cwd(remote_dir)
        file_name = None
        files = []
        ftp_conection.dir(files.append)
        if local_dir_exists(local_dir):
            # Process each file
            for line in files:
                if line.startswith('d'): # It's a directory
                    dir_name = line.split()[-1]
                    download_directories(ftp_conection, os.path.join(local_dir, dir_name), dir_name)
                else:  # It's a file
                    file_name = line.split()[-1]
                    # Download the file
                    file_name = check_files_structure(file_name)
                    with open(os.path.join(local_dir, file_name), 'wb') as f:
                        ftp_conection.retrbinary('RETR ' + file_name, f.write)
                        log.info(f'File {file_name} downloaded successfully')
            ftp_conection.cwd('..')
            return True
        else:
            raise FileExistsError(f'The directory {local_dir} does not exist')
        
    except FileExistsError as e:
        log.error(f'Failed to access of create directory {local_dir}. Error: {e}')
        return False
    except error_perm as e:
        log.error(f'Failed to change to directory {remote_dir}. Error: {e}')
        return False
    except Exception as e:
        log.error(f'An unexpected errror has ocurred. Error: {e}')
        return False

def create_local_dir(local_dir: str) -> bool:
    if not local_dir_exists(local_dir):
        os.mkdir(local_dir)
        log.info(f'Directory {local_dir} created successfully')
        return True
    else:
        log.error(f'Directory {local_dir} already exists')
        return False


def local_dir_exists(local_dir: str) -> bool:
    return os.path.isdir(local_dir)

def check_files_structure(filename:str) -> str:
    if '.' not in filename:
        filename = filename + '.txt'
        return filename
    elif re.search(r'\.\w+$', filename) is None:
        filename = filename + '.txt'
        filename = filename.replace('/', '_')
        filename = filename.replace('..', '')
        return filename
    else:
        return filename

def manage_files_directory(ftp_conection: FTP, local_dir:str, transfer:list) -> bool:
    for file in transfer:
        if file.endswith('/') or '.' not in file:
            ret_code = download_directories(ftp_conection, f"{local_dir}\\{file}", file)
            if not ret_code:
                raise IOError(f'Failed to download directory {file}')
        else:
            ret_code = download_files(ftp_conection, local_dir, file)
            if not ret_code:
                raise IOError(f'Failed to download file {file}')
    return True
    