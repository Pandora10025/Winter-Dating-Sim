# name of the character.

#Main characters
define mc = Character("[mcname]", color = "#ffac00")
define msC = Character("Ms. Claus", color = "#850101")
define frosty = Character("Frosty the 'Snowman'", color = "#8fd4ff")
define jack = Character ("Jack Frost", color = "#000bd4")
define krampus = Character("Krampus", color = "#3d0d0d")
define boogy = Character("The Boogyman", color = "#036507")

define unk = Character("Unknown 1", color = "#b0b0b0") #claus?
define unk1 = Character("Unknown 1", color = "#000bd4") #Jack
define unk2 = Character("Unknown 2", color = "#3d0d0d") #Krampus
define unk3 = Character("Unknown 3", color = "#8fd4ff") #Frosty

#Other Characters
define emily = Character("Emily", color = "#ffc1f2")

#Sprites
image Jack Happy = im.Scale("happy_JACK.png", 800, 1000)
image Jack Neu = im.Scale("neutral_JACK.png", 800, 1000)
image Jack Sad = im.Scale("upset_JACK.png", 800, 1000)

image Kramp Happy = im.Scale("HAPPY_Krampus.png", 800, 1000)
image Kramp Neu = im.Scale("NEUTRAL_Krampus.png", 800, 1000)
image Kramp Nod = im.Scale("NODDING_Krampus.png", 800, 1000)

image Frosty Neu = im.Scale("Neutral_frosty.png", 800, 1000)

image Mrs Claus Neu = im.Scale("Neutral_Mrs_Claus",800,1000)


#Character Romance Points
define fPoints = 0
define jPoints = 0
define kPoints = 0

# random variables
default frostyDate1 = False

#flash
init:
    $ flash = Fade(.25, 0, .75, color="#fff")

#click sound
# not sure if this works tbh
init python:
    def character_callback(event, **kwargs):
        if event == "end":
            renpy.music.play("click.wav", channel="audio")

    config.all_character_callbacks.append(character_callback)

# The game starts here.

