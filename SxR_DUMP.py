import platform,os
os.system("clear")
sxr = platform.architecture()[0]
if "64" in sxr:import SxR_DMP
else:print(f"The SxR tool has not yet been released for {sxr} It may be available for all bit versions soon.")
