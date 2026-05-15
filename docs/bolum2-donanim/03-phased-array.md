# 2.3 Phased Array (Faz Dizili) Antenler

Modern radar sistemlerinin vazgeçilmezi olan faz dizili antenler, mekanik bir hareket gerektirmeden hüzmenin elektronik olarak yönlendirilmesini sağlar.

## Çalışma Mantığı

Her bir anten elemanına giden sinyalin fazı ($\phi$) kontrol edilerek, yapıcı girişim (constructive interference) belirli bir yönde odaklanır.

Faz farkı ($\Delta\phi$) ile hüzme yönü ($\theta$) arasındaki ilişki:
$$\Delta\phi = \frac{2\pi d}{\lambda} \sin(\theta)$$

Burada $d$, anten elemanları arasındaki mesafedir.

## AESA vs PESA

| Özellik | PESA (Passive Electronically Scanned) | AESA (Active Electronically Scanned) |
| :--- | :--- | :--- |
| **Sinyal Kaynağı** | Tek bir merkezi verici (Magnetron/Klystron). | Her elemanın kendi T/R (Transmit/Receive) modülü vardır. |
| **Güvenilirlik** | Merkezi kaynak bozulursa sistem çöker. | "Graceful Degradation" (Birkaç modül bozulsa da sistem çalışır). |
| **LPI Özelliği** | Düşük. | Çok yüksek (Frekans atlamalı ve düşük güçte çalışabilir). |
| **Maliyet** | Daha ekonomik. | Oldukça yüksek. |

## Avantajları
* **Hız:** Milisaniyeler içinde hüzme yönü değiştirilebilir.
* **Çoklu Hedef:** Aynı anda birden fazla hüzme oluşturarak farklı hedefler takip edilebilir.
* **Hacim:** Dönen mekanik parçalar olmadığı için daha kompakt tasarımlar mümkündür.

---
*İleri Okuma: Sayısal hüzme şekillendirme (Digital Beamforming) teknikleri.*
