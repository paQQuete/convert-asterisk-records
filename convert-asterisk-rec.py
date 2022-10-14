import os
from ftplib import FTP
import pysftp
from dotenv import load_dotenv

load_dotenv()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

RECORDS_DIR = os.getenv('RECORDS_DIR')
REMOTE_DIR = os.getenv('REMOTE_DIR')
BACKUP_SERVER = os.getenv('BACKUP_SERVER')
LOGIN = os.getenv('BS_LOGIN')
PASSWORD = os.getenv('BS_PASS')

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

def convert(files_list: list):
    for eachfile in files_list:
        mp3file = str(eachfile.split('.')[0]) + str('.mp3')
        # convert .wav file to .mp3
        os.system(f'ffmpeg -i {eachfile} {mp3file} -hide_banner')

def main(records_dir: str, remote_dir: str):
    os.chdir(records_dir)
    files = os.listdir(path='.')

if __name__ == '__main__':
    main(RECORDS_DIR, REMOTE_DIR)
    ftp = MyFTP(remotefolder, '10.11.178.88', 'ftpuser', 'Secret!')
    ftp.login()

    for eachfile in files:
        mp3file = str(eachfile.split('.')[0]) + str('.mp3')
        # convert .wav file to .mp3
        os.system(f'ffmpeg -i {eachfile} {mp3file} -hide_banner')
        ftp.upload(mp3file)
        os.remove(mp3file)

