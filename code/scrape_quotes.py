import requests
from bs4 import BeautifulSoup
import random
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException


url = "https://www.thetoptens.com/best-movie-villain-quotes/"

driver = webdriver.Chrome()
driver.get(url)

while True:
    try:
        load_more = driver.find_element_by_id("loadmore")
        load_more.click()
        # time.sleep(0.2)
    except NoSuchElementException:
        print("Reached bottom of page")
        break
    except StaleElementReferenceException:
        print("Reached end of page")
        break
        

res = requests.get(url)
soup = BeautifulSoup(res.text, "html.parser")
quotes = soup.div.find_all("b")[1:]
soup.find(class_="bluebutton")



# try:
#     iframe = driver.find_element_by_id("nvpush_popup_background_iframe")
#     cross = driver.find_element_by_id("nvpush_cross")
#     cross.click()
# except:
#     pass

# while True:
#     try:
#         loadmore = driver.find_element_by_id("bottomPager")
#         loadmore.click()
#     except NoSuchElementException:
#         print("Reached bottom of page")
#         break

questions = []

for item in quotes:
    questions.append([item.text])

print(questions)


#     print(quotes)
#     quotes_text = [quotes.text for quotes in soup.div.select("b")[1:]]
#     print(quotes_text)
#     split_quote = quotes.split(separate, 1)[0]
#     print(split_quote)
#     print(i)
#     quotes = soup.find(class_="i").next_sibling
    # while not url.endswith("#"):
    #     #request quotes
    #     res = requests.get(url)
    #     res.raise_for_status()


