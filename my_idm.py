import os
import yt_dlp

def download_video(url, save_path="downloads"):
    # Create the folder if it does not exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Download settings
    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # file name based on video title
        'format': 'bestvideo+bestaudio/best',         # best quality
        'merge_output_format': 'mp4'                  # save as MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("Paste the video URL here: ")
    download_video(video_url)
    print("Download complete!")