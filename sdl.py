from sdl import SoundCloudDl


def download(url, download_path, client_id):
    s = SoundCloudDl(url, download_path, client_id)
    s.get_source_url()
    s.get_playlist_url()
    s.get_playlist()
    s.get_files()


if __name__ == "__main__":
    url = input("Enter the URL : ")
    download_path = input("Enter the download path (optional) : ")
    client_id = input("Enter the client id (optional) : ")
    download(url.strip(), download_path.strip(), client_id.strip())

