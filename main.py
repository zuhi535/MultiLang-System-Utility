import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import requests
from datetime import datetime
import os
from pathlib import Path
import shutil
import platform
import psutil
import GPUtil
from tabulate import tabulate

# Function to get size in a human-readable format
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

# Global variables for language support
LANGUAGES = {
    "english": {
        "name": "English",
        "public_ip": "Save Public IP and Identifier",
        "public_ip_success": "Identifier and IP address successfully saved in public_ip.txt file.",
        "download_virtualbox": "Download VirtualBox (Windows)",
        "download_virtualbox_success": "VirtualBox Windows installer successfully downloaded!",
        "download_debian": "Download Debian (ISO)",
        "download_debian_success": "Debian ISO successfully downloaded!",
        "download_kali": "Download Kali Linux (ISO)",
        "download_kali_success": "Kali Linux ISO successfully downloaded!",
        "download_vscode": "Download Visual Studio Code",
        "download_vscode_success": "Visual Studio Code installer successfully downloaded!",
        "download_git": "Download Git",
        "download_git_success": "Git installer successfully downloaded!",
        "clear_temp": "Clear TEMP Folder",
        "clear_temp_success": "TEMP folder content successfully cleared!",
        "system_info": "Show System Information",
        "language_label": "Language:",
        "system_info_title": "System Information",
    },
    "hungarian": {
        "name": "Magyar",
        "public_ip": "Public IP és azonosító mentése",
        "public_ip_success": "Azonosító és IP-cím sikeresen mentve a public_ip.txt fájlba.",
        "download_virtualbox": "VirtualBox letöltése (Windows)",
        "download_virtualbox_success": "VirtualBox Windows telepítő sikeresen letöltve!",
        "download_debian": "Debian letöltése (ISO)",
        "download_debian_success": "Debian ISO sikeresen letöltve!",
        "download_kali": "Kali Linux letöltése (ISO)",
        "download_kali_success": "Kali Linux ISO sikeresen letöltve!",
        "download_vscode": "Visual Studio Code letöltése",
        "download_vscode_success": "Visual Studio Code telepítő sikeresen letöltve!",
        "download_git": "Git letöltése",
        "download_git_success": "Git telepítő sikeresen letöltve!",
        "clear_temp": "TEMP mappa ürítése",
        "clear_temp_success": "A TEMP mappa tartalma sikeresen törölve!",
        "system_info": "Rendszer Információk megjelenítése",
        "language_label": "Nyelv:",
        "system_info_title": "Rendszer Információk",
    },
    "german": {
        "name": "Deutsch",
        "public_ip": "Öffentliche IP und Kennung speichern",
        "public_ip_success": "Kennung und IP-Adresse erfolgreich in der Datei public_ip.txt gespeichert.",
        "download_virtualbox": "VirtualBox herunterladen (Windows)",
        "download_virtualbox_success": "VirtualBox Windows-Installationsprogramm erfolgreich heruntergeladen!",
        "download_debian": "Debian herunterladen (ISO)",
        "download_debian_success": "Debian ISO erfolgreich heruntergeladen!",
        "download_kali": "Kali Linux herunterladen (ISO)",
        "download_kali_success": "Kali Linux ISO erfolgreich heruntergeladen!",
        "download_vscode": "Visual Studio Code herunterladen",
        "download_vscode_success": "Visual Studio Code-Installationsprogramm erfolgreich heruntergeladen!",
        "download_git": "Git herunterladen",
        "download_git_success": "Git-Installationsprogramm erfolgreich heruntergeladen!",
        "clear_temp": "TEMP-Ordner leeren",
        "clear_temp_success": "TEMP-Ordnerinhalt erfolgreich gelöscht!",
        "system_info": "Systeminformationen anzeigen",
        "language_label": "Sprache:",
        "system_info_title": "Systeminformationen",
    },
    "russian": {
        "name": "Русский",
        "public_ip": "Сохранить публичный IP и идентификатор",
        "public_ip_success": "Идентификатор и IP-адрес успешно сохранены в файл public_ip.txt.",
        "download_virtualbox": "Скачать VirtualBox (Windows)",
        "download_virtualbox_success": "Установочный файл VirtualBox для Windows успешно загружен!",
        "download_debian": "Скачать Debian (ISO)",
        "download_debian_success": "Образ Debian ISO успешно загружен!",
        "download_kali": "Скачать Kali Linux (ISO)",
        "download_kali_success": "Образ Kali Linux ISO успешно загружен!",
        "download_vscode": "Скачать Visual Studio Code",
        "download_vscode_success": "Установочный файл Visual Studio Code успешно загружен!",
        "download_git": "Скачать Git",
        "download_git_success": "Установочный файл Git успешно загружен!",
        "clear_temp": "Очистить папку TEMP",
        "clear_temp_success": "Содержимое папки TEMP успешно очищено!",
        "system_info": "Показать системную информацию",
        "language_label": "Язык:",
        "system_info_title": "Системная информация",
    }
}


