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
   - Insider threats might utilize captured beacon frames to set up unauthorized Wi-Fi access points, leading to potential security vulnerabilities.

3. **Network Parameters Exposure:**
   - Beacon frames contain information about the network configuration. Insiders capturing these frames may expose details such as SSID, supported data rates, and security settings.

4. **Location Tracking:**
   - Beacon frames may contain information that can be exploited for location tracking, revealing the movement patterns of Wi-Fi devices.


   **Example Commands:**
   - Capture Beacon frames with `-E` (Type/Subtype Filtering):
     ```bash
     sudo tcpdump -n -i en1 -vvv -E 'wlan.fc.type_subtype == 0x08'
     ```
   **Note:**
   The `-E` option is used for filtering based on specific Wi-Fi frame types/subtypes, allowing targeted captures. 

5. **Persistence and Continuous Capturing:**
   - Insider threats may set up a cronjob to achieve persistence, ensuring that the Wi-Fi beacon frame capturing script runs automatically at system reboot. Additionally, appending `&` at the end of the `tcpdump` command ensures continuous capturing even after the terminal window is closed.


## Mitigation Strategies
To mitigate the risks associated with insider threats capturing Wi-Fi beacon frames, consider the following strategies:

1. **Access Controls:**
   - Implement strong access controls to restrict unauthorized access to Wi-Fi monitoring tools and equipment specifically capturing beacon frames.

2. **Encryption:**
   - Encourage the use of encrypted communication over Wi-Fi to protect sensitive information revealed in beacon frames.

3. **Regular Audits:**
   - Conduct regular audits of Wi-Fi network configurations to detect any unauthorized changes or rogue access points.

4. **Employee Training:**
   - Provide comprehensive training to employees about the potential risks associated with capturing beacon frames and the importance of securing Wi-Fi networks.

## Usage
1. Power on your Flipper Zero, and navigate to badusb/sturdy-palm-tree and click on it. 
2. On Target machine open a terminal window and Connect the Flipper to the TARGET machine, and Click "Run" on the device.
NOTE --  you will already have gained sudo privileges in order for this badusb script to execute properly.  I am not including how one gaines sudo access and or how one then starts the attack modifying the sudoers file on the target machine.  That is left out intentionally for you to discover. Once you have sudo access or have added the correct syntax to the sudoers file proceed to test the script sturdy-palm-tree.txt -- you will also need to provide your discord webhook in place. 
3. Wait until on your Flipper you are reading 100%.
4. Disconnects Flipper Zero.
5. Download your pcap file from your discord adn open it in wireshark to inspect.
   
## Contributing
This attack is continuiously capturing packets even after the intial POST to discord (this attack captures for 1 min then sends the data to discord). I am strill trying to figure out how to modify the script so it POSTS updated data to discord every hour.
Feel free to contribute to this repository by suggesting improvements, adding more risks or mitigation strategies specific to beacon frame capture, or sharing educational resources related to insider threats in Wi-Fi monitoring.

## License
This project is licensed under the MIT License.

## Disclaimer
Please note that this payload is for educational purposes only and should not be used for illegal activities.
