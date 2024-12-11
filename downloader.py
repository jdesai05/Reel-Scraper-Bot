import instaloader
import os
import shutil
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def download_reel_from_url(url):
    # Create Instaloader instance
    x = instaloader.Instaloader()
    # Ensure it downloads only video files
    x.download_video_thumbnails = False
    x.save_metadata = False
    x.download_geotags = False
    x.download_comments = False

    try:
        # Extract the shortcode from the URL
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(x.context, shortcode)

        if post.is_video:
            # Temporary folder to isolate downloaded files
            temp_dir = "temp_reel_download"
            os.makedirs(temp_dir, exist_ok=True)
            
            # Download the reel to the temp folder
            x.dirname_pattern = temp_dir
            x.download_post(post, target="temp")

            # Find the video file in the temp directory
            for file_name in os.listdir(temp_dir):
                if file_name.endswith(".mp4"):
                    # Save as video.mp4 in the current directory
                    video_path = os.getenv("VIDEO_FILE_PATH", "video.mp4")
                    shutil.move(os.path.join(temp_dir, file_name), video_path)
                    print(f"Reel downloaded successfully as '{video_path}'!")
                    break
            else:
                print("The video file could not be found.")

            # Clean up temporary files
            shutil.rmtree(temp_dir)
        else:
            print("The URL provided does not point to a video.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the Instagram reel: ")
    download_reel_from_url(url)
