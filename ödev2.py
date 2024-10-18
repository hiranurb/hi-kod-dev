{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "98040605-4128-41d0-bfb4-5a854cbf06bc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "maaşınızı giriniz:  12000\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "vergi kesintisi: 1200.00tl\n",
      "yeni maaşınız: 10800.00tl\n"
     ]
    }
   ],
   "source": [
    "maaş = float(input(\"maaşınızı giriniz: \"))\n",
    "\n",
    "if maaş <= 10000:\n",
    "    vergi_orani = 0.05\n",
    "\n",
    "elif maaş <= 25000:\n",
    "    vergi_orani = 0.10\n",
    "\n",
    "elif maaş <= 45000:\n",
    "    vergi_orani = 0.25\n",
    "\n",
    "else:\n",
    "    vergi_orani = 0.30\n",
    "\n",
    "vergi_kesintisi = maaş*vergi_orani\n",
    "yeni_maaş =maaş - vergi_kesintisi\n",
    "print(f\"vergi kesintisi: {vergi_kesintisi:.2f}tl\")\n",
    "print(f\"yeni maaşınız: {yeni_maaş:.2f}tl\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "62ff4efd-737d-41d9-bfa6-0d3fd2b25e44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "kullanıcı adını giriniz: hiranur\n",
      "şifrenizi giriniz: 567890\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hesabınız oluşturuldu.\n"
     ]
    }
   ],
   "source": [
    "kullanıcı_adı = input(\"kullanıcı adını giriniz:\")\n",
    "sifre = input(\"şifrenizi giriniz:\")\n",
    "\n",
    "if len(sifre) >= 6:\n",
    "   print(\"hesabınız oluşturuldu.\")\n",
    "\n",
    "else:\n",
    "     print(\"şifreniz en az 6 haneli olmalıdır.\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0d212547-9a21-4f96-8ce6-0f3e78062cdb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "kullanıcı adınızı giriniz: hiranur\n",
      "şifrenizi girin (5-10 hane arası):  567890*\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hesabınız oluşturuldu.\n"
     ]
    }
   ],
   "source": [
    " kullanıcı_adı = input(\"kullanıcı adınızı giriniz:\")\n",
    " sifre = input(\"şifrenizi girin (5-10 hane arası): \")\n",
    "\n",
    "if 5 <= len(sifre) <= 10:\n",
    "    print(\"hesabınız oluşturuldu.\")\n",
    "\n",
    "else:\n",
    "    print(\"lütfen girdiğiniz şifre 5 haneden az 10 haneden fazla olmasın.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "76e9a4b6-0184-40aa-9cec-b7a43e849042",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "isminizi girin:  hiranur\n",
      "şifrenizi giriniz:  5638439485\n",
      "şifrenizi giriniz:  567890*\n",
      "şifrenizi giriniz:  gizli123\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "giriş yapıldı.\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'kalan_hak' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[18], line 14\u001b[0m\n\u001b[0;32m     11\u001b[0m     kalan_hak \u001b[38;5;241m=\u001b[39m maksimum_hak \u001b[38;5;241m-\u001b[39m (deneme\u001b[38;5;241m+\u001b[39m\u001b[38;5;241m1\u001b[39m)\n\u001b[0;32m     12\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myanlış şifre girildi,kalan hak:\u001b[39m\u001b[38;5;124m\"\u001b[39m,kalan_hak)\n\u001b[1;32m---> 14\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m kalan_hak \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m     15\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124müç yanlış deneme yapıldı.program sonlanıyor.\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'kalan_hak' is not defined"
     ]
    }
   ],
   "source": [
    "tanımlı_şifre = \"gizli123\"\n",
    "isim = input(\"isminizi girin: \")\n",
    "maksimum_hak = 3\n",
    "for deneme in range(maksimum_hak):\n",
    "    şifre = input(\"şifrenizi giriniz: \")\n",
    "\n",
    "if şifre == tanımlı_şifre:\n",
    "    print(\"giriş yapıldı.\")\n",
    "\n",
    "else:\n",
    "    kalan_hak = maksimum_hak - (deneme+1)\n",
    "    print(\"yanlış şifre girildi,kalan hak:\",kalan_hak)\n",
    "\n",
    "if kalan_hak == 0:\n",
    "    print(\"üç yanlış deneme yapıldı.program sonlanıyor.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e611ef8-33b2-4948-bb29-7a270910c39a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
