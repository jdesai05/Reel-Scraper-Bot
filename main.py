import streamlit as st
from utils.downloader import download_reel_from_url
from utils.uploader import upload_video
from utils.monitor import create_post

def main():
    st.title("Reel Processing App")
    st.write("Download a reel, upload it, and monitor its status.")

    # Initialize session state variables
    if "video_hash" not in st.session_state:
        st.session_state.video_hash = None
    if "downloaded" not in st.session_state:
        st.session_state.downloaded = False

    # Step 1: User input for reel URL
    reel_url = st.text_input("Enter the URL of the reel:", "")

    # Step 2: Download reel
    if st.button("Start Download"):
        if not reel_url:
            st.error("Please provide a reel URL.")
        else:
            try:
                with st.spinner("Downloading reel..."):
                    download_reel_from_url(reel_url)
                st.success("Video downloaded successfully.")
                st.session_state.downloaded = True
            except Exception as e:
                st.error(f"An error occurred during the download: {e}")

    # Step 3: Upload video (if downloaded)
    if st.session_state.downloaded and st.session_state.video_hash is None:
        try:
            st.write("Starting the video upload...")
            with st.spinner("Uploading video..."):
                video_hash = upload_video()
            st.session_state.video_hash = video_hash
            st.success(f"Video uploaded successfully. Hash: {video_hash}")
        except Exception as e:
            st.error(f"An error occurred during the upload: {e}")

    # Step 4: Create Post (if video uploaded)
    if st.session_state.video_hash:
        title = st.text_input("Enter Post Title:", "")
        category_id = st.text_input("Enter Post Category:", "")
        
        if st.button("Create Post"):
            if not title or not category_id:
                st.error("Both title and category are required to create the post.")
            else:
                try:
                    with st.spinner("Creating post..."):
                        create_post(st.session_state.video_hash, title, category_id)
                    st.success("Post creation complete!")
                except Exception as e:
                    st.error(f"An error occurred during post creation: {e}")

if __name__ == "__main__":
    main()
