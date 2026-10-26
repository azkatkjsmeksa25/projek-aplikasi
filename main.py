import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
# DATA REKOMENDASI LAPTOP
# =====================================

data_laptop = {
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
# FUNGSI MENAMPILKAN REKOMENDASI
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

    laptop = data_laptop[budget]
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
# MEMBUAT TAMPILAN APLIKASI (GUI)
# =====================================

root = tk.Tk()
root.title("Rekomendasi Laptop untuk Belajar")
root.geometry("720x650")
root.minsize(600, 580)
root.configure(bg="#eef3f8")

# Judul
judul = tk.Label(
    root,
    text="REKOMENDASI LAPTOP",
    font=("Arial", 21, "bold"),
    bg="#eef3f8",
    fg="#17365d"
)
judul.pack(pady=(20, 5))

subjudul = tk.Label(
    root,
    text="Pilih laptop sesuai budget dan kebutuhanmu",
    font=("Arial", 11),
    bg="#eef3f8",
    fg="#475569"
)
subjudul.pack(pady=(0, 18))

# Frame pilihan
frame_pilihan = tk.Frame(root, bg="#eef3f8")
frame_pilihan.pack(pady=5)

# Pilihan budget
tk.Label(
    frame_pilihan,
    text="Budget:",
    font=("Arial", 11, "bold"),
    bg="#eef3f8"
).grid(row=0, column=0, sticky="w", padx=8, pady=8)

pilihan_budget = ttk.Combobox(
    frame_pilihan,
    values=list(data_laptop.keys()),
    state="readonly",
    width=27,
    font=("Arial", 10)
)
pilihan_budget.grid(row=0, column=1, padx=8, pady=8)
pilihan_budget.set("Rp3 juta - Rp5 juta")

# Pilihan kebutuhan
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
    width=27,
    font=("Arial", 10)
)
pilihan_kebutuhan.grid(row=1, column=1, padx=8, pady=8)
pilihan_kebutuhan.set("Coding / TKJ")

# Tombol
frame_tombol = tk.Frame(root, bg="#eef3f8")
frame_tombol.pack(pady=12)

tombol_rekomendasi = tk.Button(
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
)
tombol_rekomendasi.pack(side="left", padx=5)

tombol_reset = tk.Button(
    frame_tombol,
    text="Reset",
    command=reset_pilihan,
    font=("Arial", 11),
    padx=15,
    pady=8,
    cursor="hand2"
)
tombol_reset.pack(side="left", padx=5)

# Kotak hasil
frame_hasil = tk.Frame(root, bg="#eef3f8")
frame_hasil.pack(fill="both", expand=True, padx=20, pady=(5, 20))

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

# Menjalankan aplikasi
root.mainloop()