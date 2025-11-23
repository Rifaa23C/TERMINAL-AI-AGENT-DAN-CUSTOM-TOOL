import os
import shutil
import psutil

#   TOOL 1 — FILE ORGANIZER
def file_organizer(path: str):
    """
    Merapikan folder berdasarkan jenis file.
    """
    if not os.path.isdir(path):
        return {"error": "Path folder tidak ditemukan."}

    folders = {
        "Images": [".jpg", ".jpeg", ".png"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Others": []
    }

    for folder in folders:
        os.makedirs(os.path.join(path, folder), exist_ok=True)

    moved_files = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False

            for folder, extensions in folders.items():
                if ext in extensions:
                    shutil.move(file_path, os.path.join(path, folder, file))
                    moved_files.append(file)
                    moved = True
                    break

            if not moved:
                shutil.move(file_path, os.path.join(path, "Others", file))
                moved_files.append(file)

    return {"status": "Berhasil dirapikan", "files_moved": moved_files}

#   TOOL 2 — SYSTEM CHECK RAM
def system_check_ram():
    """
    Mengecek sisa RAM laptop.
    """
    ram = psutil.virtual_memory()
    return {
        "total_GB": round(ram.total / (1024**3), 2),
        "available_GB": round(ram.available / (1024**3), 2),
        "percent_used": ram.percent
    }

#   TOOL 3 — KALKULATOR SUHU
def kalkulator_suhu(nilai: float, dari: str, ke: str):
    """
    Mengubah suhu dari C ke F atau F ke C.
    """
    try:
        dari = dari.upper()
        ke = ke.upper()

        if dari == "C" and ke == "F":
            hasil = (nilai * 9/5) + 32
        elif dari == "F" and ke == "C":
            hasil = (nilai - 32) * 5/9
        else:
            return {"error": "Konversi tidak valid. Gunakan C atau F."}

        return {
            "input": f"{nilai}{dari}",
            "output": f"{hasil}{ke}"
        }
    except Exception as e:
        return {"error": str(e)}


#   TOOL 4 — KALKULATOR DISKON
def kalkulator_diskon(harga: float, diskon: float):
    """
    Menghitung harga setelah diskon.
    """
    try:
        if diskon < 0 or diskon > 100:
            return {"error": "Diskon harus 0-100"}

        harga_akhir = harga - (harga * diskon / 100)

        return {
            "harga_awal": harga,
            "diskon": f"{diskon}%",
            "harga_akhir": harga_akhir
        }
    except Exception as e:
        return {"error": str(e)}


#   TOOL 5 — BACA FILE TEKS
def baca_file_teks(path: str):
    """
    Membaca isi file .txt
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        return {
            "path": path,
            "isi_file": content
        }
    except Exception as e:
        return {"error": str(e)}

#   TOOL DICTIONARY
tool_dictionary = {
    "file_organizer": file_organizer,
    "system_check_ram": system_check_ram,
    "database_query": database_query,
    "kalkulator_suhu": kalkulator_suhu,
    "kalkulator_diskon": kalkulator_diskon,
    "baca_file_teks": baca_file_teks
}
