import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
# DATA REKOMENDASI BERDASARKAN BUDGET
# =====================================

data_rekomendasi = {
    "Di bawah Rp3 juta": {
        "nama": "Laptop Bekas Bisnis",
        "harga": "Rp2.000.000 - Rp2.999.000",
        "prosesor": "Intel Core i5 generasi 8 atau setara",
        "ram": "8 GB",
        "storage": "SSD 256 GB",
    },
    "Rp3 juta - Rp5 juta": {
        "nama": "Laptop Pelajar Entry-Level",
        "harga": "Rp3.000.000 - Rp5.000.000",
        "prosesor": "Intel Core i3 atau AMD Ryzen 3",
        "ram": "8 GB",
        "storage": "SSD 256 GB",
    },
    "Rp5 juta - Rp7 juta": {
        "nama": "Laptop Pelajar Menengah",
        "harga": "Rp5.000.000 - Rp7.000.000",
        "prosesor": "Intel Core i5 atau AMD Ryzen 5",
        "ram": "8 GB - 16 GB",
        "storage": "SSD 512 GB",
    },
    "Rp7 juta - Rp10 juta": {
        "nama": "Laptop Produktivitas",
        "harga": "Rp7.000.000 - Rp10.000.000",
        "prosesor": "Intel Core i5 atau AMD Ryzen 5 generasi baru",
        "ram": "16 GB",
        "storage": "SSD 512 GB",
    },
    "Di atas Rp10 juta": {
        "nama": "Laptop Performa Tinggi",
        "harga": "Mulai Rp10.000.000",
        "prosesor": "Intel Core i5/i7 atau AMD Ryzen 5/7 generasi baru",
        "ram": "16 GB - 32 GB",
        "storage": "SSD 512 GB - 1 TB",
    }
}

# =====================================
# DATA KEBUTUHAN PENGGUNA
# =====================================

data_kebutuhan = {
    "Belajar biasa": {
        "kegunaan": "Mengetik tugas, browsing, dan belajar online",
        "saran": "Utamakan laptop yang ringan dan baterai tahan lama."
    },
    "Coding / TKJ": {
        "kegunaan": "Python, VS Code, dan praktikum jaringan",
        "saran": "Disarankan RAM 16 GB untuk multitasking dan virtual machine."
    },
    "Desain grafis": {
        "kegunaan": "Desain poster, logo, dan pengeditan gambar",
        "saran": "Pilih layar berkualitas dan RAM yang memadai."
    },
    "Editing video": {
        "kegunaan": "Mengedit video dan membuat konten",
        "saran": "Utamakan prosesor kuat, RAM besar, dan GPU sesuai kebutuhan."
    }
}

# =====================================
# DATA MEREK DAN MODEL LAPTOP (PERTEMUAN 2)
# Harga di bawah hanya contoh untuk latihan.
# =====================================

data_laptop = [
    {
        "merek": "ASUS",
        "model": "Vivobook 14",
        "harga": 7500000,
        "processor": "Intel Core i5",
        "ram": "8 GB"
    },
    {
        "merek": "Acer",
        "model": "Aspire 5",
        "harga": 8000000,
        "processor": "Intel Core i5",
        "ram": "8 GB"
    },
    {
        "merek": "Lenovo",
        "model": "IdeaPad Slim 3",
        "harga": 7000000,
        "processor": "AMD Ryzen 5",
        "ram": "8 GB"
    },
    {
        "merek": "HP",
        "model": "Pavilion 14",
        "harga": 8500000,
        "processor": "Intel Core i5",
        "ram": "16 GB"
    }
]


def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


# =====================================
# FUNGSI REKOMENDASI LAPTOP
# =====================================

