import time
from tkinter import *
from PIL import ImageTk, Image
import time

count = 0
print("For this question you'll need to guess the car in the image. . .")
time.sleep(1)
window = Tk()
window.geometry("500x500")
window.title("Guess this car")
car = Image.open('pagani_zonda1.png')
resized = car.resize((1000, 400), Image.ANTIALIAS)
new_start = ImageTk.PhotoImage(resized)
my_label = Label(window, image=new_start)
my_label.pack(pady=20)
window.mainloop()

answer_six = input('What car is this? (name and model)').lower()
answer_list = set(answer_six)
answer = ['p', 'a', 'g', 'a', 'n', 'i', ' ', 'z', 'o', 'n', 'd', 'a']
if len(answer_six) > 15:
    print("incorrect -1 life")
    a = a - 1
elif len(answer_six) < 15:
    for i in answer_list:
        if i in answer:
            count += 1
            if count >= 7:
                print("Correct! +3 points")
            else:
                print("incorrect -1 life")
            
        else:
            break
else:
    print("Inavlid response! -1 life")
print(count)
