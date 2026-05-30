"""
YDS Kelime Öğrenme Sistemi - Otomatik Veri İşleyici
Bu script resimlerdeki kelimeleri OCR ile okur ve JSON formatına dönüştürür.
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Not: OCR için pytesseract veya easyocr kullanılabilir
# pip install pytesseract pillow
# veya
# pip install easyocr

def create_vocabulary_structure(set_number, words_data, title=""):
    """Kelime setini JSON yapısına dönüştür"""
    
    if not title:
        title = f"YDS Kelime Seti - {set_number}. Gün"
    
    structure = {
        "setInfo": {
            "setId": set_number,
            "title": title,
            "totalWords": len(words_data),
            "difficulty": "intermediate",
            "category": "general",
            "createdAt": datetime.now().strftime("%Y-%m-%d"),
            "source": "YDS Kelime Kitabı",
            "tags": ["yds", "vocabulary", "english", f"day{set_number}"]
        },
        "words": words_data,
        "statistics": calculate_statistics(words_data)
    }
    
    return structure


def calculate_statistics(words_data):
    """Kelime istatistiklerini hesapla"""
    stats = {
        "totalVerbs": 0,
        "totalNouns": 0,
        "totalAdjectives": 0,
        "totalAdverbs": 0,
        "averageDifficulty": 0
    }
    
    total_difficulty = 0
    
    for word in words_data:
        word_type = word.get('type', '').lower()
        
        if 'verb' in word_type:
            stats['totalVerbs'] += 1
        elif 'noun' in word_type:
            stats['totalNouns'] += 1
        elif 'adj' in word_type:
            stats['totalAdjectives'] += 1
        elif 'adv' in word_type:
            stats['totalAdverbs'] += 1
        
        total_difficulty += word.get('difficultyLevel', 2)
    
    if words_data:
        stats['averageDifficulty'] = round(total_difficulty / len(words_data), 2)
    
    return stats


def parse_word_from_text(text_block):
    """
    Metin bloğundan kelime bilgilerini çıkar
    Format:
    WORD (type)
    Türkçe Karşılığı: ...
    Örnek Cümle: ...
    Eş ya da Yakın Anlamları: ...
    Zıt Anlamlar: ...
    """
    word_data = {
        "id": 0,  # Daha sonra ayarlanacak
        "word": "",
        "type": "",
        "phonetic": "",
        "meanings": {"primary": [], "secondary": []},
        "synonyms": [],
        "antonyms": [],
        "exampleSentence": "",
        "sentenceTranslation": "",
        "otherForms": {},
        "tips": "",
        "difficultyLevel": 2,
        "frequency": "medium"
    }
    
    # Bu fonksiyon resimden çıkan metin için özelleştirilmeli
    # OCR sonuçlarına göre parsing mantığı yazılır
    
    return word_data


def process_image_folder(folder_path):
    """Bir klasördeki tüm resimleri işle"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"❌ Klasör bulunamadı: {folder_path}")
        return None
    
    # Resim dosyalarını bul
    image_files = list(folder.glob("*.jpg")) + list(folder.glob("*.jpeg")) + list(folder.glob("*.png"))
    
    if not image_files:
        print(f"❌ Klasörde resim bulunamadı: {folder_path}")
        return None
    
    print(f"📸 {len(image_files)} resim bulundu")
    print(f"⚠️  OCR işlemi için pytesseract veya easyocr gereklidir")
    print(f"💡 Şimdilik manuel veri girişi yapabilirsiniz\n")
    
    # Kelime verileri (manuel veya OCR ile doldurulacak)
    words_data = []
    
    # Manuel veri girişi örneği
    print("📝 Manuel veri girişi başlatılıyor...")
    print("Çıkmak için kelime adına 'q' yazın\n")
    
    word_id = 1
    while True:
        print(f"\n--- Kelime {word_id} ---")
        
        word = input("İngilizce kelime: ").strip()
        if word.lower() == 'q':
            break
        
        word_type = input("Tür (adj/noun/verb/adv): ").strip()
        primary_meanings = input("Birincil anlamlar (virgülle ayır): ").split(',')
        primary_meanings = [m.strip() for m in primary_meanings]
        
        synonyms_input = input("Eş anlamlılar (virgülle ayır, boş bırakılabilir): ").strip()
        synonyms = [s.strip() for s in synonyms_input.split(',')] if synonyms_input else []
        
        antonyms_input = input("Zıt anlamlılar (virgülle ayır, boş bırakılabilir): ").strip()
        antonyms = [a.strip() for a in antonyms_input.split(',')] if antonyms_input else []
        
        example_sentence = input("Örnek cümle: ").strip()
        sentence_translation = input("Cümle çevirisi: ").strip()
        
        word_data = {
            "id": word_id,
            "word": word.lower(),
            "type": word_type,
            "phonetic": "",
            "meanings": {
                "primary": primary_meanings,
                "secondary": []
            },
            "synonyms": synonyms,
            "antonyms": antonyms,
            "exampleSentence": example_sentence,
            "sentenceTranslation": sentence_translation,
            "otherForms": {},
            "tips": "",
            "difficultyLevel": 2,
            "frequency": "medium"
        }
        
        words_data.append(word_data)
        word_id += 1
        
        more = input("\nBaşka kelime eklemek istiyor musunuz? (e/h): ").lower()
        if more != 'e':
            break
    
    return words_data


