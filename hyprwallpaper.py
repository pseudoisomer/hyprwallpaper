#!/usr/bin/env python3
import os
import shutil
import sys

chosen_wp = ''
confirmed = False
change_wallpaper = False

while confirmed == False:
	try:
		chosen_wp = input('\033[94menter the path of the new wallpaper. you can drag and drop from a file manager if you like. write exit if you wish to stop the program\n\033[0m')
		if os.path.isfile(chosen_wp):
			want = input('\033[95mare you sure you want ' + chosen_wp + ' to be your wallpaper? \033[1my/n\033[22m\033[0m \n')
			if want == 'y':
				change_wallpaper = True
				confirmed = True
			else:
				sys.exit('\033[91mif you do not want this wallpaper, please restart the program and choose one to your preferring')
		elif chosen_wp == 'exit':
			sys.exit('\033[91mprogram successfully stopped\033[0m')
	except FileNotFoundError:
		print('\033[91mfile not found, please try again\033[0m')				

command_for_wallpaper = 'preload = ' + chosen_wp + '\nwallpaper = ,' + chosen_wp

with open('//home//sudol//.config//hypr//hyprpaper.conf','w') as file:
	file.write(command_for_wallpaper)

print(f"\033[92mwallpaper successfully changed to {chosen_wp}\033[0m")
