import os
import pandas as pd
from urllib.request import urlretrieve
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed


def maybe_download_image(save_dir, image_url, label):
    """
    Download image to savel_dir/label/. The function
    will first check if the image already exists.
    Returns 0 if found, 1 if downloaded

    Args:
        save_dir: Path where images are saved
        image_url: An image url
        image: A label
    """

    # create the output path if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)

    # create label subfolder if it doesn't exist
    label_dir = os.path.join(save_dir, label)
    os.makedirs(label_dir, exist_ok=True)

    # split the file name from the url
    url, fname = os.path.split(image_url)

    # return 0 if file already there, 1 if downloaded
    save_path = os.path.join(save_dir, label, fname)
    if os.path.isfile(save_path):
        return 0
    else:
        urlretrieve(image_url, save_path)
        return 1

def get_images(save_dir, image_urls,
               image_labels, max_workers=20):
    """
    Download list of labeled images using threads.

    Args:
        save_dir: Path where images are saved
        image_urls: A list of image urls
        image_labels: A list of image labels
        max_workers: Concurrent threads (default=20)
    """
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # we build a dictionary with executors
        # as keys and the urls as values

        future_to_url = {}
        for url, label in zip(image_urls, image_labels):
            k = executor.submit(maybe_download_image,
                                save_dir, url, label)
            future_to_url[k] = url

        # we loop over executors as they complete
        # and print their return values
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                print(result, end='')
            except Exception as ex:
                print('\n%r exception: %s' % (url, ex))


train_df = pd.read_csv('./sports_train.csv')
train_path = './train/'

get_images(train_path,
           train_df['image_url'].values,
           train_df['class'].values)

test_df = pd.read_csv('./sports_test.csv')
test_path = './test/'

get_images(test_path,
           test_df['image_url'].values,
           test_df['class'].values)
