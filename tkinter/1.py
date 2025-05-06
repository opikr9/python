import os
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
os.system("cls")

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("300x200")
window.resizable(False,False)
window.title("Opik GUI")
# varFungsi
NAMADEPAN = tk.StringVar()
NAMABELAKANG = tk.StringVar()

def tombolClick():
    # print("hola")
    '''fungsi dipanggil oleh tombol'''
    pesan = f"Halo {NAMADEPAN.get()} {NAMABELAKANG.get()} done"
    showinfo(title="p",message=pesan)

# frame input
inputFrame = ttk.Frame(window)

# penempatan grid,pack,place
inputFrame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen2
# 1. label nama depan
namaDepanLabel = ttk.Label(inputFrame,text="Nama Depan: ")
namaDepanLabel.pack(padx=10,fill="x",expand=True)
#2. entry nama depan
namaDepanEntry = ttk.Entry(inputFrame,textvariable=NAMADEPAN)
namaDepanEntry.pack(padx=10,fill="x",expand=True)

# 3. label nama belakang
namaBelakangLabel = ttk.Label(inputFrame,text="Nama Belakang: ")
namaBelakangLabel.pack(padx=10,fill="x",expand=True)
#4. entry nama belakang
namaBelakangEntry = ttk.Entry(inputFrame,textvariable=NAMABELAKANG)
namaBelakangEntry.pack(padx=10,fill="x",expand=True)

# 5. Tombol


tombolSapa = ttk.Button(inputFrame,text="Sapa!",command=tombolClick)
tombolSapa.pack(fill='x',expand=True,padx=10,pady=10)

# main loop
window.mainloop()