# Default language
LANGUAGE = "english"

# Function to switch language
def switch_language(event=None):
    global LANGUAGE
    LANGUAGE = combo_language.get()
    update_language()

# Function to update GUI elements with selected language
def update_language():
    language_info = LANGUAGES[LANGUAGE]
    btn_public_ip.config(text=language_info["public_ip"])
    btn_download_virtualbox.config(text=language_info["download_virtualbox"])
    btn_download_debian.config(text=language_info["download_debian"])
    btn_download_kali.config(text=language_info["download_kali"])
    btn_download_vscode.config(text=language_info["download_vscode"])
    btn_download_git.config(text=language_info["download_git"])
    btn_clear_temp.config(text=language_info["clear_temp"])
    btn_system_info.config(text=language_info["system_info"])
    lbl_language.config(text=language_info["language_label"])

# Function to show public IP and save it
def show_public_ip_and_save():
    try:
        response = requests.get('http://httpbin.org/ip')
        data = response.json()
        ip_address = data['origin']
        
        identifier = f"user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        with open("public_ip.txt", "a") as file:
            file.write(f"Azonosító: {identifier}, Public IPv4: {ip_address}, Idő: {datetime.now()}\n")
            messagebox.showinfo("Mentés sikeres", LANGUAGES[LANGUAGE]["public_ip_success"])
            
    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt az IP-cím lekérdezése közben:\n{e}")

# Function to download VirtualBox installer for Windows
def download_virtualbox_windows_hosts():
    url = 'https://download.virtualbox.org/virtualbox/7.0.18/VirtualBox-7.0.18-162988-Win.exe'
    try:
        messagebox.showinfo("Letöltés...", LANGUAGES[LANGUAGE]["download_virtualbox"])
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            downloads_path = str(Path.home() / "Downloads")
            file_path = os.path.join(downloads_path, "VirtualBox-7.0.18-162988-Win.exe")
            
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
                
            messagebox.showinfo("Letöltés sikeres", LANGUAGES[LANGUAGE]["download_virtualbox_success"])
    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{e}")

# Function to download Debian ISO
def download_debian_iso():
    url = 'https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.5.0-amd64-netinst.iso'
    try:
        messagebox.showinfo("Letöltés...", LANGUAGES[LANGUAGE]["download_debian"])
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            downloads_path = str(Path.home() / "Downloads")
            file_path = os.path.join(downloads_path, "debian-12.5.0-amd64-netinst.iso")
            
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
                
            messagebox.showinfo("Letöltés sikeres", LANGUAGES[LANGUAGE]["download_debian_success"])
    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{e}")

# Function to download Kali Linux ISO
def download_kali_iso():
    url = 'https://cdimage.kali.org/kali-2024.2/kali-linux-2024.2-installer-amd64.iso'
    try:
        messagebox.showinfo("Letöltés...", LANGUAGES[LANGUAGE]["download_kali"])
        
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            downloads_path = str(Path.home() / "Downloads")
            file_path = os.path.join(downloads_path, "kali-linux-2024.2-installer-amd64.iso")
            
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
                
            messagebox.showinfo("Letöltés sikeres", LANGUAGES[LANGUAGE]["download_kali_success"])
    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{e}")

# Function to download VS Code installer
def download_vscode_installer():
    try:
        messagebox.showinfo("Letöltés...", LANGUAGES[LANGUAGE]["download_vscode"])

        url = 'https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user'
        file_name = 'VSCodeSetup-x64-1.64.2.exe' 

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            downloads_path = str(Path.home() / "Downloads")
            file_path = os.path.join(downloads_path, file_name)

            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            messagebox.showinfo("Letöltés sikeres", LANGUAGES[LANGUAGE]["download_vscode_success"])
        else:
            messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{response.status_code}")

    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{e}")

