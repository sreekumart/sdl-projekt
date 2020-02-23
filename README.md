# sdl-projekt
python based soundcloud music file downloader

# Usage
  1.Copy the SoundCloud URL for a particular music file<br>
  2.Execute the sdl.py<br>
  3.enter the URL as input upon prompt<br>
  4.enter the path to be downloaded to upon prompt(optional)<br>
  5.enter the client id (if the included one is expired,check the clientid file in the sdl module)(optional)
  
 # Output
  Enter the URL : https://soundcloud.com/robin-schulz/robin-schulz-waves-bootleg-1
  enter the download path (optional) : C:/music/
  enter the client id (optional) : 
  INFO:root:Fetching PlayList Source URL
  INFO:root:Fetched PlayList Source URL Successfully
  INFO:root:Fetching PlayList URL 
  INFO:root:Fetched PlayList URL Successfully
  INFO:root:Fetching Playlist Tracks URL
  INFO:root:Fetched Playlist Tracks URL Successfully
  INFO:root:Downloading Playlist Tracks
  INFO:root:Download Completed : C:\music\robin-schulz-waves-bootleg-1.mp3

 
# Requirement
  1.python3<br>
  2.requests module
  
# Improvements
  1.Progress bar during download<br>
  2.Multi threaded download using future<br>
  3.extract artist name<br>
  4.extract cover art<br>
  
# Known Issue
  1.If the clientids in the clientid file is expired then the user will have to get one and provide to the script.
  
 
