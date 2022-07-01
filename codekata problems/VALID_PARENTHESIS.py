def check_expression(string, lists=[]):
    for i in string:
        if i in dict.keys():
            if lists != [] and lists[-1] == dict[i]:
                lists.pop()
            else:
                return "NOT VALID EXPRESSION"
                break
        else:
            lists.append(i)
    return "VALID EXPRESSION"


if __name__ == "__main__":
    testcase = ["{{}[][[[]]]}", "()", "()[]{}", "(]", "[[[]]]"]
    dict = {"}": "{",

            ")": "(",

            "]": "["}
    for i in testcase:
        print(f"THE STRING {i}   --------",check_expression(i, lists=[]))
        print()