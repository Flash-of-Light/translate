def translate(word):
    translation = ""
    for letter in word:
        if letter in "aeiouAEIOU":
            translation = translation + "x"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))