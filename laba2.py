name1 = 'Angelina'
password1 = '1234'
grades1 = [12, 10, 10, 7]

name2 = 'Sofia'
password2 = '1111'
grades2 = [5, 6, 2, 10]

name3 = 'Ivan'
password3 = '2222'
grades3 = [11, 9,12, 8]

name4 = 'Max'
password4 = '3333'
grades4 = [4, 3, 5, 1]

print('------------------------------')
print(' Перевірка оцінок чотирьох студентів')
print('------------------------------')

name = input("Введіть ім'я студента ")
password = input("Введіть пароль студента ")
grades = {}

if name == name1 and password == password1:
    grades = grades1
elif name ==name2 and password == password2:
    grades = grades2
elif name ==name3 and password == password3:
    grades = grades3
elif name == name4 and password == password4:
    grades = grades4
else:
    print("Неправильне ім'я або пароль ")

if len(grades) > 0:
    print("Оцінки студентa: ", grades)
    good = 0
    bad = 0
    for grade in grades:
        
        if 5 <= grade <=12:
            good += 1
        elif 1 <= grade <= 4:
            bad += 1
        else:
            print('Wrong')
print('Задовільні - : ', good , 'оц.')
print('Незадовільні - : ', bad, 'оц.')


   
    
    
    
