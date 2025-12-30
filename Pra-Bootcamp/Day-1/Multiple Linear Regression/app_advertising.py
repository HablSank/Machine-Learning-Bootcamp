import tkinter as tk
from tkinter import messagebox
import numpy as np

try:
    theta = np.load('model_advertising.npy')
    print("Berhasil membaca model")
except Exception as e:
    print("Gagal membaca model")
    
def hitung_sales():
    try:
        