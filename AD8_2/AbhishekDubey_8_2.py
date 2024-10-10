import nmap  # Importing the nmap module
import optparse  # Importing the optparse module to handle command-line options


# Function to perform the nmap scan
def nmap_scan(tgtHost, tgtPort, onlyOpen):
    nmScan = nmap.PortScanner()  # Creating a PortScanner object
    nmScan.scan(tgtHost, tgtPort)  # Scanning the target host and port
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']  # Getting the state of the port
    if onlyOpen:
        if state == 'open':
            print("[*] " + tgtHost + " tcp/" + tgtPort + " " + state)  # Printing the result only if the port is open
    else:
        print("[*] " + tgtHost + " tcp/" + tgtPort + " " + state)  # Printing the result

# def main():
#     # Creating an OptionParser object and setting the usage message
#     parser = optparse.OptionParser('usage %prog ' + '-H <target host> -f <ports list file> [-O]')
#     parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
#     # The -p flag has been disabled in this version of the script
#     parser.add_option('-p', dest='tgtPort', type='string', help='The -p flag has been disabled in this version of the\
#     nmap scan script. Please use the -f flag and input a .txt file with ports listen within it.')
#     parser.add_option('-f', dest='tgtPortsFile', type='string', help='specific ports list in file')
#     parser.add_option('-O', action='store_true', dest='onlyOpen', default=False, help='only print open ports')
#     (options, args) = parser.parse_args()  # Parsing the command-line arguments
#
#     # If the -p flag is used, print a message and exit
#     if options.tgtPort is not None:
#         print("Sorry, this flag has been deprecated. Please use the -h flag for more information.")
#         exit(0)
#
#     tgtHost = options.tgtHost  # Getting the target host from the options
#     tgtPortsFile = options.tgtPortsFile  # Getting the ports file from the options
#     onlyOpen = options.onlyOpen  # Getting the onlyOpen flag from the options
#
#     # If the target host or ports file is not specified, print the usage message and exit
#     if (tgtHost is None) or (tgtPortsFile is None):
#         print(parser.usage)
#         exit(0)
#     elif (tgtPortsFile is not None):
#         portFile = open(tgtPortsFile)  # Opening the ports file
#         for line in portFile.readlines():  # Reading each line in the ports file
#             port = line.strip('\n')  # Stripping the newline character from the port
#             nmapScan(tgtHost, port, onlyOpen)  # Calling the nmapScan function with the target host and port
#
#
# if __name__ == '__main__':
#     main()  # Calling the main function

