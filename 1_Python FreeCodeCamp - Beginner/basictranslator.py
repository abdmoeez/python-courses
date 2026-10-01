def translate(phrase):
    translation = ""
    for index in phrase:
        if index in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + index
    return translation

print(translate(input("Enter a phrase: ")))