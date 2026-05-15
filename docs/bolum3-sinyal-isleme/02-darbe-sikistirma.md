# 3.2 Darbe Sıkıştırma (Pulse Compression)

Radar mühendisliğinde "Menzil Çözünürlüğü" ile "Maksimum Menzil" arasındaki dengeyi kuran en kritik tekniktir.

## Problem: Menzil vs Çözünürlük
*   **Daha uzun menzil** için daha uzun süreli darbeler ($\tau$) gerekir (daha fazla enerji).
*   **Daha iyi çözünürlük** ($\Delta R = c\tau/2$) için daha kısa süreli darbeler gerekir.

**Darbe Sıkıştırma**, uzun bir darbe gönderip alıcıda bunu matematiksel olarak "sıkıştırarak" her iki avantajı da elde etmemizi sağlar.

## LFM (Linear Frequency Modulation - Chirp)
En yaygın yöntemdir. Darbe süresi boyunca sinyalin frekansı doğrusal olarak artırılır veya azaltılır.

*   **Bant Genişliği ($B$):** Çözünürlük artık darbe süresine değil, bant genişliğine bağlıdır:
    $$\Delta R = \frac{c}{2B}$$

## Matched Filter (Eşlenik Filtre)
Alıcıda, gönderilen sinyalin bir kopyası ile gelen yankı sinyali korelasyona sokulur. Bu işlem SNR'ı maksimize eder.

### İşlem Adımları:
1.  Gönderilen sinyalin zaman-tersi ve kompleks konjugesi alınır.
2.  Gelen sinyal ile evrişim (convolution) yapılır.
3.  Çıkışta keskin bir "peak" (tepe noktası) elde edilir.

## Barker Kodları
Faz modülasyonu tabanlı darbe sıkıştırma yöntemidir. Belirli bir dizi (+1, -1 gibi) kullanılarak yan hüzmeler (sidelobes) minimuma indirilir. En uzun Barker kodu 13 elemanlıdır.

---
> [!NOTE]
> Darbe sıkıştırma oranı ($PCR = T \cdot B$), sistemin menzil çözünürlüğündeki iyileşmeyi temsil eder.
