# name of the character.

#Main characters
define mc = Character("[mcname]", color = "#ffac00")
define msC = Character("Ms. Clause", color = "#850101")
define frosty = Character("frosty the 'Snowman'", color = "#ADD8E6")
define jack = Character ("Jack Frost", color = "#000bd4")
define krampus = Character("Krampus", color = "#3d0d0d")

define unk = Character("Unknown 1", color = "#b0b0b0") #clause?
define unk1 = Character("Unknown 1", color = "#000bd4") #Jack
define unk2 = Character("Unknown 2", color = "#3d0d0d") #Krampus
define unk3 = Character("Unknown 3", color = "#ADD8E6") #Frosty

#Other Characters
define emily = Character("Emily", color = "#ffc1f2")

#Sprites
image Jack Happy = im.Scale("happy_JACK.png", 800, 1000)
image Jack Neu = im.Scale("neutral_JACK.png", 800, 1000)
image Jack Sad = im.Scale("upset_JACK.png", 800, 1000)


#Character Romance Points
$ fPoints = 0
$ jPoints = 0
$ kPoints = 0

# random variables
default frostyDate1 = False

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
    with vpunch

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
    with vpunch

    mc "What is going on? I don't think I did anything..."

    unk "Who ever you are in there, you are surrounded! I suggest you come out quietly." #probably Mrs. Claus  

    scene bg black screen 
    with blink_shut
    mc "Uuugh"

    scene bg hub command
    with blink_open

    unk3 "Maybe we should go in and see -" #probably frosty
    unk1 "Go in, are you nuts!" #probably Jack
    unk3 "Well how else do you expect us to know who is in there..." #frosty
    unk2 "And what, may I ask, will you do if there IS someone in there?" #probably Krampus
    unk3 "Ummm... I hadn't gotten that far..." #frosty
    unk3 "Hello! Is there anyone in there!" #frosty
    unk1 "What are you doing?!?!" #Jack 
    unk3 "I figured if we're not going in to see if someone's in there, I could call out and see if anyone responds..." #frosty
    unk1 "Of all the ideas that has to be the stu-" #Jack

    mc "Ummm... hello?" 
    unk3 "Yes! Hello!" #frosty
    unk2 "Stop talking." #Krampus

    unk2 "If you come out peacefully we'll make your suffering short." #Krampus
    unk3 "Don't say that! You'll scare them." #frosty
    unk2 "Good." #Krampus

    mc "Where is out? Where am I?"
    unk2 "You're not going to trick us, so you can drop the act." #Krampus

    mc "Trick? Who is us? And why would I want to trick you?"
    unk "..."
    unk3 "I don't know guys, it sounds like they really don't know anything..." #frosty
    unk1 "You're not allowed to have anymore thoughts." #Jack 
    unk2 "We're coming in..." #Krampus
    unk3 "NO, we are not! Have you lost your mind." #Jack
    unk2 "No. I have not." #Krampus

    "A loud clanking sound resonates through the room."
    "To your right, a part of the wall begins to move as if it is moving to the side to reveal something."

    
    #Krampus slides onto screen
    unk2 "You make any sudden movements and I will kill you." #Krampus 

    #frosty and Jack enter 
    show Jack Sad at left
    with moveinleft 
    unk1 "So who is it?" #Jack
    unk3 "Oh... hi" #frosty

    mc "Umm... hi"
    mc "Where am I? Who are you?"

    show Jack Neu at center
    with ease
    unk1 "You... really don't know, do you?" #Jack
    
    "You eye the first man to arrive."
    "He stands tall, with elf-like ears protruding out from his black and gray streaked hair."
    "You look up into his eyes, they tell the tale of an older man, hung up and annoyed with life, before slowly shaking your head."

    unk3 "We should get Mrs. C in here." #frosty
    unk2 "What is your name?" #Krampus

    mc "It's..."
    mc "I'm ..."
    mc "I'm [mcname], I think."

    show Jack Sad at center
    unk2 "You think?" #Jack

    "The one to speak this time was slightly shorter than the man that first entered. He had white hair like snow and eyes the color ice."
    "He seemed to look at you with curiosity as opposed to the last man who seemed to only be annoyed by your presence."
    
    mc "I think that's my name. My head is spinning and everything is blurry."

    "You try taking a step towards the men, but find that your legs are less reliable than you think they are, and you find yourself stumbling a bit before having to catch yourself."

    unk3 "Whoa whoa whoa. Maybe you should sit." #frosty 

    "This man seems so be slightly different than the rest. He stands taller than all of them, his broad shoulders make it so he takes up the most space, but his eyes tell a different story."
    "Instead of looking at you with an air of curiosity or annoyance, he looks concerned."
    "He slungs your arm around his shoulder as he eases you to the floor."

    unk3 "Take a few deep breaths, are you hurt anywhere." #frosty 
    unk1 "Snow! What are you doing dude, they could be dangerous." #Jack 
    unk3 "I don't know dude, they can hardly stand." #frosty
    unk2 "Go get Mrs. Clause." #Krampus
    unk1 "But-" #Jack
    unk2 "Go. For now, I think frosty is correct. And Mrs. Clause will be able to tell for sure." #krampus

    #Jack's sprite slides off screen
    show Jack Sad with moveoutleft

    mc "frosty?"

    "The hulking figure shakes in silent laughter before responding."

    frosty "Yes. I know what you're thinking..."
    frosty "Actually, no I don't know..."
    frosty "I assume you figured it out by now, but yes I am frosty the Snowman, or at least the human version of him."

    menu:
        "You seem... nice.":
            mc "You seem... nice."
            "frosty smiles with a big wide smile."
            frosty "Thank you."
        "It suits you.":
            mc "It suits you, and yet your demeanor is warm."
            "frosty smiles with a big wide smile."
            frosty "Thank you."
        "I figured you'd be something more... intimidating":
            mc "I figured, with how big you are... I was just expecting something more intimidating."
            unk "I promise, you do not want to mess with this guy."  #krampus
            frosty "It's ok Kramp, I understand. It helps that people underestimate me."

    frosty "Well I guess now is as good of a time as ever to introduce ourselves."
    frosty "As you figured, I am Frosty, Frosty the Snowman. And this is Krampus."

    "The older man gives you a small nod, acknowledging that he is in fact Krampus."

    frosty "And the guy with ice white hair is Jack. Speaking of which where is he?"
    jack "Awe man Frosty, are you really introducing me to the cutie {i}without{/i} me being there?"
    frosty "Speak of the devil..."

    "The man with ice white hair and eyes the color of fresh ice appears before you, hand streched out asking you to shake it."

    menu:
        "shake his hand":
            "You take in his hand shake it, it is cold to the touch."
        "look behind him":
            "You look behind him to see whoever it was he was supposed to get."

    "The man gives you a small wink before turining away to reveal the person who he brought along."

    #add in description for mrs. clause.

    "add in more blah blah blahh but testing for the dates...."

    menu:
        "frosty date":
            jump frosty_date_1
        "jack date":
            jump jack_date_1
        "krampus date":
            jump krampus_date_1

