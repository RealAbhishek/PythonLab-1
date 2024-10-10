#!/usr/bin/python  # Specify the interpreter to be used for the script
# -*- coding: utf-8 -*-  # Define the encoding of the script
import time  # Import the time module
import optparse  # Import the optparse module for parsing command-line options
from scapy.all import *  # Import all functions and classes from the scapy module
from IPy import IP as IPTEST  # Import the IP class from the IPy module and alias it as IPTEST


ttlValues = {}  # Initialize an empty dictionary to store TTL values
THRESH = 5  # Set the threshold value for TTL difference


def checkTTL(ipsrc, ttl):
    if IPTEST(ipsrc).iptype() == 'PRIVATE':  # Check if the IP source is private
        return  # Exit the function if the IP is private

    if ipsrc not in ttlValues:  # If the IP source is not in the ttlValues dictionary
        pkt = sr1(IP(dst=ipsrc) / ICMP(), retry=0, timeout=1, verbose=0)  # Send an ICMP packet to the IP source and get the response
        ttlValues[ipsrc] = pkt.ttl  # Store the TTL value from the response in the ttlValues dictionary

    if abs(int(ttl) - int(ttlValues[ipsrc])) > THRESH:  # Check if the difference between the TTL values exceeds the threshold
        print('\n[!] Detected Possible Spoofed Packet From: ' + ipsrc)  # Print a warning message if a possible spoofed packet is detected
        print('[!] TTL: ' + ttl + ', Actual TTL: ' + str(ttlValues[ipsrc]))  # Print the TTL values


def testTTL(pkt):
    try:
        if pkt.haslayer(IP):  # Check if the packet has an IP layer
            ipsrc = pkt.getlayer(IP).src  # Get the source IP address from the packet
            ttl = str(pkt.ttl)  # Get the TTL value from the packet and convert it to a string
            checkTTL(ipsrc, ttl)  # Call the checkTTL function with the source IP and TTL value
    except:
        pass  # Ignore any exceptions


def main():
    parser = optparse.OptionParser("usage %prog -i <interface> -t <thresh>")  # Create an OptionParser object with usage instructions
    parser.add_option('-i', dest='iface', type='string', help='specify network interface')  # Add an option for specifying the network interface
    parser.add_option('-t', dest='thresh', type='int', help='specify threshold count')  # Add an option for specifying the threshold count

    (options, args) = parser.parse_args()  # Parse the command-line options
    if options.iface == None:  # If no interface is specified
        ethernet = input("Which ethernet interface do you want to check (eth0, eth1)? ")  # Prompt the user to enter the ethernet interface
        conf.iface = ethernet  # Set the specified interface in the scapy configuration
    else:
        conf.iface = options.iface  # Set the specified interface in the scapy configuration

    if options.thresh != None:  # If a threshold is specified
        THRESH = options.thresh  # Set the threshold value
    else:
        threshold = input("What threshold do you want to set? (Default is 5) ")  # Prompt the user to enter the threshold value
        if threshold is None:
            THRESH = 5  # Set the default threshold value if none is provided
        else:
            THRESH = threshold  # Set the specified threshold value

    print("Checking for spoofers...")  # Print a message indicating that the script is checking for spoofers
    sniff(prn=testTTL, store=0)  # Start sniffing packets and call the testTTL function for each packet


if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly
