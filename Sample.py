################################################################################
# Copyright (C) 2012-2016 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, sys, inspect, thread, time
src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
#arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))

sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap
import Tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

arc1=canvas.create_oval(270,90,330,150,width=1,fill='grey')
arc2=canvas.create_oval(120,150,180,210,width=1,fill='grey')
arc3=canvas.create_oval(420,150,480,210,width=1,fill='grey')
arc4=canvas.create_oval(50,260,110,320,width=1,fill='grey')
arc5=canvas.create_oval(490,260,550,320,width=1,fill='grey')
arc6=canvas.create_oval(70,390,130,450,width=1,fill='grey')
arc7=canvas.create_oval(470,390,530,450,width=1,fill='grey')
arc8=canvas.create_oval(180,500,240,560,width=1,fill='grey')
arc9=canvas.create_oval(360,500,420,560,width=1,fill='grey')
id1=canvas.create_text(300,120,text="9",font=("Purisa",60))
id2=canvas.create_text(150,180,text="7",font=("Purisa",60))
id3=canvas.create_text(450,180,text="2",font=("Purisa",60))
id4=canvas.create_text(80,290,text="5",font=("Purisa",60))
id5=canvas.create_text(520,290,text="4",font=("Purisa",60))
id6=canvas.create_text(100,420,text="3",font=("Purisa",60))
id7=canvas.create_text(500,420,text="6",font=("Purisa",60))
id8=canvas.create_text(210,530,text="1",font=("Purisa",60))
id9=canvas.create_text(390,530,text="8",font=("Purisa",60))
IntBox_y=canvas.create_text(60,140,text='Y')
IntBox_x=canvas.create_text(60,120,text='X')
IntBox_z=canvas.create_text(60,160,text='Z')
IntBox_l=canvas.create_text(60,180,text=' ')

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
            hand_x=int(hand.palm_position.x+307)
            hand_z=int(500-hand.palm_position.y)
            hand_y=int(hand.palm_position.z)
            handnum=canvas.create_text(50,20,text="Hand number")
            handNumber=canvas.create_text(50,40,text=len(frame.hands))
            fingernum=canvas.create_text(50,60,text="Finger number")
            fingerNumber=canvas.create_text(50,80,text=len(frame.fingers))
            IntBox=canvas.create_text(50,100,text="Interactive Box")
            dot=canvas.create_oval(hand_x-2,hand_z-2,hand_x+3,hand_z+3,width=1,fill='white')
            distance9=pow((hand_x-300),2)+pow((hand_z-120),2)
            distance8=pow((hand_x-390),2)+pow((hand_z-530),2)
            distance7=pow((hand_x-150),2)+pow((hand_z-180),2)
            distance6=pow((hand_x-500),2)+pow((hand_z-420),2)
            distance5=pow((hand_x-70),2)+pow((hand_z-290),2)
            distance4=pow((hand_x-520),2)+pow((hand_z-290),2)
            distance3=pow((hand_x-100),2)+pow((hand_z-420),2)
            distance2=pow((hand_x-450),2)+pow((hand_z-180),2)
            distance1=pow((hand_x-210),2)+pow((hand_z-530),2)
            list_dis=[distance1,distance2,distance3,distance4,distance5,distance6,distance7,distance8,distance9]
            
            if (min(list_dis)==distance1):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,140,360,340,560)
                canvas.coords(id8,240,460)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc8, fill='#000000')
                    select1=canvas.create_text(500,10,text="1 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc8, fill='grey')
            elif (min(list_dis)==distance2):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,300,120,500,320)
                canvas.coords(id3,400,220)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc3, fill='#000000')
                    select2=canvas.create_text(500,20,text="2 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc3, fill='grey')
            elif (min(list_dis)==distance3):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,300,270,500)
                canvas.coords(id6,170,400)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc6, fill='#000000')
                    select3=canvas.create_text(500,30,text="3 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc6, fill='grey')				
            elif (min(list_dis)==distance4):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,360,210,560,410)
                canvas.coords(id5,460,310)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc5, fill='#000000')
                    select4=canvas.create_text(500,40,text="4 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc5, fill='grey')	
            elif (min(list_dis)==distance5):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,40,200,240,400)
                canvas.coords(id4,140,300)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc4, fill='#000000')
                    select5=canvas.create_text(500,50,text="5 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc4, fill='grey')	
            elif (min(list_dis)==distance6):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,330,300,530,500)
                canvas.coords(id7,430,400)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                if(point.direction.y < -0.5):
                    canvas.itemconfig(arc7, fill='#000000')
                    select6=canvas.create_text(500,60,text="6 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc7, fill='grey')	
            elif (min(list_dis)==distance7):
                canvas.coords(arc2,110,130,310,330)
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)
                canvas.coords(id2,210,230)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc2, fill='#000000')
                    select7=canvas.create_text(500,70,text="7 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc2, fill='grey')					
            elif (min(list_dis)==distance8):
                canvas.coords(arc1,270,90,330,150)
                canvas.coords(id1,300,120)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,250,360,450,560)
                canvas.coords(id9,350,460)
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc9, fill='#000000')
                    select8=canvas.create_text(500,80,text="8 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc9, fill='grey')	
            elif (min(list_dis)==distance9):
                canvas.coords(arc1,200,90,400,290)
                canvas.coords(id1,300,190)
                canvas.coords(arc2,120,150,180,210)
                canvas.coords(id2,150,180)
                canvas.coords(arc3,420,150,480,210)
                canvas.coords(id3,450,180)
                canvas.coords(arc4,50,260,110,320)
                canvas.coords(id4,80,290)
                canvas.coords(arc5,490,260,550,320)
                canvas.coords(id5,520,290)
                canvas.coords(arc6,70,390,130,450)
                canvas.coords(id6,100,420)
                canvas.coords(arc7,470,390,530,450)
                canvas.coords(id7,500,420)
                canvas.coords(arc8,180,500,240,560)
                canvas.coords(id8,210,530)
                canvas.coords(arc9,360,500,420,560)
                canvas.coords(id9,390,530)                   
                if (point.direction.y < -0.5):
                    canvas.itemconfig(arc1, fill='#000000')
                    select9=canvas.create_text(500,90,text="9 has been selected")
                    #time.sleep(sleep_time)
                    #canvas.itemconfig(arc1, fill='grey')

            canvas.delete(handNumber,fingerNumber,dot)

def main():
    
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