return

label before_date_2:

    scene bg black screen 

    "Blah blah blah plot and stuff"
    "guess what yoyu can choose who to go on your second date with!"

    menu:
        "frosty":
            jump frosty_date_2
        "jack":
            jump jack_date_2
        "krampus":
            jump krampus_date_2

    return

label before_date_3:

    scene bg black screen 
    "To add in later but basicaly to undestand the 3rd date..."
    "The group is going to fight the badguy, the boogyman, and they need to prep you how to fight since you are new."
    "you have to choose who you want to learn to fight with..."
    "ps: theres no 3rd date for krampus yet."
    
    menu:
        "frosty":
            jump frosty_date_3
        "jack":
            jump jack_date_3
        #"krampus":
            #jump krampus_date_3


label frosty_date_1:
    scene bg black screen 
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
    mc "It's not random, I can see why you love it here. I had a great time."

    "frosty beams, his eyes crinkling with joy."

    frosty "Really? That makes me so happy. We'll come back soon, yeah? Maybe next time we can try some of those cookies-or just hang out with the cats more. I think Mittens over there has her eye on you."

    "You glance at a fluffy calico peeking at you from behind a stack of books, and frosty laughs. It's warm and easy, and it feels like a perfect ending to the day."

    mc "Next time for sure"

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

    "You choose to knock on the door labeled Frosty again."
    "Last time you had an amazing time with him and couldn't stop thinking about what it would be like to spend another day with him."
    "So you chose to hang out with him again."

    frosty "[mcname]!"

    "Frosty says to you as he opens the door, excited to see that you choose to spend time with him again."

    mc "Hey Frosty!" 

    frosty "I'm so happy you came back! I have a fun day planned for us. Are you ready?"

    mc "Woah, someone is ready to go. Hell yeah I am!"

    frosty "Awesome! Make sure to bundle up, we're going to be outside."

    mc "Uh, Ok! Let me just grab my stuff and I'll meet you outside?"

    frosty "Perfect!"

    jump frosty_date_2