def tampilkan_rekomendasi():
    budget = pilihan_budget.get()
    kebutuhan = pilihan_kebutuhan.get()

    if not budget or not kebutuhan:
        messagebox.showwarning(
            "Peringatan",
            "Pilih budget dan kebutuhan terlebih dahulu!"
        )
        return

    laptop = data_rekomendasi[budget]
    tujuan = data_kebutuhan[kebutuhan]

    hasil.delete("1.0", tk.END)
    hasil.insert(tk.END, "HASIL REKOMENDASI LAPTOP\n")
    hasil.insert(tk.END, "=" * 42 + "\n\n")
    hasil.insert(tk.END, f"Kategori     : {laptop['nama']}\n")
    hasil.insert(tk.END, f"Budget       : {laptop['harga']}\n")
    hasil.insert(tk.END, f"Kebutuhan    : {kebutuhan}\n\n")
    hasil.insert(tk.END, "SPESIFIKASI YANG DISARANKAN\n")
    hasil.insert(tk.END, "-" * 42 + "\n")
    hasil.insert(tk.END, f"Prosesor     : {laptop['prosesor']}\n")
    hasil.insert(tk.END, f"RAM          : {laptop['ram']}\n")
    hasil.insert(tk.END, f"Penyimpanan  : {laptop['storage']}\n\n")
    hasil.insert(tk.END, "KEGUNAAN\n")
    hasil.insert(tk.END, "-" * 42 + "\n")
    hasil.insert(tk.END, tujuan["kegunaan"] + "\n\n")
    hasil.insert(tk.END, "TIPS MEMBELI\n")
    hasil.insert(tk.END, "-" * 42 + "\n")
    hasil.insert(tk.END, tujuan["saran"] + "\n\n")
    hasil.insert(
        tk.END,
        "Catatan: Harga dan spesifikasi merupakan perkiraan.\n"
        "Periksa harga, kondisi, dan spesifikasi produk terbaru."
    )


def reset_pilihan():
    pilihan_budget.set("Rp3 juta - Rp5 juta")
    pilihan_kebutuhan.set("Coding / TKJ")
    hasil.delete("1.0", tk.END)


# =====================================
# FUNGSI MENAMPILKAN DATA LAPTOP
# =====================================

def tampilkan_data_laptop():
    for widget in daftar_frame.winfo_children():
        widget.destroy()

    for laptop in data_laptop:
        kartu = tk.Frame(
            daftar_frame,
            bg="white",
            bd=1,
            relief="solid",
            padx=14,
            pady=10
        )
        kartu.pack(fill="x", padx=12, pady=7)

        tk.Label(
            kartu,
            text=f"{laptop['merek']} - {laptop['model']}",
            font=("Arial", 12, "bold"),
            bg="white",
            fg="#17365D",
            anchor="w"
        ).pack(fill="x")

        detail = (
            f"Harga       : {format_rupiah(laptop['harga'])}\n"
            f"Processor : {laptop['processor']}\n"
            f"RAM          : {laptop['ram']}"
        )

        tk.Label(
            kartu,
            text=detail,
            font=("Arial", 10),
            bg="white",
            fg="#333333",
            justify="left",
            anchor="w"
        ).pack(fill="x", pady=(5, 0))


# =====================================
# MEMBUAT JENDELA APLIKASI
# =====================================

root = tk.Tk()
root.title("Aplikasi Rekomendasi Laptop - Projek TKJ")
root.geometry("760x700")
root.minsize(620, 580)
root.configure(bg="#eef3f8")

judul = tk.Label(
    root,
    text="APLIKASI REKOMENDASI LAPTOP",
    font=("Arial", 20, "bold"),
    bg="#17365d",
    fg="white",
    pady=15
)
judul.pack(fill="x")

subjudul = tk.Label(
    root,
    text="Projek TKJ | Pilih laptop sesuai budget dan kebutuhan",
    font=("Arial", 10),
    bg="#17365d",
    fg="white",
    pady=0
)
subjudul.pack(fill="x", pady=(0, 12))

# Tab untuk memisahkan fitur Pertemuan 1 dan Pertemuan 2
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=10)

tab_rekomendasi = tk.Frame(notebook, bg="#eef3f8")
tab_daftar = tk.Frame(notebook, bg="#eef3f8")

notebook.add(tab_rekomendasi, text="Pertemuan 1 - Rekomendasi")
notebook.add(tab_daftar, text="Pertemuan 2 - Data Laptop")

# =====================================
# ISI TAB PERTEMUAN 1
# =====================================

