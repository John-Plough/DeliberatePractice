# def high(string):

#     words = string.split(' ')
#     highscore = 0
#     highword = ''

#     for word in words:
#         score = 0
#         for char in word:
#             point = ord(char) - ord('a') + 1
#             score += point
#         if score > highscore:
#             highscore = score
#             highword = word

#     return highword


def high(string):

    highscore = 0

    for word in string.split():
        score = sum(ord(char) - ord('a') + 1 for char in word)
        if score > highscore:
            highscore = score
            highword = word

    return highword


def high(text):
    words = text.split()
    scores = []

    for word in words:
        score = sum(ord(char) - ord('a') + 1 for char in word)
        scores.append(score)

    return words[scores.index(max(scores))]


def high(text):
    return max(text.split(), key=lambda word: sum(ord(char) - ord('a') + 1 for char in word))

# print(high('take two bintang and a dance please'))

def max_word_score(word):
    return sum(ord(char) - ord('a') + 1 for char in word)

def high(text):
    words = text.split()
    return max(words, key=max_word_score)


def high(text):
    return max(text.split(), key=lambda word: sum(ord(char) - ord('a') + 1 for char in word))

# print(high('take two bintang and a dance please'))




def high(text):
    return max(text.split(), key=lambda word: sum(ord(char) - ord('a') + 1 for char in word))


# def max_word_score(word):
#     return sum(ord(char) - ord('a') + 1 for char in word)

# def high(text):
#     words = text.split()
#     return max(words, key=max_word_score)


# def high(text):
#     words = text.split()
#     scores = []

#     for word in words:
#         score = sum(ord(char) - ord('a') + 1 for char in word)
#         scores.append(score)

#     return words[scores.index(max(scores))]


# def high(string):

#     highscore = 0

#     for word in string.split():
#         score = sum(ord(char) - ord('a') + 1 for char in word)
#         if score > highscore:
#             highscore = score
#             highword = word

#     return highword

print(high('take two bintangeriney and a dance please'))
