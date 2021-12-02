import time
import os

os.system("title server data maker")
os.system("color 0c")

print("======================================")
print("Dont forget star my github")
print("github.com/uazeh")
print("UazeGanteng;V")
print("======================================")
ip = input("Enter IP : ")

f = open("server_data.php", "w")
f.write(f"server|{ip}\nport|17091\ntype|1\n#maint|Maintenance message\n\nbeta_server|{ip}\nbeta_port|17091\n\nbeta_type|1\nmeta|localhost\nRTENDMARKERBS1001")
f.close()

print("Please wait......")
time.sleep(5)

os.system("cls")
print("[+] Successfully Created...")
time.sleep(5)

os.system("cls")
input("Enter any key for close......")