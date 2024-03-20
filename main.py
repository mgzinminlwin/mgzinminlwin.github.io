import requests

# Define the API URLs
api_urls = {
    "Channel1": "https://goaltv.cloudns.org/livestream/04.json",
    "Channel2": "https://goaltv.cloudns.org/livestream/05.json"
}

# Initialize the playlist
playlist = "#EXTM3U\n"

# Iterate over each API URL
for channel_name, api_url in api_urls.items():
    try:
        # Fetch data from the API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes
        data = response.json()
        
        # Get the .m3u8 URL for the respective channel
        m3u8_url = data.get("data", {}).get("hd_1")
        
        # Add the entry to the playlist
        if m3u8_url:
            playlist += f"#EXTINF:-1,{channel_name}\n{m3u8_url}\n"
        else:
            print(f"No .m3u8 URL found for {channel_name}")
    except Exception as e:
        print(f"Error fetching data from {api_url}: {e}")

# Print the playlist with #EXTM3U
print(playlist)

# Write the playlist to a file
with open("playlist.m3u", "w") as file:
    file.write(playlist)

print("Playlist created successfully!")