label frosty_date_2_no:

    "You hastily knock on the door labeled 'Frosty' feeling slightly nervous."

    "Frosty had always seemed very sweet, granted you had only known him for a few days, but due to the circumstances, you felt like you should get to know everyone better, and Frosty was the least intimidating out of the bunch."

    "After a moment or two, the door in front of you opens to reveal Frosty standing before you."

    "He towers over you, but instead of finding him intimidating, he looks down at you with a bright smile on his face."

    frosty "Y/N!"

    "You smile back at him as he welcomes you into his room."

    "Frosty's room is pretty simple, nothing too out of the ordinary here."

    "A plain-ish bed, some shelves holding small knick-knacks like a few books, a small figure, and some plants."

    "The open arrangement and lack of clutter made the room feel very cozy, especially with the plants adding a pop of color here and there." 

    "The room also had the faint scent of evergreen trees in the winter, but it wasn't cold surprisingly, for him being Frosty the Snowman, but instead was actually kind of warm."

    menu:
        "It's warm in here":
            frosty "Haha yeah. I like to keep it warm in here, contrary to popular belief…"
        "Its very cozy in here":
            frosty "Thank you! I try to keep it nice and welcoming in here, although the others aren't really ones for hanging out…"

    frosty "I'm really happy you came to hang out with me today. I have a really fun day planned and I am happy to share it with you!"

    mc "Oh wow Frosty that's so nice of you!"

    frosty "Of course! How else are we going to welcome the new member of the team? Make sure to bundle up, we're going to be outside."

    mc "Alright!"

    jump frosty_date_2


label frosty_date_2:

    "You grab your coat, scarf, and gloves, making sure you're bundled up for whatever Frosty has planned."
    "Stepping outside, you see him waiting for you at the bottom of the steps, his cheeks tinged pink from the cold and excitement."
    "There's something magical about the way he seems to glow, as if winter itself has chosen him as its representative."

    frosty "Ready to go?"

    "Frosty holds out his hand for you to take to begin your journey"

    mc "Lead the way!" 

    "You slip your hand into his. His touch is cool but not uncomfortable." 
    "It's a sensation that reminds you of holding fresh snow."
    "As the two of you walk, Frosty chatters excitedly about the day ahead."

    frosty "I hope you like skating! There's this great little rink nearby. It's got fairy lights, music, and everything!"

    "As he talks to you, you look up into his eyes and see they are sparkling like fresh frost on a windowpane"

    mc "Sounds perfect!"

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

    "As you walk back together, Frosty suddenly stops and looks at you, his expression soft and sincere."

    frosty "Thanks for choosing to spend your time with me, [mcname]. It means a lot."

    "You feel a blush rise to your cheeks, not from the cold this time."

    mc "Anytime, Frosty. I can't wait for our next adventure."

    jump before_date_3

label frosty_date_3:
    "You knock on Frosty's door, and for a moment, the quiet of the hall feels heavier than usual. It's not just the anticipation of tonight's training."
    "It's the knowledge that this might be your last night like this. Together."

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

    "When you reach the gym, the fluorescent lights buzz faintly, casting their cold glow over the stark space."
    "It's the same as always:punching bags, training dummies, rows of weights, but tonight, it feels different."

    "Frosty steps into the center of the room, motioning for you to follow."

    frosty "Alright, this is it. One last session before... well, before everything."

    "He looks at you, his usual playful demeanor giving way to something more serious."

    frosty "We're gonna make it count."

    "You nod, swallowing the lump in your throat."

    frosty "Okay, first things first:gear."

    "He holds out his hands, and the air around him chills slightly."
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
    frosty "Now, again. Keep your shoulders loose, but focus on where you want to hit. Make it count."

    "You follow his guidance, feeling the weight of the brass knuckles amplify your strikes."
    "Each punch lands with a satisfying thud, and Frosty's quiet murmurs of approval spur you on."

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

return


