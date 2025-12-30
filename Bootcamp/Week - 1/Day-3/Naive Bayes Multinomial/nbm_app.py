import tkinter as tk
from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import re


# MENDEFINISIKAN ULANG MODEL
class NaiveBayesMultinomial():
    # MENGAMBIL DATA DARI ZIP (npz)
    def __init__(self, model_path):
        data = np.load(model_path, allow_pickle=True)
        
        self._priors = data['priors']
        self._feature_probs = data['likelihood']
        self._classes = data['classes']
        self.vocabulary = data['vocab']
        
        print(len(self.vocabulary))
        
    # MEMPREDIKSI DATA MENGGUNAKAN RUMUS DISTRIBUSI MULTINOMIAL
    def predict_single(self, text):
        if not isinstance(text, str): return ""
        text_clean = text.lower()
        text_clean = re.sub(r'[^a-z\s]', '', text_clean)
        text_user = text_clean.strip()
        
        vector_input = np.array([1 if str(kata) in text_user else 0 for kata in self.vocabulary])
            
        posteriors = []
        
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            likelihood = np.sum(vector_input * np.log(self._feature_probs[idx]))
            posterior = prior + likelihood
            posteriors.append(posterior)
            
        return self._classes[np.argmax(posteriors)]
        
        
# LOAD MODEL MENGGUNAKAN TRY EXCEPTION
try:
    model = NaiveBayesMultinomial('model_nbm.npz')
    print("Berhasil memanggil model")
except Exception as e:
    model = None
    print("Gagal mengambil model")
    
    # MENGECEK DATA BARU DAN VALIDASI INPUT
def cek_data_baru():
    if model is None:
        messagebox.showerror('Model tidak ada, Load model terlebih dahulu')
            
    data_baru = entry_data.get("1.0", tk.END).strip()
        
    if data_baru is None:
        messagebox.showwarning('Input kosong, tolong input data yang benar')
            
    hasil = model.predict_single(data_baru)
        
    label_hasil.config(text=f"Kategori: {hasil}", fg='blue')
        
        
#GUI TKINTER UTAMA
root = tk.Tk()

root.title("Prediksi Naive Bayes Multinomial")
root.geometry("600x500")
root.configure(bg="lightblue")

judul = Label(root,text="Prediksi Teks", font=("Arial", 20, "bold"), bg="lightblue")
judul.pack()

deskripsi = Label(root,text="Naive Bayes Multinomial", font=("Arial", 10, "underline"), bg="lightblue")
deskripsi.pack(pady=(0, 30))

entry_data = Text(root, width=40, height=20, bg="gray", fg="white")
entry_data.pack()

enter_data = Button(text="Kirim Teks", command=cek_data_baru)
enter_data.pack(pady=30)

label_hasil = Label(text="...")

root.mainloop()