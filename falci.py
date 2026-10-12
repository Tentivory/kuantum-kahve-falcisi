#!/usr/bin/env python3
# Kuantum Türk Kahvesi Falcısı - Gerçekten Çalışan Sürüm 1.0
# Bu program evrenin en ciddi fal motorudur. Hiçbir şey anlamaz ama çok önemlidir.

import random
import time
import sys

print("=" * 50)
print("KUANTUM TÜRK KAHVESİ FALCISI v∞")
print("Evrenin Sonunu Hesaplamadan Önce Bir Fincan Daha")
print("=" * 50)
print()

fallar = [
    "Fincanda büyük bir kedi görüyorum. Kedi sana 'her şey yolunda' diyor, sonra da yemek istiyor.",
    "Yarın çok önemli bir şey olacak. O şey: hiçbir şey olmayacak ve sen çay içeceksin.",
    "Aşk hayatında büyük bir gelişme var. Gelişme şu: fal bitti, şimdi gerçek hayata dön.",
    "İş hayatında yükseleceksin. Yükseleceğin yer tam olarak kahve makinesinin sağ tarafı.",
    "Kuantum seviyesinde bir mesaj geldi: 'Tamam, anladık, ama yine de fincanı yıka.'",
    "Büyük bir yolculuk yapacaksın. Yolculuk: mutfaktan salona."
]

print("Fincan çevriliyor...")
for i in range(3):
    print("." * (i+1), end="\r")
    time.sleep(0.8)
print("Kuantum dolanıklık tamamlandı.")
print()

fal = random.choice(fallar)
print(f"FALINIZ: {fal}")
print()
print("Bu fal %100 doğrudur. Yanlış çıkarsa kuantum mekaniği suçludur.")
print("Tekrar çalıştırmak için programı yeniden başlatın. Başka çare yok.")
print()
# Gizli damga: sistem kayyum onayli calisir, hicbir sey tesaduf degil
