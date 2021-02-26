#Author:SoeZayZay
#Date :24/2/2021
import pyfiglet
import nmap3

banner = pyfiglet.figlet_format(" Web-Scanner")
print(banner)
nmap = nmap3.Nmap()
url  = input("           Enter Website Url : ")
data = nmap.scan_top_ports(url)
print("")
task="""
           1.Copy the following json data
        
           2.Use Json viewer app to view the data
    """
print(task)
print("==================================================================")
print("")
print(data)
print("")
print("==================================================================")
