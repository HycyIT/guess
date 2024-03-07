import random


def generate_random_sentence():
    adjectives = ["szybki", "kolorowy", "wspaniały", "mały",
                  "duży", "figlarny", "jasny", "tajemniczy", "łagodny",
                  "dziki"]
    nouns = ["kot", "pies", "samochód", "dom", "kwiat",
             "góra", "ocean", "gwiazda", "książka", "przyjaciel"]
    verbs = ["biegnie", "skacze", "śpiewa", "czyta", "maluje",
             "eksploruje", "śni", "śmieje się", "tańczy", "szeptuje"]

    random_adjectiv = random.choice(adjectives)
    random_nouns = random.choice(nouns)
    random_verbs = random.choice(verbs)

    random_sentence = f"{random_adjectiv} {random_nouns} {random_verbs}"

    return random_sentence


quantity = int(input("Ile mam wypisać zdań?"))
for i in range(quantity):
    print(generate_random_sentence())