tk.Label(
    tab_rekomendasi,
    text="Pilih laptop sesuai budget dan kebutuhanmu",
    font=("Arial", 11),
    bg="#eef3f8",
    fg="#475569"
).pack(pady=(18, 12))

frame_pilihan = tk.Frame(tab_rekomendasi, bg="#eef3f8")
frame_pilihan.pack(pady=5)

tk.Label(
    frame_pilihan,
    text="Budget:",
    font=("Arial", 11, "bold"),
    bg="#eef3f8"
).grid(row=0, column=0, sticky="w", padx=8, pady=8)

pilihan_budget = ttk.Combobox(
    frame_pilihan,
    values=list(data_rekomendasi.keys()),
    state="readonly",
    width=30,
    font=("Arial", 10)
)
pilihan_budget.grid(row=0, column=1, padx=8, pady=8)
pilihan_budget.set("Rp3 juta - Rp5 juta")

tk.Label(
    frame_pilihan,
    text="Kebutuhan:",
    font=("Arial", 11, "bold"),
    bg="#eef3f8"
).grid(row=1, column=0, sticky="w", padx=8, pady=8)

pilihan_kebutuhan = ttk.Combobox(
    frame_pilihan,
    values=list(data_kebutuhan.keys()),
    state="readonly",
    width=30,
    font=("Arial", 10)
)
pilihan_kebutuhan.grid(row=1, column=1, padx=8, pady=8)
pilihan_kebutuhan.set("Coding / TKJ")

frame_tombol = tk.Frame(tab_rekomendasi, bg="#eef3f8")
frame_tombol.pack(pady=12)

tk.Button(
    frame_tombol,
    text="Tampilkan Rekomendasi",
    command=tampilkan_rekomendasi,
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    font=("Arial", 11, "bold"),
    padx=12,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

tk.Button(
    frame_tombol,
    text="Reset",
    command=reset_pilihan,
    font=("Arial", 11),
    padx=15,
    pady=8,
    cursor="hand2"
).pack(side="left", padx=5)

frame_hasil = tk.Frame(tab_rekomendasi, bg="#eef3f8")
frame_hasil.pack(fill="both", expand=True, padx=18, pady=(5, 18))

hasil = tk.Text(
    frame_hasil,
    font=("Consolas", 10),
    wrap="word",
    padx=12,
    pady=12,
    height=16,
    bg="white",
    fg="#1e293b",
    relief="solid",
    borderwidth=1
)
hasil.pack(fill="both", expand=True)

# =====================================
# ISI TAB PERTEMUAN 2
# =====================================

tk.Label(
    tab_daftar,
    text=f"DAFTAR MEREK DAN MODEL LAPTOP ({len(data_laptop)} DATA)",
    font=("Arial", 13, "bold"),
    bg="#eef3f8",
    fg="#17365d"
).pack(anchor="w", padx=15, pady=(15, 8))

area = tk.Frame(tab_daftar, bg="#eef3f8")
area.pack(fill="both", expand=True, padx=8, pady=(0, 8))

canvas = tk.Canvas(area, bg="#eef3f8", highlightthickness=0)
scrollbar = ttk.Scrollbar(area, orient="vertical", command=canvas.yview)
daftar_frame = tk.Frame(canvas, bg="#eef3f8")

daftar_frame.bind(
    "<Configure>",
    lambda event: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas_window = canvas.create_window(
    (0, 0),
    window=daftar_frame,
    anchor="nw"
)

def sesuaikan_lebar(event):
    canvas.itemconfigure(canvas_window, width=event.width)

canvas.bind("<Configure>", sesuaikan_lebar)
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

tk.Button(
    tab_daftar,
    text="Muat Ulang Daftar",
    command=tampilkan_data_laptop,
    font=("Arial", 10, "bold"),
    bg="#2874a6",
    fg="white",
    activebackground="#1b4f72",
    activeforeground="white",
    relief="flat",
    padx=14,
    pady=8
).pack(pady=(0, 12))

# TAMPILKAN DATA SAAT APLIKASI DIBUKA
tampilkan_data_laptop()

# MENJALANKAN APLIKASI
root.mainloop()