# beaconBonanza  

# Introduction:

In the vast landscape of cybersecurity, where threats are constantly evolving, a new player has emerged on the scene – BeaconBonanza. This insidious yet intriguing attack leverages the WiFi frames, specifically beacon frames, to orchestrate a symphony of potential risks for unsuspecting victims. The monitoring of Wi-Fi networks, particularly the capture of beacon frames, introduces various risks when conducted by insider threats. This repository aims to increase awareness of these risks and provide educational content for testing purposes.

# Unraveling the BeaconBonanza Attack:

BeaconBonanza revolves around the capture of WiFi beacon frames, those seemingly harmless signals that WiFi devices emit to announce their presence. Imagine this attack as a choreographed dance of information, where insider threats exploit the very essence of WiFi communication to unveil sensitive details about networks.

# The sturdy-palm-tree of Beacon Frames:

Beacon frames play a crucial role in WiFi networks, providing essential information such as network names (SSID), supported data rates, and security settings. However, in the hands of malicious insiders, these innocent frames transform into powerful tools for reconnaissance.

# Identifying the Risks:

BeaconBonanza poses several risks, each note in its symphony playing a unique tune of potential harm:

1. **Network Discovery:**
   - Insiders may leverage the capture of beacon frames to identify active Wi-Fi networks, potentially revealing sensitive network information.

2. **Unauthorized Access Points:**
   - Beacon frames serve as announcements from legitimate Wi-Fi access points, providing essential information about the network, such as SSID, supported data rates, security settings, and more. While an insider threat could capture these frames, gaining knowledge about existing networks, it doesn't grant direct capability to create unauthorized access points. Setting up unauthorized access points typically involves configuring a physical Wi-Fi access point and broadcasting its own beacon frames. Capturing beacon frames alone, even with the subtype for beacon packets, doesn't enable the creation of unauthorized access points.

To set up an unauthorized access point, an attacker would typically need to:

Physically deploy a Wi-Fi access point.  Configure the access point with specific settings (SSID, security parameters, etc.).  Broadcast beacon frames from the unauthorized access point.
### Here's an overview:

#### Capture Probe Requests:  *see hexadecimal value in a-sturdy-tree.md

The attacker captures probe requests from Wi-Fi devices probing for the "**target**" SSID. These devices might be looking for available networks to connect to.  **just replace the hexadecimal in sturdy-palm.tree.txt with probe requests.**
#### Analyze SSID and Information:

The attacker examines the SSID, signal strength, and other relevant information in the captured probe requests. This information helps the attacker understand the networks that nearby devices are trying to connect to.
Manipulate Beacon Response:

Leveraging beaconBonanza.py, the attacker crafts a deceptive beacon frame response. This response includes details mimicking the legitimate "**TARGET**" access point, such as the SSID and other network information.
#### Broadcast Unauthorized Beacon: **see beaconBoogie.py**

The attacker broadcasts the manipulated beacon frame, making it appear as if there is a new instance of the "**TARGET**" Wi-Fi network. Devices that sent the probe requests may automatically connect to this unauthorized access point, thinking it is the legitimate network.
#### Potential Unauthorized Access:

Devices that connect to the manipulated beacon may unknowingly expose themselves to various security risks. The attacker can intercept or manipulate the traffic passing through the unauthorized access point, potentially leading to unauthorized access or data interception.

3. **Network Parameters Exposure:**
   - Beacon frames contain information about the network configuration. Insiders capturing these frames may expose details such as SSID, supported data rates, and security settings.

4. **Location Tracking:**
   - Beacon frames may contain information that can be exploited for location tracking, revealing the movement patterns of Wi-Fi devices.
   - Here's how beacon frames contribute to location tracking:

Signal Strength (RSSI): Beacon frames include information about the signal strength of the Wi-Fi network. By analyzing the Received Signal Strength Indication (RSSI) in beacon frames, an attacker can estimate the distance between the device capturing the frames and the Wi-Fi access point. This information can be used to triangulate the approximate location of the device.

