# SMB Availability Checker

This script is a GUI application built using the `tkinter` library. It checks the availability of SMB (Server Message Block) on a list of IP addresses and displays the status using colored labels. The IP addresses are loaded from a file named "pclist.txt". This script is designed for Windows systems.

## Usage

1. Clone the repository and navigate to the project directory.
2. Create a file named "pclist.txt" and add a list of IP addresses, one per line.
3. Modify the `link` variable in the script to match the correct path on your system.
4. Run the script using Python 3.

## Functionality

- The script checks the availability of SMB on each IP address in parallel using threading for improved performance.
- When you click on a label, it opens a network share link in Windows Explorer. The link is constructed using the IP address and a specific path.
- The labels are color-coded to indicate the SMB availability: green for available and red for unavailable.

## Dependencies

- Python 3
- `tkinter` library (usually included in Python installations)

## Example

Here's an example of how the script can be used:

1. Create a file named "pclist.txt" with the following IP addresses:
```
192.168.1.10
192.168.1.11
192.168.1.12
```
2. Modify the `link` variable in the script to match the correct path on your system.
3. Run the script using Python 3.
4. The GUI window will open, displaying labels for each IP address.
5. The script will check the SMB availability of each IP address and update the labels accordingly.
6. Click on a label to open the network share link in Windows Explorer.

## Notes

- Make sure to have the necessary permissions and network access to check the SMB availability on the IP addresses.
- The script assumes that the SMB port (port 445) is used for SMB communication.
- This script is designed for Windows systems and may not work on other operating systems.
