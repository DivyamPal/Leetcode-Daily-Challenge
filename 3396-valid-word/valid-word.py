class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = 'aeiouAEIOU'
        vflag, cflag = False, False

        for i in word:
            if i.isalpha():
                if i in vowels:
                    vflag = True
                else:
                    cflag = True
            elif not i.isdigit():
                return False

        return vflag and cflag

