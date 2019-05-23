m1 = float(input('Enter Your English marks : '))
m2 = float(input('Enter Your Hindi marks : '))
m3 = float(input('Enter Your Science marks : '))
m4 = float(input('Enter Your SST marks : '))
m5 = float(input('Enter Your Maths marks : '))
percentage = ((m1+m2+m3+m4+m5)/500) * 100 
if (percentage >= 90 and percentage <=100):
    print('You have got ' + str(percentage)  + ' And you have got A+')
elif(percentage >=80 and percentage <=90 ):
    print('You have got ' + str(percentage)  + ' And you have got A grade')
elif(percentage >=70 and percentage <=80):
    print('You have got ' + str(percentage)  + ' And you have got B+')
elif(percentage >=60 and percentage <=70):
     print('You have got ' + str(percentage)  + 'And you have got B')
elif(percentage >=55 and percentage <=60):
    print('You have got ' + str(percentage)  + ' And you have got C+')
elif(percentage >=50 and percentage <=55):
    print('You have got ' + str(percentage)  + ' And you have got C')
elif(percentage >=45 and percentage <=50):
    print('You have got ' + str(percentage)  + ' And you have got D+')
elif(percentage >=40 and percentage <=45):
    print('You have got ' + str(percentage)  + ' And you have got D')
elif(percentage >=33 and percentage <=40):
    print('You have got ' + str(percentage)  + ' And you have got E')
elif(percentage <33):
    print('You have got ' + str(percentage)  + ' And you are fail')
else: 
    print('You have entered wrong marks')
import time
time.sleep(300)