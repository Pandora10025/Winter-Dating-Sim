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
$ jPoints = 0
$ kPoints = 0

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
            "You take in his hand shake it, they are cold to the touch."
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

return

label frosty_date_1:
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

    return

label jack_date_1:

    "You step into the dimly lit gaming room, where neon LED lights cast a soft blue glow, creating an atmosphere that feels both exciting and relaxed."
    "Jack Frost is already there, sitting cross-legged on a beanbag chair. His icy white hair catches the light, giving him an ethereal look. He grins when he sees you."

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

    jack "Fair warning-I might be a little {i}frosty{/i} when I lose."

    "The game starts, and Jack is immediately in the lead. He's surprisingly good at this, dodging shells and drifting around corners with ease."

    jack "Come on, keep up!"

    "Jack continues teasing, throwing a playful glance your way."

    mc "Oh, I see how it is."

    "You focus harder, managing to snag a red shell."

    mc "Take this!" 

    "You launch the red shell, and it hits Jack's character just before the finish line. You zoom past him, claiming first place."
    "Jack stares at the screen in mock horror."

    jack "No way. You iced me!" 

    "He bursts out laughing, his laugh as light and bright as the snowflakes outside the window."

    mc "Guess you're not as unbeatable as you thought."

    jack "Okay, okay."

    "He concedes, raising his hands in surrender." 

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

    jump jack_date_2

label jack_date_2:

    "The air is crisp and cold as you step onto the ice rink, its surface gleaming under the soft glow of fairy lights strung overhead. Snowflakes drift lazily from the sky, and the entire scene feels like something out of a winter dream."
    "Jack Frost is already waiting near the edge of the rink, leaning casually against the barrier." 
    "His icy white hair sparkles under the lights, and when he spots you, he stands up straight, a playful grin spreading across his face."

    jack "About time you got here," 

    "He holds out a pair of skates for you."

    jack "I was starting to think you were scared to face the ice with me."

    "You take the skates, laughing."

    mc "Oh, I'm not scared. I just didn't want to show you up too soon."

    "Jack arches an eyebrow, a mischievous glint in his eyes."

    jack "Big talk for someone who hasn't even laced up yet."

    "Once your skates are on, Jack leads you to the rink. He steps onto the ice effortlessly, gliding backward as if he was born to skate."
    "Well, maybe he was. His movements are smooth and graceful, every motion infused with a hint of magic. You follow, a little less confident but determined not to let him show you up completely."

    jack "Need a hand?" 

    "Jack offers you his hand, his voice is teasing, but there's a genuine warmth in his expression."

    "You take his hand, and the chill of his touch sends a shiver up your spine-not unpleasant, just cool enough to remind you of who he is. He pulls you along, helping you find your balance."

    jack "There, see? You're a natural. Almost as good as me."
    mc "Watch this."

    "You try a daring spin, only to wobble precariously and nearly fall. Jack catches you easily, his laugh ringing out like bells on a frosty morning."

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

    jump jack_date_3

label jack_date_3:
    "The military gym is stark and utilitarian, with fluorescent lights casting a cool glow over the room."
    "It's filled with various equipment for physical and tactical training, but in the center of it all stands Jack Frost, leaning casually against his frost-covered staff."
    "Despite the harsh setting, he looks as effortlessly cool as ever, his icy white hair almost glowing under the lights."

    jack "Finally." 

    "Jack calls out as you approach, his voice echoing slightly in the cavernous space."

    jack "Thought you might've chickened out on me."

    "You roll your eyes, adjusting your gloves."

    mc "Chickened out? I could say the same about you. Are you sure you're not too fragile for this kind of training?"

    "Jack laughs, a sound like cracking ice."

    jack "Oh, you've got jokes. Alright then, let's see if you can back it up." 

    "He tosses you his staff, and you catch it, the icy chill of it seeping through your gloves."

    jack "First lesson, this isn't just a fancy walking stick. It's an extension of your energy. You want it to work for you? You've gotta connect with it. Otherwise, it's just a very expensive popsicle."

    "You hold the staff, feeling its weight and the faint hum of cold energy running through it."

    mc "Alright. So, how do I connect with it?"

    "Jack steps behind you, his hands lightly covering yours on the staff. His touch is cold, but not unpleasant, like the crisp air on a winter morning."

    jack "Start by grounding yourself. Feel the frost in the staff, let it flow through you. Don't fight it. You've gotta let the cold work with you, not against you."

    "You take a deep breath, focusing on the staff as Jack guides you."

    jack "Now, visualize your target. Let's start with that punching bag over there."

    "Across the gym, a heavy punching bag sways slightly, as if daring you to aim. You nod, raising the staff and focusing."

    mc "Alright, here goes nothing."
    jack "Not nothing, go big or go home."

    "You swing the staff, and a blast of frost shoots forward, encasing the punching bag in a thin layer of ice. Jack whistles, impressed."

    jack "Not bad, rookie. Not bad at all."

    "You grin, spinning the staff experimentally in your hands."

    mc "Looks like I've got the hang of this."
    jack "Don't get cocky..." 

    "There's a mischievous glint in his eye now. He steps back, spinning his own staff effortlessly."

    jack "Now let's see if you can handle a moving target."

    "With a quick motion, he sends a flurry of snow your way."
    "You scream, dodging the icy attack."

    mc "Hey! I thought we were training, not sparring!"
    jack "This {i}is{/i} training," 

    "He was laughing at you now."

    jack "You're gonna have to learn to think on your feet."

    "He flicks his staff again, sending another burst of frost toward you."
    "You block it with the staff, feeling the energy pulse through your hands."

    mc "Two can play at that game," 

    "You aim to blast frost at Jack. He dodges it easily, his movements as fluid as the wind."
    "The two of you go back and forth, the gym echoing with bursts of frost and laughter."
    "Jack keeps you on your toes, pushing you to react faster, aim better, and trust the staff's power."

    jack "Nice shot!" 

    "You manage to graze his side with a burst of frost. He spins around, his staff creating a swirl of cold air that almost knocks you off your feet."

    jack "But don't celebrate yet!"

    "By the time you both call a truce, the gym is colder than when you started, with frost covering the equipment and ice shimmering on the floor."
    "You're out of breath but exhilarated, the staff still humming faintly in your hands."
    "Jack leans on his own staff, watching you with a mix of amusement and pride."

    jack "You're not half bad. With a little more practice, you might actually keep up with me out there."

    "You smirk, leaning the staff against your shoulder."

    mc "Keep up? I'm pretty sure I'm already ahead."

    "Jack shakes his head, grinning."

    jack "Sure, sure. Keep telling yourself that, rookie. But don't forget-this was the easy part. The real mission's gonna be a lot tougher."
    mc "Good thing I've got the best trainer then." 

    "Jack's grin softens into something more genuine."

    jack "Yeah, well," 

    "Jack ruffles his hair awkwardly."

    jack "Good thing I've got the best partner."

    "You both leave the gym together, the mission looming ahead but feeling just a little less daunting with him by your side."

    return