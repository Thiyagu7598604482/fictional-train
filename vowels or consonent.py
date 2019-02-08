chth=str(input())
vowel=("a","e","i","o","u")
if(chth>="a"and chth<="z" or chth>="A" and chth<="Z"):
  if chth in vowel:
    print("Vowel")
  else:
    print("Consonant")  
else:
  print("invalid") 
