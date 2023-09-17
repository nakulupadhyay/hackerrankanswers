import random
word=('math','fill','full','come','kite','both','girl','king','cool','born','form','with','know','crow','knee','here','ball','moon','mars',
      'roof','home','away','file','like','also','love','cute','each','more','list','five','four','kind','thin','pain','bond','word','late',
      'hour','soap','tank','high','time','rate','turn','look')
print('HELLO USER!!')
print('WELCOME TO THE WORD OF JUMBLE WORD')
word=random.choice(word)
point=0
for i in range(5):
    qno=random.randrange(1,81)
    org=word
    word=list(word)
    random.shuffle(word)
    ans=input("enter your guess ")
    ans=ans.lower()
    if ans==org:
        point=point+100
        print('your answer is correct')
        print("-"*100)
        continue
    else:
        print('the word start with',org[0])
        ans=input("enter your guess ")
        ans=ans.lower()

        if ans==org:
            point=point+50
            print("your answer is correct")
        else:
            print('the word end with',org[-1])
            ans=input("enter your guess")
            ans=ans.lower()
            if ans==org:
                point=point+25
                print('your answer is correct')
            else:
                print("game is over")
    print("your score is",point)
    break
