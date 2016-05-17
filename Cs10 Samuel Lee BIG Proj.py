import time
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
        

start_room = Game_rooms("Start_room","hall1_1",None,None,None,None,None,"You have fallen into a deep cavern and there is only one way, up(u)")
hall1 = Game_rooms("Hall1","hall2","Art_room","start_room","hall3",None,None,"You have entered a corridor, you can go either: up(u),right(r),down(d),left(l)")
hall1_1 = Game_rooms("Hall1",None,None,None,None,None,None,"")
hall2 = Game_rooms("Hall2","hall4","hall5","hall1",None,None,None,"Another one, great! Yes, You are in another corridor three choices figure it out your self.")
Art_room = Game_rooms("Art_room",None,None,None,"hall1",None,None,"You have entered a room with peculiar art, there seems to be nothing else.")
hall3 = Game_rooms("Hall3",None,"hall1","W's club dungeon","hall11",None,None,"You must choose once again")
hall4 = Game_rooms("Hall4",None,None,"hall2","Cathedral",None,None,"Yay It's your first time getting to choose from two things hurry please.")
Cathedral = Game_rooms("Cathedral",None,"hall4",None,None,None,None,"You have entered a cathedral, there is a key on the ground you should pick it up.")
hall5 = Game_rooms("Hall5",None,None,"hall6","hall2",None,None,"And yet another decision to make, go back or continue but either way you'll have to continue muahaahahhahahahha") 
hall6 = Game_rooms("Hal6","hall5","hall7","The_Morgue",None,None,None,"Please choose again")
hall7 = Game_rooms("Hall7",None,None,"hall8","hall6",None,None,"Another one, time to choose again.")
The_Morgue = Game_rooms("The Morgue","hall6",None,None,None,None,None,"You have entered a room filled with the remains of the unclaimed dead, there seeems to be nothing else.")
hall8 = Game_rooms("Hall8","hall7","hall9","hall10",None,None,None,"")
hall9 = Game_rooms("Hall9",None,None,"Bobs_Hole","hall8",None,None,"")
Bobs_Hole = Game_rooms("","hall9",None,None,None,None,None,"Welcome to Bob's Hole (its not really a hole more of a room) the funnest place on middle earth.")
hall10 = Game_rooms("Hall10","hall8",None,None,"Bobs_Crying_Hole",None,None,"")
Bobs_Crying_Hole = Game_rooms("Bob's Crying Hole",None,"hall10",None,None,None,None,"This is Bob's Crying Hole, a place to mourne the dead.")
hall11 = Game_rooms("Hall11",None,"hall3","hall12",None,None,None,"")
hall12 = Game_rooms("Hall12","hall11",None,None,"hall13",None,None,"")
hall13 = Game_rooms("Hall13",None,"hall12","hall15","hall14",None,None,"")
hall14 = Game_rooms("Hall14","Blank","hall13",None,None,None,None,"")
Blank = Game_rooms("Blink",None,None,"hall14",None,None,None,"You enter an empty room thats black and white.")
hall15 = Game_rooms("Hall15","hall13","hall16","Empty_room",None,None,None,"")
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
hall32 = Game_rooms("Hall32","hall33",None,"hall31",None,None,None,"")
hall33 = Game_rooms("Hall33",None,None,"hall32","hall34",None,None,"")
hall34 = Game_rooms("Hall34","hall35","hall33",None,None,None,None,"")
hall35 = Game_rooms("Hall35",None,None,"hall34","hall36",None,None,"")
hall36 = Game_rooms("Hall36",None,"hall35","hall37","hall40",None,None,"")
hall37 = Game_rooms("Hall37","hall36","hall38",None,None,None,None,"")
hall38 = Game_rooms("Hall38",None,None,"hall39","hall37",None,None,"")
hall39 = Game_rooms("Hall39","hall38","Black_hole",None,None,None,None,"")
Black_hole = Game_rooms("Black Hole",None,None,None,"hall39",None,None,"You have entered a room that seemed as of it was pulling you towards it. Be careful and get out as soon as possible.")
hall40 = Game_rooms("Hall40","hall41","hall36",None,"hall43",None,None,"")
hall41 = Game_rooms("Hall41",None,"hall42","hall40",None,None,None,"")
hall42 = Game_rooms("Hall42","Temple",None,None,"hall41",None,None,"")
Temple = Game_rooms("Timmy\'s Temple",None,None,"hall42",None,None,None,"You enter the whitest room in this whole maze.")
hall43 = Game_rooms("Hall43","hall44","hall40",None,None,None,None,"")
hall44 = Game_rooms("Hall44",None,None,"hall43","Dope_room",None,None,"")
Dope_room = Game_rooms("Areg\'s Dope Arse Room",None,"hall44",None,None,None,None,"You enter Areg\'s Dope Arse Room gary busci runs out wearing a skin tight morphsuit and Vanessa Williams stands in the corner holding a lead pipe.")
hall45 = Game_rooms("Hall45","hall22",None,"Ogre_room","hall46",None,None,"")
Ogre_room = Game_rooms("Ogre room",None,None,None,None,None,None,"This is as far as I got =)")
#hall46 = Game_rooms()
#hall47 = Game_rooms()
#Graveyard = Game_rooms()
#hall48 = Game_rooms()
#hall49 = Game_rooms()
#Sacrafice_room = Game_rooms()
#hall50 = Game_rooms()
#hall51 = Game_rooms()
#Torture_room = Game_rooms()
#The_Path_to_Escape = Game_rooms()
#Escape = Game_rooms()





start_time = time.time()
end_time = time.time()
node = start_room
Inventory = []
Items = ['key']

if node == start_room:
    print "Controls: u,r,d,l (up,right,down,left). Most rooms don\'t have descriptions because I was in a rush and if they do it is very brief. You must choose your own path even if it is wrong."
    print ""
                                                        
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
            
                       

    if node == Cathedral:
        if command == "loot":
            if Items[0] in Inventory:
                print "you already have this item"
                print Inventory
            else:
                print "you pick up the item"
                Inventory.append(Items[0])
                print Inventory
                
    elif command == "inventory":
        print Inventory            
            
    elif node == hall1_1:
        elapsed_time = start_time/end_time + 1
        elapsed_time
        print "there is a strong force pulling you, quickly grab onto the corner(you have 5 seconds to decide)... yes or no"
        if elapsed_time == 5:
            print "You took too long"
            node == Black_hole            
        elif command == "yes":
            print "you escaped the strong force now continue with your journey"
            node = hall1
        elif command == "no":
            print "you have been moved into a new room."
            node = Dope_room
            
    elif node == Black_hole:
        print "Oh no something isn\'t right here be careful"     