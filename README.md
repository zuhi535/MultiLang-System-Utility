                                                                                                        |Step-by-step description of how a program works|
                                                                                                        -------------------------------------------------
                                                                                                        
------------------------|                                                                                                                                
1. Settings and Imports |                                                                                                                                
------------------------|                                                                                                                              |----------------------------------------------------------------------------------------------------------|
  To import directories:                                                                                                                               | Summation:                                                                                               |
  tkinter to create the GUI.                                                                                                                           |                                                                                                          |
  messagebox, scrolledtext, and ttk for special GUI elements.                                                                                          | The program is a multifunctional application that can perform various tasks, including downloads,        |
  requests for web requests.                                                                                                                           | file management, and displaying system information. Language selection provides multilingual support,    |
  datetime for date and time management.                                                                                                               | so users can use their preferred language.                                                               |
  os, path, and shutil for file and directory management.                                                                                              |----------------------------------------------------------------------------------------------------------|
  Platform and PSUTIL for system information.
  GPUtil for GPU information.
  tabulate for tabulating.

------------------------|
3. Define functions     |
------------------------|
  get_size: Convert byte sizes to human-readable formats.
  Define languages: The LANGUAGES dictionary stores English, Hungarian, German, and Russian texts.
  
-------------------------------|
5. Implement various functions |
-------------------------------|
  show_public_ip_and_save: Get and save a public IP address.
  download_virtualbox_windows_hosts: Download VirtualBox for Windows.
  download_debian_iso: Download Debian ISO.
  download_kali_iso: Download Kali Linux ISO.
  download_vscode_installer: Download Visual Studio Code.
  download_git_installer: Download Git installer.
  clear_temp_folder: Erase contents of a TEMP folder.
  display_system_info_window: Display system information in a separate window.
  show_system_info: Collect and display system information.
  
---------------------------------------|
7. Create Main Window and GUI Elements |
---------------------------------------|
  Main window setting: Window title and size.
  Set Style: Use a default style.
  Language Selection: Create a language selector drop-down menu.
  Create buttons: Create a separate button for each function and assign the corresponding functions.
  
--------------------------|
9. Set and Apply Language |
--------------------------|
  Set initial language: Update the default language using the update_language function.
  
--------------------------|
10. Main Program Cycle    |
--------------------------|
  Start the program: call root.mainloop() to make the GUI active and responsive to user interactions.

  

-------------------------------------------------------------------------------------------------|                    An example of how the program works                    |------------------------------------------------------------------------------------------

----------------------|
Select language:      |
----------------------|
The user selects a language from the drop-down menu. The switch_language function updates the GUI text based on the language you choose.

-----------------|
Save public IP:  |
-----------------|
The user clicks on the "Save Public IP and Identifier" button. The program retrieves the public IP address, generates an identifier and saves it in a file.

---------------------|
Download VirtualBox: |
---------------------|
The user clicks on the "Download VirtualBox (Windows)" button. The program downloads the VirtualBox installer from the URL you entered and saves it in your Downloads folder.

----------------------|
Download Debian ISO:  |
----------------------|
The user clicks on the "Download Debian (ISO)" button. The program downloads the Debian ISO file and saves it in your Downloads folder.

--------------------------|
To delete a TEMP folder:  |
--------------------------|
The user clicks on the "Clear TEMP Folder" button. The contents of the TEMP folder are deleted and feedback is provided on successful deletion.

--------------------------------|
To display system information:  |
--------------------------------|
The user clicks on the "Show System Information" button. The program collects system information and displays it in a separate window.
