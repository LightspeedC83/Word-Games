words = []
with open("gutenburg.txt", "r") as f:
    for line in f.read().split():
        words.append(line.strip())



with open("10k_word_repository.txt", "w") as f:
    for x in words:
        if x.isalpha() and "'" not in x:
            f.write(x+"\n")

print("done")
