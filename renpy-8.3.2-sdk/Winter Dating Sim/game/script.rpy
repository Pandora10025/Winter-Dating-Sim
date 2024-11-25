# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("[mcname]", color = "#efbf04")
define msC = Character("Ms. Clause", color = "#850101")
define frosty = Character("Frosty the 'Snowman'", color = "#000")
define jack = Character ("Jack Frost", color = "#000")
define krampus = Character("Krampus", color = "000")

define unk = Character("Unknown", color = "#808080")

# The game starts here.

label start:
    python: 
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()
        if mcname == "":
            mcname = "Noel"
        def eyewarp(x):
            return x**3.5
        blink_open = ImageDissolve("bg hub command.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
        blink_shut = ImageDissolve("bg black screen", .5, ramplen=128, reverse=True, time_warp=eyewarp)

    scene bg black screen

    "In the begining there were stories. Legends..."

    "These legends brought... wonder, joy, solace to everyone who heard them."

    "And through the strength of those feelings, that belief. Beings - icons began to manifest."

    scene bg background

    "And with these manifestastions bore one book: the Book of Lore, Legends, and Legendaries."

    "The icons believed the book to be as sacred as themselves and though much is unknown about the book, it remains protected by those whose stories it contains."

    scene bg black screen

    scene bg hub command 
    with blink_open

    scene bg black screen 
    with blink_shut 

    mc "Uhh..."

    scene bg hub command
    with blink_open

    mc "Ugh..."
    mc "Where..."
    mc "Where am I?"

    "The room is cold, and empty. Save for a golden book that rests on a podium a few feet before you."

    "An alarm sounds and sound of footsteps come closer *will be adding sfx here* "

    unk "Who ever you are in there, you are surrounded I suggest you come quietly." #probably Mrs. Claus  

    scene bg black screen 
    with blink_shut
    mc "Uuugh"

    scene bg hub command
    with blink_open

    unk "Maybe we should go in and see -" #probably Frosty
    unk "Go in, are you nuts!" #probably Jack
    unk "Well how else do you expect us to know who is in there..." #Frosty
    unk "And what, may I ask, will you do if there IS someone in there?" #probably Krampus
    unk "Ummm... I hadn't gotten that far..." #Frosty
    unk "Hello! Is there anyone in there!" #Frosty
    unk "What are you doing?!?!" #Jack 
    unk "I figured if we're not going in to see if someone's in there, I could call out and see if anyone responds..." #Frosty
    unk "Of all the ideas that has to be the stu-" #Jack

    mc "Ummm... hello" 
    unk "Yes! Hello!" #Frosty
    unk "Stop talking." #Krampus

    unk "If you come out peacefully we'll make your suffering short." #Krampus
    unk "Don't say that! You'll scare them." #Frosty
    unk "Good." #Krampus

    mc "Where is out? Where am I?"
    unk "You're not going to trick us, so you can drop the act." #Krampus

    mc "Trick? Who is us? And why would I want to trick you?"
    unk "..."
    unk "I don't know guys, they really don't sound like they know anything..." #Frosty
    unk "You're not allowed to have anymore thoughts." #Jack 
    unk "We're coming in..." #Krampus
    unk "NO, we are not! Have you lost your mind."
    unk "No. I have not." #Krampus

    "A loud clanking sound resonates through the room and a piece of the wall shifts open"
    
    #Krampus slides onto screen
    unk "You make any sudden movements and I will kill you." #Krampus 

    #Frosty and Jack enter 
    unk "So who is it?" #Jack
    unk "Oh... hi" #Frosty

    mc "Umm... hi"
    mc "Where am I? Who are you?"

    unk "You... really don't know, do you?" #Jack
    
    "You eye the first man to arrive, before slowly shaking your head."

    unk "We should get Mrs. C in here." #Frosty
    unk "What is your name?" #Krampus

    mc "It's..."
    mc "I'm ..."
    mc "I'm [mcname], I think."

    unk "You think?" #Jack
    
    mc "I think that's my name. My head is spinning and everything is a blurry."
    "You stumble a bit before catching yourself."

    unk "Whoa whoa whoa. Maybe you should sit." #Frosty 
    "The tall, broad man helps ease you to the floor." #Frosty

    unk "Take a few deep breaths, are you hurt anywhere." #Frosty 
    unk "Snow! What are you doing dude, they could be dangerous." #Jack 
    unk "I don't know dude, they can hardly stand." #Frosty
    unk "Go get Mrs. Clause - " #Krampus
    unk "But-" #Jack
    unk "Go. For now, I think Frosty is correct. And Mrs. Clause will be able to tell for sure." #krampus

    #Jack's sprite slides off screen
    mc "Frosty?"
    "The hulking figure shakes in silent laughter before responding"
    frosty "Yes. I know what you're thinking..."
    frosty "Actually, no I don't know. What do you think."

    menu:
        "You seem nice.":
         mc "You seem really kind."

        "It suits you.":
            mc "It suits you, and yet your demeanor is warm."

        "I figured you'd be named something more... intimidating":
            mc "I figured, with how big you are... I was just expecting something more intimidating."
    
    
    return
