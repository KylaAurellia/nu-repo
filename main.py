meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            }
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
i = 0
while i < 5:
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("kata tidak ditemukan")
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
    i = i + 1
