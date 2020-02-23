import requests
from sdl import helper
import os
import logging

logging.basicConfig(level=logging.INFO)

class SoundCloudDl:

    def __init__(self, file_url: str, download_path="./", client_id=""):
        self.file_url = helper.Helper.validate_url(file_url)
        self.playlist_url = None
        self.download_path = download_path
        self.source_url = None
        self.playlist = []
        self.client_id = client_id
        self.client_list = helper.Helper.get_client_list()
        self.title = helper.Helper.get_title(file_url)

    def get_source_url(self):
        logging.info("Fetching PlayList Source URL")
        response = requests.get(self.file_url)
        if response.status_code == 200:
            output = response.content.decode("utf-8")
            start_index, end_index = helper.Helper.get_indices(output)
            url = output[start_index+1:end_index-1]
            if self.client_id == "":
                self.client_id = helper.Helper.get_valid_client_id(self.client_list,url)
                if self.client_id is None:
                    logging.error("The default clientId's have been expired please provide a clientId")
                    exit(1)
            self.source_url = self.client_id
            logging.info("Fetched PlayList Source URL Successfully")
        else:
            logging.error("Request Failed with Response Status : %s", str(response.status_code))
            exit(1)

    def get_playlist_url(self):
        logging.info("Fetching PlayList URL ")
        response = requests.get(self.source_url)
        if response.status_code == 200:
            output = response.json()
            self.playlist_url = output['url']
            logging.info("Fetched PlayList URL Successfully")
        else:
            logging.error("Request Failed with Response Status : ", str(response.status_code))
            exit(1)

    def get_playlist(self):
        logging.info("Fetching Playlist Tracks URL")
        response = requests.get(self.playlist_url)
        flag = False
        url = ""
        if response.status_code == 200:
            for i in response.content.decode("utf-8"):
                if i == "h":
                    flag = True
                elif i == '\n':
                    flag = False
                    if len(url) > 0:
                        self.playlist.append(url)
                        url = ""

                if flag:
                    url += i
            logging.info("Fetched Playlist Tracks URL Successfully")
        else:
            logging.error("Request Failed with Response Status : %s", str(response.status_code))
            exit(1)

    def get_files(self):
        try:
            logging.info("Downloading Playlist Tracks")
            with open(self.download_path+self.title+".mp3", "ab") as output:
                for url in self.playlist:
                    response = requests.get(url)
                    output.write(response.content)
            logging.info("Download Completed : %s", str(os.path.abspath(self.download_path+self.title+".mp3")))
        except Exception as e:
            logging.error("Unexpected Error : %s", str(e))
            exit(1)



