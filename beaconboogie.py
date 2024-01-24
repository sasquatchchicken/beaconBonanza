from scapy.all import RadioTap, Dot11, Dot11Beacon, sendp, Dot11Elt

def send_beacon(ssid, bssid, channel=1, interval=100, loop_count=5):
    # Create a RadioTap header --  a special Scapy layer that represents the Radiotap header, which is used in wireless frames to convey information about the radio signal.
    radiotap = RadioTap()

    # Create a Dot11 layer for the beacon frame -- represents the IEEE 802.11 header. In this case, it's configured as a beacon frame (subtype=8), and the destination address (addr1) is set to the broadcast address ("ff:ff:ff:ff:ff:ff"). The source address (addr2) and transmitter address (addr3) are set to the specified BSSID (basic service set identifier). 
    beacon = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=bssid, addr3=bssid)
    
    # Create a Dot11Beacon layer with SSID and other information -- a subtype of the beacon frame. It contains information about the capabilities of the network (cap), and an element (Dot11Elt) specifying the SSID of the network.
    dot11_beacon = Dot11Beacon(cap="ESS+privacy") / Dot11Elt(ID="SSID", info=ssid)

    # Create the final frame by combining layers -- The final frame is created by combining the Radiotap header, the beacon header, and the Dot11Beacon layer.
    frame = radiotap / beacon / dot11_beacon

    # Set the channel for the frame
    frame[RadioTap].ChannelFrequency = channel

    # Send the frame in a loop -- This sends the crafted frame using Scapy's sendp function. It specifies the Wi-Fi interface ("en1"), the inter-frame gap (inter=0.1), the number of loops, and verbosity.
    sendp(frame, iface="en1", inter=0.1, loop=loop_count, verbose=1)

# Replace "your_wifi_interface" with the name of your Wi-Fi interface
# Set the desired SSID, BSSID, and optional parameters for the beacon frame
send_beacon(ssid="target", bssid="target", channel=6, interval=200, loop_count=10)
