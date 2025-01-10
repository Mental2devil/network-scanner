import tkinter as tk
from tkinter import messagebox, scrolledtext
import scapy.all as scapy
import socket
import threading
import netifaces
import os
import sys

class NetworkScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Automatic Network Scanner")

        self.scan_button = tk.Button(root, text="Scan Network", command=self.start_scan)
        self.scan_button.pack()

        self.result_text = scrolledtext.ScrolledText(root, width=80, height=20)
        self.result_text.pack()

    def start_scan(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "Scanning network...\n")
        threading.Thread(target=self.scan_network).start()

    def scan_network(self):
        try:
            interfaces = netifaces.interfaces()
            for interface in interfaces:
                addrs = netifaces.ifaddresses(interface)
                if netifaces.AF_INET in addrs:
                    for addr in addrs[netifaces.AF_INET]:
                        ip_address = addr['addr']
                        netmask = addr['netmask']
                        cidr = sum([bin(int(x)).count('1') for x in netmask.split('.')])
                        ip_range = f"{ip_address}/{cidr}"
                        self.result_text.insert(tk.END, f"Scanning interface {interface} with IP range {ip_range}\n")
                        self.scan_ip_range(ip_range, interface)
        except PermissionError:
            self.result_text.insert(tk.END, "PermissionError: Please run the script with administrative privileges.\n")
            messagebox.showerror("Permission Error", "Please run the script with administrative privileges.")
        except Exception as e:
            self.result_text.insert(tk.END, f"An error occurred: {e}\n")
            messagebox.showerror("Error", f"An error occurred: {e}")

    def scan_ip_range(self, ip_range, interface):
        try:
            # Check if the interface is up
            if not self.is_interface_up(interface):
                self.result_text.insert(tk.END, f"Interface {interface} is down. Skipping...\n")
                return

            # Create an ARP request packet
            arp_request = scapy.ARP(pdst=ip_range)
            broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request

            # Send the packet and capture the response
            self.result_text.insert(tk.END, f"Sending ARP request on interface {interface} for IP range {ip_range}\n")
            answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False, iface=interface)[0]

            # Extract the IP and MAC addresses from the response
            clients = []
            for sent, received in answered_list:
                clients.append({'ip': received.psrc, 'mac': received.hwsrc})
                self.result_text.insert(tk.END, f"Found device: IP={received.psrc}, MAC={received.hwsrc}\n")

            # Display the results in the GUI
            self.display_results(clients)
        except OSError as e:
            self.result_text.insert(tk.END, f"Network error: {e}\n")
            messagebox.showerror("Network Error", f"Network error: {e}")
        except Exception as e:
            self.result_text.insert(tk.END, f"An error occurred while scanning {ip_range}: {e}\n")
            messagebox.showerror("Error", f"An error occurred while scanning {ip_range}: {e}")

    def display_results(self, clients):
        self.result_text.insert(tk.END, "Available devices in the network:\n")
        self.result_text.insert(tk.END, "IP" + " "*18+"MAC\n")
        for client in clients:
            self.result_text.insert(tk.END, "{:16}    {}\n".format(client['ip'], client['mac']))

    def is_interface_up(self, interface):
        try:
            with open(f"/sys/class/net/{interface}/operstate", "r") as f:
                state = f.read().strip()
            return state == "up"
        except Exception:
            return False

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Please run the script with administrative privileges.")
        sys.exit(1)

    root = tk.Tk()
    app = NetworkScannerApp(root)
    root.mainloop()