label jack_date_1:

    scene bg black screen 

    "You step into the dimly lit gaming room, where neon LED lights cast a soft blue glow, creating an atmosphere that feels both exciting and relaxed."
    "Jack Frost is already there, sitting cross-legged on a beanbag chair."
    "His icy white hair catches the light, giving him an ethereal look. He grins when he sees you."

    show Jack Happy at center
    with fade
    jack "Hey!"

    "His voice is crisp but warm, like a winter breeze."

    jack "Thought this might be a cool way to hang out. Get it? Cool?"

    "He chuckles at his own pun, a mischievous glint in his icy blue eyes."
    "You laugh, shaking your head."

    mc "You're lucky I like bad jokes. What are we playing?"

    "Jack holds up two controllers."

    jack "Mario Kart. A classic choice, right? I hope you're ready for some friendly competition."

    "You settle into a beanbag next to him, taking the controller he offers. The menu screen flashes on the TV, and cheerful music fills the room."
    "As the first race begins, Jack leans over slightly, whispers..."

    show Jack Sad
    jack "Fair warning-I might be a little {i}frosty{/i} when I lose."

    "The game starts, and Jack is immediately in the lead. He's surprisingly good at this, dodging shells and drifting around corners with ease."

    jack "Come on, keep up!"

    "Jack continues teasing, throwing a playful glance your way."

    mc "Oh, I see how it is."

    "You focus harder, managing to snag a red shell."

    mc "Take this!" 

    with hpunch
    "You launch the red shell, and it hits Jack's character just before the finish line. You zoom past him, claiming first place."
    "Jack stares at the screen in mock horror."

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

    "The two of you spend the rest of the evening racing through pixelated landscapes, throwing banana peels, and laughing at each other's mishaps." 
    "Jack's energy is infectious, and you find yourself completely at ease as if the world beyond this cozy gaming room doesn't exist."
    "As the night winds down and the final race ends, Jack turns to you, his expression softening."

    jack  "This was fun," 
    
    "His voice is quieter now."

    jack "I don't usually... hang out like this. But I'm glad I did-with you."

    "Your heart warms at his words, and you smile back." 

    mc "Me too. Same time next week?"
    with fade

    jump before_date_2

label jack_date_2:

    show Jack Neu at center
    with fade
    "The air is crisp and cold as you step onto the ice rink, its surface gleaming under the soft glow of fairy lights strung overhead. Snowflakes drift lazily from the sky, and the entire scene feels like something out of a winter dream."
    "Jack Frost is already waiting near the edge of the rink, leaning casually against the barrier." 
    "His icy white hair sparkles under the lights, and when he spots you, he stands up straight, a playful grin spreading across his face."

    jack "About time you got here," 

    "He holds out a pair of skates for you."

    show Jack Happy
    jack "I was starting to think you were scared to face the ice with me."

    "You take the skates, laughing."

    mc "Oh, I'm not scared. I just didn't want to show you up too soon."

    "Jack arches an eyebrow, a mischievous glint in his eyes."

    show Jack Happy
    jack "Big talk for someone who hasn't even laced up yet."

    "Once your skates are on, Jack leads you to the rink. He steps onto the ice effortlessly, gliding backward as if he was born to skate."
    "Well, maybe he was. His movements are smooth and graceful, every motion infused with a hint of magic. You follow, a little less confident but determined not to let him show you up completely."

    jack "Need a hand?" 

    "Jack offers you his hand, his voice is teasing, but there's a genuine warmth in his expression."

    "You take his hand, and the chill of his touch sends a shiver up your spine-not unpleasant, just cool enough to remind you of who he is. He pulls you along, helping you find your balance."

    jack "There, see? You're a natural. Almost as good as me."
    mc "Watch this."

    "You try a daring spin, only to wobble precariously and nearly fall."
    with vpunch
    "Jack catches you easily, his laugh ringing out like bells on a frosty morning."

    jack "Nice try,"
    jack "But leave the fancy moves to the professional."

    "As the evening goes on, you relax more, skating side by side with Jack."
    "At one point, he waves his hand, and a shimmering frost spreads across the ice, creating intricate patterns of snowflakes and swirls that glisten under the lights."

    mc "Wow, Show-off much?"
    jack "Hey, I've got to impress you somehow."
    mc "You don't have to try so hard."

    "Jack's smirk softens into a genuine smile."

    jack "Careful." 

    "He leans in slightly, his breath cool against your cheek."

    jack "Say things like that, and I might actually believe you enjoy my company."

    "You laugh, your cheeks warm despite the cold."

    mc "Maybe I do."

    "Jack pulls back, grinning again."

    jack  "Good. Because I was thinking, next time, we could build a snow fort. Unless you're too scared to lose at that, too."
    mc "Not a chance, but you better bring your A-game."

    "The two of you skate a little longer, weaving around the rink as snow falls softly around you."
    "The world feels quiet and magical, and as Jack skates beside you, his laughter mixing with yours, you think there's no place you'd rather be."
    with fade

    jump before_date_3

