class Solution:
    def reverseWords(self, s: str) -> str:
        i = 0
        tmp = ""
        s_list = []
        while (i < len(s)):
            print(tmp)
            if (s[i] == " "):
                s_list.append(tmp)
                tmp = ""
                i += 1
                continue
            tmp = s[i] + tmp
            i += 1
        s_list.append(tmp)
        print(s_list)
        return (" ".join(s_list))