import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def upload_video():
    # Path to your video file
    video_file_path = os.getenv("VIDEO_FILE_PATH")
    upload_url_endpoint = os.getenv("UPLOAD_URL")
    flic_token = os.getenv("FLIC_TOKEN")

    # Step 1: Get the Upload URL
    headers = {
        "Flic-Token": flic_token,
        "Content-Type": "application/json"
    }

    server_side_hash = None  # Initialize the server_side_hash variable

    try:
        # Request the upload URL
        response = requests.get(upload_url_endpoint, headers=headers)
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.text}")

        if response.status_code == 200:
            data = response.json()

            if 'url' in data:
                upload_url = data['url']
                server_side_hash = data.get('hash', None)  # Extract the hash from the response
                print(f"Upload URL obtained: {upload_url}")

                if server_side_hash:
                    print(f"Server-side hash: {server_side_hash}")
                else:
                    print("Server-side hash not found in the response.")

                # Step 2: Upload the Video
                if os.path.exists(video_file_path):
                    with open(video_file_path, 'rb') as video_file:
                        upload_response = requests.put(upload_url, data=video_file)
                    # Ensure the file handle is properly closed before attempting to delete
                    print(f"File upload response status: {upload_response.status_code}")
                    
                    if upload_response.status_code == 200:
                        print("Video uploaded successfully!")

                        # Step 3: Delete the Local File
                        try:
                            os.remove(video_file_path)
                            print(f"Local file '{video_file_path}' deleted successfully.")
                        except Exception as delete_error:
                            print(f"Error deleting file: {delete_error}")
                    else:
                        print(f"Failed to upload video: {upload_response.status_code}")
                        print(f"Upload Response: {upload_response.text}")
                else:
                    print(f"File '{video_file_path}' does not exist.")
            else:
                print("Error: 'url' key not found in the response.")
                print(f"Response Content: {data}")
        else:
            print(f"Failed to get upload URL: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Return the server-side hash (even if it's None in case of error)
    return server_side_hash

if __name__ == "__main__":
    video_hash = upload_video()
    if video_hash:
        print(f"Generated server-side hash for the video")
    else:
        print("Failed to retrieve server-side hash.")
