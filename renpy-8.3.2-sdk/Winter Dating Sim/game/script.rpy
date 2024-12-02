﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Main characters
define mc = Character("[mcname]", color = "#efbf04")
define msC = Character("Ms. Clause", color = "#850101")
define frosty = Character("frosty the 'Snowman'", color = "#ffffff")
define jack = Character ("Jack Frost", color = "#000bd4")
define krampus = Character("Krampus", color = "#3d0d0d")

define unk = Character("Unknown", color = "#808080")

#Other Characters
define emily = Character("Emily", color = "#ffc1f2")


#Character Roamnce Points
$ fPoints = 0

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

    "In the begining there were stories... Legends..."

    "These legends brought... wonder, joy, solace to everyone who heard them."

    "And through the strength of those feelings, that belief, beings - icons began to manifest."

    scene bg background

    "And with these manifestastions bore one book: the Book of Lore, Legends, and Legendaries."

    "The icons believed the book to be as sacred as themselves and although much is unknown about the book, it remains protected by those whose stories it contains."

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

    "The room is cold and empty, save for a golden book that rests on a podium a few feet before you."

    menu:
        "Move closer to the book":
            "You move closer to take a look at the book."
            "It glows with a warm golden light, almost beckoning for you to reach out and touch it."
            mc "What is this book...?"

        "Look around the room":
            "You take a look around the room."
            "It is pretty barren all things concidered."
            "The room seems to center around te podium that holds the golden book..."
            mc "It seems like this room is only for this book..."

    "Before you could continue to explore, an ear pericing sound suddenly errupts around you, acopanied by the sound of urgent footsteps"

    mc "What is going on? I don't think I did anything..."

    unk "Who ever you are in there, you are surrounded! I suggest you come out quietly." #probably Mrs. Claus  

    scene bg black screen 
    with blink_shut
    mc "Uuugh"

    scene bg hub command
    with blink_open

    unk "Maybe we should go in and see -" #probably frosty
    unk "Go in, are you nuts!" #probably Jack
    unk "Well how else do you expect us to know who is in there..." #frosty
    unk "And what, may I ask, will you do if there IS someone in there?" #probably Krampus
    unk "Ummm... I hadn't gotten that far..." #frosty
    unk "Hello! Is there anyone in there!" #frosty
    unk "What are you doing?!?!" #Jack 
    unk "I figured if we're not going in to see if someone's in there, I could call out and see if anyone responds..." #frosty
    unk "Of all the ideas that has to be the stu-" #Jack

    mc "Ummm... hello?" 
    unk "Yes! Hello!" #frosty
    unk "Stop talking." #Krampus

    unk "If you come out peacefully we'll make your suffering short." #Krampus
    unk "Don't say that! You'll scare them." #frosty
    unk "Good." #Krampus

    mc "Where is out? Where am I?"
    unk "You're not going to trick us, so you can drop the act." #Krampus

    mc "Trick? Who is us? And why would I want to trick you?"
    unk "..."
    unk "I don't know guys, it sounds like they really don't know anything..." #frosty
    unk "You're not allowed to have anymore thoughts." #Jack 
    unk "We're coming in..." #Krampus
    unk "NO, we are not! Have you lost your mind." #Jack
    unk "No. I have not." #Krampus

    "A loud clanking sound resonates through the room."
    "To your right, a part of the wall begins to move as if it is moving to the side to reveal something."

    
    #Krampus slides onto screen
    unk "You make any sudden movements and I will kill you." #Krampus 

    #frosty and Jack enter 
    unk "So who is it?" #Jack
    unk "Oh... hi" #frosty

    mc "Umm... hi"
    mc "Where am I? Who are you?"

    unk "You... really don't know, do you?" #Jack
    
    "You eye the first man to arrive."
    "He stands tall, with elf-like ears protruding out from his black and gray streaked hair."
    "You look up into his eyes, they tell the tale of an older man, hung up and annoyed with life, before slowly shaking your head."

    unk "We should get Mrs. C in here." #frosty
    unk "What is your name?" #Krampus

    mc "It's..."
    mc "I'm ..."
    mc "I'm [mcname], I think."

    unk "You think?" #Jack

    "The one to speak this time was slightly shorter than the man that first entered. He had white hair like snow and eyes the color ice."
    "He seemed to look at you with curiosity as opposed to the last man who seemed to only be annoyed by your presence."
    
    mc "I think that's my name. My head is spinning and everything is blurry."

    "You try taking a step towards the men, but find that your legs are less reliable than you think they are, and you find yourself stumbling a bit before having to catch yourself."

    unk "Whoa whoa whoa. Maybe you should sit." #frosty 

    "This man seems so be slightly different than the rest. He stands taller than all of them, his broad shoulders make it so he takes up the most space, but his eyes tell a different story."
    "Instead of looking at you with an air of curiosity or annoyance, he looks concerned."
    "He slungs your arm around his shoulder as he eases you to the floor."

    unk "Take a few deep breaths, are you hurt anywhere." #frosty 
    unk "Snow! What are you doing dude, they could be dangerous." #Jack 
    unk "I don't know dude, they can hardly stand." #frosty
    unk "Go get Mrs. Clause." #Krampus
    unk "But-" #Jack
    unk "Go. For now, I think frosty is correct. And Mrs. Clause will be able to tell for sure." #krampus

    #Jack's sprite slides off screen
    mc "frosty?"

    "The hulking figure shakes in silent laughter before responding."

    frosty "Yes. I know what you're thinking..."
    frosty "Actually, no I don't know..."
    frosty "I assume you figured it out by now, but yes I am frosty the Snowman, or at least the human version of him."

    menu:
        "You seem nice.":
            mc "You seem really kind."
            "frosty smiles with a big wide smile."
            frsoty "Thank you."
            $ fPoints += 1

        "It suits you.":
            mc "It suits you, and yet your demeanor is warm."
            "frosty smiles with a big wide smile."
            frsoty "Thank you."
            $ fPoints += 1

        "I figured you'd be something more... intimidating":
            mc "I figured, with how big you are... I was just expecting something more intimidating."
            unk "I promise, you do not want to mess with this guy."  #krampus
            frosty "It's ok Kramp, I understand. It helps that people underestimate me."

    frosty "Well I guess now is as good of a time as ever to introduce ourselves."
    frosty "As you figured, I am frosty, frosty the Snowman. And this is Krampus."


