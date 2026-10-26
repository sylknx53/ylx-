# 💎 Semoizm Boilerplate

> Discord bot projeleri geliştirmek için tasarlanmış, modüler `cogs` mimarisine ve güncel `app_commands` desteğine sahip profesyonel Python altyapısı.

---

## ✨ Özellikler

* **Modüler Mimari (`Cogs`):** Komutlarınızı ve özelliklerinizi tek bir dosyaya tıkıştırmak yerine ayrı modüller halinde düzenli bir şekilde yönetin.
* **Güncel Slash Komutlar:** Discord'un güncel standartlarına tam uyumlu uygulama komutları (`app_commands`) altyapısı.
* **Güvenli Kimlik Doğrulama:** Hassas verileriniz (`TOKEN` ve `OWNER_ID`) `.env` altyapısı ile tamamen güvence altındadır.
* **Özel Durum Desteği:** `discord.CustomActivity` ile botunuzun profil durumunu dilediğiniz gibi özelleştirin.
* **Otomatik Yükleme:** `komutlar/` klasörüne eklediğiniz her yeni modül, bot başlatıldığında otomatik olarak taranır ve sisteme yüklenir.

---

## ⚙️ Kurulum ve Başlangıç

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Projeyi Klonlayın
\`\`\`bash
git clone https://github.com/semoizm/semoizm-boilerplate.git
cd semoizm-boilerplate
\`\`\`

### 2. Gerekli Kütüphaneleri Yükleyin
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. `.env` Dosyasını Oluşturun
Projenin ana dizinine **`.env`** adında bir dosya oluşturun (veya `.env.example` dosyasını kopyalayıp adını değiştirin) ve kendi bilgilerinize göre doldurun:
\`\`\`env
DISCORD_TOKEN=buraya_botunun_tokenini_yapistir
OWNER_ID=senin_discord_id_numaran
BOT_STATUS=youtube.com/semoizm
\`\`\`

### 4. Botu Çalıştırın
\`\`\`bash
python main.py
\`\`\`

---

## 📂 Proje Dosya Yapısı

semoizm-boilerplate/
├── main.py # Botun ana başlatıcı ve yükleyici dosyası
├── .env.example # Örnek çevre değişkenleri dosyası
├── .gitignore # Git tarafından takip edilmeyecek gizli dosyalar
├── requirements.txt # Gerekli python kütüphane listesi
├── LICENSE # MIT Açık Kaynak Lisansı
└── komutlar/ # Modüler komut klasörünüz (Cogs)
    ├── __init__.py
    └── genel.py # Örnek temel komutlar (örn. ping)

---

## 📝 Lisans
Bu proje [MIT License](LICENSE) lisansı altında korunmaktadır. İstediğiniz gibi geliştirip kullanabilirsiniz.
