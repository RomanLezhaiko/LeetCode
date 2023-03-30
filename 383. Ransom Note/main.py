def can_construct(ransomNote: str, magazine: str) -> bool:
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], '', 1)
            else:
                return False
        
        return True


print(can_construct('a', 'b'))
print(can_construct('aa', 'ab'))
print(can_construct('aa', 'aab'))