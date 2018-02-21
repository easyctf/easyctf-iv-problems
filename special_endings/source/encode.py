import base64

flag = "011010010110110001101100010111110110110101101001011100110111001101011111011110010110111101110101"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

outfile = open("encrypted_lines.txt", "w")
with open("quotes.txt") as f:
	for line in f:
		encoded = base64.standard_b64encode(bytes(line.rstrip()))
		if (encoded.rstrip().endswith("==") and flag != ""):
			shift = flag[:4]
			flag = flag[4:]
			charToChange = encoded[-3:-2]
			offset = int(shift, 2)
			newChar = (alphabet[alphabet.find(charToChange[:1]) + offset])
			encoded = encoded[:-3] + newChar + "=="
		elif (encoded.rstrip().endswith("=") and flag != ""):
			shift = flag[:2]
			flag = flag[2:]
			charToChange = encoded[-2:-1]
			offset = int(shift, 2)
			newChar = (alphabet[alphabet.find(charToChange[:1]) + offset])
			encoded = encoded[:-2] + newChar + "="
		outfile.write(encoded + "\n")
outfile.close()
