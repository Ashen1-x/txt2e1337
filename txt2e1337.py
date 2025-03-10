normalAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
translatedAlphabet = ["4", "8", "(", "<|", "3", "ph", "6", "|-|", "|", "J", "|<", "1", "|\/|", "|\|", "0", "|2", "Q","R", "5", "7", "|_|", "\/", "\/\/", "><", "'/","Z"]

translator = dict(zip(normalAlphabet, translatedAlphabet))

with open("message.txt", 'r') as file:
			words = file.read()
			
translated_text = "".join(
    translator.get(char.lower(), char).upper() if char.isupper() else translator.get(char, char)
    for char in words
)
                
		


print(words)
print(translated_text)



