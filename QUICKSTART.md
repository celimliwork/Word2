# ⚡ Hızlı Başlangıç Kılavuzu

## 🎯 5 Dakikada Başla

### 1️⃣ İlk Kullanım

**Adım 1:** Ana klasördeki `game.html` dosyasına çift tıkla

**Adım 2:** Bir kelime seti seç (örn: Set 1)

**Adım 3:** "Oyuna Başla" butonuna tıkla

**Adım 4:** Bir öğrenme modu seç:
- 📖 Kelime → Anlam (başlangıç için ideal)
- 🔤 Anlam → Kelime
- 🔄 Eş Anlamlı
- ↔️ Zıt Anlamlı
- ✏️ Boşluk Doldur
- 🎴 Hızlı Kart

**Adım 5:** Oyunu oyna ve öğren! 🎉

---

## 📊 Mevcut Durumunuz

✅ **1. Set Hazır** (15 kelime)
- Kelime listesi: ✅ Analiz edildi
- JSON dosyası: ✅ Oluşturuldu
- Oyun dosyası: ✅ Ana klasörde hazır
- **BAŞLAMAYA HAZIR!** 🚀

---

## 🎮 Oyun Nasıl Çalışır?

### Kullanıcı Arayüzü

```
┌─────────────────────────────────────┐
│  🎓 YDS Kelime Öğrenme Oyunu       │
│  Set seçin ve öğrenmeye başlayın    │
├─────────────────────────────────────┤
│  ┌───┐ ┌───┐ ┌───┐                 │
│  │ 1 │ │ 2 │ │ 3 │ ...             │
│  └───┘ └───┘ └───┘                 │
│  [Oyuna Başla]                      │
├─────────────────────────────────────┤
│  📖 Kelime → Anlam                  │
│  🔤 Anlam → Kelime                  │
│  ... (diğer modlar)                 │
├─────────────────────────────────────┤
│  [Soru Alanı]                       │
│  [Seçenekler]                       │
│  [Sonraki Soru Butonu]              │
└─────────────────────────────────────┘
```

### Oyun Akışı

1. **Oyunu Aç:** `game.html` dosyasına çift tıkla
2. **Set Seç:** Mevcut setlerden birini seç
3. **Mod Seç:** Öğrenme modunu tıkla
4. **Soruyu Oku:** Ekranda gösterilen soruyu oku
5. **Cevapla:** 4 seçenekten birini seç
6. **Geri Bildirim:** Anında doğru/yanlış öğren
7. **İlerle:** Sonraki soruya geç
8. **Sonuç:** Tüm kelimeler bitince özet istatistik gör

---

## 📈 Öğrenme Stratejisi

### 🔰 Başlangıç Seviyesi
**1. Hafta:** Sadece "Kelime → Anlam" modu
- Her gün 20 dakika
- Aynı seti 3 gün üst üste tekrar et
- %80+ başarıya ulaş

### 📚 Orta Seviye
**2-3. Hafta:** Tüm modları kullan
- Her moddan 2-3 soru
- Rotatif çalışma
- Zor gelen modlarda odaklan

### 🏆 İleri Seviye
**4. Hafta ve sonrası:**
- Karma modlar
- Hız odaklı çalışma
- Yeni setleri entegre et

---

## 🆕 Yeni Set Ekleme (Basit Yöntem)

### Manuel Yöntem

1. **Klasör Oluştur**
   ```
   images/2/
   ```

2. **JSON Hazırla**
   - `vocabulary_template.json` dosyasını kopyala
   - `images/2/vocabulary.json` olarak kaydet

3. **Kelimeleri Gir**
   - JSON dosyasını aç
   - Resimlere bakarak kelimeleri yaz
   - Ortak şemayı koru!

4. **Oyunu Yenile**
   - `game.html` sayfasını yenile (F5)
   - Set 2 otomatik görünür!

5. **Oyna!**
   - Set 2'yi seç ve öğrenmeye başla

### Otomatik Yöntem (Python)

