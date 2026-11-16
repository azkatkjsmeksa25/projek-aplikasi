import tkinter as tk
from tkinter import ttk, messagebox

# =====================================
# DATA REKOMENDASI PERTEMUAN 1
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
# DATA LAPTOP PERTEMUAN 2
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

# =====================================
# FUNGSI FORMAT RUPIAH
# =====================================

def format_rupiah(angka):
    return "Rp" + f"{angka:,}".replace(",", ".")


# =====================================
# FUNGSI PERTEMUAN 1
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
        "Catatan: Harga dan spesifikasi merupakan perkiraan."
    )


def reset_pilihan():
    pilihan_budget.set("Rp3 juta - Rp5 juta")
    pilihan_kebutuhan.set("Coding / TKJ")
    hasil.delete("1.0", tk.END)


# =====================================
# FUNGSI PERTEMUAN 2
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
            f"Processor   : {laptop['processor']}\n"
            f"RAM         : {laptop['ram']}"
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
# FUNGSI PERTEMUAN 3
# PENCARIAN LAPTOP
# =====================================

def cari_laptop():
    kata_kunci = entry_cari.get().lower().strip()
    budget = pilihan_filter.get()

    if not kata_kunci and budget == "Semua Budget":
        hasil_cari.delete("1.0", tk.END)
        hasil_cari.insert(
            tk.END,
            "Masukkan merek/model atau pilih budget untuk mencari laptop."
        )
        return

    hasil_filter = []

    for laptop in data_laptop:

        cocok_kata = (
            kata_kunci in laptop["merek"].lower()
            or kata_kunci in laptop["model"].lower()
            or kata_kunci in laptop["processor"].lower()
        )

        cocok_budget = True

        if budget == "Di bawah Rp3 juta":
            cocok_budget = laptop["harga"] < 3000000

        elif budget == "Rp3 juta - Rp5 juta":
            cocok_budget = 3000000 <= laptop["harga"] <= 5000000

        elif budget == "Rp5 juta - Rp7 juta":
            cocok_budget = 5000000 < laptop["harga"] <= 7000000

        elif budget == "Rp7 juta - Rp10 juta":
            cocok_budget = 7000000 < laptop["harga"] <= 10000000

        elif budget == "Di atas Rp10 juta":
            cocok_budget = laptop["harga"] > 10000000

        if cocok_kata and cocok_budget:
            hasil_filter.append(laptop)

    hasil_cari.delete("1.0", tk.END)

    hasil_cari.insert(tk.END, "HASIL PENCARIAN LAPTOP\n")
    hasil_cari.insert(tk.END, "=" * 42 + "\n\n")

    if hasil_filter:

        hasil_cari.insert(
            tk.END,
            f"Ditemukan {len(hasil_filter)} laptop.\n\n"
        )

        for nomor, laptop in enumerate(hasil_filter, start=1):

            hasil_cari.insert(
                tk.END,
                f"{nomor}. {laptop['merek']} - {laptop['model']}\n"
            )

            hasil_cari.insert(
                tk.END,
                f"   Harga     : {format_rupiah(laptop['harga'])}\n"
            )

            hasil_cari.insert(
                tk.END,
                f"   Prosesor  : {laptop['processor']}\n"
            )

            hasil_cari.insert(
                tk.END,
                f"   RAM       : {laptop['ram']}\n\n"
            )

    else:
        hasil_cari.insert(
            tk.END,
            "Laptop tidak ditemukan.\n"
            "Silakan ubah kata kunci atau budget."
        )


def reset_pencarian():
    entry_cari.delete(0, tk.END)
    pilihan_filter.set("Semua Budget")
    hasil_cari.delete("1.0", tk.END)


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
    text="Projek TKJ | Rekomendasi, Data, dan Pencarian Laptop",
    font=("Arial", 10),
    bg="#17365d",
    fg="white"
)
subjudul.pack(fill="x", pady=(0, 12))


# =====================================
# MEMBUAT TAB
# =====================================

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=15, pady=10)

tab_rekomendasi = tk.Frame(notebook, bg="#eef3f8")
tab_daftar = tk.Frame(notebook, bg="#eef3f8")
tab_pencarian = tk.Frame(notebook, bg="#eef3f8")

