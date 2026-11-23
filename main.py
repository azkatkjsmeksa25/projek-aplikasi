import tkinter as tk
from tkinter import ttk, messagebox


# =========================
# DATA LAPTOP
# =========================

daftar_laptop = [
    {
        "nama": "ASUS Vivobook Go 14",
        "harga": 4500000,
        "processor": "AMD Ryzen 3",
        "ram": "8 GB",
        "storage": "256 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding"],
        "deskripsi": "Cocok untuk belajar, tugas sekolah, dan coding ringan."
    },
    {
        "nama": "Acer Aspire Lite",
        "harga": 5000000,
        "processor": "Intel Core i3",
        "ram": "8 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding"],
        "deskripsi": "Cocok untuk tugas sekolah dan kegiatan sehari-hari."
    },
    {
        "nama": "Lenovo IdeaPad Slim 3",
        "harga": 6000000,
        "processor": "AMD Ryzen 5",
        "ram": "8 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding"],
        "deskripsi": "Cocok untuk multitasking dan pemrograman."
    },
    {
        "nama": "ASUS Vivobook 15",
        "harga": 7000000,
        "processor": "Intel Core i5",
        "ram": "16 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding", "desain"],
        "deskripsi": "Cocok untuk coding dan desain ringan."
    },
    {
        "nama": "Acer Aspire 5",
        "harga": 7500000,
        "processor": "Intel Core i5",
        "ram": "16 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding", "desain"],
        "deskripsi": "Cocok untuk belajar TKJ, multitasking, dan desain ringan."
    },
    {
        "nama": "Lenovo IdeaPad Slim 5",
        "harga": 8500000,
        "processor": "AMD Ryzen 5",
        "ram": "16 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding", "desain"],
        "deskripsi": "Cocok untuk pekerjaan sekolah dan aplikasi produktivitas."
    },
    {
        "nama": "ASUS Vivobook S",
        "harga": 9500000,
        "processor": "AMD Ryzen 7",
        "ram": "16 GB",
        "storage": "512 GB SSD",
        "gpu": "Integrated Graphics",
        "kebutuhan": ["umum", "coding", "desain"],
        "deskripsi": "Cocok untuk multitasking dan pekerjaan yang lebih berat."
    },
    {
        "nama": "Acer Aspire 7",
        "harga": 10500000,
        "processor": "Intel Core i7",
        "ram": "16 GB",
        "storage": "1 TB SSD",
        "gpu": "NVIDIA GeForce RTX",
        "kebutuhan": ["umum", "coding", "desain", "editing"],
        "deskripsi": "Cocok untuk desain grafis dan editing."
    },
    {
        "nama": "Lenovo LOQ",
        "harga": 12000000,
        "processor": "Intel Core i5",
        "ram": "16 GB",
        "storage": "512 GB SSD",
        "gpu": "NVIDIA GeForce RTX",
        "kebutuhan": ["coding", "desain", "editing"],
        "deskripsi": "Cocok untuk editing, desain, dan aplikasi berat."
    },
    {
        "nama": "ASUS TUF Gaming",
        "harga": 14000000,
        "processor": "AMD Ryzen 7",
        "ram": "16 GB",
        "storage": "1 TB SSD",
        "gpu": "NVIDIA GeForce RTX",
        "kebutuhan": ["coding", "desain", "editing"],
        "deskripsi": "Cocok untuk editing video dan pekerjaan grafis."
    },
    {
        "nama": "Acer Nitro",
        "harga": 15000000,
        "processor": "Intel Core i7",
        "ram": "16 GB",
        "storage": "1 TB SSD",
        "gpu": "NVIDIA GeForce RTX",
        "kebutuhan": ["coding", "desain", "editing"],
        "deskripsi": "Cocok untuk editing video dan penggunaan aplikasi berat."
    },
    {
        "nama": "Lenovo Legion",
        "harga": 18000000,
        "processor": "AMD Ryzen 7",
        "ram": "32 GB",
        "storage": "1 TB SSD",
        "gpu": "NVIDIA GeForce RTX",
        "kebutuhan": ["coding", "desain", "editing"],
        "deskripsi": "Cocok untuk multitasking berat dan pekerjaan kreatif."
    }
]


# =========================
# PENGATURAN BUDGET
# =========================

