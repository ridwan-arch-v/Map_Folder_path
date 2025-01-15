import os
import pyperclip
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from tkinter import ttk

def simpan_status_tutorial(status):
    with open("tutorial_status.txt", "w") as file:
        file.write(str(status))

def baca_status_tutorial():
    if os.path.exists("tutorial_status.txt"):
        with open("tutorial_status.txt", "r") as file:
            status = file.read().strip()
            return status == "True"
    return False

def tampilkan_tutorial(root, tutorial_selesai_callback):
    tutorial_text = (
        "Selamat datang di aplikasi Struktur Folder Logger!\n\n"
        "Dengan aplikasi ini, Anda dapat memilih folder untuk dianalisis.\n"
        "Struktur folder dan file akan ditampilkan di jendela aplikasi dan disalin ke clipboard.\n\n"
        "Setelah selesai, aplikasi akan menyimpan hasil struktur folder ke dalam file log."
    )
    
    def lanjutkan_tutorial():
        simpan_status_tutorial(True)
        tutorial_window.destroy()  
        tutorial_selesai_callback()

    tutorial_window = tk.Toplevel(root)
    tutorial_window.title("Tutorial")
    tutorial_window.geometry("400x300")
    tutorial_window.config(bg="#f4f4f9")  
    label_tutorial = tk.Label(tutorial_window, text=tutorial_text, justify=tk.LEFT, font=("Helvetica", 12), bg="#f4f4f9")
    label_tutorial.pack(pady=20, padx=20)
    tombol_lanjutkan = tk.Button(tutorial_window, text="Lanjutkan", command=lanjutkan_tutorial, font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
    tombol_lanjutkan.pack(pady=10)
    tombol_tidak = tk.Button(tutorial_window, text="Tidak, Terima Kasih", command=lambda: tutorial_window.destroy(), font=("Helvetica", 12), bg="#f44336", fg="white", relief="flat")
    tombol_tidak.pack(pady=5)

def tanyakan_ulang_tutorial(root, lanjutkan_tutorial_callback):
    if messagebox.askyesno("Tutorial Lagi?", "Apakah Anda ingin melihat tutorial lagi?"):
        lanjutkan_tutorial_callback()

def salin_dan_simpan_log_ke_app(path_induk, output_text_widget):
    if not os.path.isdir(path_induk):
        messagebox.showerror("Error", f"Path '{path_induk}' tidak valid atau bukan folder.")
        return
    
    nama_project = os.path.basename(path_induk)
    nama_log = f"struktur_{nama_project}.txt"
    log_path = os.path.join(os.path.dirname(__file__), nama_log)
    
    def proses_folder(path, indent=0, is_last=False):
        items = os.listdir(path)
        folders = [item for item in items if os.path.isdir(os.path.join(path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(path, item))]
        
        for idx, folder in enumerate(folders):            
            if idx == len(folders) - 1:
                output_text_widget.insert(tk.END, f"{'|  ' * indent}└── {folder}/\n")
                output_text_widget.yview(tk.END)  
                proses_folder(os.path.join(path, folder), indent + 1, True)
            else:
                output_text_widget.insert(tk.END, f"{'|  ' * indent}├── {folder}/\n")
                output_text_widget.yview(tk.END)  
                proses_folder(os.path.join(path, folder), indent + 1, False)
        
        for idx, file in enumerate(files):
            output_text_widget.insert(tk.END, f"{'|  ' * indent}├── {file}\n")
            output_text_widget.yview(tk.END)  

    output_text_widget.insert(tk.END, f"{nama_project}/\n")
    output_text_widget.yview(tk.END)  
    proses_folder(path_induk, 1, False)

    with open(log_path, 'w', encoding='utf-8') as log_file:
        log_file.write(f"{nama_project}/\n")
        output_text_widget.delete('1.0', tk.END)  
        output_text_widget.insert(tk.END, f"{nama_project}/\n")  
        proses_folder(path_induk, 1, False)

    with open(log_path, 'r', encoding='utf-8') as log_file:
        log_content = log_file.read()

    pyperclip.copy(log_content)      
    messagebox.showinfo("Sukses", f"Struktur folder telah disalin ke clipboard dan disimpan di {log_path}")

def pilih_folder(output_text_widget):
    path_induk = filedialog.askdirectory()  
    if path_induk:
        salin_dan_simpan_log_ke_app(path_induk, output_text_widget)

root = tk.Tk()
root.title("Struktur Folder Logger")
root.geometry("700x500")
root.config(bg="#f4f4f9")  

label = tk.Label(root, text="Pilih folder untuk menganalisis strukturnya:", font=("Helvetica", 14), bg="#f4f4f9")
label.pack(pady=10)

tutorial_selesai = baca_status_tutorial()

if not tutorial_selesai:
    tampilkan_tutorial(root, lambda: pilih_folder(output_text))  

button = tk.Button(root, text="Pilih Folder", command=lambda: pilih_folder(output_text), font=("Helvetica", 12), bg="#4CAF50", fg="white", relief="flat")
button.pack(pady=20)
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=15, font=("Courier New", 10), bg="#ffffff", fg="#333333", relief="flat")
output_text.pack(pady=10)

root.mainloop()
