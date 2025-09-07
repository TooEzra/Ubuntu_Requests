import os
import requests
from urllib.parse import urlparse

def download_image(url):
    # Create FetchImages directory if it doesn't exist
    if not os.path.exists("FetchedImages"):
        os.makedirs("FetchedImages")

    try:
        # Fetch image content
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad status codes

        # Check important HTTP headers
        content_type = response.headers.get('Content-Type', '')
        if not content_type.startswith('image'):
            print("URL does not point to an image. Skipping...")
            return

        # Generate filename from URL and ensure uniqueness
        filename = urlparse(url).path.split('/')[-1]
        if not filename:
            filename = "image_" + url.split('/')[-1][:10] + ".jpg"
        filepath = os.path.join("FetchedImages", filename)

        # Prevent duplicate downloads
        if os.path.exists(filepath):
            print("Image already exists. Skipping download...")
            return

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(response.content)
        print(f"Image successfully downloaded to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except Exception as e:
        print(f"Unexpected error with {url}: {e}")

def main():
    print("Enter the URL of an image (or multiple URLs separated by spaces):")
    urls = input().strip().split()

    for url in urls:
        download_image(url)

if __name__ == "__main__":
    main()