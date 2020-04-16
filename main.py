# print('Welcome World')
# voter_list = ['muhammed' , 'darpan,' , 'manish']
# print('hey user, Please ENTER YOUR NAME FOR VERIFICATION')
# name = input()

# if name in voter_list:
    # print('hey ' + name + ', You are Eligible for vote here')
# else:
    # print('Hey ' + name + ',You are Not eligible for vote here')    

# marks_of_physics = [2 , 4 , 6 , 8]
# print('no of students are:' , len(marks_of_physics)) 
# for marks in range(0, len(marks_of_physics)):
#     print('student ' + str(marks+1) + ' marks :',marks_of_physics[marks])

# student_list = [22,24,25,26]
# print(student_list)


# for num in range(0,100,2):
#     print(num)

# from gtts import gTTS
# speak = gTTS('Hi Nayeem Kaise Ho aap')
# speak.save('welcome.mp3')

import random

print('enter number')
num = input()

print('Your OTP is :')
for i in range(6):
    otp = random.choice(num)
    print(otp, end='')