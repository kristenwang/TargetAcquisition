################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, sys, inspect, thread, time
import Leap
import Tkinter as tk
import math

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack()

diameter = int(input('Enter distance(<700): '))
width = int(input('Enter width(<50): '))
center_x = 400
center_y = 400

IntBox_y=canvas.create_text(60,140,text='Y')
IntBox_x=canvas.create_text(60,120,text='X')
IntBox_z=canvas.create_text(60,160,text='Z')
IntBox_l=canvas.create_text(60,180,text=' ')

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

arc = [0]
for j in range (1,10):
    arc.append(canvas.create_oval(Posi_x[j]-width,Posi_y[j]-width,Posi_x[j]+width,Posi_y[j]+width,width=1,fill='grey'))

target_id = [0]
for i in range (1,10):
    target_id.append(canvas.create_text(Posi_x[i],Posi_y[i],text=i,font=("Purisa",60)))

def back_to_ori(target):
    global canvas, arc, Posi_x, width, Posi_y, target_id
    canvas.coords(arc[target],Posi_x[target]-width,Posi_y[target]-width,Posi_x[target]+width,Posi_y[target]+width)
    canvas.coords(target_id[target],Posi_x[target],Posi_y[target])

def bubble(target_num):
    global canvas, diameter, width, center_x, center_y
    for i in range (1,9):
        back_to_ori(i)
    if (target_num == 1):
        canvas.coords(arc[1],Posi_x[1]-2*width,Posi_y[1]-4*width,Posi_x[1]+3*width,Posi_y[1]+1*width)
        canvas.coords(target_id[1],Posi_x[1]+0.5*width,Posi_y[1]-1.5*width)
    elif (target_num == 2):
        canvas.coords(arc[2],Posi_x[2]-3*width,Posi_y[2]-2*width,Posi_x[2]+2*width,Posi_y[2]+3*width)
        canvas.coords(target_id[2],Posi_x[2]-0.5*width,Posi_y[2]+0.5*width)
    elif (target_num == 3):
        canvas.coords(arc[3],Posi_x[3]-1*width,Posi_y[3]-3.5*width,Posi_x[3]+4*width,Posi_y[3]+1.5*width)
        canvas.coords(target_id[3],Posi_x[3]+1.5*width,Posi_y[3]-1*width)
    elif (target_num == 4):
        canvas.coords(arc[4],Posi_x[4]-4*width,Posi_y[4]-2.4*width,Posi_x[4]+1*width,Posi_y[4]+2.6*width)
        canvas.coords(target_id[4],Posi_x[4]-1.5*width,Posi_y[4]-0*width)
    elif (target_num == 5):
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


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    
	
    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        point=frame.pointables.frontmost
        sleep_time=0.3
        global arc1,arc2,arc3,arc4,arc5,arc6,arc7,arc8,arc9
        global id1,id2,id3,id4,id5,id6,id7,id8,id9
        global canvas,IntBox_l,IntBox_x,IntBox_y,IntBox_z

        if point.is_valid:
            i_box=frame.interaction_box
            x_de=int(i_box.width)
            y_de=int(i_box.height)
            z_de=int(i_box.depth)
            leapoint=point.stabilized_tip_position
            normalizedPoint = i_box.normalize_point(leapoint, False)   
            def leap_to_world(self, leap_point, iBox):
                leap_point.z *= -1.0; #right-hand to left-hand rule
                normalized = iBox.normalize_point(leap_point, False)
                normalized = normalized + Leap.Vector(0.5, 0, 0.5); #recenter origin
                return normalized * 100.0; #scale
			
            app = leap_to_world(self,leapoint,i_box)
            canvas.itemconfig(IntBox_x,text='X in boundary')
            canvas.itemconfig(IntBox_y,text='Y in boundary')
            canvas.itemconfig(IntBox_z,text='Z in boundary')
            canvas.itemconfig(IntBox_l,text=' ')
        else:
            canvas.itemconfig(IntBox_l,text='Out of boundary')
            canvas.itemconfig(IntBox_x,text=' ')
            canvas.itemconfig(IntBox_y,text=' ')
            canvas.itemconfig(IntBox_z,text=' ')

        # Get hands
        for hand in frame.hands:
            hand_x=int(hand.palm_position.x+400)
            hand_z=int(500-hand.palm_position.y)
            hand_y=int(hand.palm_position.z)
            handnum=canvas.create_text(50,20,text="Hand number")
            handNumber=canvas.create_text(50,40,text=len(frame.hands))
            fingernum=canvas.create_text(50,60,text="Finger number")
            fingerNumber=canvas.create_text(50,80,text=len(frame.fingers))
            IntBox=canvas.create_text(50,100,text="Interactive Box")
            dot=canvas.create_oval(hand_x-2,hand_z-2,hand_x+3,hand_z+3,width=1,fill='white')
            distance9=pow((hand_x-Posi_x[9]),2)+pow((hand_z-Posi_y[9]),2)
            distance8=pow((hand_x-Posi_x[8]),2)+pow((hand_z-Posi_y[8]),2)
            distance7=pow((hand_x-Posi_x[7]),2)+pow((hand_z-Posi_y[7]),2)
            distance6=pow((hand_x-Posi_x[6]),2)+pow((hand_z-Posi_y[6]),2)
            distance5=pow((hand_x-Posi_x[5]),2)+pow((hand_z-Posi_y[5]),2)
            distance4=pow((hand_x-Posi_x[4]),2)+pow((hand_z-Posi_y[4]),2)
            distance3=pow((hand_x-Posi_x[3]),2)+pow((hand_z-Posi_y[3]),2)
            distance2=pow((hand_x-Posi_x[2]),2)+pow((hand_z-Posi_y[2]),2)
            distance1=pow((hand_x-Posi_x[1]),2)+pow((hand_z-Posi_y[1]),2)
            list_dis=[distance1,distance2,distance3,distance4,distance5,distance6,distance7,distance8,distance9]
            
            if (min(list_dis)==distance1):
                bubble(1)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc8, fill='#000000')
                    select1=canvas.create_text(500,10,text="1 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc8, fill='grey')
            elif (min(list_dis)==distance2):
                bubble(2)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc3, fill='#000000')
                    select2=canvas.create_text(500,20,text="2 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc3, fill='grey')
            elif (min(list_dis)==distance3):
                bubble(3)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc6, fill='#000000')
                    select3=canvas.create_text(500,30,text="3 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc6, fill='grey')				
            elif (min(list_dis)==distance4):
                bubble(4)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc5, fill='#000000')
                    select4=canvas.create_text(500,40,text="4 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc5, fill='grey')	
            elif (min(list_dis)==distance5):
                bubble(5)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc4, fill='#000000')
                    select5=canvas.create_text(500,50,text="5 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc4, fill='grey')	
            elif (min(list_dis)==distance6):
                bubble(6)
                if(point.direction.y < -0.5):
                    canvas.itemconfig(arc7, fill='#000000')
                    select6=canvas.create_text(500,60,text="6 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc7, fill='grey')	
            elif (min(list_dis)==distance7):
                bubble(7)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc2, fill='#000000')
                    select7=canvas.create_text(500,70,text="7 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc2, fill='grey')					
            elif (min(list_dis)==distance8):
                bubble(8)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc9, fill='#000000')
                    select8=canvas.create_text(500,80,text="8 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc9, fill='grey')	
            elif (min(list_dis)==distance9):
                bubble(9)                 
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc1, fill='#000000')
                    select9=canvas.create_text(500,90,text="9 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc1, fill='grey')

            canvas.delete(handNumber,fingerNumber,dot)

def main():

    person = input('Enter participant ID: ')

    with open('log.csv', 'w') as csvfile:
        fieldnames = ['ID', 'trial', 'time', 'click', 'location_x', 'location_y', 'target_hit']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    with open('log.csv', 'a') as f:
        write = csv.writer(f)
        write.writerow({'ID': person, 'trial': '1', 'time': int(time.time()), 'click':'1', 'location_x':1, 'location_y':1, 'target_hit':1})
        write.writerow({'ID': person, 'trial': '1', 'time': int(time.time()), 'click':'1', 'location_x':1, 'location_y':1, 'target_hit':2})
    
    # Create a sample listener and controller
    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
	
    root.mainloop()
	
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
	

if __name__ == "__main__":

    main()