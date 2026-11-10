import json
import urllib.request

json_url = "https://github.com/codito/akashvani/raw/refs/heads/master/stations.json"

# Fetch JSON data
req = urllib.request.urlopen(json_url)
stations = json.loads(req.read().decode("utf-8"))

# Build M3U content
m3u_lines = ["#EXTM3U"]

for station in stations:
  name = station.get("name", "Unknown Station")
  stream_url = station.get("stream_url", "")
  state = station.get("state", "Radio")
  epg_id = station.get("epg_id", "")

  # Construct extended metadata attributes
  extinf_parts = [f'#EXTINF:-1 tvg-name="{name}"']
  
  if epg_id:
    extinf_parts.append(f'tvg-id="{epg_id}"')
    
  extinf_parts.append(f'tvg-logo="https://raw.githubusercontent.com/bsmjsambalpuri/Radio-Playlist/refs/heads/main/fm.png"')
  extinf_parts.append(f'group-title="{state}"')

  extinf = f"{' '.join(extinf_parts)},{name}"

  m3u_lines.append(extinf)
  m3u_lines.append(stream_url)

# Save to file
with open("playlist.m3u", "w", encoding="utf-8") as f:
  f.write("\n".join(m3u_lines))

print(f"Successfully generated playlist with {len(stations)} stations.")