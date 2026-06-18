sentence=" Python Daily Practice "
count=0

for char in sentence.lower():
  if char in "aeiou":
    count+=1

print(" Total vowels:", count) 

#output:
# Total vowels:6
