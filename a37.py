# Division obtained by the student.

a, b, c, d, e = input('enter the marks of subject out of 50 :').split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)

percentage = (a + b + c + d + e) / 500 * (100)
if a <= 100 and b <= 100 and c <= 100 and d <= 100 and e <= 100:
    if percentage >= 60:
        print('student get first division.')
    elif 50 <= percentage <= 59:
        print('student get second division.')
    elif 40 <= percentage <= 49:
        print('student get third division.')
    elif percentage < 40:
        print('failed')
else:
    print("Entered marks are not out of 50.")
