def censor(text, word):
    new = copy(text)
    for i in range(len(text)):
        for j in range(len(word)):
            if text[i+j] != word[j]:
                break
        else:
            for j in range(len(word)):
                new[i+j]
    return new
print censor('Ah Ah','Ah')
