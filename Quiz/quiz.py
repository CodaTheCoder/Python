print("Hi Welcome to the quiz")
score = 0

likeToPlay = input("Do you want to play my Quiz about Coding [yes/no]")

if likeToPlay == "yes":
    print("Ok here we go!")

else:
    print("Sorry See you later!")
    quit()

firstQ = input("What is one of the first Programming Languages to exist?")

if firstQ == "Basic":
    print("Nice you got that Correct Well done")
    score += 1

else:
    print("I don't think that is correct sorry")
    score -= 1

SecondQ = input("Complete The Sentence I use Azure ___ OPS")

if SecondQ == "Dev":
    print("Nice you know Your Stuff")
    score += 1

else:
    print("Maybe another time you'll get that right")
    score -= 1

ThirdQ = input("What does HTML stand for? Don't press Space")

if ThirdQ == "HyperTextMarkupLanguage" : 
    print("Correct Nice :)")
    score += 1

else:
    print("Wrong -1 from the score buddy")
    score -= 1

FourthQ = input("And the final Question, Do you Program [yes/no]?")

if FourthQ == "yes":
    print("Man your a true Programer")
    score += 1

else:
    print("You Don't! I'll give you a point though!")
    score += 1

print("And your score is")
print(score)
print("Anyways GoodBye!")


