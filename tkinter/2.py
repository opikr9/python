import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# display
window = tk.Tk()
# window.config(bg="yellow")
window.configure(bg="white")
window.resizable(False,False)
window.geometry("300x200")
window.title("Kenalan!")


# Fungsi
NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()

def tombol_click():
    pesan = f"Halo {NAMADEPAN.get()} {NAMABELAKANG.get()} Adios"
    showinfo(title="p",message=pesan)
    
# frame input
frame_input = ttk.Frame(window)
frame_input.pack(padx=10,pady=10,fill="x",expand=True)

# 1. label nama depan
label_nama_depan = ttk.Label(frame_input,text="Nama Depan")
label_nama_depan.pack(fill="x",expand=True)

# 2. input nama depan
input_nama_depan = ttk.Entry(frame_input,textvariable=NAMADEPAN)
input_nama_depan.pack(fill="x",expand=True)

# 3. label nama belakang
label_nama_belakang = ttk.Label(frame_input,text="Nama Belakang")
label_nama_belakang.pack(fill="x",expand=True)

# 4. input nama belakang
input_nama_belakang = ttk.Entry(frame_input,textvariable=NAMABELAKANG)
input_nama_belakang.pack(fill="x",expand=True)


# 5. tombol sapa
tombol_sapa = ttk.Button(frame_input,text="Sapa!",command=tombol_click)
tombol_sapa.pack(padx=10,pady=10,expand=True,fill="x")

# mainloop
window.mainloop()