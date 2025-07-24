# Test Automation Suite

> Bu projedeki tüm otomasyon testleri https://www.saucedemo.com/ demo e-ticaret sitesi üzerinde çalışmaktadır.

Bu proje, saucedemo.com üzerinde temel e-ticaret kullanıcı akışlarını otomatik test etmek için hazırlanmıştır.

## Kurulum

1. Python 3.9+ kurulu olmalı.
2. Bağımlılıkları yükleyin:
   ```
   python -m pip install -r requirements.txt
   ```

## Testleri Çalıştırma

```
python -m pytest --html=report.html --self-contained-html
```

## Testler
- Login testi (başarılı giriş)
- Negatif login testi (hatalı şifre ile giriş ve hata mesajı kontrolü)
- Sepete ürün ekleme testi (ürün sepete ekleniyor ve ikon kontrolü)
- Sepete ekle + API ile kontrol testi (örnek API ile doğrulama)
- Sepetten ürün silme testi (sepete eklenen ürünü silip, sepetin boş olduğunu kontrol eder)
- Başarılı checkout testi (ödeme adımlarını tamamlayıp sipariş mesajını kontrol eder)
- Farklı kullanıcı rolleriyle giriş testi (locked_out_user, problem_user)
- Ürün detay sayfası testi (ürün listesinden detay sayfasına geçiş ve ürün adı kontrolü)
- Sepet boşken checkout denemesi testi (sepet boşken checkout adımına geçiş kontrolü)
- Fiyat ve toplam hesaplama testi (sepete birden fazla ürün eklenip toplam fiyatın doğruluğu kontrol edilir)
- Logout (çıkış) testi (kullanıcı çıkış yaptıktan sonra login sayfasına yönlendirme kontrolü)
- Filtreleme ve sıralama testi (ürünler fiyata göre artan şekilde sıralanıyor mu kontrolü)
- Görsel ve link kontrolleri testi (ürün görsellerinin ve linklerinin kırık olup olmadığını kontrol eder)
- Form validasyon testi (checkout sırasında zorunlu alanlar boş bırakıldığında hata mesajı kontrolü)
- Tarayıcılar arası test (login ve ürün listeleme akışı hem Chrome hem Firefox ile çalıştırılır)
- Responsive (mobil) testi (farklı ekran boyutlarında ana sayfanın ve ürünlerin doğru yüklendiği kontrol edilir)
- Performans testi (ana sayfanın yüklenme süresi ölçülür, belirli bir süreden uzun sürerse hata verir)
- Kampanya/indirim testi (indirimli ürün eklenip fiyatın ve toplamın doğruluğu kontrol edilir - örnek olarak ilk ürünle yapılır)
- Hatalı URL ve 404 sayfası testi (geçersiz ürün linkine gidildiğinde hata/404 sayfası kontrolü)
- Kullanıcı kayıt (register) testi (yeni kullanıcı kaydı oluşturulup kayıt formunun açıldığı kontrol edilir - örnek olarak automationpractice.com ile)
  > Not: Bu test demo/örnek amaçlıdır, gerçek ortamda çalışmayabilir.
- Şifre sıfırlama testi (şifremi unuttum akışının çalıştığı kontrol edilir - örnek olarak automationpractice.com ile)
  > Not: Bu test demo/örnek amaçlıdır, gerçek ortamda çalışmayabilir.
- Çoklu ürün sepet testi (farklı ürünleri sepete ekle, çıkar, tekrar ekle ve sepetin güncel durumunu kontrol et)
- Kullanıcı oturumu süresi testi (login olduktan sonra belirli bir süre bekle, oturumun açık kalıp kalmadığını veya otomatik logout olup olmadığını kontrol et)

## Raporlama
- pytest-html ile HTML raporu otomatik üretilir.

## Notlar
- requests kütüphanesini eklememizin sebebi, Python ile **HTTP istekleri** (GET, POST, vs.) kolayca gönderebilmek içindir.
- Selenium ile web arayüzünde bir işlem yapıyoruz (ör: sepete ürün ekleme).
- Sonra, arka plandaki API’ye (ör: sepette hangi ürünler var?) bir **HTTP isteği** atıp sonucu kontrol etmek istiyoruz.
- Python’ın standart kütüphanesinde bu kadar kolay ve pratik bir HTTP istemcisi yok.  
- requests ile örnek kullanım:
  ```python
  import requests
  response = requests.get("https://api.site.com/cart")
  assert response.status_code == 200
  ```
- Yani, **web arayüzünde yapılan işlemin gerçekten arka planda gerçekleşip gerçekleşmediğini** API üzerinden doğrulamak için requests kullanıyoruz.
- Eğer sadece web arayüzüyle sınırlı kalacaksan, requests’e gerek yok.  
- Ama API ile kontrol de yapmak istiyorsan, eklememiz gerekir. 