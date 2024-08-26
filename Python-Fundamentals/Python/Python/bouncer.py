# ask for age

age = input("How old are you: ")
if age:
   if int(age) >= 18 and int(age) < 21:
       # 18-21 wristband
       print("You can enter, but need a wristband!")
   elif int(age) >= 21:
       # 21+ drink, normal entry
       print("You are good to enter and can drink!")
   else:
       # too young, sorry
       print("You can't come in, little one ! :(")
else:
    print("Please enter an age!")
    