# Function to download Git installer
def download_git_installer():
    try:
        messagebox.showinfo("Letöltés...", LANGUAGES[LANGUAGE]["download_git"])

        url = 'https://github.com/git-for-windows/git/releases/download/v2.40.0.windows.1/Git-2.40.0-64-bit.exe'
        file_name = 'Git-2.40.0-64-bit.exe' 

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            downloads_path = str(Path.home() / "Downloads")
            file_path = os.path.join(downloads_path, file_name)

            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            messagebox.showinfo("Letöltés sikeres", LANGUAGES[LANGUAGE]["download_git_success"])
        else:
            messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{response.status_code}")

    except requests.RequestException as e:
        messagebox.showerror("Hiba történt", f"Hiba történt a letöltés közben:\n{e}")

# Function to clear TEMP folder
def clear_temp_folder():
    temp_folder = os.path.join(os.environ['TEMP'])
    
    for filename in os.listdir(temp_folder):
        file_path = os.path.join(temp_folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            # Itt érdemes logolni a hibát, ha szükséges, de ne jeleníts meg hibaüzenetet minden egyes problémás fájlra/könyvtárra
            print(f"Hiba történt a fájl törlése közben {file_path}. Hiba: {e}")
    
    # Ha a nyelv beállítás helyesen van definiálva, akkor itt használható
    if LANGUAGE in LANGUAGES:
        messagebox.showinfo("Sikeres törlés", LANGUAGES[LANGUAGE]["clear_temp_success"])
    else:
        messagebox.showinfo("Sikeres törlés", "Sikeres törlés")  # Alapértelmezett üzenet, ha nincs megfelelő nyelvi beállítás

# Function to display system information in a separate window
def display_system_info_window(system_info):
    dialog = tk.Toplevel()
    dialog.title(LANGUAGES[LANGUAGE]["system_info_title"])

    # Calculate the center position of the screen
    window_width = 800  # Width of the dialog window
    window_height = 600  # Height of the dialog window

    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()

    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)

    dialog.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

    text = scrolledtext.ScrolledText(dialog, wrap="word", height=40, width=100)
    text.insert(tk.END, system_info)
    text.configure(state="disabled")
    text.pack(padx=10, pady=10)

    dialog.transient(root)
    dialog.grab_set()
    root.wait_window(dialog)

# Function to show system information
def show_system_info():
    try:
        uname = platform.uname()
        system_info = f"""
System: {uname.system}
Node Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}
Processor: {uname.processor} \n
"""
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        system_info += f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}\n\n"

        system_info += "=== CPU Information: ===\n"
        system_info += f"Physical cores: {psutil.cpu_count(logical=False)}\n"
        system_info += f"Total cores: {psutil.cpu_count(logical=True)}\n"

        cpufreq = psutil.cpu_freq()
        system_info += f"Max Frequency: {cpufreq.max:.2f}Mhz\n"
        system_info += f"Min Frequency: {cpufreq.min:.2f}Mhz\n"
        system_info += f"Current Frequency: {cpufreq.current:.2f}Mhz\n"

        per_core_usage = psutil.cpu_percent(percpu=True)
        table_headers = ['Core', 'Usage (%)']
        table_data = [[f'Core {i}', f'{usage:.2f}%'] for i, usage in enumerate(per_core_usage)]
        cpu_usage_per_core_str = tabulate(table_data, headers=table_headers, tablefmt='grid')
        system_info += "\nCPU Usage Per Core:\n"
        system_info += cpu_usage_per_core_str + "\n\n"

        svmem = psutil.virtual_memory()
        system_info += "=== Memory Information: ===\n"
        system_info += f"Total: {get_size(svmem.total)}\n"
        system_info += f"Available: {get_size(svmem.available)}\n"
        system_info += f"Used: {get_size(svmem.used)}\n"
        system_info += f"Percentage: {svmem.percent}%\n"

        partitions = psutil.disk_partitions()
        for partition in partitions:
            system_info += f"\n=== Device: {partition.device} ===\n"
            system_info += f"  Mountpoint: {partition.mountpoint}\n"
            system_info += f"  File system type: {partition.fstype}\n"
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                system_info += f"  Total Size: {get_size(partition_usage.total)}\n"
                system_info += f"  Used: {get_size(partition_usage.used)}\n"
                system_info += f"  Free: {get_size(partition_usage.free)}\n"
                system_info += f"  Percentage: {partition_usage.percent}%\n\n"
            except PermissionError:
                continue

        gpus = GPUtil.getGPUs()
        if gpus:
            for gpu in gpus:
                system_info += f"\n=== GPU: {gpu.name} ===\n"
                system_info += f"  Load: {gpu.load * 100}%\n"
                system_info += f"  Free Memory: {get_size(gpu.memoryFree)}\n"
                system_info += f"  Used Memory: {get_size(gpu.memoryUsed)}\n"
                system_info += f"  Total Memory: {get_size(gpu.memoryTotal)}\n"
                system_info += f"  Temperature: {gpu.temperature}°C\n\n"
        else:
            system_info += "No GPU information available.\n\n"

        network_io = psutil.net_io_counters()
        system_info += "=== Network Information: ===\n"
        system_info += f"Data sent: {get_size(network_io.bytes_sent)}\n"
        system_info += f"Data received: {get_size(network_io.bytes_recv)}\n\n"

        display_system_info_window(system_info)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Main window setup
