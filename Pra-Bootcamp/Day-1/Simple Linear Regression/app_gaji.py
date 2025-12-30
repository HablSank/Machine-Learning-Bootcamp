import numpy as np
import tkinter as tk
from tkinter import messagebox

try:
    theta = np.load('model_gaji.npy')
    print("Berhasil membaca theta")
except Exception as e:
    print("Gagal membaca theta")
    
def hitung_gaji():
    try:
        tahun = float(entry_tahun.get())
        
        # Input: [1, tahun]
        # Angka 1 untuk Intercept, 'tahun' untuk Slope
        input_data = np.array([1, tahun])
        
        # HITUNG (Rumus Regresi)
        # Hasil = [1, tahun] @ theta
        prediksi = input_data @ theta
        
        # Ambil angkanya (karena hasilnya array)
        gaji = prediksi[0]
        
        # Tampilkan (Format uang biar keren)
        label_hasil.config(text=f"Estimasi Gaji: Rp {gaji:,.0f}", fg="green", font=("Arial", 14, "bold"))
        
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka tahun yang benar ya!")

# --- 3. TAMPILAN GUI ---
root = tk.Tk()
root.title("Salary Predictor - LKS")
root.geometry("400x300")

# Judul
tk.Label(root, text="Prediksi Gaji Karyawan", font=("Helvetica", 16, "bold")).pack(pady=20)

# Input Form
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Pengalaman Kerja (Tahun):", font=("Arial", 12)).pack(side="left", padx=10)
entry_tahun = tk.Entry(frame, font=("Arial", 12), width=10)
entry_tahun.pack(side="left")

# Tombol
btn = tk.Button(root, text="HITUNG GAJI", command=hitung_gaji, bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=20, pady=5)
btn.pack(pady=20)

# Hasil
label_hasil = tk.Label(root, text="...", font=("Arial", 12))
label_hasil.pack()

# Footer
tk.Label(root, text="Powered by Simple Linear Regression", font=("Arial", 8, "italic"), fg="gray").pack(side="bottom", pady=10)

root.mainloop()