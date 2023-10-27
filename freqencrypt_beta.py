#Пока не допилил, нужно где-то найти эталонные значения для биграмм в ру алфавите, считать частоту без биграмм на пайтоне крайне тяжело(как оказалось)

#Эталонные частоты символов алфавита 
symbolsFreqsStandart = [8.17, 1.49, 2.78,4.25, 12.7, 2.23, 2.02, 6.09, 6.97, 0.15, 0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76,0.98, 2.36,0.15, 1.97, 0.05]
#Эталонные частоты биграмм алфавита
bigrammsFreqsStandart = {}

#Словарь биграмм с частотами
bigramms = {}
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

#Функция шифрования по ключу
#text - list символов текста
#key - list с перестановкой на алфавите
def encrypt(text, key):
	result = []
	for i in range(len(text)):
		result.append(key[alphabet.index(text[i])])

	return result

#Функция дешифрования по ключу
#code - list символов шифра
#key - list с перестановкой на алфавите
def decrypt(code, key):
	result = []
	for i in range(len(code)):
		result.append(alphabet[key.index(code[i])])

	return result

#Функция взламывает шифр замены
#code - list символов шифра
def hack(code):
	#С помощью частотного анализа найти первый ключ
	#ПЕРВЫЙ ЭТАП. Частотный анализ символов шифротекста
	freqs = [0 for i in range(26)]
	for i in range(len(code)):
		freqs[ alphabet.index(code[i]) ] += 1
	
	for i in range(len(freqs)):
		freqs[i] = (freqs[i] / len(code)) * 100

	#Отсортировать полученные частоты
	freqsSorted = sorted(freqs)

	#Задача: выстроить символы алфавита по частотам в шифре
	key = []
	for i in range(len(freqsSorted)):
		symb = alphabet[freqs.index(freqsSorted[i])]
		if not(symb in key):
			key.append(symb)
		#Если попались символы с одинаковыми частотами
		else:
			#Взять другой(следующий) символ с такой частотой
			curFreq = freqsSorted[i]
			for j in range(len(freqs)):
				if freqs[j] == curFreq: 
					s = alphabet[j]
					if not(s in key):
						key.append(s)
						break

	#Развернуть ключ, чтобы получилось в порядке убывания частот
	key = list(reversed(key))
	#Первичный ключ
	print('First key: ', key)

	#Выполняем дешифровку этим ключом
	text = decrypt(code, key)

	#ВТОРОЙ ЭТАП. Нахождение ключа частотным анализом биграмм
	#Посчитать частоту биграмм в полученном тексте
	for i in range(1, len(text)):
		bigramms[ text[i-1] + text[i] ] += 1

	for k, v in bigramms.items():
		bigramms[k] = (bigramms[k] / (len(text)-1)) * 100

	#Посчитать рейтинг биграмм для этого ключа
	bigrammsRating = 0
	for k, v in bigramms.items():
		bigrammsRating += (bigramms[k] - bigrammsFreqsStandart[k]) ** 2

	#Выполняем перестановки на ключе до тех пор, пока рейтинг улучшается
	prevBigrammsRating = bigrammsRating
	#Величина, через которую брать символы(соседи, через один, через два и так далее)
	step = 1
	while True:
		findGoodBigrammFlag = False
		for i in range(0, 26):
			if i + step >= 26:
				break

			#Меняем местами два символа в ключе
			key[i], key[ i + step ] = key[i + step], key[i]

			#Копируем частоты биграмм
			copyBigrammsFreq = {k:v for k, v in bigramms.items()}

			#Меняем частоты биграмм в словаре, чтобы не расшифровывать текст по новой
			for sym in alphabet:
				if sym == alphabet[i] or sym == alphabet[i + step]:
					continue

				bigramms[sym + alphabet[i]], bigramms[sym + alphabet[i + step]] = bigramms[sym + alphabet[i + step]], bigramms[sym + alphabet[i]]
				bigramms[alphabet[i] + sym], bigramms[alphabet[i + step] + sym] = bigramms[alphabet[i + step] + sym], bigramms[alphabet[i] + sym]

			bigramms[alphabet[i] + alphabet[i + step]], bigramms[alphabet[i + step] + alphabet[i]] = bigramms[alphabet[i + step] + alphabet[i]], bigramms[alphabet[i] + alphabet[i + step]]
			bigramms[alphabet[i] + alphabet[i]], bigramms[alphabet[i + step] + alphabet[i + step]] = bigramms[alphabet[i + step] + alphabet[i + step]], bigramms[alphabet[i] + alphabet[i]]

			#Считаем новый рейтинг биграмм
			bigrammsRating = 0
			for k, v in bigramms.items():
				bigrammsRating += (bigramms[k] - bigrammsFreqsStandart[k])**2	

			#Если рейтинг улучшился - оставляем перестановку в ключе
			#и ставим step в 1
			if bigrammsRating < prevBigrammsRating:
				findGoodBigrammFlag = True
				prevBigrammsRating = bigrammsRating
				step = 1
				break
			#Иначе - меняем символы обратно, возвращаем частоты
			else:
				key[i], key[i + step] = key[i + step], key[i]
				for k, v in copyBigrammsFreq.items():
					bigramms[k] = v
		#Если за весь проход улучшающая перестановка не нашлась,
		#увеличиваем расстояние и идем еще раз
		if findGoodBigrammFlag == False:
			step += 1
			if step >= 25:
				break

	print('Final key: ', key)

	return key

print("\n--------------------------\n     MADE BY yngBRANb \n      Никита Карпов\n--------------------------\n")