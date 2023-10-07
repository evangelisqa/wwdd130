import random

single_determiners = ["The", "One", "A"]
plural_determiners = ["Some", "Many", "Two"]
single_nouns = [
    "Bird",
    "Adult",
    "Boy",
    "Child",
    "Car",
    "Cat",
    "Dog",
    "Woman",
    "Man",
    "Girl",
]
plural_nouns = [
    "Birds",
    "Adults",
    "Boys",
    "Children",
    "Cars",
    "Cats",
    "Dogs",
    "Women",
    "Men",
    "Girls",
]
verb_past = [
    "Drank",
    "Ate",
    "Laughed",
    "Grew",
    "Slept",
    "Ran",
    "Thought",
    "Wrote",
    "Walked",
    "Talked",
]
present_tense_singular = [
    "Drinks",
    "Eats",
    "Grows",
    "Sleeps",
    "Runs",
    "Thinks",
    "Writes",
    "Walks",
    "Talks",
]
present_tense_plural = [
    "Drink",
    "Eat",
    "Grow",
    "Sleep",
    "Run",
    "Think",
    "Write",
    "Walk",
    "Talk",
]
future_tense = [
    "Will drink",
    "Will eat",
    "Will grow",
    "Will sleep",
    "Will run",
    "Will think",
    "Will write",
    "Will walk",
    "Will talk",
]
prepositions = [
    "about",
    "above",
    "across",
    "after",
    "along",
    "around",
    "at",
    "before",
    "behind",
    "below",
    "beyond",
    "by",
    "despite",
    "except",
    "for",
    "from",
    "in",
    "into",
    "near",
    "of",
    "off",
    "on",
    "onto",
    "out",
    "over",
    "past",
    "to",
    "under",
    "with",
    "without",
]


def get_determiner(quantity):
    if quantity == 1:
        return random.choice(single_determiners)
    else:
        return random.choice(plural_determiners)


def get_noun(quantity):
    if quantity == 1:
        return random.choice(single_nouns)
    else:
        return random.choice(plural_nouns)


def get_verb(quantity, tense):
    if tense == "past":
        return random.choice(verb_past)
    elif tense == "present" and quantity == 1:
        return random.choice(present_tense_singular)
    elif tense == "present" and quantity == 2:
        return random.choice(present_tense_plural)
    elif tense == "future":
        return random.choice(future_tense)


def get_preposition():
    return random.choice(prepositions)


def get_prepositional_phrase(quantity):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    preposition_word = get_preposition()
    return f"{preposition_word} {determiner} {noun}"


# Your other code for make_sentence and main goes here...
def make_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    return f"{determiner} {noun} {verb} {prepositional_phrase}."


def main():
    print(make_sentence(1, "past"))
    print(make_sentence(2, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(2, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "future"))


if __name__ == "__main__":
    main()
