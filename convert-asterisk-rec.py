import os
from ftplib import FTP
import pysftp
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class MyFTP(FTP):
    def __init__(self, path, *args, **kwargs):
        super(MyFTP, self).__init__(*args, **kwargs)
        self.__path = path
        self.__navigation()

        def __navigation(self):
            self.cwd(self.__path)

        def upload(self, file):
            with open(file, 'rb') as fobj:
                self.storbinary('STOR' + file, fobj, 1024)



def main():
    os.chdir(RECORDS_DIR)
    files_list = os.listdir(path='.')
    with pysftp.Connection(host=BACKUP_SERVER, username=LOGIN, password=PASSWORD) as sftp:
        sftp.cwd(REMOTE_DIR)

        for eachfile in files_list:
            mp3file = str(eachfile.split('.')[0]) + str('.mp3')
            # convert .wav file to .mp3
            os.system(f'ffmpeg -i {eachfile} -vn -ar 44100 -ac 2 -ab 192k -f mp3 {mp3file}')

            sftp.put(eachfile, mp3file)


if __name__ == '__main__':

    RECORDS_DIR = os.getenv('RECORDS_DIR')
    REMOTE_DIR = os.getenv('REMOTE_DIR')
    BACKUP_SERVER = os.getenv('BACKUP_SERVER')
    LOGIN = os.getenv('BS_LOGIN')
    PASSWORD = os.getenv('BS_PASS')

    main()