label start:
    python: 
        mcname = renpy.input("What is your name?", length=32)
        mcname = mcname.strip()
        if mcname == "":
            mcname = "Noel"
        def eyewarp(x):
            return x**3.5
        blink_open = ImageDissolve("bg book room.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
        blink_shut = ImageDissolve("bg black screen.jpg", .5, ramplen=128, reverse=True, time_warp=eyewarp)

    scene bg black screen
    play music "audio/bg music.wav"
    #Floating In The Midnight Breeze by FoolBoyMedia -- https://freesound.org/s/332323/ -- License: Attribution NonCommercial 4.0

    "In the beginning there were stories... Legends..."

    "These legends brought... wonder, joy, solace to everyone who heard them."

    "And through the strength of those feelings, that belief, beings - icons began to manifest."

    scene bg background

    "And with these manifestations bore one book: the Book of Lore, Legends, and Legendaries."

    "The icons believed the book to be as sacred as themselves and although much is unknown about the book, it remains protected by those whose stories it contains."

    scene bg black screen
    with None

    scene bg book room
    with blink_open

    scene bg black screen 
    with blink_shut 

    mc "Uhh..."

    scene bg book room
    with blink_open
    with vpunch

    mc "Ugh..."
    mc "Where..."
    mc "Where am I?"

    "The room is cold and empty, save for a golden book that rests on a podium a few feet before you."

    menu:
        "Move closer to the book.":
            scene bg the book with fade
            "You move closer to take a look at the book."
            play sound "audio/book glow.wav"
            "It glows with a warm golden light, almost beckoning for you to reach out and touch it."
            mc "What is this book...?"
            "As you get closer, the book's glow brightens and a sense of warmth tingles at your fingertips."
            $ renpy.sound.play("audio/alarm.mp3", loop=True)
            "Before you could reach it, however, an ear piercing alarm suddenly erupts around you, accompanied by the sound of urgent footsteps."
            with vpunch

        "Look around the room.":
            "You take a look around the room."
            "There are several paintings on the wall, but none of them seem to hold any particular meaning."
            "The room seems to center around a podium that holds a golden book..."
            mc "It seems like this room is only for this book."
            scene bg the book with fade
            play sound "audio/book glow.wav"
            "It glows with a warm golden light, almost beckoning for you to reach out and touch it."
            $ renpy.sound.play("audio/alarm.mp3", loop=True)
            "Before you could continue to explore, an ear piercing alarm suddenly erupts around you, accompanied by the sound of urgent footsteps"
            with vpunch

    scene bg book room 
    mc "What's going on? I don't think I did anything."

    unk1 "If someone's in there, you are surrounded! I suggest you come out quietly." #probably Mrs. Claus - this CANNOT be Mrs. Claus because someone else goes to get her later 

    scene bg black screen 
    with blink_shut
    mc "Uuugh"

    scene bg book room
    with blink_open

    stop sound
    unk3 "Maybe we should go in and see." #probably frosty
    unk1 "Go in? Are you nuts?" #probably Jack
    unk3 "Well, how else do you expect us to know who's in there?" #frosty
    unk2 "And what, may I ask, will you do if there is someone in there?" #probably Krampus
    unk3 "I..." #frosty
    unk3 "oh..."#frosty
    unk3 "Ummm... I hadn't gotten that far..." #frosty
    unk3 "Hello? Is there anyone in there?" #frosty
    unk1 "What are you doing?" #Jack 
    unk3 "I figured that if we're not going in to see if someone's in there, I could call out and see if anyone responds." #frosty
    unk1 "Of all the ideas that has to be the stu-" #Jack

    mc "Ummm... hello?" 
    unk3 "Yes! Hello?" #frosty
    unk2 "Stop talking." #Krampus

    unk2 "If you come out peacefully, we'll make your suffering short." #Krampus
    unk3 "Don't say that! You'll scare them." #frosty
    unk2 "Good." #Krampus

    mc "Where is out? Where am I?"
    unk2 "You're not going to trick us, so you can drop the act." #Krampus

    mc "Trick? Who is us? And why would I want to trick you?"
    unk2 "..."
    unk3 "I don't know guys, it sounds like they really don't know anything..." #frosty
    unk1 "You're not allowed to have any more thoughts." #Jack 
    unk2 "We're coming in." #Krampus
    unk1 "NO, we are not! Have you lost your mind?" #Jack
    unk2 "I have not." #Krampus

    play sound "audio/clank.wav"
    "A loud clanking sound resonates through the room."
    "To your right, a part of the wall begins to move to the side, revealing something. Or rather someone."
    
    show Kramp Neu at right
    with moveinleft
    unk2 "You make any sudden movements and I will kill you." #Krampus 

    #Jack enter 
    show Jack Sad at center 
    with moveinleft 
    #frosty enters
    show Frosty Neu at left 
    with moveinleft


    unk1 "So who is it?" #Jack
    unk3 "Oh... hi." #frosty

    mc "Umm... hi"
    mc "Where am I? Who are you?"

    show Jack Neu at center
    with ease
    unk1 "You really don't know, do you?" #Jack
    
    "You eye the first man to arrive."
    hide Jack Neu 
    hide Frosty Neu
    show Kramp Neu at center 
    with fade

    "He stands tall, with elf-like ears protruding out from his black and gray streaked hair."
    "His eyes tell the tale of an older man, hung up and exhausted with life. You look up at him, before slowly shaking your head."

    show Kramp Neu at right
    show Jack Neu at center
    show Frosty Neu at left
    with fade

    unk3 "We should get Mrs. C in here." #frosty
    unk2 "What is your name?" #Krampus

    #frosty moves out of frame
    hide Frosty Neu 
    with moveoutleft

    show Jack Neu at left with ease

    mc "It's..."
    mc "I'm ..."
    mc "I'm [mcname]... I think."

    show Jack Sad at center
    hide Kramp Nod 
    with fade

    unk2 "You think?" #Jack

    "The one to speak this time is slightly shorter than the first man who entered. He has white hair like snow and eyes the color of ice."
    "He looks at you with curiosity as opposed to the other man's annoyance."
    
    mc "I think that's my name. My head is spinning and everything is blurry."

    "You try pushing yourself to your feet, but find that your legs are less reliable than you think. You stumble a bit before having to catch yourself."

    hide Jack Sad with fade

    #frosty comes back into frame looking worried in center
    show Frosty Neu at center 
    with moveinleft

    unk3 "Whoa whoa whoa. Maybe you should sit." #frosty 

    "This man seems to be slightly different from the rest. He stands taller than all of them, his broad shoulders towering over you, but his eyes tell a different story."
    "Instead of looking at you with curiosity or annoyance, he looks concerned."
    "He offers you a hand and helps you ease yourself to the floor."

    show Kramp Neu at right 
    show Jack Sad at left 
    with ease

    unk3 "Take a few deep breaths. Are you hurt anywhere?" #frosty 
    unk1 "Snow! What are you doing? They could be dangerous." #Jack 
    unk3 "I don't know dude - they can hardly stand." #frosty
    unk2 "Go get Mrs. Claus." #Krampus
    unk1 "But-" #Jack
    unk2 "Go. For now, I think Frosty is correct. And Mrs. Claus will be able to tell for sure." #krampus

    hide Jack Sad with moveoutleft

    mc "Frosty?"
    #frosty moves to center looking happy
    "The hulking figure lets out a short laugh before responding."

    frosty "Yes. I know what you're thinking."
    frosty "Actually, no I don't know..."
    frosty "I'm Frosty the Snowman."
    mc "Snowman?"
    frosty "Yeah, the whole silk hat and corncob pipe thing… the kids love it. The label makes them laugh you know?"
    "He drops his head towards you, and whispers like he's about to share a secret." 
    frosty "It's better than having a seven foot tall ice giant talking to them, and moms are scary when they don't know if you're nice."


    menu:
        "You seem... nice.":
            mc "You seem... nice."
            "Frosty smiles widely and chuckles once more."
            frosty "Thank you."
        "It suits you.":
            mc "It suits you, and yet your demeanor is warm."
            "Frosty smiles widely and chuckles once more."
            $ fPoints += 1
            frosty "Thank you."
        "I figured you'd be something more... intimidating.":
            mc "I figured, with how big you are, I was just expecting a name more intimidating."
            unk2 "I promise, you do not want to mess with this guy."  #krampus
            frosty "It's ok Kramp, I understand. It helps that people underestimate me."

    frosty "Maybe now is as best a time to introduce ourselves."
    frosty "As I said before, I'm Frosty, and this is Krampus."

    show Kramp Nod at right 
    with dissolve
    "The older man gives you a small nod of acknowledgement."
    show Kramp Neu at right 
    with dissolve

    frosty "And the guy with the white hair is Jack. Speaking of which, where is he?"
    jack "Awe man Frosty, are you really introducing me when {i}I'm{/i} not there?"
    krampus "Speak of the devil..."

    show Jack Neu at left 
    with moveinleft
    "The man with white hair and eyes the color of ice appears before you, hand stretched out in an invitation to shake it."

    menu:
        "Shake his hand.":
            "You take his hand and shake it. His skin is cold to the touch."
            $ jPoints += 1
        "Look behind him.":
            "You notice a figure standing behind him, and tilt your head to try and get a better look at them."

    "The man gives you a small wink before turning away to reveal the person he brought along."
    hide Kramp Neu with moveoutright
    show Jack Neu at center 
    show Frosty Neu at right 
    with ease

    show Mrs Claus Neu at left with moveinleft

    "A short, older woman stands with her arms crossed. She wears an indiscernible expression."
    "Her hair is completely grey and pinned in a half up and half down style that fell around her shoulders. She wore a black and red dress."
    "You weren't sure why, but she struck you as vaguely familiar. You felt that her presence set you at ease."
    mc "..."
    mc "Nadia?"
    
    "The name pops into your head like a flash and spills out of your lips before you can stop it. "
    "For a moment the older woman's face shifts with surprise, before morphing into indignance."

    msC "Who are you and how did you get in here?" #changed unknown to mrs. claus because we already know who she is
    mc "My name is [mcname] and I'm not sure."
    mc "I just woke up here."

    "The woman's face pinches."
    msC "How did you know my name?"

    mc "I.."
    mc "I don't know. It was the first thing that popped in my head when I saw you."
    mc "I feel like... like I've seen you before."

    msC "Where?"

    mc "I don't know."

    msC "You're going to have to do a little better than that." 

    mc "I swear, I woke up in this room and was just trying to get my bearings when the alarm started blaring."
    mc "And... ugh."

    scene bg black screen with blink_shut 
    scene bg book room with blink_open

    "When your vision returns the woman is closer."
    "You feel her hand press against your forehead."
    "Her once an indignant frown morphs into a concerned furrow." 

    msC "Why didn't you tell me they were sick?"

    show Jack Sad at left with dissolve

    jack "Sick? I knew they seemed out of sorts, but I didn't know they were sick when I came to get you."

    "The woman sighs as she looks back at you."

    msC "You may call me Mrs. Claus. Everyone here does - well, most people do."
    msC "We're going to have to get you somewhere more comfortable so we can check you out."
    msC "Do you feel well enough to stand, my dear?"

    mc "I think so."

    "You try again to stand, hoping that your shaking legs will hold up this time."
    "You aren't quite there yet, and you can feel your knees beginning to buckle beneath you. Before you can hit the floor. however, a gentle hand pulls up your arms to steady you." 
    with vpunch
    "You look to your side and find Krampus looking at you intently, before quickly letting go and looking away."
    show Kramp Neu at right 
    with moveinright
    hide Jack Sad with moveoutleft

    menu:
        "Say thank you.":
            "You murmur a quiet thank you and get an almost imperceptible nod in return." 
            $ kPoints += 1
        "Smile and keep walking":
            "You give him a small smile before turning towards Mrs. Claus."

    "Mrs. Claus leads you out of the room into a hallway." 

    scene bg hallway 
    with dissolve

    play sound "audio/foot steps.wav"
    "The wall slides shut behind you, the hinges fitting seamlessly into the pattern of the rest of the stone."
    "You make your way through the winding maze of corridors and arches, occasionally passing a collection of curious beings."
    "Squat, gnome-like creatures with tall green hats adorned with bells or bows"
    "Small, winged pixies fluttering across the hall in clothes made of silk ribbons and decorative cloth"
    "You even see a row of mice walking on two feet wearing tiny red vests."
    "They all stop to greet Mrs. Claus before eyeing you and scurrying off."
    "Before long, Mrs. Claus stops at a door and ushers you inside." 

    scene bg sitting room 
    with dissolve

    show Mrs Claus Neu at center with moveinright 

    msC "Take a seat, my dear, while I look you over."

    "You sit quietly as the older woman flits around you, examining your head and checking your temperature with a hand on your forehead once again."

    msC "Outside of the dizzy spells, how are you feeling?"

    mc" Okay, I think. My head was pounding when I first woke up, but it's eased up since then."

    "Mrs. Claus nods but the look of concern does not leave her face." 

    msC "And you can't remember how you got in that room?"

    "You shake your head."

    msC "And I suppose you can't remember where you came from either?"

    mc "No."
    mc "I'm sorry."

    msC " What are you apologizing for, dear?"

    mc "I can't help but feel like I've caused you all some trouble." 

    msC "It's no more trouble then we've already been seeing. Don't you worry about it."

    "You wait for an exaplanation, but Mrs.Claus doesn't expand on what she meant by that. She only takes a step back, seemingly satisfied with her examination of you."

    msC "It can't be helped. You'll have to remain here for now until we figure out what to do with you." 

    show Kramp Neu at right 
    with moveinright

    krampus "Mrs. Claus surely you-"

    msC "And what do you suggest we do with them?"
    msC "They barely know who they are let alone where they came from. Surely you're not suggesting that we set the poor thing out in the world with no memories whatsoever."

    krampus "... no, I suppose not" 

    msC "Good."
    msC "Now that that is settled. I'm happy to say you're not as warm as you were earlier, so I don't think you're running a fever. You likely just need some rest."
    msC "You can use this room for the time being."

    hide Kramp Neu with dissolve

    "You take a moment to finally get a good look at the room you've entered."
    "It's a nice bedroom with a table and chairs by the window, as well as a fire place on the opposite side of the room. A small cot lays against the wall where the door to the hall is located."
    "You are seated in a plush chair by said fireplace, and when you look behind you, you find a small vestibule with a shelf crammed full of books."
    "The room is warm and comfortable, and you finally let out the rest of the tension that you didn't realize you were still carrying since your first encounter."

    "In the silence, you pick up on the whispered conversation happening behind the door."

    show Kramp Neu at right 
    show Jack Neu at left
    show Mrs Claus Neu at center
    with dissolve 

    msC "...keep an eye on them."

    jack "You mean like guarding them?"

    msC "No, I don't think they're dangerous."

    krampus "Are you sure about that?"

    msC "Look, they were right about one thing. The moment I saw them it felt like I'd met them before."
    msC "It was something very familiar that I can't seem to place right this moment. But they don't seem dangerous. Not even remotely."
    msC "Until I figure it out, I want you to see if you can help them jog their memories."
    msC "Anything you think could help."

    "The door clicks open again."

    hide Kramp Neu 
    hide Jack Neu
    hide Mrs Claus Neu
    with dissolve 

    show Frosty Neu at center with dissolve
    "Frosty approaches you with a soft smile on his face."

    frosty "It's ok to be scared or overwhelmed. I can't imagine what it feels like to be you right now, but no one here is going to hurt you. I promise."

    "Mrs. Claus comes over once more."

    show Frosty Neu at left with ease
    show Mrs Claus Neu at right with moveinright

    msC "Someone will come check on you in the morning, but for now I suggest you lay down and get some rest."

    "She waves her arms, and ushers everyone out of the room."

    hide Frosty Neu with moveoutright
    hide Mrs Claus with moveoutright

    "You decide to take Mrs. Claus' advice, getting up from the chair to lay on the cot in the corner. It doesn't take long for you drift off to sleep."

    scene bg black screen with fade

    with flash
    play sound "audio/child laugh.mp3"
    "A bright shimmering golden light flashes in your vision, and you hear the sound of childish laughter."
    "The golden book shines before you, brilliant and warm."
    "But you can feel the darkness creeping in."
    "The book's warm light dims as the sound of tearing paper slices through the air."
    play sound "audio/evil laugh.mp3"
    "Vicious, maniacal laughter replaces the sounds of joyous children, and the silhouette of a figure looms ever closer.."

    scene bg sitting room with vpunch 

    "You wake with a start, covered in a cold sweat." 
    "It was just a dream, you tell yourself. Before you have time to process any further, you hear a knock on the door"

    msC "Dear? Are you awake?"

    mc "Yes, come in."

    show Mrs Claus Neu at center with moveinright

    "Mrs. Claus enters with a warm smile, holding a small tray with a steaming cup of tea."

    msC "Good morning, dear. I thought you might need something to calm your nerves after yesterday's excitement."

    "She sets the tray on a nearby table and sits on the chair across from you, her gaze gentle but perceptive."

    msC "Did you sleep well? You look like you've seen a ghost."

    mc "I... I think I had a dream. Or maybe a memory? It’s hard to tell."

    msC "Dreams have a funny way of showing us what we need to see, even if we don't understand them yet. But don't worry too much for now."

    "She pats your hand gently before standing again."

    msC "Come along now. Breakfast is ready, and everyone is waiting. I think you’ll feel better with a full stomach."

    mc "Alright. Thank you, Mrs. Claus."

    hide Mrs Claus Neu with moveoutright
    scene bg hallway with dissolve

    "You follow Mrs. Claus down the winding hallway to enter a large dining room filled with the smell of fresh bread, bacon, and something sweet."

    scene bg dining room

    "A long wooden table sits at the center, already occupied by three men."

    #show Frosty Happy at left with moveinleft
    show Jack Happy at right with moveinright
    show Krampus Neu at center with moveinbottom

    "Frosty, Jack, and Krampus look up as you enter. Frosty waves enthusiastically, while Jack smirks with his usual mischief. Krampus gives a silent nod of acknowledgment."

    frosty "Hey, there they are! Good morning, sleepyhead."

    jack "Took you long enough. I was starting to think you got lost again."

    krampus "Leave them alone, Jack."

    "Mrs. Claus ushers you to a seat at the table, and plates of food are quickly passed your way."

    msC "Eat up, dear. You’ll need your strength."

    "Frosty is the first to break the silence."

    frosty "So, how are you feeling this morning? A little less dizzy, I hope?"

    mc "Better, thank you."
    mc "Although, there are a few things that I'm still wondering about."

    jack "Questions are good! It means you’re curious. And curiosity leads to adventure."

    krampus "Or trouble, in your case."

    "Jack smirks but doesn’t deny it, while Frosty offers you a win grin."

    msC "Speaking of adventure, I’m sure the three of you have plenty to do today."

    jack "Oh, you know me, Mrs. C. Always finding something fun to get into."

    frosty "I’ve got a few things to take care of, but nothing too urgent."

    krampus "And I have work to do."

    msC "Good, good. And you..." 

    "She turns to you with a smile."

    msC "You shouldn’t spend all day cooped up by yourself. Why don’t you join one of them? A little fresh air might help clear your mind."

    show Jack Happy at right with ease
    #show Frosty Happy at left with ease
    show Krampus Neu at center with ease

    "Jack immediately perks up, leaning forward with a playful grin."

    jack "You heard the lady! I’m free all day, and I happen to be excellent company. We could play some games, and maybe find something you like."

    "Frosty gives Jack a pointed look before turning to you with his usual cheerful demeanor."

    frosty "If you’d rather take things slow, I was going to head out to a dog cafe. It’s peaceful there, and you might enjoy the company."

    "Krampus crosses his arms, his expression neutral but inviting."

    krampus "I’ll be skiing today. If you want to join, you’re welcome to. It's a fun activity."


    stop music fadeout 1.0


    menu:
        "Go to the dog cafe with Frosty":
            jump frosty_date_1
            $ fPoints += 2
        "Play games with Jack":
            jump jack_date_1
            $ jPoints += 2
        "Go skiing with Krampus":
            jump krampus_date_1
            $ kPoints += 2

return

label before_date_2:

    scene bg black screen 

    "Blah blah blah plot and stuff"
    "guess what yoyu can choose who to go on your second date with!"

    menu:
        "Frosty":
            jump frosty_date_2
            $ fPoints += 2
        "Jack":
            jump jack_date_2
            $ jPoints += 2
        "Krampus":
            jump krampus_date_2
            $ kPoints += 2

    return

label before_date_3:

    scene bg black screen
    "The next morning, you wake up to the sounds of chatter in the hall."
    play sound "audio/foot steps.wav"
    "You can hear footsteps rushing by your door every so often, followed by muffled voices that you can't quite make out."
    scene bg hallway
    "Disoriented and a little groggy, you slowly make your way outside."
    "You find Ms. Claus standing a little ways away scribbling furiously at a large clipboard."

    msC "Oh, good morning dear. Did you sleep well?" 

    "You nod, and rub your eyes."

    msC "Good. Tomorrow, you'll be out on your first mission, so today's the time to prepare!" 

    mc "A mission?"

    msC "I know it's early, but we're all getting rather busy and we need all hands on deck. It's nothing too dangerous - just a reconnaissance mission to Easter Island."

    msC "Don't worry too much. I'm sure you're quite capable, and you'll have the boys along with you. You also have today to train and prepare." 

    "She looks back down at her clipboard, and frowns, before scribbling something down again."

    msC "I'm sorry I don't have the time to help you myself, but I'm sure the others would be more than happy to work with you. Why don't you find one of them and try your hand in the training room?"
    
    menu:
        "Go to Frosty":
            jump frosty_date_3
            $ fPoints += 2
        "Go to Jack":
            jump jack_date_3
            $ jPoints += 2
        "Go to Krampus":
            jump krampus_date_3
            $ kPoints += 1


label frosty_date_1:
    scene bg hallway
    play sound "audio/door knock.wav"
    "You hastily knock on the door labeled 'Frosty' feeling slightly nervous."

    "Frosty had always seemed very sweet, granted you had only known him for a few days, but due to the circumstances, you felt like you should get to know everyone better, and frosty was the least intimidating out of the bunch."

    "After a moment or two, the door in front of you opens to reveal frosty standing before you."

    "He towers over you, but instead of finding him intimidating, he looks down at you with a bright smile on his face."

    frosty "[mcname]"

    "You smile back at him as he welcomes you into his room."

    scene bg frosty bedroom
    with dissolve 

    "frosty's room is pretty simple, nothing too out of the ordinary here."
    "A plain-ish bed, some shelves holding small knick-knacks like a few books, a small figure, and some plants."
    "The open arrangement and lack of clutter made the room feel very cozy, especially with the plants adding a pop of color here and there."
    "The room also had the faint scent of evergreen trees in the winter, but it wasn't cold surprisingly, for him being frosty the Snowman, but instead was actually kind of warm."

    menu:
        "It's warm in here":
            frosty "Haha yeah. I like to keep it warm in here, contrary to popular belief..."
        "Its very cozy in here":
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

    scene bg cat cafe
    with dissolve

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
    play sound "audio/cat meows.wav"

    frosty "Whiskers!" 

    "Frosty's face lights up as though he's greeting an old friend."

    frosty  "This little guy always says hi first. He's kind of like the cafe's unofficial mascot."

    play sound "audio/cat purr.wav"
    "Whiskers leans in, sniffing frosty's outstretched hand before rubbing against it. frosty grins and gently scratches behind the cat's ears."

    frosty "See? Total sweetheart."
    mc "Do you come here a lot?" 

    "Whiskers curls up comfortably on the table between you."
    "Frosty nods, his tone easygoing but warm."

    frosty "Yeah, whenever I need a little pick-me-up. Something about being here just... makes the world feel softer, y'know? Plus, cats are great company. They don't expect much—just a little kindness—and they give so much back."
    "You glance around the cafe, taking in the peaceful vibe." 

    "A sleek black cat is perched on a windowsill, watching the passersby, while a fluffy orange tabby dozes in a sunbeam."
    "The room feels alive yet tranquil, and you can see why frosty loves it here"
    play sound "audio/foot steps.wav"
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

    play sound "audio/cat purr.wav"
    "There's a moment of quiet as Frosty seems lost in thought, absently scratching Whiskers' chin."
    "You sip your hot chocolate, watching him with a new appreciation. For all his cheerful energy, frosty has a way of grounding a room, making it feel safe and welcoming."

    frosty "Thanks for coming with me today,"
    frosty "I know it's kind of random, but I wanted to share this place with you. It means a lot to me."
    mc "It's not random, I can see why you love it here. I had a great time."

    "frosty beams, his eyes crinkling with joy."

    frosty "Really? That makes me so happy. We'll come back soon, yeah? Maybe next time we can try some of those cookies-or just hang out with the cats more. I think Mittens over there has her eye on you."

    play sound "audio/cat meows.wav"
    "You glance at a fluffy calico peeking at you from behind a stack of books, and frosty laughs. It's warm and easy, and it feels like a perfect ending to the day."

    mc "Next time for sure"

    scene bg outside
    show snow
    with dissolve

    play sound "audio/foot steps.wav"
    "You both step outside into the cold and crisp air."

    frosty "Next time," 

    "Frosty echoes your sentiment, his bright smile lingering as he walks beside you."

    jump before_date_2

    $ frostyDate1 = True

label frosty_date_2_start:

    if frostyDate1:
        jump frosty_date_2_yes

    if not frosty_date_1:
        jump frosty_date_2_no

return

label frosty_date_2_yes:

    scene bg hallway
    play sound "audio/door knock.wav"
    "You choose to knock on the door labeled Frosty again."
    "Last time you had an amazing time with him and couldn't stop thinking about what it would be like to spend another day with him."
    "So you chose to hang out with him again."

    frosty "[mcname]!"

    scene bg frosty bedroom
    with dissolve
    "Frosty says to you as he opens the door, excited to see that you choose to spend time with him again."

    mc "Hey Frosty!" 

    frosty "I'm so happy you came back! I have a fun day planned for us. Are you ready?"

    mc "Woah, someone is ready to go. Hell yeah I am!"

    frosty "Awesome! Make sure to bundle up, we're going to be outside."

    mc "Uh, Ok! Let me just grab my stuff and I'll meet you outside?"

    frosty "Perfect!"

    jump frosty_date_2


label frosty_date_2_no:

    scene bg hallway
    play sound "audio/door knock.wav"
    "You hastily knock on the door labeled 'Frosty' feeling slightly nervous."

    "Frosty had always seemed very sweet, granted you had only known him for a few days, but due to the circumstances, you felt like you should get to know everyone better, and Frosty was the least intimidating out of the bunch."

    "After a moment or two, the door in front of you opens to reveal Frosty standing before you."

    "He towers over you, but instead of finding him intimidating, he looks down at you with a bright smile on his face."

    frosty "[mcname]"

    scene bg frosty bedroom
    with dissolve 

    "You smile back at him as he welcomes you into his room."

    "Frosty's room is pretty simple, nothing too out of the ordinary here."

    "A plain-ish bed, some shelves holding small knick-knacks like a few books, a small figure, and some plants."

    "The open arrangement and lack of clutter made the room feel very cozy, especially with the plants adding a pop of color here and there." 

    "The room also had the faint scent of evergreen trees in the winter, but it wasn't cold surprisingly, for him being Frosty the Snowman, but instead was actually kind of warm."

    menu:
        "It's warm in here":
            frosty "Haha yeah. I like to keep it warm in here, contrary to popular belief..."
        "Its very cozy in here":
            frosty "Thank you! I try to keep it nice and welcoming in here, although the others aren't really ones for hanging out..."

    frosty "I'm really happy you came to hang out with me today. I have a really fun day planned and I am happy to share it with you!"

    mc "Oh wow Frosty that's so nice of you!"

    frosty "Of course! How else are we going to welcome the new member of the team? Make sure to bundle up, we're going to be outside."

    mc "Alright!"

    jump frosty_date_2


label frosty_date_2:

    "You grab your coat, scarf, and gloves, making sure you're bundled up for whatever Frosty has planned."
    scene bg outside
    show snow
    "Stepping outside, you see him waiting for you at the bottom of the steps, his cheeks tinged pink from the cold and excitement."
    "There's something magical about the way he seems to glow, as if winter itself has chosen him as its representative."

    frosty "Ready to go?"

    "Frosty holds out his hand for you to take to begin your journey"

    mc "Lead the way!" 

    "You slip your hand into his. His touch is cool but not uncomfortable." 
    "It's a sensation that reminds you of holding fresh snow."
    play sound "audio/snow foot steps.wav"
    "As the two of you walk, Frosty chatters excitedly about the day ahead."

    frosty "I hope you like skating! There's this great little rink nearby. It's got fairy lights, music, and everything!"

    "As he talks to you, you look up into his eyes and see they are sparkling like fresh frost on a windowpane"

    mc "Sounds perfect!"

    play music "audio/winter music.mp3"
    scene bg ice rink
    play sound "audio/ice skating.wav"
    "When you arrive, the scene is just as Frosty described: the rink is surrounded by tall trees wrapped in twinkling lights, and a soft melody drifts through the crisp air."
    "Couples and families glide gracefully, or hilariously awkwardly, across the ice, their laughter mingling with the soft crunch of skates."
    "Frosty turns to you, a playful grin on his face."

    frosty "So, are you a natural, or should I prepare for a lot of falling?"
    mc "Guess you'll just have to find out, but I did just become a person and all only a few days ago."
    
    "He laughs and grabs your hand again, leading you toward the rental booth."
    "Soon enough, you're both lacing up your skates. Frosty finishes first and hops up, balancing effortlessly."

    mc "Show-off..."
    frosty "I can't help it. Ice and I, we go way back."

    "Once you're ready, he helps you to your feet."
    "Your first steps on the ice are a little shaky, but Frosty is right there beside you, steadying you with his hands."

    frosty "Just take it slow." 

    "Frosty's voice is soft and reassuring"

    frosty "I've got you."

    "The two of you make your way onto the rink."
    "At first, you're clinging to Frosty's arm for dear life, but his patience and encouragement soon have you finding your balance."

    mc "See? You're doing great!"

    "You smile widely at him and he smiles back."
    "His rosy cheeks and gentle nature give you a sense of comfort that you have yet to experience in this world yet."
    "Frosty not only makes you feel at ease but he feels like home to you."
    "As the evening goes on, you and Frosty laugh, stumble, and eventually find a rhythm."
    "There's a moment when he spins you around, his laughter echoing like bells in the winter air."
    "For a brief second, you feel weightless, as if the world is nothing but you, him, and the sparkling ice beneath your feet."
    "By the time you leave the rink, your cheeks are red from the cold and exertion, and your heart is warm from the joy of the evening."

    mc "That was amazing!"

    "He smiles, his breath visible in the frosty air."

    frosty "I'm glad you had fun. I knew today would be special."

    scene bg outside
    show snow
    "As you walk back together, Frosty suddenly stops and looks at you, his expression soft and sincere."

    frosty "Thanks for choosing to spend your time with me, [mcname]. It means a lot."

    "You feel a blush rise to your cheeks, not from the cold this time."

    mc "Anytime, Frosty. I can't wait for our next adventure."
    with fade
    stop sound

    jump before_date_3

label frosty_date_3:
    scene bg hallway
    play sound "audio/door knock.wav"
    "You knock on Frosty's door, and for a moment, the quiet of the hall feels heavier than usual. It's not just the anticipation of tonight's training."
    "It's the knowledge that this might be your last night like this. Together."

    scene bg frosty bedroom
    with dissolve
    "When the door swings open, Frosty is already smiling, his usual easy warmth lighting up the space."
    "But tonight, there's something different in his expression a softness, an understanding."

    frosty "[mcname]!"

    "His voice is quieter than usual but no less welcoming."

    frosty "You ready to do this?"

    "You nod, trying to steady yourself."

    mc "Yeah. Let's go."

    "He steps aside to let you in, then falls into step beside you as you head toward the gym."
    "The silence between you isn't awkward; it's something shared, unspoken but understood."

    frosty "I know I've been saying this every day lately,"

    "Frosty says while rubbing the back of his neck."

    frosty "but I'm really glad you picked me to train with. I mean, I'm not saying I'm the best fighter around, but..."

    "He pauses, glancing at you with a small, crooked smile."

    frosty "I'm glad it's me."

    mc "I wouldn't have it any other way,"

    "His smile widens just enough to make your chest ache."

    scene bg training room
    with dissolve
    "When you reach the gym, the fluorescent lights buzz faintly, casting their cold glow over the stark space."
    "It's the same as always: punching bags, training dummies, rows of weights, but tonight, it feels different."

    "Frosty steps into the center of the room, motioning for you to follow."

    frosty "Alright, this is it. One last session before... well, before everything."

    "He looks at you, his usual playful demeanor giving way to something more serious."

    frosty "We're gonna make it count."

    "You nod, swallowing the lump in your throat."

    frosty "Okay, first things first: gear."

    "He holds out his hands, and the air around him chills slightly."
    play sound "audio/magic.wav"
    "Snow swirls in his palms, compressing and solidifying into a pair of brass knuckles that glint like polished ice."
    "This time, they're more intricate than before, the designs etched into them sharp and deliberate."
    "He hands them to you with a small smile."

    frosty "They're not just weapons, they're a part of me. I wanted you to have something... just in case."

    "You slip them on, the cold seeping into your skin before settling into a comfortable warmth."

    mc "They're perfect,"

    "You are at a loss for words for how kind of a gesture this is. You look up at him smiling."

    mc "Thank you."

    "He grins, but it's softer this time."

    frosty "Alright, let's get to work."

    "Frosty moves to a training dummy, his movements fluid but deliberate as he demonstrates the basics: balance, power, precision."
    "He keeps his instructions simple but effective, adjusting your stance with gentle nudges and murmured encouragement."

    frosty "Good,"

    "He steps back to watch as you throw another punch."
    play sound "audio/punch.wav"
    with hpunch

    frosty "Now, again. Keep your shoulders loose, but focus on where you want to hit. Make it count."

    play sound "audio/punch.wav"
    "You follow his guidance, feeling the weight of the brass knuckles amplify your strikes."
    play sound "audio/punch.wav"
    "Each punch lands with a satisfying thud, and Frosty's quiet murmurs of approval spur you on."
    play sound "audio/punch.wav"
    with hpunch

    "As the session continues, the room feels warmer, like the space between you is charged with something unspoken."
    "When he steps closer to demonstrate a block, his hands linger on yours for just a moment longer than necessary."

    frosty "You've got this, you're stronger than you think, [mcname]. I've always known that."

    "His words sit with you, sinking deeper than the physical strain of the training."
    "You push yourself harder, knowing this is your last chance to prepare."

    "By the time you're finished, the two of you are sitting side by side on the floor, your backs against the wall."
    "The gym is quiet now, save for the faint hum of the lights."

    frosty "[mcname],"

    "Frosty starts, his tone unusually soft. He hesitates for a moment before continuing." 

    frosty "No matter what happens tomorrow... I just want you to know... I'm proud of you."
    frosty "You're everything this world needs. And if it comes down to it..."

    "He trails off, his gaze dropping to the floor before meeting yours again."

    frosty "You'll make it. I know you will."

    mc "Frosty..."

    frosty "Hey"

    "He flashes you a grin that doesn't quite reach his eyes."

    frosty "No sad stuff, okay? We've got enough of that coming. Let's just... stay here a little longer. Just us."

    "You nod, leaning your head against his shoulder."
    "His arm comes up around you, pulling you closer."
    "For a moment, it feels like time slows, like the world beyond this room doesn't exist."

    "And even though the battle looms large on the horizon, here, in this moment, you feel safe."

    "Together, you sit in the glow of the fluorescent lights, knowing this is the end of one chapter and the start of another."
    "Whatever comes next, you'll carry this moment with you. Always."
    with fade
    return


label jack_date_1:

    scene bg jack bedroom

    "You step into the dimly lit gaming room, where neon LED lights cast a soft blue glow, creating an atmosphere that feels both exciting and relaxed."
    "Jack Frost is already there, sitting cross-legged on a beanbag chair."
    "His icy white hair catches the light, giving him an ethereal look. He grins when he sees you."

    show Jack Happy at center
    with fade
    jack "Hey!"

    show Jack Neu at center
    "His voice is crisp but warm, like a winter breeze."

    jack "Thought this might be a cool way to hang out. Get it? Cool?"

    show Jack Happy at center
    "He chuckles at his own pun, a mischievous glint in his icy blue eyes."
    "You laugh, shaking your head."

    mc "You're lucky I like bad jokes. What are we playing?"

    "Jack holds up two controllers."

    show Jack Neu at center
    jack "Mario Kart. A classic choice, right? I hope you're ready for some friendly competition."

    scene bg gaming
    with dissolve
    "You settle into a beanbag next to him, taking the controller he offers. The menu screen flashes on the TV, and cheerful music fills the room."
    "As the first race begins, Jack leans over slightly, whispers..."

    show Jack Sad
    jack "Fair warning-I might be a little {i}frosty{/i} when I lose."

    play sound "audio/mario kart.mp3" volume 0.5
    "The game starts, and Jack is immediately in the lead. He's surprisingly good at this, dodging shells and drifting around corners with ease."

    show Jack Neu at center
    jack "Come on, keep up!"

    "Jack continues teasing, throwing a playful glance your way."

    mc "Oh, I see how it is."

    "You focus harder, managing to snag a red shell."

    mc "Take this!" 

    with hpunch
    "You launch the red shell, and it hits Jack's character just before the finish line. You zoom past him, claiming first place."
    "Jack stares at the screen in mock horror."

    show Jack Sad at center
    jack "No way. You iced me!" 

    show Jack Happy
    "He bursts out laughing, his laugh as light and bright as the snowflakes outside the window."

    mc "Guess you're not as unbeatable as you thought."

    show Jack Neu
    jack "Okay, okay."

    "He concedes, raising his hands in surrender." 

    show Jack Happy
    jack "Best two out of three? Or... want to team up and take on the AI together?"

    "You can't help but smile at the suggestion."

    mc "Let's team up. I'd hate to embarrass you again."

    "Jack shakes his head with a grin."

    jack "Alright, but if we win, I'm taking credit. Deal?"

    hide Jack Happy with fade
    "The two of you spend the rest of the evening racing through pixelated landscapes, throwing banana peels, and laughing at each other's mishaps." 
    "Jack's energy is infectious, and you find yourself completely at ease as if the world beyond this cozy gaming room doesn't exist."
    "As the night winds down and the final race ends, Jack turns to you, his expression softening."

    scene bg jack bedroom

    show Jack Happy at center
    jack  "This was fun," 
    
    "His voice is quieter now."

    jack "I don't usually... hang out like this. But I'm glad I did-with you."

    "Your heart warms at his words, and you smile back." 

    mc "Me too. Same time next week?"
    with fade

    jump before_date_2

label jack_date_2:

    scene bg ice rink
    show Jack Neu at center
    with fade
    play sound "audio/ice skating.wav"
    "The air is crisp and cold as you step onto the ice rink, its surface gleaming under the soft glow of fairy lights strung overhead. Snowflakes drift lazily from the sky, and the entire scene feels like something out of a winter dream."
    "Jack Frost is already waiting near the edge of the rink, leaning casually against the barrier." 
    "His icy white hair sparkles under the lights, and when he spots you, he stands up straight, a playful grin spreading across his face."

    jack "About time you got here," 

    "He holds out a pair of skates for you."

    show Jack Happy
    jack "I was starting to think you were scared to face the ice with me."

    "You take the skates, laughing."

    mc "Oh, I'm not scared. I just didn't want to show you up too soon."

    show Jack Neu
    "Jack arches an eyebrow, a mischievous glint in his eyes."

    show Jack Happy
    jack "Big talk for someone who hasn't even laced up yet."

    "Once your skates are on, Jack leads you to the rink. He steps onto the ice effortlessly, gliding backward as if he was born to skate."
    "Well, maybe he was. His movements are smooth and graceful, every motion infused with a hint of magic. You follow, a little less confident but determined not to let him show you up completely."

    show Jack Neu
    jack "Need a hand?" 

    "Jack offers you his hand, his voice is teasing, but there's a genuine warmth in his expression."
    "You take his hand, and the chill of his touch sends a shiver up your spine-not unpleasant, just cool enough to remind you of who he is. He pulls you along, helping you find your balance."

    show Jack Happy
    jack "There, see? You're a natural. Almost as good as me."
    mc "Watch this."

    "You try a daring spin, only to wobble precariously and nearly fall."
    with vpunch
    "Jack catches you easily, his laugh ringing out like bells on a frosty morning."

    show Jack Neu
    jack "Nice try,"
    jack "But leave the fancy moves to the professional."

    hide Jack Happy with fade
    "As the evening goes on, you relax more, skating side by side with Jack."
    "At one point, he waves his hand, and a shimmering frost spreads across the ice, creating intricate patterns of snowflakes and swirls that glisten under the lights."

    show Jack Happy at center
    mc "Wow, Show-off much?"
    show Jack Sad
    jack "Hey, I've got to impress you somehow."
    mc "You don't have to try so hard."

    show Jack Happy
    "Jack's smirk softens into a genuine smile."

    jack "Careful." 

    show Jack Neu
    "He leans in slightly, his breath cool against your cheek."

    jack "Say things like that, and I might actually believe you enjoy my company."

    "You laugh, your cheeks warm despite the cold."

    mc "Maybe I do."

    show Jack Happy
    "Jack pulls back, grinning again."

    jack  "Good. Because I was thinking, next time, we could build a snow fort. Unless you're too scared to lose at that, too."
    mc "Not a chance, but you better bring your A-game."

    hide Jack Happy with fade
    "The two of you skate a little longer, weaving around the rink as snow falls softly around you."
    "The world feels quiet and magical, and as Jack skates beside you, his laughter mixing with yours, you think there's no place you'd rather be."
    with fade
    stop sound

    jump before_date_3

label jack_date_3:
    scene bg training room
    "The military gym is stark and utilitarian, with fluorescent lights casting a cool glow over the room."
    "It's filled with various equipment for physical and tactical training, but in the center of it all stands Jack Frost, leaning casually against his frost-covered staff."
    "Despite the harsh setting, he looks as effortlessly cool as ever, his icy white hair almost glowing under the lights."

    show Jack Neu at center
    jack "Finally." 

    "Jack calls out as you approach, his voice echoing slightly in the cavernous space."

    show Jack Sad
    jack "Thought you might've chickened out on me."

    "You roll your eyes, adjusting your gloves."

    mc "Chickened out? I could say the same about you. Are you sure you're not too fragile for this kind of training?"

    show Jack Happy
    "Jack laughs, a sound like cracking ice."

    jack "Oh, you've got jokes. Alright then, let's see if you can back it up." 

    "He tosses you his staff, and you catch it, the icy chill of it seeping through your gloves."

    show Jack Neu
    jack "First lesson, this isn't just a fancy walking stick. It's an extension of your energy. You want it to work for you? You've gotta connect with it."
    jack "Otherwise, it's just a very expensive popsicle."

    "You hold the staff, feeling its weight and the faint hum of cold energy running through it."

    mc "Alright. So, how do I connect with it?"

    hide Jack Neu
    "Jack steps behind you, his hands lightly covering yours on the staff. His touch is cold, but not unpleasant, like the crisp air on a winter morning."

    jack "Start by grounding yourself. Feel the frost in the staff, let it flow through you. Don't fight it. You've gotta let the cold work with you, not against you."

    "You take a deep breath, focusing on the staff as Jack guides you."

    jack "Now, visualize your target. Let's start with that punching bag over there."

    "Across the gym, a heavy punching bag sways slightly, as if daring you to aim. You nod, raising the staff and focusing."

    mc "Alright, here goes nothing."
    jack "Not nothing, go big or go home."

    with hpunch
    play sound "audio/magic.wav"
    "You swing the staff, and a blast of frost shoots forward, encasing the punching bag in a thin layer of ice. Jack whistles, impressed."

    show Jack Happy at center
    jack "Not bad, rookie. Not bad at all."

    "You grin, spinning the staff experimentally in your hands."

    mc "Looks like I've got the hang of this."

    show Jack Neu
    jack "Don't get cocky..." 

    "There's a mischievous glint in his eye now. He steps back, spinning his own staff effortlessly."

    jack "Now let's see if you can handle a moving target."

    "With a quick motion, he sends a flurry of snow your way."
    with vpunch
    "You scream, dodging the icy attack."

    mc "Hey! I thought we were training, not sparring!"
    jack "This {i}is{/i} training," 

    show Jack Happy
    "He was laughing at you now."

    jack "You're gonna have to learn to think on your feet."

    "He flicks his staff again, sending another burst of frost toward you."
    with hpunch
    "You block it with the staff, feeling the energy pulse through your hands."

    mc "Two can play at that game," 

    hide Jack Happy
    play sound "audio/magic.wav"
    "You aim to blast frost at Jack. He dodges it easily, his movements as fluid as the wind."
    "The two of you go back and forth, the gym echoing with bursts of frost and laughter."
    "Jack keeps you on your toes, pushing you to react faster, aim better, and trust the staff's power."

    show Jack Happy
    jack "Nice shot!" 

    play sound "audio/magic.wav"
    "You manage to graze his side with a burst of frost. He spins around, his staff creating a swirl of cold air that almost knocks you off your feet."

    show Jack Neu
    jack "But don't celebrate yet!"

    "By the time you both call a truce, the gym is colder than when you started, with frost covering the equipment and ice shimmering on the floor."
    "You're out of breath but exhilarated, the staff still humming faintly in your hands."
    "Jack leans on his own staff, watching you with a mix of amusement and pride."

    show Jack Happy
    jack "You're not half bad. With a little more practice, you might actually keep up with me out there."

    "You smirk, leaning the staff against your shoulder."

    mc "Keep up? I'm pretty sure I'm already ahead."

    "Jack shakes his head, grinning."

    jack "Sure, sure. Keep telling yourself that, rookie. But don't forget-this was the easy part. The real mission's gonna be a lot tougher."
    mc "Good thing I've got the best trainer then." 

    "Jack's grin softens into something more genuine."

    show Jack Neu
    jack "Yeah, well," 

    "Jack ruffles his hair awkwardly."

    show Jack Happy
    jack "Good thing I've got the best partner."

    "You both leave the gym together, the mission looming ahead but feeling just a little less daunting with him by your side."
    with fade
    return
label krampus_date_1:

    scene bg skiing
    "The air is crisp and biting as you stand at the top of the ski slope, looking down at the endless stretch of sparkling white snow."
    "The sun glints off the frosted peaks, and in the distance, the evergreens sway in the cold wind."
    show Kramp Neu at center
    with fade
    "Beside you stands Krampus, his imposing frame dressed in a sleek black ski suit, horns curling up from under his custom-made helmet."
    "His yellow eyes gleam with mischief as he adjusts his skis."

    show Kramp Happy
    krampus "Ready to eat some snow?" 

    "You tighten your gloves and adjust your goggles."

    mc "Eat snow? You're awfully confident for someone who's about to get left behind."

    show Kramp Nod
    krampus "Careful, little one. Pride comes before a tumble down the mountain."

    hide Kramp Nod
    "With a flick of his ski poles, he pushes off, gliding down the slope with a natural ease that makes it clear he's done this a thousand times before."
    "His thick tail flicks behind him like a rudder, helping him navigate the twists and turns with precision."

    krampus "Come on!"
    krampus "Try to keep up, unless you're scared of a little speed!"

    "You grit your teeth and launch yourself after him, the wind whipping past your face as you pick up speed."
    "The slope is steeper than you expected, and your heart pounds as you swerve to avoid small drifts of snow and the occasional tree."
    "Krampus stays just ahead of you, his laughter carrying on the wind."

    krampus "You're not bad!"
    krampus "But you'll never catch me at that pace!"
    mc "Oh, we'll see about that!"

    "You push yourself harder, gaining ground as you race toward him."
    show Kramp Happy at center
    "Krampus glances back, his grin widening." 

    krampus "Impressive!"

    "He slows just enough to let you pull alongside him." 
    "Then, with a wicked gleam in his eye, he taps the tip of his ski pole to the snow, sending a small flurry of powder into your path."
    with hpunch

    mc "Hey!" 

    "You swerve to avoid the icy spray."

    krampus "Just keeping things interesting"

    "Krampus' chuckle resonates through the crisp air."
    hide Kramp Happy
    "The two of you race neck and neck, weaving down the mountain with increasing speed."
    "Krampus leaps off a small ridge, landing gracefully and glancing back to see if you dare follow."
    show Kramp Happy at center
    "Not wanting to back down, you take the jump, your skis hitting the snow with a satisfying thud."
    with vpunch

    krampus "Not bad!" 
    krampus "Maybe you've got some spirit after all."

    "As the slope levels out near the bottom, the two of you come to a stop near a small lodge."
    "Your legs are shaky from the exertion, but your adrenaline is pumping, and you can't stop smiling."

    mc "That was amazing!"

    show Kramp Neu
    "Krampus leans on his ski poles, his horns catching the late afternoon light."

    show Kramp Happy
    krampus "Not bad for a rookie!"
    show Kramp Nod
    krampus "Though I'd still say I won."

    mc "You wish!" 
    mc "I was right behind you the whole time."

    krampus "Close..." 
    show Kramp Happy
    krampus "but next time, I'll make sure you can't keep up."
    mc "Next time?"

    "You raise an eyebrow."
    "He grins, baring sharp teeth."

    show Kramp Nod
    krampus "You didn't think this was a one-time thing, did you?"
    krampus "I've got plenty of slopes to show you... if you think you can handle them."

    "You smile, feeling the warmth of the challenge in his tone."

    mc "Bring it on, Krampus. I'll take you on any mountain."

    show Kramp Happy
    "His laugh echoes across the snowy peaks as the two of you head into the lodge, your competitive banter continuing over mugs of steaming hot cocoa."
    "There's a spark of excitement and fun in his presence, and you can't help but look forward to the next adventure."
    with fade

    jump before_date_2

label krampus_date_2:
    scene bg bar
    "The bar is dimly lit and cozy, with flickering candlelight reflecting off bottles of aged whiskey and frosted mugs of beer."
    "The air is warm, a welcome contrast to the biting cold outside, and the hum of quiet conversation mingles with the crackle of a nearby fireplace."
    show Kramp Neu at center
    "Seated at a corner table, Krampus cuts an imposing figure even in this laid-back setting. His dark fur peeks out from under a tailored coat, and his horns curl gracefully, catching the soft glow of the lights."
    "When you approach, his crimson eyes lift to meet yours, and a wicked grin spreads across his face."

    show Kramp Happy 
    krampus  "There you are." 
    krampus "I was beginning to think you got lost in the snow."

    "Sliding into the seat across from him, you smirk."

    mc  "I don't get lost that easily. What are we drinking?"

    "Krampus gestures to the bartender, who brings over two glasses filled with a dark amber liquid."

    show Kramp Neu
    krampus "Mulled wine."
    krampus "Warms you up from the inside out. Unless you can't handle a little heat?"
    show Kramp Nod

    "You raise an eyebrow and take a sip. The wine is rich and spiced, with a subtle warmth that spreads through your chest."

    mc  "Not bad." 
    mc "But I expected something... stronger from you."

    show Kramp Happy
    with vpunch
    "His laugh is low and rough, like boots crunching through snow."

    show Kramp Nod
    krampus  "Careful, little one. Challenge me, and you might regret it."

    mc "Oh, I'm not scared." 
    mc "What else you got?"

    show Kramp Neu
    "Krampus signals again, and this time the bartender brings over a pair of frosted shot glasses filled with a glowing blue liquid."

    show Kramp Happy
    krampus "Icefire shots." 
    show Kramp Neu
    krampus "They burn cold going down. Think you can keep up?"

    "You pick up the glass, the chill biting against your fingertips."

    mc "Only one way to find out."

    "The two of you toast, and you down the shot in one gulp. It's like swallowing a snowstorm, the icy burn rushing through your throat and leaving a strangely invigorating warmth behind."
    "You cough slightly, and Krampus laughs, his shoulders shaking."

    show Kramp Happy
    krampus "Not bad." 
    show Kramp Nod
    krampus "But I barely saw you flinch. Maybe there's more to you than I thought."

    mc "Was that supposed to impress me?" 
    mc "Because I'm still standing."
    
    "Krampus leans back in his chair, swirling the remnants of his drink." 

    show Kramp Neu
    krampus "Alright, you're tougher than most. But let's see how sharp you are after another round."

    "The night goes on with more drinks, each one seemingly more exotic and potent than the last."
    "Between sips, Krampus regales you with darkly humorous tales of his escapades: scaring the naughty into good behavior, outwitting hunters, and even a wild snowball fight with Jack Frost that left a village buried under a week's worth of snow."

    krampus "So, what about you?" 
    krampus "What's the wildest thing you've ever done?"

    "You laugh, shaking your head."

    mc "Oh no, I'm not falling for that one. You'll have to work harder if you want my secrets."

    show Kramp Happy
    "His grin is all sharp teeth and mischief."

    show Kramp Neu
    krampus  "Fair enough. But don't think I won't figure you out eventually."

    "As the bar starts to quiet down, you realize how much you've been enjoying yourself."
    "Despite his intimidating presence, Krampus is surprisingly easy to talk to-charming in his own gruff, devil-may-care way."
    play sound "audio/foot steps.wav"
    "When you finally get up to leave, he follows you to the door, his towering frame casting a shadow over the snow-dusted street outside."
    scene bg outside
    show snow

    show Kramp Happy
    krampus "This was fun!" 
    krampus "You've got spirit. I like that."

    mc "Maybe we'll do it again sometime." 

    "Krampus smirks, his sharp teeth glinting in the moonlight."

    krampus "Careful what you wish for. I've got plenty more tricks up my sleeve."

    play sound "audio/snow foot steps.wav"
    "As you part ways, the warmth of the bar lingers with you, along with the memory of Krampus's devilish grin and the laughter you shared."
    "Something tells you this won't be the last time you cross paths with him."
    with fade
    
    jump before_date_3

    label krampus_date_3:

    scene bg training room
    "The gym smells of leather, chalk, and sweat, the air thick with the energy of past battles fought and won."
    "It's stark with heavy punching bags hanging in neat rows and a well-worn boxing ring in the corner."
    "The sharp clang of metal weights echoes as you walk in, but your attention is locked on Krampus, who's standing near a makeshift sparring mat."
    "He's shed his usual coat, his broad chest and arms exposed save for the thick fur that covers him like armor."
    "His claws flex and curl as he stretches, and his horns gleam under the cold fluorescent lights. His red eyes fix on you as you approach, a grin playing at the corners of his sharp mouth."

    show Kramp Neu at center
    krampus "Well, well"
    show Kramp Happy
    krampus "Look who finally decided to show up. Thought you might back out when you heard the words 'bare knuckle.'"

    "You roll your shoulders, matching his smirk."

    mc "And miss out on the chance to put you on the mat? Not a chance." 
    show Kramp Nod
    krampus "Big talk. Let's see if you can back it up."

    "Krampus motions for you to step onto the mat, and you do, kicking off your boots and wrapping your hands with the provided bandages."
    "As you finish, he saunters over, his claws dragging lightly across the mat as if testing its texture."

    show Kramp Neu
    krampus "First lesson..."
    krampus "Boxing isn't just about throwing punches. It's about control. You've got to stay balanced, protect yourself, and know when to strike. Otherwise, you're just flailing around, waiting to get flattened."

    "He steps closer, towering over you but not in a way that feels threatening. His massive hands hover over yours, guiding them into position."

    show Kramp Nod
    krampus "Hands up. Chin down. And for the love of god, don't drop your guard."

    "You mimic his stance, fists up and knees slightly bent."

    mc  "Like this?"
    show Kramp Happy
    krampus "Not bad." 
    show Kramp Neu
    krampus "But you're too stiff. Loosen up, or you'll telegraph every move."

    "Before you can adjust, he flicks out a clawed hand-not hard, but fast enough to tap the side of your head."
    play sound "audio/punch.wav"
    with vpunch

    show Kramp Nod
    krampus "See? Wide open."

    mc "Hey!"

    "You protest, resetting your stance."

    mc "I wasn't ready."

    show Kramp Neu
    krampus "You think your enemies are going to wait for you to be ready?" 
    krampus "Stay focused, or you're just giving me more opportunities to humiliate you."

    "You narrow your eyes, determination sparking."

    mc "Alright, big guy. Let's see what you've got."

    show Kramp Happy
    "Krampus raises an eyebrow, clearly amused."

    krampus "That's the spirit."

    show Kramp Neu
    "He squares up in front of you, his movements are surprisingly fluid for someone so large."

    krampus "Try to hit me." 

    play sound "audio/punch.wav"
    "You hesitate for half a second before throwing a jab at his midsection. He sidesteps effortlessly, tapping your wrist to deflect the blow."

    krampus "Too slow." 

    play sound "audio/punch.wav"
    "You try again, this time feinting with one hand and aiming higher with the other. Krampus blocks with ease, his reflexes razor-sharp."

    show Kramp Happy
    krampus  "That's better." 
    show Kramp Nod
    krampus "But your footing's off. You're leaning too far forward."

    mc "Fine." 
    mc "What about this?"

    play sound "audio/punch.wav"
    "You launch a series of quick strikes, mixing high and low targets. Krampus blocks and dodges most of them, but one punch grazes his side. He steps back, laughing."
    play sound "audio/punch.wav"

    show Kramp Happy
    krampus "Now that's more like it. You've got some fire in you."
    mc "Was there ever any doubt?"

    show Kramp Nod
    "He shakes his head, his grin never fading." 

    show Kramp Neu
    krampus "Oh, I didn't doubt it. I just like seeing it for myself."

    hide Kramp Neu
    play sound "audio/punch.wav"
    "For the next hour, he pushes you harder, teaching you how to move, dodge, and strike with precision."
    "His critiques are sharp but never cruel, and every time you land even the smallest hit, he praises you with a mix of amusement and genuine pride."
    "By the end of the session, your knuckles are sore, and your body feels like it's been through a storm."
    "But there's a satisfaction in the ache, a sense of accomplishment."

    show Kramp Happy at center
    krampus "You did good."
    show Kramp Nod
    krampus "For a beginner, anyway."

    mc "Thanks." 
    mc "You're not a bad teacher."

    "He chuckles, his red eyes glinting."

    show Kramp Happy
    krampus "Careful with the compliments. I might start expecting you to listen next time."

    mc "Next time?"

    show Kramp Neu
    "Krampus leans back, his claws resting on his knees."

    show Kramp Nod
    krampus "Oh, this was just the warm-up. The real fun starts when we get into advanced techniques. If you're up for it, of course."

    "You grin, despite your exhaustion."

    mc "Bring it on."

    "Krampus smirks, baring his sharp teeth."

    show Kramp Happy
    krampus "You've got guts. I like that."

    "With Krampus by your side, even the toughest challenges seem a little more thrilling-and a lot more fun."
    with fade
    return

label before_mission:

    scene bg easter island
    "Date: 12.16.2024"
    "Time: 0600"
    "Location: Easter Island, Outskirts"
    

    show Jack Neu at center
    show Kramp Neu at Right
    show Frosty Neu at left
    "You, Jack Frost, Krampus, and Frosty arrive on Easter Island bright and early the following day." 
   
    kramp "Let's go through it one more time."

    kramp "We are here on Easter Island on reconnaissance for information on the Easter Bunny. The Easter Bunny's pages were the most recent to go missing, and soon after the Bunny himself disappeared as well."

    jack "Right. This is where he spent his time, so this is where we're looking."
    
    frosty "Should we split up?"

    kramp "Yes, to cover more ground. Let's take pairs."

    "All three of them look at you, seeming to wait for you to pick a partner." 
    "You'll go with..."
    menu:
        "Jack":
            jump jack_easter_island
            $ jPoints += 2
        "Frosty":
            jump frosty_easter_island
            $ fPoints += 2
        "Krampus":
            jump krampus_easter_island
            $ kPoints += 2
    with fade


label jack_easter_island:
    scene bg easter island
    "The air grows colder as you and Jack step into the Egg Collection Depot. Rows upon rows of towering, rainbow-colored crates stretch out before you, the vibrant hues eerily dim under the flickering lights."
    "A faint, mechanical hum echoes through the space, accompanied by the rhythmic clinking of conveyor belts that have long since stopped running."
    play sound "audio/foot steps.wav"
    "Jack walks beside you, his staff tapping softly against the tiled floor."

    show Jack Neu at center
    jack "Well, this place screams 'cheerful holiday magic,' doesn't it?"

    "You glance up at the crates stacked precariously high."

    mc "More like abandoned magic. What do you think happened here?"

    "Jack shrugs, twirling his staff absently."

    show Jack Sad
    jack "Could be sabotage. Could be someone didn't pay their electricity bill. Either way, it's weird that no one's here."

    "As you move deeper into the depot, the silence feels oppressive. You notice broken eggshells scattered along the floor, their once-bright pastel colors dulled."
    "Jack kneels to examine them, brushing his gloved fingers over the shards."

    show Jack Neu
    jack "These weren't dropped by accident." 
    jack "Something smashed them on purpose."

    "You frown, looking around for more clues."

    mc "If this is sabotage, it's targeted. Why the eggs?"

    "Jack rises, his expression grim."

    show Jack Sad
    jack  "Because without the eggs, Easter doesn't happen. Whoever's behind this knew exactly what they were doing."

    "A sudden noise-a faint scuffling coming from another room-catches your attention. Jack instinctively raises his staff, a faint frost spreading across the ground around him."

    show Jack Neu
    jack "Stay close."

    "You nod, heart pounding as the two of you move toward the sound."
    "Jack looks at you, his expression sharp and determined."
    "You exchange a brief, tense glance before entering the next room, both of you ready for whatever-or whoever-you might find."
    with fade
    return

label krampus_easter_island:

    scene bg easter island
    "The air is damp and heavy as you and Krampus descend into the labyrinthine distribution tunnels beneath the Easter hub."
    "The walls are carved from rough stone, lined with rusted tracks that once ferried brightly painted egg crates to the surface."
    "Now, the tracks lie abandoned, with overturned carts and shattered eggs littering the ground."
    play sound "audio/foot steps.wav"
    "Krampus strides ahead, his claws clicking faintly against the stone floor."

    show Kramp Nod at center
    krampus  "Cheerful place." 
    krampus "Nothing says holiday spirit like a crypt for candy."

    "You glance around uneasily. The tunnel feels more claustrophobic with each step, the dim light from Krampus's glowing lantern barely illuminating the path ahead."

    mc  "This used to be the heart of the operation."
    mc "Without these tunnels, there's no distribution. Whoever hit this place really wanted Easter to grind to a halt."

    show Kramp Neu
    "Krampus huffs, his breath visible in the chilly air." 

    krampus "Makes sense. Take out the foundation, and the whole thing collapses. Classic sabotage."

    "As you move deeper, the tracks lead to a large, sealed gate. The metal is dented, with deep claw marks raked across its surface. Krampus kneels to examine them, his sharp claws tracing the grooves."

    show Kramp Nod
    krampus "Not a rabbit." 
    krampus "Too big. Something else tore this open."

    mc "Could it be who-or what-took the Bunny?"

    show Kramp Neu
    krampus "Maybe." 
    krampus "Or maybe it's something worse. Either way, we're not stopping here."

    "He plants his claws on the edge of the gate and pushes, the metal groaning under his strength."
    "The gate creaks open just enough for the two of you to slip through, revealing a sprawling cavern filled with abandoned egg crates. Some are smashed, while others are eerily intact, stacked haphazardly as if left in a rush."
    "Krampus sniffs the air as his expression darkens."

    show Kramp Nod
    krampus  "Something was here recently."

    "You pause, listening. There's a faint sound somewhere in the distance, but nothing else."

    mc  "Do you think it's still here?"

    show Kramp Neu
    krampus  "If it is, we'll deal with it. Come on."

    "As you continue through the cavern, you spot something unusual-a set of wheel tracks, fresh and cutting through the dust. They veer off into another room."
    "Krampus notices them too, his grin fading into a focused scowl."

    show Kramp Neu
    krampus "Could be our missing Bunny. Or whoever took him."

    mc "Do we follow?"

    show Kramp Neu
    krampus "We follow. But stay close. This feels like a trap."

    "Together, you walk into the room with the sense of unease pressing down on you both."
    with fade
    return

label frosty_easter_island:
    scene bg easter island
    play sound "audio/light buzz.wav"
    "The fluorescent lights buzz faintly as you and Frosty step into the Snowflake Engineering Bay, the heart of winter's magic production. The air is crisp and cool, carrying the faint scent of ozone and pine. Frosty runs a gloved hand along one of the frost-covered consoles, his breath fogging in the chilly air."
    mc "This is where the snowflakes are made?"
    frosty "Yeah. Every flurry, every blizzard, every perfectly unique snowflake starts here."
    mc "It's... empty."
    frosty "Yeah, and that's a problem. This place is usually a flurry of activity-pun intended."

    "Rows of intricate machinery line the room, their surfaces frosted over like forgotten relics. Frosty moves ahead, his boots crunching softly against the frost-covered floor. He kneels beside a shattered snowflake mold, lifting a shard with care."
    frosty "This isn't just damage. It's deliberate."
    mc "Someone sabotaged it?"
    frosty "Looks like it. These molds are tough. Whoever did this knew exactly where to hit to shut the whole system down."

    "As Frosty inspects the room, the frost on the machines seems to shift slightly, catching the dim light in a way that makes the space feel alive. You notice a set of deep, uneven gouges along the floor, trailing toward one of the larger machines."
    mc "Frosty, look at this. What could've made those marks?"
    "Frosty joins you, crouching down to trace the grooves with his finger. His brow furrows."
    frosty "Not claws. Too smooth for that. Maybe some kind of tool? Whatever it was, it dragged something heavy out of here."
    mc "The molds?"
    frosty "Could be. But why take them? If you just wanted to stop the snowflake production, smashing them would've been easier. This feels... bigger."

    "A faint sound-a distant hiss of air-draws both of your attention. Frosty rises to his full height, his expression hardening as he glances toward the source of the noise."
    frosty "Stay behind me."
    mc "You think someone's still here?"
    frosty "Or something. Either way, I don't want you getting hurt."

    "He steps forward, the room seeming colder with every step he takes. You follow closely, your breath visible in the frosty air. The hiss grows louder as you approach a massive piece of machinery, its outer shell cracked and leaking vapor."
    mc "What is that?"
    frosty "A snow generator. Or what's left of one."

    "He leans closer, his eyes narrowing as he examines the cracks. The vapor suddenly shifts, coalescing into a thick cloud of mist that begins to swirl around the machine. Frosty instinctively raises his hand, summoning a thin sheet of ice that forms a barrier between you and the mist."
    frosty "Looks like someone didn't want us snooping around."
    mc "Can you stop it?"
    frosty "I can try. But I need you to stay sharp, okay? If this thing is more than just a defense system, we're in for a fight."

    "With a sharp flick of his wrist, Frosty sends a wave of ice shooting toward the machine. The mist recoils, dissipating for a moment before reforming, more aggressive than before. Frosty's jaw tightens."
    frosty "Figures. Nothing's ever simple, huh?"

    "As the mist closes in, Frosty glances back at you, his expression determined."
    frosty "We're gonna get through this. Together."
    mc "Right."

    "With Frosty leading the charge, you brace yourself for whatever's coming next, the chill in the air matching the resolve between you."
    return

label confrontation:
    scene easter island
    "You round the corner to be faced with all three of your companions, who look at you in surprise to have also found each other." 
    show Jack Neu at center 
    with moveinright
    show Kramp Neu at right
    with moveinleft
    show frosty at left
    with moveinbottom

    mc "We followed the trail here. What's going on?" 

    "The other pair look at each other, and echo the same sentiment." 

    kramp "What did everyone find?" 

    mc "Sabotage, broken machinery..." 

    frosty "Wait, if everything leads here then - "

    play sound "audio/crash.mp3"
    "A loud crash cuts Frosty off as everyone turns to the source of the noise. It's only now that you take stock of the room that you're in." 

    "The room is large but enclosed, with the only windows high enough up the walls that you can't see through them and only a single pair of enormous double doors by your right."
    "The only other exits are the ones you and your companions came through, which are a little ways behind you." 
    "On your left are several rows of flat tables with the remnants of decorations strewn about. It looks like this was made for an assembly line of some kind." 

    play sound "audio/boom.mp3"
    "Another loud boom breaks through your thoughts, and you turn just in time to see the double doors fly open as an enormous, hulking figure bursts into the room."
    "The thing is all hanging flesh and melting limbs, and the thick scent of rot makes you gag on your breath." 

    "You stumble back, arms raised in self defense before your companions rush to your side." 
    
    #frosty sad
    frosty "What is that?" 

    kramp "The Boogyman. Spread out!"
    hide Kramp Neu with moveoutleft
    hide Jack Neu with moveoutright
    hide Frosty Neu with moveoutbottom

    play sound "audio/evil laugh.mp3"
    "The Boogyman roars in delight, its body undulating under the weight of its own mass." 

    boogy "Three legends in one place? And you? Oh, you're something special, aren't you?"

    mc "What? What do you mean?" 

    "You realize a fraction of a second too late that the Boogyman is raising an arm to strike."
    "In a panic, you cover your head, hoping to protect your extremities at the very least." 

    with vpunch
    with flash
    "Instead, you catch a bright flash of light out of the corner of your eye, and look up to see Jack blast a flying fleshy blob out of the sky." 

    show Jack Sad at center
    with moveinbottom
    jack "Move!"
    with hpunch
    hide Jack Sad with easeoutbottom

    "You dive sideways, finding cover behind the tables as the monster turns to Jack. At your side, you find a pair of glowing yellow eyes."

    show Kramp Nod at left
    kramp "It's outnumbered. We can win it if we cover for each other and focus it while it's distracted. Do you understand?" 
    show Kramp Neu at center 
    with ease

    "He only gives you a second to nod before leaping over the table to send a barrage of hits into the Boogyman's side, the wrappings around his hands sparking with energy."

    "Something feels off, though. Krampus' hits seem slower than they should, and you realize with a start that the Boogyman's melting, wax-like body is clinging onto the man's punches."

    mc "Wait! It's grabbing onto you!" 

    "Before you can move, you watch as Krampus hits again, and finds himself unable to draw back."

    kramp "What-"

    play sound "audio/roar.mp3"
    "With a roar, the monster lifts Krampus up by his arm and flings him into a wall with a sickening crunch."

    show Kramp Nod at center
    kramp "..."

    #sad
    frosty "Krampus!" 

    show Jack Sad at left
    with easeinleft
    jack "I've got him. Cover me!" 
    hide Kramp Nod

    "As Jack Frost dashes away, you watch Frosty raise a brass covered knuckle to send a heavy punch into the Boogyman's back."
    "The metal carves a grotesque arc into the monster's back, blood pooling as it opens its mouth in a thundering cry." 

    boogy "You'll pay for that!" 
    with hpunch

    play sound "audio/heartbeat.wav"
    "With Jack only halfway to Krampus and Frosty all alone in the face of the Boogyman's rage, you realize that this is your shot. You can feel your heart pounding in your chest."

    "You step out from behind the table."

    menu:
        "Attack The Boogyman":
            "You throw everything you have at the Boogyman, only stopping to let Frosty grab its attention before attacking again." 
            "It's a grueling effort, and you can feel exhaustion creeping through your body with every attack. Your efforts aren't in vain, however. You also see the monster slowing down." 
            "Chunks of waxy flesh are now scattered across the terrain, leaving steaming pools of goop that you have to jump over and around as you move. The Boogyman's roars are deeper, and rumbling."

    "It lobs another projectile at you, and something clicks in your mind."
    with hpunch

    mc "The eyes! It's not protecting it's eyes!" 

    "From across the warehouse, Frosty nods. He's heard your message."

    "You watch as he throws another hit at the Boogyman, and the monster turns slowly around with its arms in the air - arms that are now away from its face." 

    menu:
        "Aim for its eyes.":
            "With as much strength as you can muster, you sprint forward to make an attack at its face."
            "Your hit spears straight through the Boogyman's sagging, lifeless eyes."
            "The flesh parts almost effortlessly there, unobstructed by the meat that covers the rest of its body, and it recoils almost inward."

    "You have to fall back to avoid being sucked in by its limbs as the monster twists and roars in agony."
    with vpunch
    "From the other side, you can see Frosty making a similar retreat to avoid the bubbling goop."
    "As you hit the ground, someone calls out behind you."
    with fade

    scene bg black screen

    "The world is dark, quiet, almost suffocating"
    "This feeling…"
    "Sorrow… despair… hollow emptiness"
    "Cold, unrelenting unhappiness.."
    "We felt it before… before"
    with flash 

    play sound "audio/child laugh.mp3"

    #particles of snow falls

    "Nicolai and Nadia Claus, arbiters of joy for good little children"

    "Krampus a stern teacher, a warning against naughtiness in the cold seasons"

    "Jack Frost, a trickster, a reminder that there is fun to have in the short hours of day."

    "Frosty the Snowman, a memory of the wonders of childhood and the magic that remains."

    "And there it was that warmth that creeps in on a cold winter's night, the melodies of songs and words filled with delight." 

    "And there we were, a manifestation of it all, every word, every rhyme, every song contained in a vessel, pages on pages on pages long."

    scene bg easter island 
    with flash

    "You wake to find yourself next to Krampus, who also seems to be trying to get his bearings."

    "Jack stands guard over you both alternating between casting an ice shield to block Boogey's projectiles and lobbying his own frozen sickles."

    mc "Jack!"

    show Jack Neu at center with ease
    jack "Well good morning, sleeping beauty, nice of you to rejoin us!"

    show Kram Neu at left with ease
    krampus "Frost–"

    jack "Not the time, got it, got it"

    "Krampus stood slowly, holding out his hand to help you up as well."

    mc "I have an idea."

    jack "Well, I'm all ears, sweetheart. I think that Frosty's punches are only succeeding at pissing the meat sack off." 

    "You look over to see Frosty, dodging in and out of the hulking grasp of the Boogeyman taking shots at the eyes whenever possible." 

    "You can't tell for sure from this distance, but he seems to be unwavering. You also know he can't keep that up forever."

    mc "We need snow, lots and lots of snow. As close to a blizzard as you can manage."

    jack "You're kidding…"

    mc "Snow, Frost. Go."

    hide Jack Neu with moveoutbottom
    show Kramp Neu at center with ease

    "You turn to Krampus and find he is looking at you intently."

    krampus "You're glowing."

    "You look down to see a golden shimmer emanating from your body."

    mc "Yes. Yes, I am."
    mc "Come on we need to get to Frosty."

    "You and Krampus make your way across the room, ducking behind and through the debris."
    "The temperature in the room drops dramatically and the panes of the windows above begin to rattle frantically."
    "The howling of the wind outside grows louder and louder."

    krampus "So this plan-"

    "He stops abruptly before shoving you under a table just as the shattering of glass rings out."
    with hpunch

    "The wind whips in and flurries of snow follow in its wake."

    play sound "audio/evil laugh.mp3"
    "A howl from the creature cackles out."

    boogey "You're going to have to do a lot better than a little wind and snowflakes to beat me"

    mc "Thanks."
    mc "We have to keep moving."

    "You brace yourself against the wind and peek over the table to assess the situation."

    hide Kramp Neu 
    show Jack Neu at right
    with fade

    "Jack stands off to the side, staff glowing bright blue with the wind and snow swirling around him to fill the room."

    show Frosty Ney at left with moveinleft

    "Frosty is still dodging in and out of range of the Boogeyman, his movements slightly slower as he battles against the force of the wind to keep his momentum."

    "Despite its jeering, the movement of the gooey amalgamation is noticeably slower, sloppier."
    "Small parts of the gooping flesh are beginning to congeal and slowly solidify"

    show Kram at center with moveinbottom
    krampus "The plan."
    "You nod in agreement."
    mc "If it freezes then it can be shattered." 
    krampus "..."
    krampus "That could work." 

    "Before you can respond, he leaps across the table and you scramble to follow him."

    hide Jack Neu with moveoutright
    show Kram Neu at right with ease

    krampus "Frosty–"

    "Frosty dodges another molten ball of goo and turns to face us."

    frosty "Hey! You guys are okay!"
    frosty "That's great, I was really starting to get worried."

    krampus "Yea-"

    frosty "You think, you can get Jack to tone it down with the wind-"
    "He ducks another ball of goo."
    frosty "It's really killing my flow, and I think I've really got the guy on the hook now."

    krampus "That's what-"
    "He pulls us to the side out of the way of another attack."
    krampus "The wind and snow is part of the plan."
    krampus "Aim for the freezing bits on the body." 

    "You watch Frosty take in the instruction with a nod before jumping right back into the fray."
    hide Kram Neu
    hide Frosty Neu
    with fade

    "You spread out, launching attacks from all directions."
    "Slowly chipping away at the howling creature." 

    boogey "No!"
    boogey "No.."
    boogey "This is not over!"

    "With one final strike, it was over. Frozen and chipped pieces lay scattered across the floor as the Boogeyman fractures to pieces." 

    "The wind dies down and the snow settles peacefully on the ground."
    "You hear the murmur of words flow around you as everyone lets out a sigh of relief."
    "But you can't focus on what is being said as you catch a glimpse of a golden glow coming from the bottom of the pile of frozen pieces." 

    if (kPoints< 4 and jPoints < 4 and fPoints < 4):
         menu:
            "Go towards the glow" :
                jump neutral_ending 
    if (kPoints >= 4):
        jump krampus_ending
    if (jPoints >= 4):
        jump jack_ending
    if (fPoints >= 4):
        jump frosty_ending

label neutral_ending:
    "You walk towards the glow and as you get closer that familiar warmth tingles at your fingertips."
    "Brushing aside the frozen pieces, you find three torn golden pages." 

    show Frosty Neu at right with moveinright 

    frosty "[mcname]... what's going on?"

    show Jack Sad at left with moveinleft
    show Kram Neu at center with moveinbottom

    jack "Yeah, I've been meaning to ask about the whole… glowing thing…"

    "You pickup the pages before turning around, smiling softly:"
    mc "It's time for me to go home."

    jack "Home? Did I miss something?"

    show Kram Nod at center with dissolve

    "Krampus gives you a knowing look and a small nod as the golden radiance slowly engulfs you."

    krampus "The book."

    mc "Thank you, for everything. This has been wonderful."

    "And with that the light envelops you completely."

    hide Kram Nod
    hide Jack Sad
    hide Frosty Neu
    scene bg book room 
    with flash 

    "When it dies down, you are back in the book room of the North Base."

    "You're approaching the pedestal when you sense a presence beside you."

    msC "You could at least say goodbye first." 
    show Mrs Claus Neu at right with moveinright

    mc "So, you figured it out."
    msC "And you did as well, my dear."

    mc "Goodbye doesn't mean much."
    mc "I'll be where I've always have been." 

    "Mrs. Claus' face takes on a bittersweet expression as she steps closer"
    with vpunch

    msC "Then, how about…"
    msC "I'll see you later." 

    "She embraces you in a long hug." 

    mc "I'll see you later, Nadia." 
    mc "Keep an eye on them, yes?"

    "You can feel the silent laughter shake her form before she pulls away."

    msC "Always."
    hide Mrs Claus Neu with dissolve 

    "And with that you approach the book, missing pages in hand." 

    scene bg the book
    with fade

    "You finally touch the warm golden pages, and the spirit of the book finally returns home"

    scene bg black screen with blink_shut

label jack_ending: 
    ""
label frosty_ending: 
    ""
label kram_ending:
    ""
    return




