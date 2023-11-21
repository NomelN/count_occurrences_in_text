import cProfile


"""In order to run the tests simply run

python -m pytest a9number_v3.py

In order to see the profiling, you need to add the option -s
"""

def count_occurrences_in_text(word, text):
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    # TODO: your code goes here, but it's OK to add new functions or import modules if needed
    
    word_count = 0  # Initialize a counter for the occurrences of the word
    len_word = len(word)  # Length of the word
    len_text = len(text)  # Length of the text
    i = 0  # Initialize an index to traverse the text

    # Remove text markdown (non-alphabetic characters) from the start of the text
    while (i < len_text and text[i].isalpha() == False) and (text[i] == text[len_text - 1]):
        i += 1
        len_text -= 1
    start = i

    # Count matching word in text separated by non-alphabetic or "'" characters
    while i < len_text:
        j = 0  # Initialize an index to traverse the word
        if i == start or (text[i - 1].isalpha() == False and text[i - 1] != "'"):
            # Check if the current character is the start or is separated by non-alphabetic or "'" character
            while (j < len_word and i < len_text) and (word[j].lower() == text[i].lower()):
                # Check if characters in the word match characters in the text (case-insensitive)
                i += 1
                j += 1
            if j == len_word and (i == len_text or (text[i].isalpha() == False and text[i] != "'")):
                # If the entire word is matched and the next character is non-alphabetic or "'", increment the counter
                word_count += 1
        if j == 0:
            i += 1  # Move to the next character if no match is found in the current iteration

    # This does pass the unittests:
    return word_count


def test_count_occurrences_in_text():
    text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
Yes is is true, I like PYTHON
and my name is GEORGES"""
    # test with a little text.
    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    # regard ' as text:
    assert 0 == count_occurrences_in_text("maley", "John O'maley is my friend")

    # Test it but with a BIG length file.
    text = """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """The quick brown fox jump over the lazy dog.The quick brown Georges jump over the lazy dog."""
    text += """esrf sqfdg sfdglkj sdflgh sdflgjdsqrgl """ * 4000
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy python."""
    text += """The quick brown fox jump over the true lazy dog.The quick brown fox jump over the lazy dog."""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500
    text += """ I vsfgsdfg sfdg sdfg sdgh sgh I sfdgsdf"""
    text += """The quick brown fox jump over the lazy dog.The quick brown fox jump over the lazy dog.""" * 500

    assert 3 == count_occurrences_in_text("Georges", text)
    assert 3 == count_occurrences_in_text("GEORGES", text)
    assert 3 == count_occurrences_in_text("georges", text)
    assert 0 == count_occurrences_in_text("george", text)
    assert 3 == count_occurrences_in_text("python", text)
    assert 3 == count_occurrences_in_text("PYTHON", text)
    assert 2 == count_occurrences_in_text("I", text)
    assert 0 == count_occurrences_in_text("n", text)
    assert 1 == count_occurrences_in_text("true", text)
    assert 1 == count_occurrences_in_text(
        "'reflexion mirror'", "I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida"
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror", "I am a senior citizen and I live in the Fun-Plex (Reflexion Mirror) in Sopchoppy, Florida"
    )
    assert 1 == count_occurrences_in_text("reflexion mirror", "Reflexion Mirror\" in Sopchoppy, Florida")
    assert 1 == count_occurrences_in_text(
        "reflexion mirror", "I am a senior citizen and I live in the Fun-Plex «Reflexion Mirror» in Sopchoppy, Florida"
    )
    assert 1 == count_occurrences_in_text(
        "reflexion mirror",
        "I am a senior citizen and I live in the Fun-Plex \u201cReflexion Mirror\u201d in Sopchoppy, Florida"
    )
    assert 1 == count_occurrences_in_text(
        "legitimate", "who is approved by OILS is completely legitimate: their employees are of legal working age"
    )
    assert 0 == count_occurrences_in_text(
        "legitimate their", "who is approved by OILS is completely legitimate: their employees are of legal working age"
    )
    assert 1 == count_occurrences_in_text(
        "get back to me", "I hope you will consider this proposal, and get back to me as soon as possible"
    )
    assert 1 == count_occurrences_in_text(
        "skin-care", "enable Delavigne and its subsidiaries to create a skin-care monopoly"
    )
    assert 1 == count_occurrences_in_text(
        "skin-care monopoly", "enable Delavigne and its subsidiaries to create a skin-care monopoly"
    )
    assert 0 == count_occurrences_in_text(
        "skin-care monopoly in the US", "enable Delavigne and its subsidiaries to create a skin-care monopoly"
    )
    assert 1 == count_occurrences_in_text("get back to me", "When you know:get back to me")
    assert 1 == count_occurrences_in_text(
        "don't be left", """emergency alarm warning.
Don't be left unprotected. Order your SSSS3000 today!"""
    )
    assert 1 == count_occurrences_in_text(
        "don", """emergency alarm warning.
Don't be left unprotected. Order your don SSSS3000 today!"""
    )
    assert 1 == count_occurrences_in_text("take that as a 'yes'", "Do I have to take that as a 'yes'?")
    assert 1 == count_occurrences_in_text("don't take that as a 'yes'", "I don't take that as a 'yes'?")
    assert 1 == count_occurrences_in_text("take that as a 'yes'", "I don't take that as a 'yes'?")
    assert 1 == count_occurrences_in_text("don't", "I don't take that as a 'yes'?")
    assert 1 == count_occurrences_in_text("attaching my c.v. to this e-mail", "I am attaching my c.v. to this e-mail.")
    assert 1 == count_occurrences_in_text("Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''")
    assert 1 == count_occurrences_in_text(
        "Linguist Specialist", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text(
        "Laboratory Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''"
    )
    assert 1 == count_occurrences_in_text("Floor", "'''Linguist Specialist Found Dead on Laboratory Floor'''")
    assert 1 == count_occurrences_in_text("Floor", "''Linguist Specialist Found Dead on Laboratory Floor''")
    assert 1 == count_occurrences_in_text("Floor", "__Linguist Specialist Found Dead on Laboratory Floor__")
    assert 1 == count_occurrences_in_text("Floor", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''")
    assert 1 == count_occurrences_in_text("Linguist", "'''Linguist Specialist Found Dead on Laboratory Floor'''")
    assert 1 == count_occurrences_in_text("Linguist", "''Linguist Specialist Found Dead on Laboratory Floor''")
    assert 1 == count_occurrences_in_text("Linguist", "__Linguist Specialist Found Dead on Laboratory Floor__")
    assert 1 == count_occurrences_in_text("Linguist", "'''''Linguist Specialist Found Dead on Laboratory Floor'''''")


SAMPLE_TEXT_FOR_BENCH = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
Bob Carter
"""


def doit():
    """
    Run count_occurrences_in_text on a few examples
    """
    i = 0
    for x in range(400):
        i += count_occurrences_in_text("word", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("sugar", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("help", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("heavily", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("witfull", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("dog", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("almost", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("insulin", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("attaching", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("asma", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("neither", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("won't", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("green", SAMPLE_TEXT_FOR_BENCH)
        i += count_occurrences_in_text("parabole", SAMPLE_TEXT_FOR_BENCH)
    return i


def test_profile():
    with cProfile.Profile() as pr:
        assert doit() == 2000
        pr.print_stats()
