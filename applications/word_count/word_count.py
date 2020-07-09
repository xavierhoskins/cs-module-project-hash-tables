def word_count(s):
    # Your code here

    word_counter = {}

    for w in s:
        w = w.lower()
        if w in word_counter:
            # for each consecutive letter add + 1
            word_counter[w] += 1
        else:
            #if letter appears once set it to 1
            word_counter[w] = 1

    return word_counter

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))