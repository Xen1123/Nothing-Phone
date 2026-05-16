from pathlib import Path
import shutil
import subprocess
import sys
import os
import time
print(r"""

███╗   ██╗ ██████╗ ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
██╔██╗ ██║██║   ██║   ██║   ███████║██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██║   ██║   ██║   ██╔══██║██║██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    
                                        
""")
print("This Script Restores Your Nothing Phone Firmware Or Flashes A Custom ROM Based On What Images Are In Your Directory!")
confirm = input("Are Your Images In Your Current Directory? (y/n)")
if confirm.lower() != "y":
     print("Please Make Sure Your Images Are Right! <3")
     sys.exit()
else:
     confirm = input("Are You REALLY Sure? On Some Devices, Restoring From EDL Is A Real Pain... (y/n)")
     if confirm.lower() != "y":
          print("Second Thoughts I See...")
          sys.exit()
     else:
          print("Alright Then!")

adb_path = shutil.which("adb")
if not adb_path:
     print("ADB Not Installed Or In Your PATH!")
     sys.exit()
else:
     print(f"ADB Found At: {adb_path}")

fastboot_path = shutil.which("fastboot")
if not fastboot_path:
     print("Fastboot Not Installed Or In Your PATH!")
     sys.exit()
else:
     print(f"Fastboot Found At: {fastboot_path}")

print("Rebooting To Bootloader Fastboot (ABL)")
subprocess.run([
     "adb", "reboot", "bootloader"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

subprocess.run([
     "fastboot", "reboot", "bootloader"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.name == 'nt':
     os.system('cls')
else:
     os.system('clear')

images = [
     "boot", "vendor_boot", "dtbo", "recovery", "abl", "aop", "aop_config", "bluetooth", "cpucp_dtb", "cpucp", 
     "devcfg", "dsp", "featenabler", "hyp", "imagefv", "init_boot", "keymaster", "modem", "multiimgoem", "odm", 
     "pvmfw", "qupfw", "shrm", "tz", "uefi", "uefisecapp", "vbmeta", "vbmeta_system", "vbmeta_vendor", "xbl", 
     "xbl_config", "xbl_ramdump"
]

for img in images:
     file_path = Path(f"{img}.img")

     if file_path.is_file():
          print(f"\nFlashing {img} . . .")
          subprocess.run([
               "fastboot", "flash", f"{img}_a", file_path
          ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
          subprocess.run([
               "fastboot", "flash", f"{img}_b", file_path
          ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.name == 'nt':
     os.system('cls')
else:
     os.system('clear')

print(r"""

███╗   ██╗ ██████╗ ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
██╔██╗ ██║██║   ██║   ██║   ███████║██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██║   ██║   ██║   ██╔══██║██║██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝    
                                        
               Going To Fastbootd
""")

subprocess.run([
     "fastboot", "reboot", "fastboot"
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(5)

if os.name == 'nt':
     os.system('cls')
else:
     os.system('clear')

images = [
     "product", "system", "system_dlkm", "system_ext", "vendor", "vendor_dlkm"
]

for img in images:
     file_path = Path(f"{img}.img")

     if file_path.is_file():
          print(f"\nFlashing {img} . . .")
          subprocess.run([
               "fastboot", "flash", img, file_path
          ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

confirm = input("Reboot To System? (y/n)")
if confirm.lower() != "y":
     print("Okay! Staying Put!")
     sys.exit()
else:
     subprocess.run([
          "fastboot", "reboot"
     ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if os.name == 'nt':
     os.system('cls')
else:
     os.system('clear')

print(r"""                                      
                                                          
███╗   ██╗ ██████╗ ████████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
████╗  ██║██╔═══██╗╚══██╔══╝██║  ██║██║████╗  ██║██╔════╝ 
██╔██╗ ██║██║   ██║   ██║   ███████║██║██╔██╗ ██║██║  ███╗
██║╚██╗██║██║   ██║   ██║   ██╔══██║██║██║╚██╗██║██║   ██║
██║ ╚████║╚██████╔╝   ██║   ██║  ██║██║██║ ╚████║╚██████╔╝
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝                                                     
                                        
                      All Done!
""")

sys.exit(0)