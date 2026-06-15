def centerFormation(event):
    # event.target is the unit running this event handler.
    unit = event.target
    # Now use unit.moveXY to move the unit to the fire.
    unit.moveXY(40, 37)

# This spawns the four soldiers:
game.spawnXY("soldier", 16, 57)
game.spawnXY("soldier", 15, 13)
game.spawnXY("soldier", 63, 13)
game.spawnXY("soldier", 67, 57)

# This sets the soldier's spawn action to the function centerFormation:
game.setActionFor("soldier", "spawn", centerFormation) 

def sayHi(event):
    unit = event.target
    unit.say("Hi")

game.spawnXY("munchkin", 20, 20)
game.spawnXY("munchkin", 30, 40)
game.setActionFor("munchkin", "spawn", sayHi)

