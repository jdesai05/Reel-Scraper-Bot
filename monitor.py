import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def create_post(hash_value, title, category_id):
    # API Headers
    headers = {
        "Flic-Token": os.getenv("FLIC_TOKEN"),
        "Content-Type": "application/json"
    }

    # Validating user inputs
    if not title or not hash_value or not category_id.isdigit():
        print("Invalid input. Please make sure all fields are correctly filled.")
        return

    # Post details
    post_payload = {
        "title": title,
        "hash": hash_value,
        "is_available_in_public_feed": False,
        "category_id": int(category_id)
    }

    try:
        # Create Post
        response = requests.post(
            os.getenv("POST_URL"),
            headers=headers,
            json=post_payload
        )
        
        print(f"Response Status Code (Create Post): {response.status_code}")
        print(f"Response Content: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "success":
                print("Post created successfully!")
                print(f"Post Message: {data.get('message')}")
                print(f"Post Identifier: {data.get('identifier')}")
                print(f"Post Slug: {data.get('slug')}")
            else:
                print("Post creation failed. Response:", data)
        else:
            print(f"Failed to create post: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"An error occurred while creating the post: {e}")

if __name__ == "__main__":
    create_post()
