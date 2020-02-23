import re
import configparser
import requests
import logging

logging.basicConfig(level=logging.INFO)

class Helper:

    @staticmethod
    def get_indices(output : str) -> int:
        result = re.search('\"transcodings\":\[{\"url\":', output)
        start_index = result.end()
        result = re.search(',"preset":', output)
        end_index = result.start()
        return start_index,end_index

    @staticmethod
    def get_title(url : str) -> str:
        names = url.split("/")
        return names[-1]

    @staticmethod
    def validate_url(url : str):
        result = re.match('(https://soundcloud.com)(/+)(.+)(/+)(.+)',url)
        if result is None:
            logging.error("Please provide a valid url ,eg: https://soundcloud.com/drake300k/war-1")
            exit(1)
        return url

    @staticmethod
    def get_client_list():
        client_list = []
        with open('./sdl/clientid','r') as file:
            for line in file:
                client_list.append(line)
        return client_list

    @staticmethod
    def get_valid_client_id(client_list,url):
        for client in client_list:
            response = requests.get(url+"?client_id="+client[0:len(client)-1])
            if response.status_code == 200:
                return url+"?client_id="+client[0:len(client)-1]
        return None



