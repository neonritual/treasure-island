print('''
*******************************************************************************
.                                     ,
.              ,-.       _,---._ __  / \

.             /  )    .-'       `./ /   \

.            (  (   ,'            `/    /|
.             \  `-"             \'\   / |
.              `.              ,  \ \ /  |
.               /`.          ,'-`----Y   |
.              (            ;        |   '
.              |  ,-.    ,-'         |  /
.    TREASURE  |  | (   |            | /  HUNTER
.              )  |  \  `.___________|/
.              `--'   `--'
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("An old cat pirate told you about a mysterious island where, in the center of a maze, there was a cave of lost pirate treasures. But beware! Danger awaits! You enter the maze...") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

first = input("You reach a fork in the road. Do you go <right> or <left>?\n").lower() 

if first == "left":
  second = input("You reach the center of the hedge maze and find an open door leading downwards, just like the old pirate said. But just outside the door there is a large chest, with an open lock. Do you <open> the chest or <enter> the cave?  \n").lower() 
else:
  print("You turn right, and continue on... and on... and on... You never find the end of the maze, and eventually, you become another skeleton fertilizing the hedges. \nTHE END")

if second == "enter":
    third = input("You enter the cave and light a lantern as you descend into the darkness. Finally, at the end of a long hallway you see four doors. Each is marked only by a swipe of color. Anything could be behind them. Will you choose the <blue>, <red>, <gold>, or <white> door?  \n").lower() 
else:
    print("You open the suspicious chest, and a pair of scaly arms reach up from　the darkness, pull you into the chest with a thud. You are never seen again...\nTHE END")

if third == "blue":
  print("You open the blue door, and a strong wind almost pushes it back into your face, blowing out the light of your lantern. The smell of salt water is strong, and before you can begin to close he door a long, slimy tentacle shoots out from the darkness, pulling you with into an eternal black sea.\nTHE END")

elif third == "red":
  print("As you open the red door, suddenly the brass knob is too hot to touch. In fact everything is too hot to touch-- lava comes pouring out from behind the door, consuming the room and everything in it. Encased in dried lava, at least no future explorers will make the same mistake you did.\nTHE END")

elif third == "white":
  print("You open the white door, and quickly your vision is blurred by fluttering white snowflakes. Thousands, and thousands of cold snowflakes fly into the room, a total whiteout, leaving you frozen in place for eternity. At least the next explorer won't make the same mistake you did.\nTHE END")

elif third == "gold":
  print("While you're a little nervous picking the most obvious answer, you open the gold door and you immediately shield your eyes from the glare of piles and piles of shining, glittering gold and jewels. Huzzah! IT looks like the obvious choice was the right one after all. You pocket whatever you can carry and thank the cat pirate for your new found fortune.\nTHE END")

else:
  print("Out of nowhere a cat paw smacks you in the head. The cat pirate's voice can be heard saying, 'Oi! Learn to spell, or no treasure for you!'")