MAC Address Tracking: Beacon frames include the MAC address of the Wi-Fi access point. In scenarios where Wi-Fi access points are fixed and known, tracking the MAC addresses in beacon frames over time can provide insights into the movement patterns of Wi-Fi devices. For example, if a device consistently associates with different access points in a specific sequence, it may indicate a predictable movement pattern.

Probe Requests and Responses: While not strictly beacon frames, probe requests and responses also play a role in location tracking. Devices often send probe requests to discover nearby Wi-Fi networks. Analyzing these requests, along with beacon frames, can help in mapping the presence and movement of Wi-Fi devices.

SSIDs and Network Information: Beacon frames include information about the SSID (network name) and other network configuration details. Analyzing the SSIDs and associated information in beacon frames can reveal information about the physical locations of Wi-Fi networks. This, combined with signal strength, contributes to location tracking.


   **Example Commands:**
    The `-E` option is used for filtering based on specific Wi-Fi frame types/subtypes, allowing targeted captures. 
   - Capture Beacon frames with `-E` (Type/Subtype Filtering):
     ```bash
     sudo tcpdump -n -i en1 -vvv -E 'wlan.fc.type_subtype == 0x0088'
     ```
   - Capture Probe request frames with `-E` (Type/Subtype Filtering):  
      ```bash
     sudo tcpdump -n -i en1 -vvv -E 'wlan.fc.type_subtype == 0x0040'
     ```
      **open pcap in wireshark and filter for EAPOL, if you have frames named KEY1 KEY2 KEY3 KEY4 it suggests that you have successfully captured the 4 way handshake.**
   **Note: for every set of frames numbered KEY1-4 represents a 4 way handshake**
  
5. **Persistence and Continuous Capturing:**
   - Insider threats may set up a cronjob to achieve persistence, ensuring that the Wi-Fi beacon frame capturing script runs automatically at system reboot. Additionally, appending `&` at the end of the `tcpdump` command ensures continuous capturing even after the terminal window is closed.
   - **replace the beacon hexadecimal in the script sturdy-palm-tree.txt with the frame hexadecimal you would like to capture from the list provided in a-sturdy-tree.md**


## Mitigation Strategies
To mitigate the risks associated with insider threats capturing Wi-Fi beacon frames, consider the following strategies:

1. **Access Controls:**
   - Implement strong access controls to restrict unauthorized access to Wi-Fi monitoring tools and equipment specifically capturing beacon / probe frames.

2. **Encryption:**
   - Encourage the use of encrypted communication over Wi-Fi to protect sensitive information revealed in beacon frames.

3. **Regular Audits:**
   - Conduct regular audits of Wi-Fi network configurations to detect any unauthorized changes or rogue access points.

## Usage
1. Power on your Flipper Zero, and navigate to badusb/sturdy-palm-tree and click on it. 
2. On Target machine open a terminal window and Connect the Flipper to the TARGET machine, and Click "Run" on the device.
NOTE --  you will already have gained sudo privileges in order for this badusb script to execute properly.  I am not including how one gaines sudo access and or how one then starts the attack modifying the sudoers file on the target machine.  That is left out intentionally for you to discover. Once you have sudo access and have added the correct syntax to the sudoers file proceed to test the script sturdy-palm-tree.txt -- you will also need to provide your discord webhook in place. 
3. Wait until on your Flipper you are reading 100%.
4. Disconnects Flipper Zero.
5. Download your pcap file from your discord and open it in wireshark. Proceed with reconn
6. for testing purposes one may choose to add  **a-sturdy-tree.md** and **beaconBoogie.py** to the files hosted on the target machine. Once shell is achieved on the **target** navigate to directory hosting files and run **beaconBoogie.py** to launch a rougeAP  You must act responsibly and in the bounds of the law.  
   
## Contributing
This attack is continuiously capturing packets even after the intial POST to discord (this attack captures for 1 min then sends the data to discord). I am strill trying to figure out how to modify the script so it POSTS updated data to discord every hour.
Feel free to contribute to this repository by suggesting improvements, adding more risks or mitigation strategies specific to beacon frame capture, or sharing educational resources related to insider threats in Wi-Fi monitoring.

## License
This project is licensed under the MIT License.

## Disclaimer
Please note that this repo and all payloads are for educational purposes only and should not be used for illegal activities.