```bash
# Terminal/Command Prompt'ta
cd C:\Users\recep\Desktop\yds
python process_vocabulary.py
```

**ÖNEMLİ:** 
- Her JSON dosyası aynı şemayı kullanmalı
- Klasör isimleri sayısal ve sıralı olmalı (1, 2, 3...)
- Oyun dosyası ana klasörde kalmalı (kopyalanmaz)

---

## 🎯 Hedefler ve İzleme

### Günlük Hedef
- ✅ 15 yeni kelime öğren
- ✅ 15 eski kelimeyi tekrar et
- ✅ Toplam 30 dakika çalış

### Haftalık Hedef
- ✅ 100+ kelime öğren
- ✅ %80+ başarı oranı
- ✅ Tüm modları dene

### Aylık Hedef
- ✅ 500+ kelime hazine
- ✅ 10+ set tamamla
- ✅ YDS için hazır ol

---

## 🔍 Sık Sorulan Sorular

### Oyun açılmıyor?
- Tarayıcınızın JavaScript'i aktif olmalı
- Dosya yolunda Türkçe karakter sorun olabilir
- Farklı tarayıcı dene (Chrome öneriliPromise)

### JSON dosyası hatalı?
- `vocabulary_template.json` kullan
- Virgül ve tırnak işaretlerine dikkat et
- Online JSON validator ile kontrol et

### Kelimeler çok kolay/zor?
- `difficultyLevel` değerini ayarla (1-5)
- Karışık set oluştur (farklı levellar)
- Sadece zor kelimelere odaklan

### İstatistikler kayboldu?
- Tarayıcı her açılışta sıfırlanır (şu an)
- İleride localStorage özelliği eklenecek
- Not defterine manuel kaydet

---

## 💡 Pro İpuçları

### 🎯 Odaklanma
- Dikkat dağınıklığını minimize et
- Sessiz ortam tercih et
- Pomodoro tekniği (25dk çalış, 5dk mola)

### 🧠 Hafıza Teknikleri
- Kelimeyi cümlede kullan
- Görsel ilişkilendirme yap
- Kişisel hikaye oluştur
- Yüksek sesle tekrar et

### 📝 Not Alma
- Zor kelimeleri işaretle
- Kendi cümlelerini yaz
- Grupla (temalar, benzer kelimeler)

### 🔁 Tekrar Stratejisi
```
Gün 0:  İlk öğrenme
Gün 1:  İlk tekrar    (+1 gün)
Gün 3:  İkinci tekrar (+2 gün)
Gün 7:  Üçüncü tekrar (+4 gün)
Gün 15: Final tekrar  (+8 gün)
```

---

## 🛠️ Troubleshooting

### Problem: JSON parse error
**Çözüm:** 
- JSON validator kullan (jsonlint.com)
- Virgülleri kontrol et
- Türkçe karakter encoding (UTF-8)

### Problem: Seçenekler gösterilmiyor
**Çözüm:**
- Console'u aç (F12)
- Hataları kontrol et
- vocabulary.json yolunu kontrol et

### Problem: Oyun donuyor
**Çözüm:**
- Sayfayı yenile (F5)
- Cache'i temizle (Ctrl+Shift+Del)
- Farklı tarayıcı dene

---

## 📞 Destek

Sorun mu yaşıyorsun?

1. `README.md` dosyasını oku
2. `prompt.txt` dosyasını incele
3. Console loglarına bak (F12)
4. JSON yapısını kontrol et

---

## 🎉 Başarı Hikayen

```
┌─────────────────────────────────────┐
│  📅 1. Gün:   15 kelime ✓           │
│  📅 7. Gün:   100 kelime ✓          │
│  📅 30. Gün:  500 kelime ✓          │
│  📅 60. Gün:  YDS'ye HAZIRSIN! 🎓  │
└─────────────────────────────────────┘
```

**Haydi başla!** Her gün biraz daha yaklaşıyorsun hedefine! 💪✨

---

Son güncelleme: 30 Mayıs 2026
