# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Prisoner = Character("Prisoner")
define SpaceGuard = Character("Space Guard")




# The game starts here.

label start:
play sound "audio/prelude.mp3" loop
"Prisoner" "I've been in this space station for as long as I can remember..."
show entrance_door 
with fade 

show prisoner with moveinleft
"Prisoner" "They've held me captive in this room for such a long time"
"Prisoner" "With hardly any food or drink to keep me alive..."
"Prisoner" "All because I know the true nature of the person behind this space station."
"Prisoner" "Well, I won't be silenced any longer. I am breaking out and exposing him once and for all!"
hide prisoner

scene breakpoint_1
SpaceGuard "Man, I'm falling asleep over here. Maybe I should go on a jog-"
stop sound
play sound "audio/boom.mp3"
play music "audio/escape_music.mp3" fadein 1.5 volume 0.5 fadeout 1.5
"Space Guard" "What the hell was that?"
"Space Guard" "Hey! The prisoner is escaping! Everyone, after them!"
show prisoner with moveinbottom
play sound "audio/running.mp3" volume 1.0 loop 
"Prisoner" "Damn! They're onto me already!? I gotta hurry and find the exit! But where-?"
"Prisoner" "No! A split path! I don't know which hall to take!" 
"Space Guard!" "STOP! Or else we'll be forced to use force!"
"Prisoner" "Gimme a break!"
menu path_choice_1:
    "Which way should I go?!"
    "Run Left":
        Prisoner "I'll go Left!"
        "Space Guard" "HEY!"
        scene dead_end
        show prisoner with easeinbottom
        "Prisoner" "Ok. All I need to do is open the door-"
        "Prisoner" "Wait! It won't open! Why is it locked!"
        stop music 
        "Space Guard" "Hands where I can see them! No where to run!"
        play sound "audio/death_sound.mp3"
        "Prisoner" "Oh come on!"
        "Incorporeal Narrator" "What an unfortunate fate."
        return False 


    "Run Right":
        "Prisoner" "I'll go right!"
        "Space Guard" "HEY!"
        scene breakpoint_2
        show prisoner with moveinbottom
        "Prisoner" "Looks like I went the right way. Nice!"
        
"Space Guard" "You can't run forever! Stop making this difficult!"
"Prisoner" "Then stop chasing me! You guys can't keep the truth hidden forever!"
"Space Guard" "Quit your ranting and surrender!"
"Prisoner" "How ignorant can these guys... Wait wha-!"
"Prisoner" "Another split path? Just my luck... welp."
menu path_choice_2:
    "Do I go straight or go left?"
    "Keep going forward":
        Prisoner "Full Speed Ahead!"
        "Space Guard" "We're losing them. Shoot!"
        scene final_breakpoint
        show prisoner with moveinright
        Prisoner "I think I lost those guys. About time they took a hint!"


    "Go Left":
        "Prisoner" "Uhh- Left it is, then!"
        "Space Guard" "The captive should be weak from hardly eating, how are they so FAST?!"
        scene dead_end2
        show prisoner with easeinleft
        "Prisoner" "..."
        stop music
        "Prisoner" "Are you kidding me? A room full of spikes?"
        play sound "audio/death_sound.mp3"
        "Prisoner" "Why would a space station even need this? What kind of place are they running!?"
        "Incorporeal Narrator" "What a hilarious fate."
        return False
        
"Prisoner" "I've been running for a while now. Some type of exit from this place should be close by." 
Prisoner "I'd wager my ticket to freedom is behind on of these 2 doors..."
Prisoner "The question is..."
menu final_choice:
    "Which door do I open"
    "Left Door":
        Prisoner "I'll open this one."
        scene the_exit
        stop music
        stop sound 
        show prisoner with easeinleft
        
    "Right Door":
        Prisoner "I'll open this one."
        scene black_hole
        show prisoner with easeinbottom
        stop music
        Prisoner "AH-"
        hide prisoner with dissolve
        "Incorporeal Narrator""The poor prisoner was sucked into a black hole, ripped apart and torn apart by its unparalelled force..."
        play sound "audio/death_sound.mp3"
        "Incorporeal Narrator" "What a... very random fate..."
        return False
Prisoner "The exit! I'm free! I can go back home!"
play sound "audio/good_ending.mp3"
Prisoner "I can also finally tell everyone the truth about this place. This'll teach them for capturing me!"
Prisoner "I win! Woohoo!"
"Incorporeal Narrator" "What a fortuitious fate."

      

return True