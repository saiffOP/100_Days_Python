# def add(*args):
#     a = 0
#     for n in args:
#         a = a + n
#     print(a)
#
#
# add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

import pywhatkit as kit
import smtplib

number = "+919370299894"

kit.sendwhatmsg(
    number,
    "Python code likha hu usse aaya hai ye msg", 23, 56
)
