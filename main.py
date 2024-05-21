print("Hello World")


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "VIBE": "Aura, enerji",
            "TOXIC": "Sağlıksız, zarar verici",
            }
            
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
#print(word)

if word in meme_dict.keys():
    print("anlamı =" ,meme_dict[word])
else:
    print("Sözlüğünüzde  bu kelime bulunamadı")
    
