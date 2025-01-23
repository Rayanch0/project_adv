def Ask_Questions(data) :
   for qst in data : 
       print(qst["question"])
       for opt in qst["options"] :
           print("\t",opt)

       while True :
            answer = input("choose an answer : ") 
            if answer in ["a" , "b" , "c" ] :
                if verify_answer(data , qst["question"] , answer) :
                   global score
                   score += 1
                   break   
                else :
                     print("Wrong answer ")
                     print(f"Correct answer is : {qst['answer']}")
                     break
               
            else :
                    print("Please choose a valid answer")