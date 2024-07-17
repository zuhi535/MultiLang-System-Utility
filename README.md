1. Settings and Imports
To import directories:
tkinter to create the GUI.
messagebox, scrolledtext, and ttk for special GUI elements.
requests for web requests.
datetime for date and time management.
os, path, and shutil for file and directory management.
Platform and PSUTIL for system information.
GPUtil for GPU information.
tabulate for tabulating.

2. Define functions
get_size: Convert byte sizes to human-readable formats.
Define languages: The LANGUAGES dictionary stores English, Hungarian, German, and Russian texts.

3. Language switching features
switch_language: Change language based on user choice.
update_language: Update text in GUI elements based on the current language.

4. Implement various functions
show_public_ip_and_save: Get and save a public IP address.
download_virtualbox_windows_hosts: Download VirtualBox for Windows.
download_debian_iso: Download Debian ISO.
download_kali_iso: Download Kali Linux ISO.
download_vscode_installer: Download Visual Studio Code.
download_git_installer: Download Git installer.
clear_temp_folder: Erase contents of a TEMP folder.
display_system_info_window: Display system information in a separate window.
show_system_info: Collect and display system information.

5. Create Main Window and GUI Elements
Main window setting: Window title and size.
Set Style: Use a default style.
Language Selection: Create a language selector drop-down menu.
Create buttons: Create a separate button for each function and assign the corresponding functions.

6. Set and Apply Language
Set initial language: Update the default language using the update_language function.

7. Main Program Cycle
Start the program: call root.mainloop() to make the GUI active and responsive to user interactions.
