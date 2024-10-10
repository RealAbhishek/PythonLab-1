#!/usr/bin/python  # Specify the interpreter to be used for the script
# -*- coding: utf-8 -*-  # Define the encoding of the script
from scapy.all import *  # Import all functions and classes from the scapy module


def printPcap(pcap):
    for pkt in pcap:  # Iterate over each packet in the pcap file
        if IP in pkt:  # Check if the packet has an IP layer
            try:
                print('[+] Src: ' + pkt[IP].src + ' -->  Dst: ' + pkt[IP].dst)  # Print the source and destination IP addresses
            except:  # Handle any exceptions that occur
                print("nothing to report")  # Print a message if an exception occurs
                pass  # Continue to the next packet


def main():
    print("Welcome to the Print Direction script.")  # Print a welcome message
    pcap = input("Select which pcap file you want to inspect? ")  # Prompt the user to enter the pcap file to inspect

    try:
        packets = rdpcap(pcap)  # Read the pcap file and store the packets
    except Exception as e:  # Handle any exceptions that occur while reading the pcap file
        print(e)  # Print the exception message
        print("Something went wrong, let's try again, shall we?")  # Print a message indicating an error occurred
        main()  # Call the main function again to retry

    try:
        printPcap(packets)  # Call the printPcap function to print the packet details
    except Exception as e:  # Handle any exceptions that occur while printing the packet details
        print(e)  # Print the exception message
        print("Goodbye")  # Print a goodbye message
        exit(0)  # Exit the script


if __name__ == '__main__':
    main()  # Call the main function if the script is executed directly
