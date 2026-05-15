# 1.3 Temel Radar Denklemi

Radar denklemi, bir radar sisteminin menzil performansını belirleyen en temel matematiksel araçtır. Bu denklem, iletilen güç ile hedeften dönen ve alıcı tarafından yakalanan güç arasındaki ilişkiyi kurar.

## Denklemin Türetilmesi

### 1. İletilen Güç Yoğunluğu ($S_t$)
Kayıpsız ve her yöne eşit ışıma yapan (isotropic) bir antenin $R$ mesafesindeki güç yoğunluğu:
$$S_{iso} = \frac{P_t}{4\pi R^2}$$

Yönlü (directional) bir anten kullanıldığında, kazanç ($G$) faktörü eklenir:
$$S_t = \frac{P_t G}{4\pi R^2}$$

### 2. Hedef Tarafından Yakalanan ve Yansıtılan Güç
Hedefin bu enerjiyi yansıtma kapasitesi Radar Kesit Alanı ($\sigma$) ile ifade edilir. Hedeften yansıyan güç yoğunluğu:
$$S_r = \frac{P_t G \sigma}{(4\pi R^2) (4\pi R^2)} = \frac{P_t G \sigma}{(4\pi)^2 R^4}$$

### 3. Alıcı Anten Tarafından Yakalanan Güç ($P_r$)
Alıcı antenin etkili açıklığı ($A_e$) kullanılarak alınan güç hesaplanır ($A_e = \frac{G \lambda^2}{4\pi}$):
$$P_r = S_r A_e = \frac{P_t G \sigma}{(4\pi)^2 R^4} \cdot \frac{G \lambda^2}{4\pi}$$

Sonuç olarak **Temel Radar Denklemi**:
$$P_r = \frac{P_t G^2 \lambda^2 \sigma}{(4\pi)^3 R^4}$$

## Değişkenlerin Analizi

*   **$P_t$ (Transmit Power):** İletilen tepe gücü. Menzil, gücün dördüncü köküyle orantılıdır ($R \propto \sqrt[4]{P_t}$). Gücü 2 katına çıkarmak menzili sadece %19 artırır.
*   **$G$ (Antenna Gain):** Anten kazancı karesel etki yapar. Bu yüzden anten tasarımı kritik önemdedir.
*   **$\lambda$ (Wavelength):** Frekans arttıkça dalga boyu küçülür, bu da aynı anten boyutu için daha yüksek kazanç sağlar ancak yayılım kayıpları artar.
*   **$\sigma$ (RCS):** Hedefin yansıtma yüzeyi. Stealth uçaklar bu değeri minimize etmeye çalışır.

---
> [!TIP]
> Gerçek dünyada bu denkleme sistem kayıpları ($L$) ve gürültü faktörü de eklenmelidir.
