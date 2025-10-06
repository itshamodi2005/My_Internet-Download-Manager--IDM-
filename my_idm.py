import os
import yt_dlp
from colorama import Fore, Style, init
from tqdm import tqdm

# Ensure yt-dlp uses local ffmpeg
yt_dlp.utils.DEFAULT_OUTTMPL = '%(title)s.%(ext)s'
yt_dlp.utils.postprocessor_opts = {
    'ffmpeg_location': os.path.join(os.path.dirname(__file__), "ffmpeg_bin")
}

init(autoreset=True)
APP_NAME = "Hamodi Internet Download Manager"
VERSION = "v1.0.0"

def banner():
    print(Fore.CYAN + r"""

.---.  .---.    ____    ,---.    ,---.    ,-----.     ______     .-./`)  ______     ,---.    ,---. 
|   |  |_ _|  .'  __ `. |    \  /    |  .'  .-,  '.  |    _ `''. \ .-.')|    _ `''. |    \  /    | 
|   |  ( ' ) /   '  \  \|  ,  \/  ,  | / ,-.|  \ _ \ | _ | ) _  \/ `-' \| _ | ) _  \|  ,  \/  ,  | 
|   '-(_{;}_)|___|  /  ||  |\_   /|  |;  \  '_ /  | :|( ''_'  ) | `-'`"`|( ''_'  ) ||  |\_   /|  | 
|      (_,_)    _.-`   ||  _( )_/ |  ||  _`,/ \ _/  || . (_) `. | .---. | . (_) `. ||  _( )_/ |  | 
| _ _--.   | .'   _    || (_ o _) |  |: (  '\_/ \   ;|(_    ._) ' |   | |(_    ._) '| (_ o _) |  | 
|( ' ) |   | |  _( )_  ||  (_,_)  |  | \ `"/  \  ) / |  (_.\.' /  |   | |  (_.\.' / |  (_,_)  |  | 
(_{;}_)|   | \ (_ o _) /|  |      |  |  '. \_/``".'  |       .'   |   | |       .'  |  |      |  | 
'(_,_) '---'  '.(_,_).' '--'      '--'    '-----'    '-----'`     '---' '-----'`    '--'      '--' 
                                                                                                   

HamodIDM v1.0.0 - portable build
""")


def download_hook(d):
    """
    This hook runs every time yt-dlp updates download info.
    We use it to show percentage progress in the terminal.
    """
    if d['status'] == 'downloading':
        total = d.get('total_bytes', 0)             # Total file size in bytes
        downloaded = d.get('downloaded_bytes', 0)   # How much is downloaded so far
        if total > 0:
            percent = downloaded / total * 100      # Calculate percent complete
            print(Fore.GREEN + f"\rDownloading: {percent:.2f}%", end="")
    elif d['status'] == 'finished':
        print(Fore.MAGENTA + "\nMerging audio & video...")

def download_video(url, save_path="downloads"):
    # Create the folder if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Download settings
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',   # file name based on video title
        'format': 'bestvideo+bestaudio/best',          # best quality
        'merge_output_format': 'mp4',                  # save as MP4
        'progress_hooks': [download_hook]              # Show Download hook
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    banner()

    save_path = input(Fore.CYAN + "Enter download folder (default: downloads): ").strip()
    if save_path == "":
        save_path = "downloads"

    video_url = input(Fore.CYAN + "Paste the video URL here: ").strip()
    print(Fore.YELLOW + f"\nStarting download... File will be saved in: {save_path}\n")

    download_video(video_url, save_path)
    print(Fore.GREEN + "\Download complete!")