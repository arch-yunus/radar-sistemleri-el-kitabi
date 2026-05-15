import numpy as np
import matplotlib.pyplot as plt

def calculate_radar_range(pt, g, sigma, freq, pr_min, loss_db=0):
    """
    Temel Radar Menzil Denklemi Hesabı
    
    Parametreler:
    - pt: Verici gücü (Watt)
    - g: Anten kazancı (Doğal sayı, dBi değil)
    - sigma: Radar Kesit Alanı (m^2)
    - freq: Çalışma frekansı (Hz)
    - pr_min: Minimum saptanabilir güç (Watt)
    - loss_db: Sistem kayıpları (dB)
    """
    c = 3e8
    wavelength = c / freq
    loss = 10**(loss_db / 10)
    
    numerator = pt * (g**2) * (wavelength**2) * sigma
    denominator = ((4 * np.pi)**3) * pr_min * loss
    
    range_m = (numerator / denominator)**0.25
    return range_m

if __name__ == "__main__":
    # Örnek Parametreler (X-Band Radar)
    PT = 1000      # 1 kW
    G = 31.6       # ~15 dBi
    SIGMA = 1.0    # 1 m^2 (İnsan veya küçük İHA)
    FREQ = 10e9    # 10 GHz
    PR_MIN = 1e-12 # -90 dBm civarı
    
    r = calculate_radar_range(PT, G, SIGMA, FREQ, PR_MIN)
    print(f"Hesaplanan Maksimum Menzil: {r/1000:.2f} km")
