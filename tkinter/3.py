import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Sapa!")

# fungsi
NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()

def tombol_click():
    pesan = f"Halo {NAMADEPAN.get()} {NAMABELAKANG.get()} Adios)"
    showinfo(title="hola",message=pesan)

# input frame
input_frame = ttk.Frame()
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# 1. label nama depan
label_nama_depan = ttk.Label(input_frame,text="Nama Depan")
label_nama_depan.pack(fill="x",expand=True)

# 2. input nama depan
input_nama_depan = ttk.Entry(input_frame,textvariable=NAMADEPAN)
input_nama_depan.pack(fill="x",expand=True)

# 3. label nama belakang
label_nama_belakang = ttk.Label(input_frame,text="Nama Belakang")
label_nama_belakang.pack(fill="x",expand=True)

# 4. input nama depan
input_nama_belakang = ttk.Entry(input_frame,textvariable=NAMABELAKANG)
input_nama_belakang.pack(fill="x",expand=True)

# 5.tombol sapa
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(padx=10,pady=10,expand=True,fill="x")

# looping window
window.mainloop()