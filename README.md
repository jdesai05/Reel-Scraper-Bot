# Video Upload and Instagram Reel Downloader

This project involves multiple functionalities, including downloading Instagram reels, uploading videos, and creating posts via an API. It is designed to automate the process of downloading Instagram reels and uploading them to a platform with specific categories. The project is built using Python and makes use of the following libraries and APIs:

- **Instaloader**: A Python package used to download Instagram content such as reels and posts.
- **Requests**: A simple HTTP library used for making API calls to interact with the upload and post creation services.

## Features

- **Download Instagram Reels**: 
  - Download videos from Instagram reels using the URL.
  - The video is saved as `video.mp4` in the current directory.

- **Upload Video**:
  - Upload videos to a specific platform (Socialverse) via an API.
  - It supports retrieving the upload URL and uploading the video in chunks.

- **Create Post**:
  - Create a post on Socialverse with details like title, category, and the video hash.

## Setup

### Prerequisites

Ensure you have the following installed:

- [Python 3.6+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [Instaloader](https://github.com/instaloader/instaloader)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/video-bot.git
   cd video-bot
