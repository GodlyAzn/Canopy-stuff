import sys
direction_keys = ['n','e','s','w','u','d','open','move books']

player_choices = ['yes','no','neither','leave','enter','fine']
dialogue_node = 'Ghost'

def display_options(node):
    print '\nYour Options Are:'
    for i,p in enumerate(node['paths']):
        print '\t%d: "%s"' % (i, p[2])

def player_says(destination, text):
    global dialogue_node
    print 'You say:"%s"' % text
    dialogue_node = destination

#def conversation(character):
 #   dictionary = dialogue
  #  node = dialogue[character]
   # dialogue_node = character
    #while True:
     #   if:
      #  else:
       #     break
    
        

world_map = {
    'Kitchen':{
        'description':'You are in a kitchen there doesn\'t seem to be anything or anyone.',
        'paths':{
            'n':'Door',
            }
        },
    'Door':{
        'description':'This door has a sign that says library and it doesn\'t seem locked',
        'paths':{
            'open':'Library'
        }
    },
    'Library':{
        'description':'You opened the door and entered a dimly lit library full of old books.You can\'t go back',
        'paths':{
            'n':'Bookcase',
            'e':'Wall',
            'w':'Painting',
        }
    },
    'Bookcase':{
        'description':'You see a bookcase that isn\'t dusty and notice a book missing you feel a breeze coming form the spot of the missing book.',
        'paths':{
            'move books':'Staircase',
            's':'Library'
        }
    },
    'Wall':{
    'description':'blank',
    'paths':{
        'n':'none',
        'w':'Library'    
        }
    },
    'Painting':{
        'description':'An ugly painting of a best with red eyes',
        'paths':{
            'n':'nothing',
            'e':'Library'
        }
    },
    'Staircase':{
        'description':'A dark stair-way leading down with only two torches at the bottom.',
        'paths':{
            'd':'Dim Room'
        }
    },
    'Dim Room':{
    'description':'After reaching the bottom you hear a door shut behind you. You look around and realize you cant see very well but you can see two paths',
    'paths':{
        'e':'Tunnel',
        's':'Armoury'
        }
    },
    'Tunnel':{
    'description':'You have entered a long tunnel leading to, who knows. You reach the end and see three signs with writing on them. One says Infirmary, Another says Prison, and the final one says catacombs.',
    'paths':{
        'n':'Infirmary',
        'e':'Prison',
        's':'Catacombs',
        'w':'Dim Room'
        }
    },
    'Armoury':{
    'description':'You enter a room that is full of weapons and tools.',
    'paths':{
        'n':'Dim Room'
        }
    },
    'Infirmary':{
    'description':'You enter a room filled with medical tools and you see blood all over the floor. You see a door that says exit but is locked. You hear foot steps coming towards the door that is locked but stops right in front of the door. Moments later you are alone',
    'paths':{
        's':'Tunnel'
        }
    },
    'Prison':{
    'description':'You have entered a room filled with prison cells. You hear many screams coming from each cell. As you walk by each one you see nothing and the screaming just continues. You are now in the middle of this prison and you are facing a large stairway.',
    'paths':{
        'u':'Silent_Cell',
        'w':'Tunnel'
        }
    },
    'Catacombs':{
    'description':'You have entered a room filled with bones and a stench so fowl you could die.The room also contains a key',
    'paths':{
        'n':'Tunnel'
        }
    },
    'Silent_Cell':{
    'description':'You see a soundless cell with what looks like an exit.',
    'paths':{
        'n':'Exit'    
        }
    },
    'Exit':{
    'description':'You are now outside in the dark. You can only see man next to a large door. You walk up to the man and he says something to you.'
    }
}

dialogue = {
    'Ghost':{
    'info':'Welcome to the Death Zone. As of now you are dead. You are about to enter the Gates of Hades. Do you wish to leave this place or enter the door.',
    'paths':[
        (player_says,'Leave','leave'),
        (player_says,'Go_on','enter')
        ],
    },
    'Leave':{
        'info':'Well you can\'t leave so just go foward',
        'paths':[
            (player_says,'Running_Away','no'),
            (player_says,'Go_on','fine')
        ],
    },
    'Go_on':{
        'info':'Yes you have guts I\'ll be enjoying them later so good luck in Hades.'    
    },
    'Running_Away':{
    'info':'Look there is no where to go other than foward so just gooo!!!',
    'paths':[
        (player_says,'Forced','no'),
        (player_says,'Go_on','fine')
        ],
    },
    'Forced':{
    'info':'Are you disobeying me,Thanatos, I will not allow this.Guards do it! You were pushed in now I can finally leave ugh!!!',
    }
        
}




player_location = 'Kitchen'

while True:
    if player_location == 'Exit':
        print world_map['Exit']['description']
        break                         
    room = world_map[player_location]
    print player_location
    print room['description']
    command = raw_input('Go somewhere sheesh:')
    if command in ['q','quit','exit']:
        sys.exit(0)
    if command in direction_keys:
        if command in room['paths']:
            player_location = room['paths'][command]
        else:
            print 'You cant go that way,'
    else:
        print 'I don\'t know that \"%s\".\n\n'  % command

while True:
    node = dialogue[dialogue_node]
    if player_location == 'Exit':
        print 'Ghost says: %s' %node['info']
    
        if 'paths' in node:
                display_options(node)
        
        #ask for input
                response = raw_input('>')
        #Quit When I want
                if response in ['q','quit']:
                    sys.exit(0)
            
        #Move to next node
                try:
                    path = node['paths'][int(response)]
                    function = path[0]
                    args = path[1:]
                    function(*args)
                except:
                        print 'Try a number this time'    
        else:
            sys.exit(0)       
    