def save_vocabulary_json(folder_path, set_number, words_data):
    """Kelime verisini JSON olarak kaydet"""
    folder = Path(folder_path)
    
    vocabulary = create_vocabulary_structure(set_number, words_data)
    
    output_file = folder / "vocabulary.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(vocabulary, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ JSON dosyası oluşturuldu: {output_file}")
    print(f"📊 Toplam kelime sayısı: {len(words_data)}")
    print(f"📈 İstatistikler: {vocabulary['statistics']}")
    
    return output_file


def copy_game_html(source_folder, target_folder):
    """NOT: Artık oyun dosyası ana klasörde, kopyalamaya gerek yok"""
    print(f"ℹ️  Oyun dosyası ana klasörde (index.html)")
    print(f"ℹ️  Yeni set otomatik olarak algılanacak, oyunu yenileyin")
    return


def main():
    print("=" * 60)
    print("🎓 YDS Kelime Öğrenme Sistemi - Otomatik Veri İşleyici")
    print("=" * 60)
    print()
    
    # Klasör seçimi
    images_folder = input("images klasörünün yolu (örn: C:/Users/.../yds/images): ").strip()
    
    if not images_folder:
        images_folder = "images"
    
    images_path = Path(images_folder)
    
    if not images_path.exists():
        print(f"❌ Klasör bulunamadı: {images_folder}")
        return
    
    # Set numarası
    set_number = input("\nSet numarası (örn: 1, 2, 3...): ").strip()
    
    try:
        set_number = int(set_number)
    except ValueError:
        print("❌ Geçersiz set numarası")
        return
    
    # İşlenecek klasör
    set_folder = images_path / str(set_number)
    
    if not set_folder.exists():
        create = input(f"\n⚠️  Klasör mevcut değil. Oluşturulsun mu? ({set_folder}) (e/h): ").lower()
        if create == 'e':
            set_folder.mkdir(parents=True, exist_ok=True)
            print(f"✅ Klasör oluşturuldu: {set_folder}")
        else:
            return
    
    # Resimleri işle
    words_data = process_image_folder(set_folder)
    
    if not words_data:
        print("\n❌ Kelime verisi oluşturulamadı")
        return
    
    # JSON kaydet
    save_vocabulary_json(set_folder, set_number, words_data)
    
    # Bilgilendirme
    print("\nℹ️  Oyun dosyası ana klasörde (index.html)")
    print("ℹ️  Tarayıcıda index.html'i yenileyin, yeni set otomatik görünecek")
    
    print("\n" + "=" * 60)
    print("✅ İşlem tamamlandı!")
    print(f"🎮 Oyunu başlatmak için: ana klasördeki index.html")
    print(f"🔄 Yeni seti görmek için: Sayfayı yenile (F5)")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  İşlem kullanıcı tarafından iptal edildi")
    except Exception as e:
        print(f"\n❌ Hata oluştu: {e}")