notebook.add(tab_rekomendasi, text="Pertemuan 1 - Rekomendasi")
notebook.add(tab_daftar, text="Pertemuan 2 - Data Laptop")
notebook.add(tab_pencarian, text="Pertemuan 3 - Pencarian")


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
    width=30
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
    width=30
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
    font=("Arial", 11, "bold"),
    padx=12,
    pady=8
).pack(side="left", padx=5)

tk.Button(
    frame_tombol,
    text="Reset",
    command=reset_pilihan,
    padx=15,
    pady=8
).pack(side="left", padx=5)

frame_hasil = tk.Frame(tab_rekomendasi, bg="#eef3f8")
frame_hasil.pack(fill="both", expand=True, padx=18, pady=10)

hasil = tk.Text(
    frame_hasil,
    font=("Consolas", 10),
    wrap="word",
    padx=12,
    pady=12,
    bg="white",
    fg="#1e293b"
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
area.pack(fill="both", expand=True, padx=8, pady=8)

canvas = tk.Canvas(
    area,
    bg="#eef3f8",
    highlightthickness=0
)

scrollbar = ttk.Scrollbar(
    area,
    orient="vertical",
    command=canvas.yview
)

daftar_frame = tk.Frame(canvas, bg="#eef3f8")

daftar_frame.bind(
    "<Configure>",
    lambda event: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
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
    bg="#2874a6",
    fg="white",
    padx=14,
    pady=8
).pack(pady=(0, 12))


# =====================================
# ISI TAB PERTEMUAN 3
# =====================================

tk.Label(
    tab_pencarian,
    text="CARI LAPTOP YANG KAMU INGINKAN",
    font=("Arial", 15, "bold"),
    bg="#eef3f8",
    fg="#17365d"
).pack(pady=(20, 15))

tk.Label(
    tab_pencarian,
    text="Masukkan merek, model, atau prosesor laptop:",
    font=("Arial", 10),
    bg="#eef3f8"
).pack()

entry_cari = tk.Entry(
    tab_pencarian,
    font=("Arial", 12),
    width=38,
    relief="solid",
    bd=1
)
entry_cari.pack(pady=10, ipady=6)

tk.Label(
    tab_pencarian,
    text="Filter berdasarkan budget:",
    font=("Arial", 10, "bold"),
    bg="#eef3f8"
).pack(pady=(8, 4))

pilihan_filter = ttk.Combobox(
    tab_pencarian,
    values=[
        "Semua Budget",
        "Di bawah Rp3 juta",
        "Rp3 juta - Rp5 juta",
        "Rp5 juta - Rp7 juta",
        "Rp7 juta - Rp10 juta",
        "Di atas Rp10 juta"
    ],
    state="readonly",
    width=30
)
pilihan_filter.pack(pady=5)
pilihan_filter.set("Semua Budget")

frame_tombol_cari = tk.Frame(
    tab_pencarian,
    bg="#eef3f8"
)
frame_tombol_cari.pack(pady=12)

tk.Button(
    frame_tombol_cari,
    text="Cari Laptop",
    command=cari_laptop,
    bg="#2563eb",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=20,
    pady=8
).pack(side="left", padx=5)

tk.Button(
    frame_tombol_cari,
    text="Reset",
    command=reset_pencarian,
    font=("Arial", 11),
    padx=20,
    pady=8
).pack(side="left", padx=5)

frame_hasil_cari = tk.Frame(
    tab_pencarian,
    bg="#eef3f8"
)
frame_hasil_cari.pack(
    fill="both",
    expand=True,
    padx=18,
    pady=10
)

hasil_cari = tk.Text(
    frame_hasil_cari,
    font=("Consolas", 10),
    wrap="word",
    padx=12,
    pady=12,
    bg="white",
    fg="#1e293b"
)
hasil_cari.pack(fill="both", expand=True)

hasil_cari.insert(
    tk.END,
    "Silakan masukkan merek atau model laptop,\n"
    "kemudian tekan tombol Cari Laptop."
)


# =====================================
# MENJALANKAN APLIKASI
# =====================================

tampilkan_data_laptop()

root.mainloop()