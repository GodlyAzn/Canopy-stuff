#import time
import sys
node = None
class Game_rooms:
    def __init__(self, name, n_path, e_path, s_path, w_path, up_path, down_path, description):
        self.name = name
        self.u = n_path
        self.r = e_path
        self.d = s_path
        self.l = w_path
        self.j = up_path
        self.c = down_path
        self.description = description
        
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]
        

start_room = Game_rooms("Start_room","hall1",None,None,None,None,None,"You have fallen into a deep cavern and there is only one way, up(u)")
hall1 = Game_rooms("Hall1","hall2","Art_room","start_room","hall3",None,None,"You have entered a corridor, you can go either: up(u),right(r),down(d),left(l)")
hall2 = Game_rooms("Hall2","hall4","hall5","hall2",None,None,None,"Another one, great! Yes, You are in another corridor three choices figure it out your self.")
Art_room = Game_rooms("Art_room",None,None,None,"hall1",None,None,"You have entered a room with peculiar art, there seems to be nothing else.")
hall3 = Game_rooms("Hall3",None,"hall1","W's club dungeon","hall11",None,None,"You must choose once again")
hall4 = Game_rooms("Hall4",None,None,"hall2","Cathedral",None,None,"Yay It's your first time getting to choose from two things hurry please.")
Cathedral = Game_rooms("Cathedral",None,"hall4",None,None,None,None,"You have entered a cathedral, there is a key on the ground you should pic it up.")
hall5 = Game_rooms("Hall5",None,None,"hall6","hall2",None,None,"And yet another decision to make, go back or continue but either way you'll have to continue muahaahahhahahahha") 
hall6 = Game_rooms("Hal6","hall5","hall7","The_Morgue",None,None,None,"Please choose again")
hall7 = Game_rooms("Hall7",None,None,"hall8","hall6",None,None,"Another one, time to choose again.")
The_Morgue = Game_rooms("The Morgue","hall6",None,None,None,None,None,"You have entered a room filled with the remains of the unclaimed dead, there seeems to be nothing else.")
hall8 = Game_rooms("Hall8","hall7","hall9","hall10",None,None,None,"")
hall9 = Game_rooms("Hall9",None,None,"Hernans_Hole","hall8",None,None,"")
Bobs_Hole = Game_rooms("","hall9",None,None,None,None,None,"Welcome to Bob's Hole (its not really a hole more of a room) the funnest place on middle earth.")
hall10 = Game_rooms("Hall10","hall8",None,None,"Hernans_Crying_Hole",None,None,"")
Bobs_Crying_Hole = Game_rooms("Bob's Crying Hole",None,"hall10",None,None,None,None,"This is Bob's Crying Hole, a place to mourne the dead.")
hall11 = Game_rooms("Hall11",None,"hall3","hall12",None,None,None,"")
hall12 = Game_rooms("Hall12","hall11",None,None,"hall13",None,None,"")
hall13 = Game_rooms("",None,"hall12","hal15","hall14",None,None,"")
hall14 = Game_rooms("","Blank","hall13",None,None,None,None,"")
Blank = Game_rooms("Blink",None,None,"hall14",None,None,None,"You enter an empty room thats black and white.")
hall15 = Game_rooms("","hall13","hall16","Empty_room",None,None,None,"")
Empty_room = Game_rooms("Empty Space","hall15",None,None,None,None,None,"Literally an empty room")
hall16 = Game_rooms("Hall16",None,"hall17","Soundless_room","hall15",None,None,"")
Soundless_room = Game_rooms("The Soundless Room","hall16",None,None,None,None,None,"You enter a room filled with souls screaming in horror and yet you can only see. You are unable to hear them.")
hall17 = Game_rooms("Hall17","hall19","hall18",None,"hall16",None,None,"")
hall18 = Game_rooms("Hall18",None,None,"Blind_room","hall17",None,None,"")
Blind_room  =Game_rooms("Sightless","hall18",None,None,None,None,None,"You enter a pitch-black room and in the darkness you reach out and feel as if you are in a never ending room. Each step making a loud echo within the room. You hear a loud voice saying 'leaaave this place if you want to live.'.A strong force pushes you back to the door, now leave because now there is nothing left except the door.")
hall19 = Game_rooms("Hall19",None,"hall20","hall17",None,None,None,"")
hall20 = Game_rooms("Hall20",None,"Food","hall21","hall19",None,None,"")
Food = Game_rooms("Kitchen",None,None,None,"hall20",None,None,"Yess finally you found the kitchen now check the frige for food because you know you are starving just like that man hanging form the ceiling")
hall21 = Game_rooms("Hall21","hall20","hall22","hall48",None,None,None,"")
hall22 = Game_rooms("Hall22",None,"hall23","hall45","hall21",None,None,"")
hall23 = Game_rooms("Hall23","hall24",None,None,"hall22",None,None,"")
hall24 = Game_rooms("Hall24","hall25","hall28","hall23",None,None,None,"")
hall25 = Game_rooms("Hall25",None,None,"hall24","hall26",None,None,"")
hall26 = Game_rooms("Hall26","hall271","hall25",None,None,None,None,"")
hall271 = Game_rooms("Hall27_1",None,"hall27","hall26",None,None,None,"")
hall27 = Game_rooms("Hall27_2","Barracks",None,None,"hall271",None,None,"")
Barracks = Game_rooms("Barracks",None,None,"hall27",None,None,None,"You enter a room filled with beds made of straw and skeletons on the floor.")
hall28 = Game_rooms("Hall28",None,None,"hall29","hall24",None,None,"")
hall29 = Game_rooms("Hall29","hall28","hall30",None,None,None,None,"")
hall30 = Game_rooms("Hall30","hall31",None,None,"hall29",None,None,"")
hall31 = Game_rooms("Hall31",None,None,"hall30","hall32",None,None,"")
hall32 = Game_rooms("Hall32","hall33",None,"hall31",None,None,"")
hall33 = Game_rooms("Hall33","")
hall34 = Game_rooms()
hall35 = Game_rooms()
hall36 = Game_rooms()
hall37 = Game_rooms()
hall38 = Game_rooms()
hall39 = Game_rooms()
Black_hole = Game_rooms()
hall40 = Game_rooms()
hall41 = Game_rooms()
hall42 = Game_rooms()
Temple = Game_rooms()
hall43 = Game_rooms()
hall44 = Game_rooms()
Dope_room = Game_rooms()
hall45 = Game_rooms()
Ogre_room = Game_rooms()
hall46 = Game_rooms()
hall47 = Game_rooms()
Graveyard = Game_rooms()
hall48 = Game_rooms()
hall49 = Game_rooms()
Sacrafice_room = Game_rooms()
hall50 = Game_rooms()
hall51 = Game_rooms()
Torture_room = Game_rooms()
The_Path_to_Escape = Game_rooms()
Escape = Game_rooms()





node = start_room


    
while True:
    print node.name
    print node.description
    movement = ['u','r','d','l','j','c']
    command = raw_input('>').strip().lower()
    if command in ['q','quit','exit']:
        print 'You have either given up, died, or won soo wichever one you did, good job xD.'
        sys.exit(0)
    if command in movement:
        try:
            node.move(command)
        except:
            print 'Unable to continue that direction choose a different path'            