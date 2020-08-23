frnd1='bhavesh'
frnd2='medhank'

# calculate the sum of ASCII number of friend 1
frndcount1=0
for letter in frnd1:
    frndcount1+=ord(letter)
print(frndcount1)

# calculate the sum of ASCII number of friend 1
frndcount2=0
for letter in frnd2:
    frndcount2+=ord(letter)
print(frndcount2)

# divding it by the total sum of ascii from a-z i.e 2727
percent=((frndcount1+frndcount2)/2727)*100
print(f"Percentage of your Friendship is :- {int(percent)}%")



