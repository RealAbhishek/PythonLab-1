import subprocess  # Import the subprocess module to run system commands
from getpass import getpass  # Import getpass to securely get the password input


def run_nmap():
    print("Welcome to the NMAP decoy scan script")  # Print a welcome message
    target = input("Enter the target IP: ")  # Prompt the user to enter the target IP address
    decoy = input("Enter the decoy IP: ")  # Prompt the user to enter the decoy IP address
    ttl = input("Enter the TTL: ")  # Prompt the user to enter the TTL (Time To Live) value
    password = input("Enter the password: ")  # Prompt the user to enter the password

    # Define the Nmap command as a list of arguments
    command = ["nmap", target, "-D", decoy, "-ttl", ttl]

    # Construct the command string to run Nmap with sudo, using the provided password
    cmd = "echo " + password + " | sudo -S nmap " + target + " -D " + decoy + " -ttl " + ttl

    # Execute the command using subprocess.call
    proc = subprocess.call(cmd, shell=True)

    # Clear the password variable for security reasons
    password = ""

    # The following block is commented out, but it shows an alternative way to run the command
    # try:
    #     # Run the command and capture the output
    #     result = subprocess.run(command, capture_output=True, text=True, check=True)
    #     print("Nmap Scan Output:\n", result.stdout)  # Print the output of the Nmap scan
    # except subprocess.CalledProcessError as e:
    #     print("An error occurred while running Nmap:", e)  # Print an error message if the command fails


if __name__ == "__main__":
    run_nmap()  # Call the run_nmap function if the script is executed directly
