# QuartzzDev

import time
import random

oyunTur = ["Macera","Korku","Aksiyon","Komedi","Gerilim","Simulasyon","Strateji","Platform","Battle Royal"]
oyunKisiSayisi = ["Tek Oyunculu","Çok Oyunculu","Co-Op","LAN"]
oyunCevre = ["Bahçe","Dağ","Orman","Ev","Okul","Uçak","Araba","Şehir","Kasaba","Köy","Zindan","Polis Departmanı","Hastane"]
oyunKural = ["Oyuncu Yere Düşerse , Bölüm Tekrar Başlar","Her Bölümü Geçmek İçin Belirli Bir Süre Olacak","Kırmızı Işık Yanmadan Hareket Edilemez","En Az 3 Kere Zıplama Zorunluluğu","En Az 1 Kere Ateş Edilmeli",]
oyunGizliOzellik = ["Oyuncu Çift Zıplayabilir","Oyuncu Yere Değdiğinde Hızı x2 Artar","Oyuncu Her Zıpladığında Hızı x5 Azalır"]
oyunAlakasizOzellik = ["Oyuncunun Kafasına Her 5 saniyede bir blok düşer","Oyuncu ilerlerken aniden durur","Oyuncu Bi Anda Işık Görür","Oyuncu Bi Anda Farklı bir yere ışınlanır"]

input = input("Başlatmak İçin [Enter] ")

def secimYap():
    oyun = "Oyunun Türü :",random.choice(oyunTur) , "Oyundaki Kişi Türü :",random.choice(oyunKisiSayisi) , "Oyundaki Çevre :",random.choice(oyunCevre) , "Oyundaki Kurallar :",random.choice(oyunKural), "Oyundaki Gizli Özellik :",random.choice(oyunGizliOzellik) , "Oyundaki Alakasız Özellik",random.choice(oyunAlakasizOzellik)
    print(oyun)

secimYap()
