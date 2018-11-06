import os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_mincraft_versions(dirs = None):
    page = requests.get("https://mcversions.net/")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = soup.findAll("li")
    version = {}
    for i in data:
        try:
            ver = i.find(attrs={'class': "version"}).text
            time = i.find(attrs={'class': "time"}).text
            server_link = i.find(attrs={'class': "server"})['href']
            # print(server_link)
            version[ver] = dict(
                version = ver,
                released = time,
                link = server_link
            )
        except:
            break
    # for i in version:
        # print(i)
    return version


def download_new_version(ver):
    # print("Getting Version: ", ver['version'])
    path = os.path.join(os.getcwd(), 'game_versions')
    filename = os.path.join(path, f"{ver['version']}_server.jar")
    for file in os.listdir(path):
        if ver['version'] in file:
            print(f"already have version: {ver['version']}")
            return filename
    download = requests.get(ver['link'], stream=True)
    with open(filename, 'wb') as handle:
        for data in tqdm(download.iter_content()):
            handle.write(data)
    return filename


# versions = get_mincraft_versions()
# current_version = list(versions)[0]
# ver = versions[current_version]
# current_version_filepath = download_new_version(ver)
