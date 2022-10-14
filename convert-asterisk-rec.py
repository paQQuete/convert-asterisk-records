import os
from ftplib import FTP
import pysftp
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


def main():
    os.chdir(RECORDS_DIR)
    files_list = os.listdir(path='.')
    with pysftp.Connection(host=BACKUP_SERVER, username=LOGIN, password=PASSWORD) as sftp:
        sftp.cwd(REMOTE_DIR)
        for eachfile in files_list:
            sftp.put(eachfile, eachfile)
            os.remove(eachfile)


if __name__ == '__main__':

    RECORDS_DIR = os.getenv('RECORDS_DIR')
    REMOTE_DIR = os.getenv('REMOTE_DIR')
    BACKUP_SERVER = os.getenv('BACKUP_SERVER')
    LOGIN = os.getenv('BS_LOGIN')
    PASSWORD = os.getenv('BS_PASS')

    main()