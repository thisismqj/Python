def isMatch(s: str, p: str) -> bool:
    index = 0
    index_max = len(s)
    wrong_flag = False
    for this in range(len(p)):
        if index == index_max:
            return False
        if p[this] == "*":
            if wrong_flag:
                index += 1
                wrong_flag = False
                continue
            if p[this-1] == ".":
                index = index_max
                continue
            for each in s[index-1:]:
                if each != p[this-1]:
                    index -= 1
                    break
                else:
                    index += 1
            continue
        if p[this] == s[index] or p[this] == ".":
            index += 1
        else:
            if wrong_flag:
                return False
            wrong_flag = True

    if index < index_max:
            return False
    return True
isMatch("aaa", "a*a")