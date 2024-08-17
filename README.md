# Blue-Eye
Network Traffic Visualization using Python

# Overview
This project provides a Python script that processes network traffic data from a .pcap file and visualizes it on Google Maps using KML (Keyhole Markup Language). The script extracts IP addresses from the network packets, geolocates the IP addresses, and generates a KML file to display source and destination points along with connecting lines. The source points are marked in blue, and the destination points are marked in red, making it easy to visualize the flow of traffic between locations.

# Features
1. IP Geolocation: Fetches precise geolocation data for IP addresses using the ipinfo.io API.
2. KML Generation: Generates KML files that can be imported into Google Maps or Google Earth for visualizing network traffic.
3. Custom Styling: Source markers are styled in blue, and destination markers in red, with connecting lines between them.
4. Error Handling: Includes basic error handling to skip invalid packets and handle potential issues with API requests.

# Requirements
Python 3.7 or above
The following Python libraries:
  dpkt
  requests
  socket

# Installation
1. Clone the repository:

git clone https://github.com/death10101/Blue-Eye

cd Blue-Eye

2. Install the required libraries:
Use pip to install the necessary dependencies:

pip install dpkt requests

3. Set up an API Key (Optional):
If you want to avoid hitting rate limits on the ipinfo.io API, you can sign up for a free API key and modify the script to include the API key:

# Usage
1. Place the .pcap file in the project directory:
Make sure the .pcap file containing the network traffic data is located in the same directory as the script.
The default filename used in the script is wire.pcap.

2. Run the script:
Execute the Python script to process the .pcap file and generate the KML output:

python main.py

3. View the output:
The script will output the generated KML data directly to the console.
To save it to a file:

python main.py > output.kml

You can then import output.kml into Google Maps or Google Earth to visualize the network traffic.

# Customization
1. Source IP Address:
The script uses a fixed source IP address **(xxx.xxx.xxx.xxx)**. 
You can modify the source_ip variable in the script to change this.

2. Marker and Line Styling:
The KML styles for markers and lines can be customized in the **main()** function.
The current setup uses **blue for source markers**, **red for destination markers**, **and a semi-transparent blue line**.

# Example Output

This image shows the source and destination markers with connecting lines on Google Maps, illustrating the flow of network traffic.

<img width="636" alt="Screenshot 2024-08-17 160327" src="https://github.com/user-attachments/assets/32fe686e-5271-4765-80eb-45044f123233">

