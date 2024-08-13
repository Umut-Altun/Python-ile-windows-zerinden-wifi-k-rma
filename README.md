# 🔍 WiFi Şifrelerini Görüntüleme Aracı

Bu proje, Windows işletim sistemi üzerinde kayıtlı WiFi ağlarının adlarını (SSID) ve şifrelerini Python kullanarak görüntülemeye olanak tanır. `netsh` komutu aracılığıyla WiFi profillerini alır ve şifrelerini çözerek kullanıcıya sunar.

## 📋 Özellikler
- **Tüm WiFi Profillerini Listeleme**: Bilgisayarınızda kayıtlı tüm WiFi profillerinin adlarını listeler.
- **WiFi Şifrelerini Görüntüleme**: Şifrelenmiş WiFi profillerinin şifrelerini çözer ve görüntüler.
- **Şifresi Olmayan Ağları Atla**: Şifre koruması olmayan ağları otomatik olarak atlar.

## 🛠 Kullanılan Teknolojiler
- **Python**: Ana programlama dili.
- **subprocess Modülü**: Komut satırı komutlarını çalıştırmak ve çıktıları almak için kullanılır.
- **re Modülü**: Düzenli ifadelerle metin işlemleri gerçekleştirilir.

## 📖 Proje Adımları
1. **Modüllerin İçe Aktarılması**: Gerekli Python modülleri projeye dahil edilir.
2. **WiFi Profillerinin Çıkarılması**: `subprocess` modülü kullanılarak `netsh wlan show profiles` komutu çalıştırılır ve tüm WiFi profilleri alınır.
3. **Profil Bilgilerinin Alınması**: Her profil için `netsh wlan show profile [profil_ismi] key=clear` komutu çalıştırılır.
4. **Şifrelerin Çözümlenmesi**: Şifreler varsa çözümlenir ve WiFi profili ile birlikte bir listeye eklenir.
5. **Sonuçların Görüntülenmesi**: Tüm WiFi profilleri ve varsa şifreleri ekrana yazdırılır.

## 🚀 Nasıl Kullanılır
1. Projeyi bilgisayarınıza klonlayın veya indirin.
2. Python'un yüklü olduğundan emin olun.
3. `wifi_sifre_goruntuleme.py` dosyasını çalıştırarak WiFi şifrelerini görüntüleyin.

## 📄 Uyarılar
- Bu araç yalnızca Windows işletim sisteminde çalışır.
- Şifreleri görüntülemek için yönetici (admin) haklarına sahip olmanız gerekebilir.
- Bu kod, kişisel kullanımlar için tasarlanmıştır; izinsiz ağ şifrelerine erişmek yasalara aykırıdır.

Bu projeyi kullanırken dikkatli olun ve yasal sınırlar içinde kalın!
