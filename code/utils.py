import urllib.request

def download_data(data):
    for filename, url in data:
        urllib.request.urlretrieve(url, './data/{}.txt'.format(filename))
        print("Downloaded '{}' to 'data/' folder.".format(filename))