pilihan_budget = {
    "Rp3 - 5 juta": (3000000, 5000000),
    "Rp5 - 7 juta": (5000000, 7000000),
    "Rp7 - 9 juta": (7000000, 9000000),
    "Rp9 - 12 juta": (9000000, 12000000),
    "Rp12 juta ke atas": (12000000, 999999999)
}

pilihan_kebutuhan = {
    "Belajar biasa": "umum",
    "Coding / TKJ": "coding",
    "Desain grafis": "desain",
    "Editing video": "editing"
}


# =========================
# FUNGSI BANTU
# =========================

def format_rupiah(nominal):
    return "Rp{:,.0f}".format(nominal).replace(",", ".")


def cari_laptop(nama):
    for laptop in daftar_laptop:
        if laptop["nama"] == nama:
            return laptop
    return None


def tampilkan_text(widget, isi):
    widget.config(state="normal")
    widget.delete("1.0", tk.END)
    widget.insert(tk.END, isi)
    widget.config(state="disabled")


# =========================
# FUNGSI REKOMENDASI
# =========================

def rekomendasikan_laptop():
    budget = combo_budget.get()
    kebutuhan = combo_kebutuhan.get()

    if not budget or not kebutuhan:
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih budget dan kebutuhan terlebih dahulu."
        )
        return

    batas_min, batas_max = pilihan_budget[budget]
    kategori = pilihan_kebutuhan[kebutuhan]

    hasil = []

    for laptop in daftar_laptop:
        if batas_min <= laptop["harga"] <= batas_max:
            if kategori in laptop["kebutuhan"]:
                hasil.append(laptop)

    if not hasil:
        tampilkan_text(
            output_rekomendasi,
            "Maaf, laptop yang sesuai belum ditemukan.\n"
            "Silakan pilih budget atau kebutuhan lainnya."
        )
        return

    hasil.sort(key=lambda x: x["harga"])

    teks = "HASIL REKOMENDASI LAPTOP\n"
    teks += "=" * 40 + "\n\n"
    teks += f"Budget: {budget}\n"
    teks += f"Kebutuhan: {kebutuhan}\n"
    teks += f"Jumlah laptop ditemukan: {len(hasil)}\n\n"

    for nomor, laptop in enumerate(hasil, start=1):
        teks += f"{nomor}. {laptop['nama']}\n"
        teks += f"Harga: {format_rupiah(laptop['harga'])}\n"
        teks += f"Processor: {laptop['processor']}\n"
        teks += f"RAM: {laptop['ram']}\n"
        teks += f"Storage: {laptop['storage']}\n"
        teks += f"GPU: {laptop['gpu']}\n"
        teks += f"Keterangan: {laptop['deskripsi']}\n"
        teks += "-" * 40 + "\n"

    tampilkan_text(output_rekomendasi, teks)


# =========================
# FUNGSI PERBANDINGAN
# =========================

