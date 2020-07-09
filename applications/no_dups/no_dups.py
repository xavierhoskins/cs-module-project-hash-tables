def no_dups(s):
    # Your code here

    if len(s) < 1:
        # returns empty string
        return ""
    else:
        cache = {}
        # splits string into a list/array each word is an index
        s = s.split(" ")
        for i in s:
            cache[i] = i
        # .join() combines each index back into a string.
        # .keys() displays list of all keys in dictionary
        return " ".join(list(cache.keys()))


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))