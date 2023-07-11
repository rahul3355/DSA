def groupAnagrams(words):
    # Write your code here.
    anagrams = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)

        else:
            anagrams[sortedWord] = [word]

    return list(anagrams.values())
