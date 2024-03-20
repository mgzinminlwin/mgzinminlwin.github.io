playlist_entries = [
    {
        "tvg-logo": "http://localhost:8080/maharbhawdi.png",
        "group-title": "MM",
        "title": "Mahar Bhawdi",
        "url": "https://ppradio.b-cdn.net/LiveApp/streams/rHEBIW7pjQLU1677679374164.m3u8"
    },
    {
        "tvg-logo": "http://localhost:8080/mrtv4.png",
        "group-title": "MM",
        "title": "MRTV-4",
        "url": "https://ppradio.b-cdn.net/LiveApp/streams/w3g3EYjBtqgJ1677679288037.m3u8"
    }
]

playlist = "#EXTM3U\n"

for entry in playlist_entries:
    playlist += f"#EXTINF:-1 tvg-logo=\"{entry['tvg-logo']}\" group-title=\"{entry['group-title']}\", {entry['title']}\n{entry['url']}\n"

# Write the playlist to a file
with open("playlist.m3u", "w") as file:
    file.write(playlist)

# Print the contents of the playlist file
print("Playlist created successfully!\n")
print(playlist)
