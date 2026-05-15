# 4.3 Kalman Filtresi ve Tahmin Teorisi

Kalman Filtresi, radar ölçümlerindeki gürültüyü (noise) minimize ederek hedefin gerçek konum ve hızını tahmin etmek için kullanılan yinelemeli (recursive) bir algoritmadır.

## Durum-Uzay Modeli (State-Space)
Hedefin durumu ($x$) genellikle konum ($p$) ve hız ($v$) bileşenlerinden oluşur:
$$x = [p_x, p_y, v_x, v_y]^T$$

## Algoritma Adımları

### 1. Tahmin (Predict)
Sistemin bir sonraki durumunu mevcut bilgilere dayanarak tahmin eder.
*   **Durum Tahmini:** $\hat{x}_{k|k-1} = F \hat{x}_{k-1|k-1}$
*   **Hata Kovaryansı:** $P_{k|k-1} = F P_{k-1|k-1} F^T + Q$

### 2. Güncelleme (Update / Correct)
Yeni bir radar ölçümü ($z$) geldiğinde tahmini düzeltir.
*   **Kalman Kazancı ($K$):** $K_k = P_{k|k-1} H^T (H P_{k|k-1} H^T + R)^{-1}$
*   **Durum Güncelleme:** $\hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H \hat{x}_{k|k-1})$
*   **Kovaryans Güncelleme:** $P_{k|k} = (I - K_k H) P_{k|k-1}$

## Değişkenlerin Anlamı
*   **$F$ (State Transition Matrix):** Hedefin hareket modeli (sabit hız vb.).
*   **$Q$ (Process Noise):** Modeldeki belirsizlik (manevra vb.).
*   **$R$ (Measurement Noise):** Radar sensörünün ölçüm hatası.
*   **$K$ (Kalman Gain):** Model tahminine mi yoksa sensör ölçümüne mi daha çok güvenileceğini belirler.

---
*Uygulama Notu: Radarlarda genellikle menzil ve açı bilgisi doğrusal olmadığı için EKF (Extended Kalman Filter) tercih edilir.*