label frosty Date 1:
    "You hastily knock on the door labeled 'frosty' feeling slightly nervous."

    "frosty had always seemed very sweet, granted you had only known him for a few days, but due to the circumstances, you felt like you should get to know everyone better, and frosty was the least intimidating out of the bunch."

    "After a moment or two, the door in front of you opens to reveal frosty standing before you."

    "He towers over you, but instead of finding him intimidating, he looks down at you with a bright smile on his face."

    frosty "Y/N!"

    "You smile back at him as he welcomes you into his room."

    #scene bg frosty bedroom
    #with dissolve 

    "frosty's room is pretty simple, nothing too out of the ordinary here."

    "A plain-ish bed, some shelves holding small knick-knacks like a few books, a small figure, and some plants."
    "The open arrangement and lack of clutter made the room feel very cozy, especially with the plants adding a pop of color here and there."
    "The room also had the faint scent of evergreen trees in the winter, but it wasn't cold surprisingly, for him being frosty the Snowman, but instead was actually kind of warm."

    menu:
        mc "It's warm in here"
            frosty "Haha yeah. I like to keep it warm in here, contrary to popular belief..."
        mc "Its very cozy in here"
            frosty "Thank you! I try to keep it nice and welcoming in here, although the others aren't really ones for hanging out..."

    frosty "So.. What do you want to do today?"

    mc "Hmm. I'm not sure.."

    frosty "Well I have an idea if you would like..."

    mc "Oh? Sure what is it?"

    frosty "Well... there is this cat cafe near here that I like to go to sometimes. Oh wait, are you allergic to cats? Oh shoot I didn't think about that... Well we can do something else if you-"

    mc "No haha frosty it's ok I'm not allergic to cats. That sounds amazing, let's go!"

    frosty "Really?" 

    "His eyes light up as he looks at you with a bright smile on his face. He reminds you of a golden retriever in the way he gets so excited about things."

    mc "Yes really!"

    frosty "Oh my god yay I'm so excited! Let's go!"

    "frosty quickly grabs a tote bag and heads out with you to the Cat Cafe." 

    #scene bg cat cafe
    #with dissolve

    "You both step into the local cat cafe with frosty by your side. As you look over to him, his face is beaming with joy looking at the cats behind the glass."

    unk "Hi frosty!" 

    frosty "Hi emily!"

    emily "Oh I see you brought a friend this time!"

    mc "Oh, Hi, I'm [mcname]"

    emily "Nice to meet you! I'm emily. I own this cat cafe. Can I get you anything to drink before going in?"

    frosty "One hot chocolate please!"

    mc "I'll also take a hot chocolate."

    frosty "Good choice" 

    "You and frosty settle into a cozy little corner of the cafe, where the warm lighting and soft hum of conversation make everything feel calm and inviting."
    "A curious gray tabby pads over to investigate, hopping onto the table with an elegant leap."

    frosty "Whiskers!" 

    "Frosty's face lights up as though he's greeting an old friend."

    frosty  "This little guy always says hi first. He's kind of like the cafe's unofficial mascot."

    "Whiskers leans in, sniffing frosty's outstretched hand before rubbing against it. frosty grins and gently scratches behind the cat's ears."

    frosty "See? Total sweetheart."

    mc "Do you come here a lot?" 

    "Whiskers curls up comfortably on the table between you."

    "Frosty nods, his tone easygoing but warm."

    frosty "Yeah, whenever I need a little pick-me-up. Something about being here just... makes the world feel softer, y'know? Plus, cats are great company. They don't expect much—just a little kindness—and they give so much back."
    "You glance around the cafe, taking in the peaceful vibe." 

    "A sleek black cat is perched on a windowsill, watching the passersby, while a fluffy orange tabby dozes in a sunbeam."
    "The room feels alive yet tranquil, and you can see why frosty loves it here"
    "Emily, the cafe's owner, brings over your drinks, breaking the quiet moment."

    emily "Here we go! One hot chocolate for you," 

    "She sets a cup in front of frosty,"

    emily "and one for you." 

    "She places yours down with a smile."

    frosty "Thanks, emily!" 
    frosty "Oh! And thanks for saving me one of those cat-shaped cookies last time. It was delicious!"

    "Emily laughs."

    emily "Of course! I know you've got a soft spot for them."

    "frosty turns to you, his eyes bright."

    frosty "You've gotta try them next time. They're so good. Not just cute-like, legit delicious. But only if you're into cookies. Are you into cookies?"

    "He pauses, then shakes his head at himself."

    frosty "Sorry, I'm rambling."

    "You smile, finding his enthusiasm endearing."

    mc "I'll give them a shot next time."

    "As the conversation flows, Whiskers hops into frosty's lap, and frosty immediately freezes, as if he's just been granted an incredible honor." 

    frosty "Okay,"

    "Frosty looks at you with wide eyes"

    frosty "I think I've been chosen."

    "You chuckle."

    mc "Looks like it."

    "Frosty gently strokes Whiskers, a soft smile tugging at his lips."

    frosty "This is the best. You know, cats don't care about what you look like or anything. They just... know if you' re good people. Or a good whatever we are, I guess."

    "There's a moment of quiet as Frosty seems lost in thought, absently scratching Whiskers' chin."

    "You sip your hot chocolate, watching him with a new appreciation. For all his cheerful energy, frosty has a way of grounding a room, making it feel safe and welcoming."

    frosty "Thanks for coming with me today,"

    frosty "I know it's kind of random, but I wanted to share this place with you. It means a lot to me."

    mc"It's not random, I can see why you love it here. I had a great time."

    "frosty beams, his eyes crinkling with joy."

    frosty "Really? That makes me so happy. We'll come back soon, yeah? Maybe next time we can try some of those cookies-or just hang out with the cats more. I think Mittens over there has her eye on you."

    "You glance at a fluffy calico peeking at you from behind a stack of books, and frosty laughs. It's warm and easy, and it feels like a perfect ending to the day."

    mc "Next time for sure"

    "You both step outside into the cold and crisp air."

    frosty "Next time," 

    "Frosty echoes your sentiment, his bright smile lingering as he walks beside you."

    return