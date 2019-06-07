def main(w):
    if len(w) == 0:
        return 0
    d = {}
    s = set()

    for i in range(len(w)):
        s.add(w[i])
    
    def helper(word, s, d):
        for i in range(len(word)):
            newword = word[:i] + word[i+1:] #remove one character
            if newword in s:
                if newword in d:
                    return d[newword]
                return helper(newword, s, d) + 1
        return 0

    longest = 0;
    for i in range(len(w)):
        lens = helper(w[i], s, d) + 1;
        d[w[i]] = lens;
        longest = max(longest, lens);
    print longest

if __name__ == '__main__':
    main(["abcd", "bcd", "bd", "defgh", "cd", "d"])