new_list = [['Why so serious? - The Joker (The Dark Knight)'], ['No, I am your father - Darth Vader (Empire Strikes Back)'], ["All of you are beneath me! I am a god, you dull creature, and I shall not be bullied by... - Loki (Marvel's The Avengers)"], ["You know I've noticed an infestation here. Everywhere I look in fact nothing but undeveloped, unevolved, barely cautious, pond scum totally convinced of their own superiority as they scurry about their short, pointless lives - Edgar the Bug (Men in Black)"], ['Tony Stark was able to build this in a cave... with a box of scraps - Obadiah Stane / Iron Manger (Iron Man)'], ["When they touch down, we'll blow the roof, they'll spend a month sifting through rubble, and by the time they figure out what went wrong, we'll be sitting on a beach, earning twenty percent. - Hans Gruber (Die Hard)"], ["One, two, Freddy's coming for you. Three, Four, better lock your door. Five, Six, grab your crucifix. Seven, Eight, Gonna stay up late. Nine, Ten never sleep again. - Freddy Krueger (A Nightmare on Elm Street)"], ["It's just Boris - Boris the Animal (Men in Black 3)"], ['What a tremendously hostile world that a rat must endure. Yet not only does he survive, he thrives. Because our little foe has an instinct for survival and preservation second to none... And that Monsieur is what a Jew shares with a rat. - Hans Landa'], ['What an excellent day for an exorcism - Regan MacNiel (The Exorcist)'], ['Moria. You fear to go into those mines. The Dwarves delved too greedily and too deep. You know what they awoke in the darkness Khazad-Dum. Shadow and flame. - Saruman (The Lord of the Rings: The Fellowship of the Ring)'], ["Okay, I'll take him back, right after you suck these little Chinese nuts! - Mr Chow (The Hangover)"], ["I don't feel I have to wipe everybody out, Tom. Just my enemies - Michael Corleone (The Godfather)"], ['I ate his liver with some fava beans and a nice Chianti. Tss - Hannibal Lecter (Silence of the Lambs)'], ["I'll be back - T-800 (The Terminator)"], ['Have you seen this boy? - T-100 (Terminator II: Judgement Day)'], ['Must...have... Precious - Gollum (The Lord of the Rings)'], ["You know my name but who are you? Just another American who saw too many movies as a child? Another orphan of a bankrupt culture who thinks he's John Wayne? Rambo? Marshal Dillon? - Hans Gruber (Die Hard)"], ['Heeeeres Johnny - Jack Torrance (The Shining)'], ['Dave, this conversation can serve no purpose anymore. Goodbye. - Hal-9000 (2001: A Space Odyssey)'], ['That depends. Do you see me? - Anton Chigurh (No Country for Old Men)'], ['Kneel before Zod! - General Zod (Superman II)'], ["Ever danced with the Devil by the pale moonlight? - Joker (Tim Burton's Batman)"], ["You best start believing in ghost stories, Miss Turner. You're in one! - Barbossa (Curse of the Black Pearl)"], ['You have failed me for the last time, Admiral. - Darth Vader (The Empire Strikes Back)'], ['Harry Potter. The boy who lived. Come to die. AVADA KEDAVRA - Lord Voldemort (Deathly Hallows Part 2)'], ["There is another organism on this planet that follows the same pattern. Do you know what it is? A virus. Human beings are a disease, a cancer of this planet. You're a plague and we are the cure. - Agent Smith (The Matrix)"], ['Would you like to play a game? - Jigsaw (saw 1-7)'], ["I don't have to tell her? Your mother and I are friends. You know that. - Nurse Ratched (One Flew Over the Cuckoos Nest)"], ['Is this your King?! - Killmonger (Black Panther)'], ['One ring to rule them all, one ring to find them, one ring to bring them all and in the darkness, blind them - Sauron (Lord of the Rings)'], ['No, Mr Bond. I expect you to die! - Auric Goldfinger (Goldfinger)'], ["Marion: I'll tell you everything. Toht (holding flaming poker): Yes, I know you will. - Major Toht (Raiders of the Lost Ark)"], ["I've seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion. I watched C-beams glitter in the dark near the Tannhauser gate. All those moments will be lost in time... like tears in rain... Time to die. - Roy Batty"], ['When it is done and Gotham is ashes, then you have my permission to die. - Bane (The Dark Knight Rises)'], ['You sly dog! You got me monologuing! - Syndrome (The Incredibles)'], ['Little pigs, little pigs, let me come in - Jack Torrance (The Shining)'], ["They cast a spell on you, you know, the Jews. When you work closely with them, like I do, you see this. They have this power. It's like a virus. Some of my men are infected with this virus. - Amon Goeth (Schindlers List)"], ["I have to go now, I'm having an old friend for dinner. - Hannibal Lecter (Silence of the Lambs)"], ['I am your number one fan. There is nothing to worry about. You are going to be just fine. - Annie Wilkes (Misery)'], ['Quite simply, I have harnessed the power of the Gods. - Red Skull (Captain America: The First Avenger)'], ["Everything they built will fall, and from the ashes of their world, we'll build a better one. - Apocalypse (X Men: Apocalypse)"], ["It's a Vibranium car you idiots! The bullets won't penetrate. - Ulysses Klaue (Black Panther)"], ['But no matter, no matter, things have changed. I can touch you... Now! Astounding what a few drops of your blood will do, eh, Harry? - Lord Voldemort (Goblet of Fire)'], ['Keep your friends close but keep your enemies closer - Michael Corleone (Godfather Part II)'], ['You Save the Hero Instead of Saving Yourself - Lockdown (Transformers: Age of Extinction)'], ['As my first act with this new authority, I will create a Grand Army of the Republic - Emperor Palpatine (Star Wars: Episode III - Revenge of the Sith)'], ["Look at everybody's favorite scarer now, you stupid, pathetic waste! You've been #1 for too long, Sullivan! Now your time is up! And don't worry; I'll take good care of the kid! - Randal Boggs (Monsters Inc.)"], ['Show me again, the power of the darkness... and I will let nothing stand in our way. Show me, Grandfather, and I will finish, what you started. - Kylo Ren (Star Wars: The Force Awakens)'], ['Man is forbidden! - Shere Khan (The Jungle Book 2016)'], ["''You must be stupid to think death would be so easy, don't you know we intend to kill you a thousand times? To the end of infinity, if infinity can have an end'' - President Curval (120 Days of Sodom)"], ['1. Why so serious? - The Joker (The Dark Knight)'], ["2. No, I am your father - Darth Vader (Empire Strikes Back)"], ["I ate his liver with some fava beans and a nice Chianti. Tss - Hannibal Lecter (Silence of the Lambs)"], ["1. No, I am your father - Darth Vader (Empire Strikes Back)"], ["Must...have... Precious - Gollum (The Lord of the Rings)"], ["Why so serious? - The Joker (The Dark Knight)"], ["You know I've noticed an infestation here. Everywhere I look in fact nothing but undeveloped, unevolved, barely cautious, pond scum totally convinced of their own superiority as they scurry about their short, pointless lives - Edgar the Bug (Men in Black)"], ["Tony Stark was able to build this in a cave... with a box of scraps - Obadiah Stane / Iron Manger (Iron Man)"], ["All of you are beneath me! I am a god, you dull creature, and I shall not be bullied by... - Loki (Marvel's The Avengers)"]]