def bandingkan_laptop():
    nama1 = combo_laptop1.get()
    nama2 = combo_laptop2.get()

    if not nama1 or not nama2:
        messagebox.showwarning(
            "Peringatan",
            "Silakan pilih kedua laptop yang ingin dibandingkan."
        )
        return

    if nama1 == nama2:
        messagebox.showwarning(
            "Peringatan",
            "Pilih dua laptop yang berbeda untuk dibandingkan."
        )
        return

    pilihan_laptop1 = cari_laptop(nama1)
    pilihan_laptop2 = cari_laptop(nama2)

    if pilihan_laptop1 is None or pilihan_laptop2 is None:
        messagebox.showerror(
            "Error",
            "Data laptop tidak ditemukan."
        )
        return

    hasil_perbandingan = (
        "HASIL PERBANDINGAN LAPTOP\n"
        + "=" * 55 + "\n\n"
        + f"{pilihan_laptop1['nama']}\n"
        + f"Harga: {format_rupiah(pilihan_laptop1['harga'])}\n"
        + f"Processor: {pilihan_laptop1['processor']}\n"
        + f"RAM: {pilihan_laptop1['ram']}\n"
        + f"Storage: {pilihan_laptop1['storage']}\n"
        + f"GPU: {pilihan_laptop1['gpu']}\n\n"
        + "-" * 55 + "\n\n"
        + f"{pilihan_laptop2['nama']}\n"
        + f"Harga: {format_rupiah(pilihan_laptop2['harga'])}\n"
        + f"Processor: {pilihan_laptop2['processor']}\n"
        + f"RAM: {pilihan_laptop2['ram']}\n"
        + f"Storage: {pilihan_laptop2['storage']}\n"
        + f"GPU: {pilihan_laptop2['gpu']}\n\n"
        + "=" * 55 + "\n"
    )

    selisih = abs(
        pilihan_laptop1["harga"] - pilihan_laptop2["harga"]
    )

    if pilihan_laptop1["harga"] < pilihan_laptop2["harga"]:
        hasil_perbandingan += (
            f"{pilihan_laptop1['nama']} lebih murah "
            f"{format_rupiah(selisih)}.\n"
        )
    elif pilihan_laptop2["harga"] < pilihan_laptop1["harga"]:
        hasil_perbandingan += (
            f"{pilihan_laptop2['nama']} lebih murah "
            f"{format_rupiah(selisih)}.\n"
        )
    else:
        hasil_perbandingan += "Harga kedua laptop sama.\n"

    if pilihan_laptop1["ram"] == pilihan_laptop2["ram"]:
        hasil_perbandingan += "RAM kedua laptop sama.\n"
    else:
        hasil_perbandingan += (
            f"RAM lebih besar: "
            f"{pilihan_laptop1['nama'] if int(pilihan_laptop1['ram'].split()[0]) > int(pilihan_laptop2['ram'].split()[0]) else pilihan_laptop2['nama']}.\n"
        )

    tampilkan_text(output_perbandingan, hasil_perbandingan)


# =========================
# FUNGSI PANDUAN
# =========================

def tampilkan_panduan():
    panduan = """
PANDUAN PENGGUNAAN APLIKASI
================================

1. TAB REKOMENDASI LAPTOP
   - Pilih budget yang tersedia.
   - Pilih kebutuhan laptop.
   - Klik tombol Cari Rekomendasi.
   - Hasil laptop akan ditampilkan.

2. TAB PERBANDINGAN LAPTOP
   - Pilih laptop pertama.
   - Pilih laptop kedua.
   - Pastikan nama laptop berbeda.
   - Klik tombol Bandingkan Laptop.
   - Hasil perbandingan akan ditampilkan.

3. TAB PANDUAN
   - Baca petunjuk penggunaan aplikasi.

TIPS MEMILIH LAPTOP
================================

Belajar biasa:
Laptop dengan RAM 8 GB dan SSD sudah cukup
untuk tugas sekolah dan browsing.

Coding / TKJ:
Disarankan RAM minimal 8 GB dan SSD
agar aplikasi pemrograman berjalan lebih nyaman.

Desain grafis:
Disarankan RAM 16 GB dan processor yang cukup kuat.

Editing video:
Disarankan RAM 16 GB atau lebih serta GPU
yang mendukung pekerjaan editing.

Catatan:
Harga dan spesifikasi laptop dalam aplikasi
merupakan data contoh dan dapat berubah.
"""
    tampilkan_text(output_panduan, panduan)


# =========================
# MEMBUAT WINDOW
# =========================

root = tk.Tk()
root.title("Aplikasi Rekomendasi Laptop untuk Belajar")
root.geometry("850x650")
root.minsize(700, 550)
root.configure(bg="#f1f4f9")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TNotebook",
    background="#f1f4f9"
)

style.configure(
    "TNotebook.Tab",
    padding=(12, 8),
    font=("Arial", 10, "bold")
)

style.configure(
    "TButton",
    padding=8,
    font=("Arial", 10, "bold")
)

style.configure(
    "TLabel",
    background="#f1f4f9",
    font=("Arial", 10)
)


# =========================
# HEADER
# =========================

header = tk.Frame(root, bg="#243b55", pady=15)
header.pack(fill="x")

judul = tk.Label(
    header,
    text="APLIKASI REKOMENDASI LAPTOP",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#243b55"
)
judul.pack()

subjudul = tk.Label(
    header,
    text="Pilih laptop sesuai budget dan kebutuhan belajar",
    font=("Arial", 10),
    fg="white",
    bg="#243b55"
)
subjudul.pack(pady=(5, 0))


# =========================
# NOTEBOOK / TAB
# =========================

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True, padx=12, pady=12)


tab_rekomendasi = tk.Frame(notebook, bg="#f1f4f9")
tab_perbandingan = tk.Frame(notebook, bg="#f1f4f9")
tab_panduan = tk.Frame(notebook, bg="#f1f4f9")

