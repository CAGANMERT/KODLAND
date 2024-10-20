meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "Bir şakaya karşılık cevap",
            "SHEESH" : "Onaylamamak",
            "CREEPY" : "Korkunç",
            "AGGRO" : "Agresifleşmek / Sinirlenmek",
            "FLEX" : "Hava atmak",
            "OK BOOMER" : "Bir başkasını sakinleşmesi için söylenen söz",
            "AFK" : "Bilgisayar başında olmayan / Oyunda hareket etmeyenler için kullanılan söz",
            "SISTA" : "Kız kardeş",
            "STALK" : "Birinin sosyal medya hesabına bakmak",
            "TROLL" : "Huzur bozan kişiler için kullanılan söz / Şaka",
            "STORY" : "Geçici süreli paylaşım",
            "MENTION" : "Gönderiye etiketlemek",
            "BFF" : "En iyi arkadaşlar",
            "FAKE" : "Sahte",
            "MEME" : "Mizahi içerik",
            "VIRAL" : "Hızla yayılan içerik",
            "GHOSTING" : "İlişki sonlandırmak",
            "EZ" : "Kolay",
            }

for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print("Anlam:",meme_dict[word])
    else:
        print("Maalesef bu kelime sözlüğümüzde mevcut değildir.") 