label jack_date_3:
    "The military gym is stark and utilitarian, with fluorescent lights casting a cool glow over the room."
    "It's filled with various equipment for physical and tactical training, but in the center of it all stands Jack Frost, leaning casually against his frost-covered staff."
    "Despite the harsh setting, he looks as effortlessly cool as ever, his icy white hair almost glowing under the lights."

    show Jack Neu at cetner
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

    "Jack steps behind you, his hands lightly covering yours on the staff. His touch is cold, but not unpleasant, like the crisp air on a winter morning."

    jack "Start by grounding yourself. Feel the frost in the staff, let it flow through you. Don't fight it. You've gotta let the cold work with you, not against you."

    "You take a deep breath, focusing on the staff as Jack guides you."

    jack "Now, visualize your target. Let's start with that punching bag over there."

    "Across the gym, a heavy punching bag sways slightly, as if daring you to aim. You nod, raising the staff and focusing."

    mc "Alright, here goes nothing."
    jack "Not nothing, go big or go home."

    with hpunch
    "You swing the staff, and a blast of frost shoots forward, encasing the punching bag in a thin layer of ice. Jack whistles, impressed."

    jack "Not bad, rookie. Not bad at all."

    "You grin, spinning the staff experimentally in your hands."

    mc "Looks like I've got the hang of this."
    jack "Don't get cocky..." 

    show Jack Happy
    "There's a mischievous glint in his eye now. He steps back, spinning his own staff effortlessly."

    jack "Now let's see if you can handle a moving target."

    "With a quick motion, he sends a flurry of snow your way."
    with vpunch
    "You scream, dodging the icy attack."

    mc "Hey! I thought we were training, not sparring!"
    show Jack Neu
    jack "This {i}is{/i} training," 

    show Jack Happy
    "He was laughing at you now."

    jack "You're gonna have to learn to think on your feet."

    "He flicks his staff again, sending another burst of frost toward you."
    with hpunch
    "You block it with the staff, feeling the energy pulse through your hands."

    mc "Two can play at that game," 

    "You aim to blast frost at Jack. He dodges it easily, his movements as fluid as the wind."
    "The two of you go back and forth, the gym echoing with bursts of frost and laughter."
    "Jack keeps you on your toes, pushing you to react faster, aim better, and trust the staff's power."

    jack "Nice shot!" 

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

    scene bg black screen 
    "The air is crisp and biting as you stand at the top of the ski slope, looking down at the endless stretch of sparkling white snow."
    "The sun glints off the frosted peaks, and in the distance, the evergreens sway in the cold wind."
    "Beside you stands Krampus, his imposing frame dressed in a sleek black ski suit, horns curling up from under his custom-made helmet."
    "His yellow eyes gleam with mischief as he adjusts his skis."

    krampus "Ready to eat some snow?" 

    "You tighten your gloves and adjust your goggles."

    mc "Eat snow? You're awfully confident for someone who's about to get left behind."

    krampus "Careful, little one. Pride comes before a tumble down the mountain."

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
    "Krampus glances back, his grin widening." 

    krampus "Impressive!"

    "He slows just enough to let you pull alongside him." 
    "Then, with a wicked gleam in his eye, he taps the tip of his ski pole to the snow, sending a small flurry of powder into your path."

    mc "Hey!" 

    "You swerve to avoid the icy spray."

    krampus "Just keeping things interesting"

    "Krampus' chuckle resonates through the crisp air."
    "The two of you race neck and neck, weaving down the mountain with increasing speed."
    "Krampus leaps off a small ridge, landing gracefully and glancing back to see if you dare follow."
    "Not wanting to back down, you take the jump, your skis hitting the snow with a satisfying thud."

    krampus "Not bad!" 
    krampus "Maybe you've got some spirit after all."

    "As the slope levels out near the bottom, the two of you come to a stop near a small lodge."
    "Your legs are shaky from the exertion, but your adrenaline is pumping, and you can't stop smiling."

    mc "That was amazing!"

    "Krampus leans on his ski poles, his horns catching the late afternoon light."

    krampus "Not bad for a rookie!"
    krampus "Though I'd still say I won."
    mc "You wish!" 
    mc "I was right behind you the whole time."
    krampus "Close..." 
    krampus "but next time, I'll make sure you can't keep up."
    mc "Next time?"

    "You raise an eyebrow."
    "He grins, baring sharp teeth."

    krampus "You didn't think this was a one-time thing, did you?"
    krampus "I've got plenty of slopes to show you... if you think you can handle them."

    "You smile, feeling the warmth of the challenge in his tone."

    mc "Bring it on, Krampus. I'll take you on any mountain."

    "His laugh echoes across the snowy peaks as the two of you head into the lodge, your competitive banter continuing over mugs of steaming hot cocoa."
    "There's a spark of excitement and fun in his presence, and you can't help but look forward to the next adventure."

    jump before_date_2

