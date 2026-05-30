# 🎓 YDS Kelime Öğrenme Sistemi

Modern ve etkileşimli YDS kelime öğrenme platformu. Bilimsel öğrenme yöntemleri ile kelimeleri kalıcı olarak öğrenin.

## 📁 Proje Yapısı

```
yds/
├── index.html              # TEK OYUN DOSYASI (tüm setler için)
├── prompt.txt             # Proje tanım ve geliştirme kılavuzu
├── README.md              # Bu dosya
└── images/
    ├── 1/                 # 1. Kelime Seti
    │   └── vocabulary.json    # Set 1 verisi
    ├── 2/                 # 2. Kelime Seti (gelecek)
    │   └── vocabulary.json    # Set 2 verisi
    └── ...                # Diğer setler
```

**Mimari:**
- ✅ Tek oyun dosyası tüm setler için
- ✅ Otomatik set tespiti
- ✅ Ortak JSON şeması
- ✅ Ölçeklenebilir yapı

## 🚀 Hızlı Başlangıç

### 1. Oyunu Başlat
```bash
# Ana klasördeki index.html dosyasını aç
# Çift tıkla veya tarayıcıya sürükle bırak
```

### 2. Set Seç
- Oyun açıldığında mevcut tüm setler otomatik gösterilir
- İstediğin seti seç (örn: Set 1, Set 2...)
- "Oyuna Başla" butonuna tıkla

### 3. Mod Seç ve Öğren
- 6 farklı öğrenme modundan birini seç
- Soruları cevapla ve öğren!

### 4. Yeni Set Ekleme

1. `images` klasörü altında yeni numara ile klasör oluştur (örn: `images/2`)
2. `vocabulary.json` şablonunu kullanarak veri dosyası oluştur
3. Oyunu yenile - yeni set otomatik görünür!

## 🎮 Öğrenme Modları

### 📖 Kelime → Anlam
İngilizce kelime verilir, Türkçe anlamını seçersin.
- En temel öğrenme modu
- Kelime tanıma becerisi geliştirir

### 🔤 Anlam → Kelime
Türkçe anlam verilir, doğru İngilizce kelimeyi bulursun.
- Kelime üretme becerisini artırır
- Yazma için gerekli

### 🔄 Eş Anlamlı (Synonym)
Kelimenin eş anlamlısını bulursun.
- Kelime dağarcığını genişletir
- Akademik yazıda çeşitlilik sağlar

### ↔️ Zıt Anlamlı (Antonym)
Kelimenin zıt anlamlısını seçersin.
- Kavramsal anlama derinleşir
- Karşılaştırmalı düşünme gelişir

### ✏️ Boşluk Doldur
Cümledeki boşluğa uygun kelimeyi yerleştirirsin.
- Bağlamsal kullanımı öğretir
- Gerçek sınav formatına hazırlar

### 🎴 Hızlı Kart (Flash Card)
Kartın önünde kelime, arkasında anlam ve örnek cümle.
- Hızlı tekrar için ideal
- Hafıza pekiştirme

## 📊 vocabulary.json Veri Formatı

Her kelime seti için standart JSON formatı:

```json
{
  "setInfo": {
    "setId": 1,
    "title": "YDS 60 Günde - 1. Gün",
    "totalWords": 15,
    "difficulty": "intermediate",
    "category": "general",
    "createdAt": "2026-05-30"
  },
  "words": [
    {
      "id": 1,
      "word": "example",
      "type": "noun",
      "phonetic": "/ɪɡˈzɑːmpl/",
      "meanings": {
        "primary": ["örnek"],
        "secondary": ["misal", "numune"]
      },
      "synonyms": ["sample", "instance"],
      "antonyms": [],
      "exampleSentence": "This is an example sentence.",
      "sentenceTranslation": "Bu bir örnek cümledir.",
      "otherForms": {
        "verb": "exemplify",
        "adjective": "exemplary"
      },
      "tips": "For example: örneğin",
      "difficultyLevel": 2,
      "frequency": "very high"
    }
  ]
}
```

## 🎯 Özellikler

- ✅ 6 Farklı Öğrenme Modu
- ✅ Gerçek Zamanlı İstatistikler
- ✅ İlerleme Takibi
- ✅ Puan Sistemi
- ✅ Modern ve Minimal Arayüz
- ✅ Mobil Uyumlu
- ✅ Offline Çalışma
- ✅ Genişletilebilir Yapı

## 📱 Kullanım İpuçları

### Etkili Öğrenme Stratejisi

1. **Günlük Rutininler**
   - Her gün aynı saatte 20-30 dakika çalış
   - Yeni kelimeleri sabah öğren
   - Akşam tekrar yap

2. **Mod Rotasyonu**
   - Her modu sırayla kullan
   - Zor gelen modda daha fazla zaman harca
   - Flash card ile günü bitir

3. **Spaced Repetition**
   - 1. gün: Yeni kelimeler
   - 2. gün: Tekrar
   - 4. gün: Tekrar
   - 7. gün: Tekrar
   - 15. gün: Tekrar
   - 30. gün: Final tekrar

4. **Performans Takibi**
   - %70'in altında başarı → Tekrar et
   - %70-85 arası → İyi, devam et
   - %85+ → Mükemmel, bir sonraki sete geç

## 🔧 Teknik Detaylar

### Teknolojiler
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- Vanilla JavaScript (ES6+)
- JSON veri yapısı

### Tarayıcı Desteği
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

### Performans
- Dosya boyutu: ~15KB (HTML+CSS+JS)
- JSON boyutu: ~20-30KB per set
- Yükleme süresi: <100ms
- Offline çalışma: ✅

## 📈 Gelecek Özellikler (Planlanan)

- [ ] Sesli telaffuz desteği
- [ ] Kelime çizim/yazım pratiği
- [ ] Çoklu set karışık oyun modu
- [ ] Detaylı istatistik raporları
- [ ] Haftalık/aylık ilerleme grafikleri
- [ ] Başarı rozetleri ve ödüller
- [ ] Karanlık mod tema
- [ ] Özel çalışma listeleri oluşturma
- [ ] CSV/Excel import/export
- [ ] Mobil uygulama versiyonu

## 🤝 Katkıda Bulunma

Yeni özellik fikirlerin mi var? `prompt.txt` dosyasını güncelle ve sistem otomatik olarak geliştirilecek!

## 📝 Lisans

Bu proje kişisel eğitim amaçlıdır.

## 💡 İpucu

Her yeni kelime seti eklendiğinde sistem otomatik olarak genişler. Sadece:
1. Yeni klasör oluştur (`images/n`)
2. Resimleri ekle
3. JSON oluştur
4. Oyunu başlat!

---

**Başarılar!** 🎓✨

Son güncelleme: 30 Mayıs 2026
