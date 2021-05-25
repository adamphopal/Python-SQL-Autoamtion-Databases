from getpass import getpass
import fire
import os
import requests
import shutil

THIS_FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(THIS_FILE_PATH)
DOWNLOADS_DIR = os.path.join(BASE_DIR, "downloads")
os.makedirs(DOWNLOADS_DIR, exist_ok=True)



def download_file(directory, url=None, fname=None):
    if fname == None:
        fname = os.path.basename(url)
    dl_path = os.path.join(directory, fname)
    with requests.get(url, stream=True) as r:
        with open(dl_path, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return new_dl_path



if __name__ == '__main__':
    fire.Fire(download_file(DOWNLOADS_DIR, url, name))
