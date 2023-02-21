import random

word = ['chaos', 'datascience', 'factory', 'chauffer']
lives = 5
score = 0

def update_clue(guess, clue, secret_word):
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            clue[i] = guess
        elif guess == secret_word:
            clue = guess   
    winner = ''.join(clue) == secret_word
    
    return winner  

def fun_hint(guess, secret_word):
    word_dict = {
        'chaos': 'ความวุ่นวาย',
        'datascience': 'วิทยาการข้อมูล',
        'factory': 'โรงงาน',
        'chauffer': 'คนขับรถ'
    }
    if guess == 'hint':
        for key in word_dict:
            if key == secret_word:
                word_hint = [word_dict[key]]
    return word_hint

def each_guess_in_secret_word(guess, clue, secret_word):
    for i in range(len(guess)):
        for j in range(len(secret_word)):
            if guess[i] == secret_word[j]:
                keep_word += (guess[i])
        
while(len(word) > 0 and lives > 0 ):
    #สับไพ่และใบ้เบาะแส
    print('ชีวิตที่เหลือ : ' + str(lives))
    print('มีคะแนนรวมทั้งหมด : ' + str(score))
    random.shuffle(word)
    secret_word = word.pop()
    clue = list('?'*len(secret_word))
    while(True):
        print(clue)
        guess = input('เดาคำมาสิ : ' )
        print(guess[0])
        print('                           ')
        #ถ้าคำที่ทายมายังไม่หมด
        if guess in secret_word:
            print("It's correct") 
            winner = update_clue(guess, clue, secret_word)
            #ถ้าทายคำหมดแล้วให้เพิ่มscoreเป็น 1 
            #if guess in secret_word:
            check_each_guess = each_guess_in_secret_word(guess, clue, secret_word)



            if guess == secret_word:
                winner = update_clue(guess, clue, secret_word)
                #ถ้าทายคำหมดแล้วให้เพิ่มscoreเป็น 1 
                if winner:
                    score = score + 1  
                    print('เย้ ได้scoreแล้วว : ' + str(score))
                    print('คำนั้นคือ : ' + guess) 
                    break    
            elif winner:
                score = score + 1  
                print('เย้ ได้scoreแล้วว : ' + str(score))
                print(''.join(clue)) 
                break     
        #ถ้าคำที่ทายมายังไม่หมดและทายผิด
        elif guess == 'hint':
            word_hint = fun_hint(guess, secret_word)
            if word_hint:
                print('คำที่ใบ้ : ' + str(word_hint))
        else:  
            lives = lives - 1
            print('ว้ายตายแล้วคร้าบเสียไป 1 ชีวิตเลยเหลือ : ' +str(lives))
        if lives <= 0 :
            print('นายแพ้แล้วล่ะ เกมจบแล้ว')
            break 
print('GOOD GAME AND GOOD BYE BRO!!!!!!!!!')








































































