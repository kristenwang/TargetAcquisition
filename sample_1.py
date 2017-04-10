import os, sys, time
import tkinter as tk
import math
import csv


diameter = int(input('Enter distance(<700): '))
width = int(input('Enter width(<50): '))
center_x = 400
center_y = 400
person = input('Enter participant ID: ')

Posi_x = [0,center_x - (diameter/2*math.sin(2/18*math.pi)),center_x + (diameter/2*math.sin(4/18*math.pi)),center_x - (diameter/2*math.cos(3/18*math.pi)),center_x + (diameter/2*math.cos(1/18*math.pi)),center_x - (diameter/2*math.cos(1/18*math.pi)),center_x + (diameter/2*math.cos(3/18*math.pi)),center_x - (diameter/2*math.sin(4/18*math.pi)),center_x + (diameter/2*math.sin(2/18*math.pi)),center_x]
Posi_y = [0]
Posi_y.append(center_y + (diameter/2*math.cos(2/18*math.pi)))
Posi_y.append(center_y - (diameter/2*math.cos(4/18*math.pi)))
Posi_y.append(center_y + (diameter/2*math.sin(3/18*math.pi)))
Posi_y.append(center_y - (diameter/2*math.sin(1/18*math.pi)))
Posi_y.append(center_y - (diameter/2*math.sin(1/18*math.pi)))
Posi_y.append(center_y + (diameter/2*math.sin(3/18*math.pi)))
Posi_y.append(center_y - (diameter/2*math.cos(4/18*math.pi)))
Posi_y.append(center_y + (diameter/2*math.cos(2/18*math.pi)))
Posi_y.append(center_y - (diameter/2))

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg="white")

arc = [0]
for j in range (1,10):
    arc.append(canvas.create_oval(Posi_x[j]-width,Posi_y[j]-width,Posi_x[j]+width,Posi_y[j]+width,width=1,fill='grey'))

target_id = [0]
for i in range (1,10):
    target_id.append(canvas.create_text(Posi_x[i],Posi_y[i],text=i,font=("Purisa",60)))

def startNew():
    global arc, target_id
    #canvas.delete(arc,target_id)
    for j in range (1,10):
        canvas.coords(arc[j],Posi_x[j]-width,Posi_y[j]-width,Posi_x[j]+width,Posi_y[j]+width)
        canvas.itemconfig(arc[j], fill='grey')
        canvas.coords(target_id[j],Posi_x[j],Posi_y[j])
    with open('log.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow(['ID', 'trial', 'time', 'click', 'location_x', 'location_y', 'target_hit'])
    f.close()

#frame = tk.Frame(root, bg='grey', width=800, height=40)
#frame.pack(fill='x')
button1 = tk.Button(root, text='new trial',command=startNew)
button1.pack(side='top', padx=20)
canvas.pack()

def back_to_ori(target):
    global canvas, arc, Posi_x, width, Posi_y, target_id
    canvas.coords(arc[target],Posi_x[target]-width,Posi_y[target]-width,Posi_x[target]+width,Posi_y[target]+width)
    canvas.coords(target_id[target],Posi_x[target],Posi_y[target])

def bubble(target_num):
    global canvas, diameter, width, center_x, center_y
    for i in range (1,9):
        back_to_ori(i)
    if (target_num == 1):
        with open('log.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow([person, '1', int(time.time()), '1', 1, 1, 1])
        f.close()
        canvas.coords(arc[1],Posi_x[1]-2*width,Posi_y[1]-4*width,Posi_x[1]+3*width,Posi_y[1]+1*width)
        canvas.coords(target_id[1],Posi_x[1]+0.5*width,Posi_y[1]-1.5*width)
    elif (target_num == 2):
        with open('log.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow([person, '1', int(time.time()), '1', 1, 1, 2])
        f.close()
        canvas.coords(arc[2],Posi_x[2]-3*width,Posi_y[2]-2*width,Posi_x[2]+2*width,Posi_y[2]+3*width)
        canvas.coords(target_id[2],Posi_x[2]-0.5*width,Posi_y[2]+0.5*width)
    elif (target_num == 3):
        with open('log.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow([person, '1', int(time.time()), '1', 1, 1, 3])
        f.close()
        canvas.coords(arc[3],Posi_x[3]-1*width,Posi_y[3]-3.5*width,Posi_x[3]+4*width,Posi_y[3]+1.5*width)
        canvas.coords(target_id[3],Posi_x[3]+1.5*width,Posi_y[3]-1*width)
    elif (target_num == 4):
        with open('log.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow([person, '1', int(time.time()), '1', 1, 1, 4])
        f.close()
        canvas.coords(arc[4],Posi_x[4]-4*width,Posi_y[4]-2.4*width,Posi_x[4]+1*width,Posi_y[4]+2.6*width)
        canvas.coords(target_id[4],Posi_x[4]-1.5*width,Posi_y[4]-0*width)
    elif (target_num == 5):
        with open('log.csv', 'a') as f:
            write = csv.writer(f)
            write.writerow([person, '1', int(time.time()), '1', 1, 1, 5])
        f.close()
        canvas.coords(arc[5],Posi_x[5]-1*width,Posi_y[5]-2.4*width,Posi_x[5]+4*width,Posi_y[5]+2.6*width)
        canvas.coords(target_id[5],Posi_x[5]+1.5*width,Posi_y[5]-0*width)
    elif (target_num == 6):
        canvas.coords(arc[6],Posi_x[6]-3.5*width,Posi_y[6]-3*width,Posi_x[6]+1.5*width,Posi_y[6]+2*width)
        canvas.coords(target_id[6],Posi_x[6]-1*width,Posi_y[6]-0.5*width)
    elif (target_num == 7):
        canvas.coords(arc[7],Posi_x[7]-2*width,Posi_y[7]-2*width,Posi_x[7]+3*width,Posi_y[7]+3*width)
        canvas.coords(target_id[7],Posi_x[7]+0.5*width,Posi_y[7]+0.5*width)
    elif (target_num == 8):
        canvas.coords(arc[8],Posi_x[8]-3*width,Posi_y[8]-4*width,Posi_x[8]+2*width,Posi_y[8]+1*width)
        canvas.coords(target_id[8],Posi_x[8]-0.5*width,Posi_y[8]-1.5*width)
    elif (target_num == 9):
        canvas.coords(arc[9],Posi_x[9]-2.5*width,Posi_y[9]-1*width,Posi_x[9]+2.5*width,Posi_y[9]+4*width)
        canvas.coords(target_id[9],Posi_x[9]-0*width,Posi_y[9]+1.5*width)

def main():

    with open('log.csv', 'w') as csvfile:
        fieldnames = ['ID', 'trial', 'time', 'click', 'location_x', 'location_y', 'target_hit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    csvfile.close()
    bubble(1)
    bubble(2)
    bubble(3)
    bubble(4)
    bubble(5)
    bubble(6)
    bubble(7)
    bubble(8)
    bubble(9)
    root.mainloop()


if __name__ == "__main__":

    main()
