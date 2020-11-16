def encrypt(word):
	volwes = ['a','e','i','o','u']
	word = [word[i] for i in range(0, len(word))]
	word.reverse()
    for volwe in word:

        if volwe == 'a':
            word[word.index(volwe)] = '0'

        elif volwe == 'e':
            word[word.index(volwe)] = '1'

        elif volwe == 'i':
            word[word.index(volwe)] = '2'

        elif volwe == 'o':
            word[word.index(volwe)] = '3'

        elif volwe == 'u':
            word[word.index(volwe)] = '4'

	print(word)

	word = ''.join(word)

encrypt('karaka')
