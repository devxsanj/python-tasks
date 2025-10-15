def countVowels(word):
    vowels = "aeiouAEIOU"
    count = 0
    
    for char in word:
        if char in vowels:
            count += 1
        else:
            print(f"'{char}'is not a vowel.")
            
    return count
        
print(countVowels("sanjana"))