import pandas as pd
import urllib.request
import time

def url_to_jpg(i, name,url,file_path ):

    time.sleep(3)
    filename = name
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)

    print('{} saved.'.format(filename))
    return None


FILENAME = 'Image_Download_02.csv'
FILE_PATH = 'images_02/'

df = pd.read_csv(FILENAME)
name = df.name


for i, URL, in enumerate(df.values):
    url_to_jpg(i, name[i] ,URL[0],FILE_PATH)