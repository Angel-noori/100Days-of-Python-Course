print("Welcome to Kaun Banega Crorepati! Let's play Zidi Game!\nBelow, you'll be asked questions and you have to choose from the option 'A', 'B', 'C', 'D'\n")
flag = True
n = 2
amount = 0;

# Used while conditions cases for questioning with options by Zidi
while(n>0):
  print("What is the capital city of Pakistan")
  print(" A. Islamabad\n B. Karachi\n C. Lahore\n D. Peshawar")
  op = input("Your option?: ").lower()

  if op != "a":
    print("Sorry, That's a wrong answer. You won", amount)
    flag = False
    break;

  else:
    amount += 10000
    print("Congrats! You won", amount, "\n")
    n -= 1

  if(flag):
    print("What is the meaning of Pakistan?")
    print(" A. Muslim Land\n B. Desert\n C. Land of five rivers\n D. Holy Land")
    op = input("Your option?: ").lower()

    if op != "d":
      print("Sorry, That's a wrong answer. You won", amount)
      flag = False
      break;

    else:
      amount += 10000
      print("Congrats! You won", amount, "\n")
      n -= 1

    if(flag):
      print("Who designed Pakistan’s national flag?")
      print(" A. Fatima Jinnah\n B. Wali Khan\n C. Ameer-ud-din Khidwai\n D. Tika Khan")
      op = input("Your option?: ").lower()
  
      if op != "c":
        print("Sorry, That's a wrong answer. You won", amount)
        flag = False
        break;
  
      else:
        amount += 10000
        print("Congrats! You won", amount, "\n")
        n -= 1

print("Total amount won is: ", amount)