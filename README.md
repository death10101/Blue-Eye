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
Clone the repository:
'''bash
git clone https://github.com/death10101/Blue-Eye
cd Blue-Eye

