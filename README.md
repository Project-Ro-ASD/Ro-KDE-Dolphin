# Ro-KDE-Dolphin

Ro-ASD için KDE **Dolphin (Dosya Yöneticisi)** entegrasyon ve downstream özelleştirme bileşeni.

Bu depo yeni bir dosya yöneticisi yazmaz ve Dolphin'in tam fork'u değildir. KDE'nin mevcut Dolphin uygulamasını kullanmaya devam eder; Ro-ASD'ye özel arayüz (menü, araç çubuğu, paneller, görünüm, sağ tık menüsü, metinler) değişikliklerini küçük ve izlenebilir bir downstream katmanda tutar.

## Amaç

- Dolphin'in dosya işlemleri davranışını (KIO, izinler, kopyalama/taşıma, çöp kutusu) korumak
- Ro-ASD'ye özel arayüz değişikliklerini upstream KDE kaynaklarından ayırmak
- mümkün olduğunda patch yerine override kullanmak
- KDE Gear güncellemelerinde taşınması kolay küçük değişiklikler üretmek
- Fedora/Ro-ASD paketleme ve test zinciri için tek sahiplik noktası oluşturmak

## Bu depo ne değildir?

- Dolphin'in veya KDE kaynak ağacının tam fork'u değildir.
- KIO, KIO worker'ları ya da dosya sistemi arka ucu üzerinde değişiklik yeri değildir.
- Genel Plasma tema, icon theme, cursor, Kvantum/pencere dekorasyonu veya wallpaper deposu değildir. Bunlar `Ro-Theme` sorumluluğundadır.
- Genel dağıtım kimliği deposu değildir. Bu alan `ro-asd-branding` tarafından sahiplenilir.
- Genel sistem/masaüstü varsayılanlarının sahibi değildir. Bu alan `ro-asd-defaults` sorumluluğundadır.
- System Settings özelleştirmeleri burada yapılmaz. Bu alan `Ro-KDE-SystemSettings` sorumluluğundadır.

## Yapı

```text
.roasd/                 Ro-ASD component metadata
assets/                 Yalnız Dolphin'e özgü görseller
docs/                   Mimari, ownership, upstream haritası ve patch kaynak notu şablonu
overrides/              kxmlgui / servicemenu / çeviri override katmanı
packaging/fedora/       Fedora RPM entegrasyonu
patches/                Upstream KDE projesine göre ayrılmış patch'ler
scripts/                Doğrulama ve bakım araçları
tests/                  Component ve runtime smoke testleri
VERSION                 Component sürümü
```

## Patch yaklaşımı

Değişikliklerde tercih sırası:

1. mevcut KDE yapılandırma mekanizması (kcfg ayarları, kxmlgui)
2. güvenli asset, servicemenu veya çeviri override
3. yalnız gerekiyorsa upstream kaynağa dar kapsamlı patch

Dolphin QtWidgets (C++) ile yazılmıştır, QML katmanı yoktur. Bu yüzden menü/araç çubuğu ve metin dışındaki görsel değişikliklerin çoğu patch gerektirir. Patch'ler yalnız arayüz katmanına (`src/views`, `src/panels`, `src/statusbar`, `src/dolphinmainwindow.*` vb.) dokunmalıdır.

Tam KDE kaynak kodu bu depoya vendörlenmez. Bir patch eklenirken hangi KDE projesine ait olduğu, hangi upstream sürüm/commit üzerinde hazırlandığı ve neden gerekli olduğu [docs/PATCH-PROVENANCE-TEMPLATE.md](docs/PATCH-PROVENANCE-TEMPLATE.md) şablonuyla belgelenir.

## Component bilgisi

```text
Ro-ASD type:       component
class:             desktop-integration
component id:      ro-kde-dolphin
initial version:   0.1.0
Fedora baseline:   44
```

Makinece okunabilir tanım `.roasd/component.json` dosyasındadır.

## Doğrulama

```bash
python3 scripts/validate.py
```

GitHub Actions aynı component sözleşmesini pull request ve `main` değişikliklerinde kontrol eder.

## Durum

**Bootstrap / architecture phase**

Henüz production KDE patch'i veya RPM paketi yoktur. İlk gerçek iş, Ro-ASD için Dolphin'de değiştirmek istediğimiz arayüz öğelerini tek tek listeleyip her birinin override mı patch mi olacağına karar vermektir.

## Lisans

GPL-3.0. Upstream Dolphin GPL-2.0-or-later lisanslıdır; bu depodaki patch'ler upstream dosyaların lisansını devralır.