root = tk.Tk()
root.title("Multi-functional App")
root.resizable(False, False)

# Get screen width and height
window_width = 800
window_height = 600

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate position for center alignment
x = (screen_width - window_width) // 1
y = (screen_height - window_height) // 1

style = ttk.Style(root)
style.theme_use("clam")  # Use a default theme

frame_main = ttk.Frame(root, padding="10")
frame_main.grid(column=0, row=0, sticky="nsew")

# Language selection
lbl_language = ttk.Label(frame_main, text="Language:")
lbl_language.grid(column=0, row=0, sticky="w")
combo_language = ttk.Combobox(frame_main, values=list(LANGUAGES.keys()), state="readonly")
combo_language.grid(column=1, row=0, sticky="ew")
combo_language.current(0)
combo_language.bind("<<ComboboxSelected>>", switch_language)

# Creating button frame
frame_buttons = ttk.LabelFrame(frame_main, text="Operations", padding="10")
frame_buttons.grid(column=0, row=1, columnspan=2, pady="10", sticky="nsew")

# Creating buttons
btn_public_ip = ttk.Button(frame_buttons, text="Save Public IP and Identifier", command=show_public_ip_and_save)
btn_public_ip.grid(column=0, row=0, padx="5", pady="5", sticky="ew")

btn_download_virtualbox = ttk.Button(frame_buttons, text="Download VirtualBox (Windows)", command=download_virtualbox_windows_hosts)
btn_download_virtualbox.grid(column=1, row=0, padx="5", pady="5", sticky="ew")

btn_download_debian = ttk.Button(frame_buttons, text="Download Debian (ISO)", command=download_debian_iso)
btn_download_debian.grid(column=0, row=1, padx="5", pady="5", sticky="ew")

btn_download_kali = ttk.Button(frame_buttons, text="Download Kali Linux (ISO)", command=download_kali_iso)
btn_download_kali.grid(column=1, row=1, padx="5", pady="5", sticky="ew")

btn_download_vscode = ttk.Button(frame_buttons, text="Download Visual Studio Code", command=download_vscode_installer)
btn_download_vscode.grid(column=0, row=2, padx="5", pady="5", sticky="ew")

btn_download_git = ttk.Button(frame_buttons, text="Download Git", command=download_git_installer)
btn_download_git.grid(column=1, row=2, padx="5", pady="5", sticky="ew")

btn_clear_temp = ttk.Button(frame_buttons, text="Clear TEMP Folder", command=clear_temp_folder)
btn_clear_temp.grid(column=0, row=3, padx="5", pady="5", sticky="ew")

btn_system_info = ttk.Button(frame_buttons, text="Show System Information", command=show_system_info)
btn_system_info.grid(column=1, row=3, padx="5", pady="5", sticky="ew")

# Set initial language
update_language()

root.mainloop()