notebook.add(tab_rekomendasi, text="Rekomendasi")
notebook.add(tab_perbandingan, text="Perbandingan")
notebook.add(tab_panduan, text="Panduan")


# =========================
# TAB REKOMENDASI
# =========================

frame_input = tk.Frame(tab_rekomendasi, bg="#f1f4f9")
frame_input.pack(fill="x", padx=15, pady=15)

tk.Label(
    frame_input,
    text="Pilih Budget:",
    font=("Arial", 10, "bold"),
    bg="#f1f4f9"
).grid(row=0, column=0, sticky="w", pady=5)

combo_budget = ttk.Combobox(
    frame_input,
    values=list(pilihan_budget.keys()),
    state="readonly",
    width=30
)
combo_budget.grid(row=0, column=1, padx=10, pady=5)
combo_budget.set("Rp3 - 5 juta")

tk.Label(
    frame_input,
    text="Pilih Kebutuhan:",
    font=("Arial", 10, "bold"),
    bg="#f1f4f9"
).grid(row=1, column=0, sticky="w", pady=5)

combo_kebutuhan = ttk.Combobox(
    frame_input,
    values=list(pilihan_kebutuhan.keys()),
    state="readonly",
    width=30
)
combo_kebutuhan.grid(row=1, column=1, padx=10, pady=5)
combo_kebutuhan.set("Belajar biasa")

btn_rekomendasi = ttk.Button(
    frame_input,
    text="Cari Rekomendasi",
    command=rekomendasikan_laptop
)
btn_rekomendasi.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=12
)

frame_output_rekomendasi = tk.Frame(tab_rekomendasi)
frame_output_rekomendasi.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

output_rekomendasi = tk.Text(
    frame_output_rekomendasi,
    wrap="word",
    font=("Arial", 10),
    height=15
)
output_rekomendasi.pack(fill="both", expand=True)

output_rekomendasi.config(state="disabled")


# =========================
# TAB PERBANDINGAN
# =========================

frame_compare_input = tk.Frame(tab_perbandingan, bg="#f1f4f9")
frame_compare_input.pack(fill="x", padx=15, pady=15)

nama_laptop = [laptop["nama"] for laptop in daftar_laptop]

tk.Label(
    frame_compare_input,
    text="Laptop Pertama:",
    font=("Arial", 10, "bold"),
    bg="#f1f4f9"
).grid(row=0, column=0, sticky="w", pady=5)

combo_laptop1 = ttk.Combobox(
    frame_compare_input,
    values=nama_laptop,
    state="readonly",
    width=35
)
combo_laptop1.grid(row=0, column=1, padx=10, pady=5)
combo_laptop1.set(nama_laptop[0])

tk.Label(
    frame_compare_input,
    text="Laptop Kedua:",
    font=("Arial", 10, "bold"),
    bg="#f1f4f9"
).grid(row=1, column=0, sticky="w", pady=5)

combo_laptop2 = ttk.Combobox(
    frame_compare_input,
    values=nama_laptop,
    state="readonly",
    width=35
)
combo_laptop2.grid(row=1, column=1, padx=10, pady=5)
combo_laptop2.set(nama_laptop[1])

btn_compare = ttk.Button(
    frame_compare_input,
    text="Bandingkan Laptop",
    command=bandingkan_laptop
)
btn_compare.grid(
    row=2,
    column=0,
    columnspan=2,
    pady=12
)

frame_output_compare = tk.Frame(tab_perbandingan)
frame_output_compare.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

output_perbandingan = tk.Text(
    frame_output_compare,
    wrap="word",
    font=("Arial", 10),
    height=15
)
output_perbandingan.pack(fill="both", expand=True)

output_perbandingan.config(state="disabled")


# =========================
# TAB PANDUAN
# =========================

frame_panduan = tk.Frame(tab_panduan)
frame_panduan.pack(fill="both", expand=True, padx=15, pady=15)

output_panduan = tk.Text(
    frame_panduan,
    wrap="word",
    font=("Arial", 10),
    height=20
)
output_panduan.pack(fill="both", expand=True)

output_panduan.config(state="disabled")

tampilkan_panduan()


# =========================
# MENJALANKAN APLIKASI
# =========================

root.mainloop()