label krampus_date_2:
    "The bar is dimly lit and cozy, with flickering candlelight reflecting off bottles of aged whiskey and frosted mugs of beer."
    "The air is warm, a welcome contrast to the biting cold outside, and the hum of quiet conversation mingles with the crackle of a nearby fireplace."
    "Seated at a corner table, Krampus cuts an imposing figure even in this laid-back setting. His dark fur peeks out from under a tailored coat, and his horns curl gracefully, catching the soft glow of the lights."
    "When you approach, his crimson eyes lift to meet yours, and a wicked grin spreads across his face."

    krampus  "There you are." 
    krampus "I was beginning to think you got lost in the snow."

    "Sliding into the seat across from him, you smirk."

    mc  "I don't get lost that easily. What are we drinking?"

    "Krampus gestures to the bartender, who brings over two glasses filled with a dark amber liquid."

    krampus "Mulled wine."
    krampus "Warms you up from the inside out. Unless you can't handle a little heat?"

    "You raise an eyebrow and take a sip. The wine is rich and spiced, with a subtle warmth that spreads through your chest."

    mc  "Not bad." 
    mc "But I expected something... stronger from you."

    "His laugh is low and rough, like boots crunching through snow."

    krampus  "Careful, little one. Challenge me, and you might regret it."
    mc "Oh, I'm not scared." 
    mc "What else you got?"

    "Krampus signals again, and this time the bartender brings over a pair of frosted shot glasses filled with a glowing blue liquid."

    krampus "Icefire shots." 
    krampus "They burn cold going down. Think you can keep up?"

    "You pick up the glass, the chill biting against your fingertips."

    mc "Only one way to find out."

    "The two of you toast, and you down the shot in one gulp. It's like swallowing a snowstorm, the icy burn rushing through your throat and leaving a strangely invigorating warmth behind."
    "You cough slightly, and Krampus laughs, his shoulders shaking."

    krampus "Not bad." 
    krampus "But I barely saw you flinch. Maybe there's more to you than I thought."
    mc "Was that supposed to impress me?" 
    mc "Because I'm still standing."
    
    "Krampus leans back in his chair, swirling the remnants of his drink." 

    krampus "Alright, you're tougher than most. But let's see how sharp you are after another round."

    "The night goes on with more drinks, each one seemingly more exotic and potent than the last."
    "Between sips, Krampus regales you with darkly humorous tales of his escapades: scaring the naughty into good behavior, outwitting hunters, and even a wild snowball fight with Jack Frost that left a village buried under a week's worth of snow."

    krampus "So, what about you?" 
    krampus "What's the wildest thing you've ever done?"

    "You laugh, shaking your head."

    mc "Oh no, I'm not falling for that one. You'll have to work harder if you want my secrets."

    "His grin is all sharp teeth and mischief."

    krampus  "Fair enough. But don't think I won't figure you out eventually."

    "As the bar starts to quiet down, you realize how much you've been enjoying yourself."
    "Despite his intimidating presence, Krampus is surprisingly easy to talk to-charming in his own gruff, devil-may-care way."
    "When you finally get up to leave, he follows you to the door, his towering frame casting a shadow over the snow-dusted street outside."

    krampus "This was fun!" 
    krampus "You've got spirit. I like that."
    mc "Maybe we'll do it again sometime." 

    "Krampus smirks, his sharp teeth glinting in the moonlight."

    krampus "Careful what you wish for. I've got plenty more tricks up my sleeve."

    "As you part ways, the warmth of the bar lingers with you, along with the memory of Krampus's devilish grin and the laughter you shared."
    "Something tells you this won't be the last time you cross paths with him."
    
    jump before_date_3