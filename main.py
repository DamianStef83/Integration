# Damian Stefaniuk
# Family Cookbook
# Welcome
print("Hello, Reader!")
# Introduction
print("Welcome to my Family Cook Book")
print("")  # Separates lines
print("I am glad you decided to learn my family's christmas traditions!")
print("")
# Purpose outlined
print("Today, we will learn how to make Vareniki.")
print("")
# Age
age=int(input("How old are you?:"))
if (age>=18):
      print("This is a delicious dish not only for christmas, but all the"
            " time!")
      print("")
else:
      print("Starting to cook at a young age is a great thing!")
      print("")
# beginning of recipe
# https://www.196flavors.com/ukraine-vareniki/
flour = 2  # cups
eggs = 2
dMilk = .5   # d is for dough
dVOil = 2  # tablespoons (Dough)
salt = 1   # teaspoon
potato = 1  # lb
onion = 2
fMilk = .5  # f is filling
fVOil = 4  # filling in tablespoons
butter = 4  # tablespoons
print("In order to begin your dough, you will need:")
# using + to include the ingredients for the dough
print("2 cups Flour, " + "2 Eggs, " + "1/2 cup Milk, "
      + "2 Tablespoons of Vegetable Oil, " + "and a teaspoon of Salt.")
print("")
print("When beginning your process, you will want to combine the flour, eggs,"
      "milk, and vegetable oil.")
print("")
print("Once you have kneaded a nice dough together, cover for 30 minutes, "
      "but make sure it is away from any heat.")
print("")
print("During those 30 minutes, you can take some time off to do anything, "
      "including this math quiz!")
quiz=int(input("What is 12 * 3 + 7?"))
# created a quiz to show I can use basic numeric operators
ans = (12 * 3 +7)
if (quiz == ans):
      print("Nice Job! You aced it!")
      print("")
else:
      print("Looks  like  you failed")
      print("")
print("Now that the 30 minutes are up, uncover your dough, and")
print("cut your dough  into  2 or  3  pieces and roll  out  each piece into"
      "a thickness of about 1/8th of an inch.")
print("")
print("Using a cookie cutter, cut your dough in circles of about 3 inches"
      "in diameter")
print("")
print("Lets go prepare the filling now!")
print("")
# Begins filling recipe
print("In order to begin your filling, you will need: 1 lb of potatoes, 2 "
      "onions, 1/2 cup boiling milk, 4 tablespoons vegetable oil, and 4"
      " tablespoons butter")
print("")
print("Start your filling by heating the vegetable oil in  a frying pan and "
      "fry the onions over medium heat, stirring regularly until golden brown"
      ", then drain them of their oil and place on plate lined with paper "
      "towel")
print("")
print("Then, you want to peel and boil the potatoes in a large amount of "
      "slightly salted water")
print("")
print("When ready, drain potatoes using a large skimmer and keep the boiling "
      "water for cooking")
print("")
print("Place the cooked potatoes in a large bowl and using a potato masher, "
      "mash the potato, gradually adding boiling milk. Add the butter and, "
      "optionally a little boiling water from the potatoes, and mix until "
      "a slightly firm consistency is obtained.")
print("")
print("Follow by adding fried onions and mix. Season with salt and pepper")
print("")
# Putting together
print("Now that you have your filling, place 1 teaspoon of filling in the "
      "center of each circle  of dough, fold them in half and pinch the edges"
      " with wet  hands.")
print("")
print("Now  that you have your raw Vareniki, heat a large abount of boiling"
      " salt water in a casserole dish")
print("")
print("Now, immerse the Vareniki into simmering water and cook for 180 "
      "seconds. Lets do a countdown!")
# 180 second "Countdown" for the recipe
for x in range(180,-1,-1):
      print(x)
print("")
print("Now that your Vareniki are ready, drain the water.")
print("")
print("Now  that they are ready, place the boiled vareniki into a bowl")
print("")
print("Sprinkle the top with onions, salt  lightly, and  pepper. Mix this g"
      "ently in your  bowl.")
print("")
print("Finally, sprinkle with chopped spring onion")
print("")
print("")
print("What makes this dish special to the Stefaniuk household is the extras!")
print("")
# Explaining how we use sour cream on our vareniki
print("Get some sour cream and put it on your plate with the Vareniki. This "
      "makes them  taste a lot better, just like putting sour cream on your"
      " baked potatoes.")
print("")
# going by traditions, we begin to expirience a typical christmas
print("Now that you've successfully made them, we can enjoy the rest of the"
      " christmas traditions of the Stefaniuk Household!")
print("")
# Ukranian Carolers always show up to my grandparents on Christmas Eve
print("Let's start by listening to the carolers outside! What song do you thi"
      "nk they'll sing? a? Or b? A is Shchedryk and b is Kolyadnytsya")
# Dialect between Learner and Me to explain why  the songs are in Ukranian
print("What are those songs?")
print("They are Ukranian songs due to us  being located in Chicago's Ukrainan"
      " Village! Select one! a or b?")
# select song
a = "Shchedryk"
b="Kolyadnytsya"
c = ""
song = input("What song?")

if song == a:
      print("Lets listen! ")
      print("")
      print("Carolers (singing): Shchedryk shchedryk, shchedrivochka Pryletila"
            " lastivochka Stala sobi shchebetaty Hospodarya vyklykaty"
            "Vyydy, vyydy, hospodaryu  Podyvysya na kosharu Tam ovechky"
            " pokotylys? A yahnychky narodylys? V tebe tovar ves? khoroshyy"
            " Budesh? maty mirku hroshey V tebe tovar ves? khoroshyy "
            "Budesh? maty mirku hroshey Khoch ne hroshey, to polova"
            "V tebe zhinka chornobrova Shchedryk shchedryk, shchedrivochka")
      print("")
elif song == b:
      print("That's is a good song! Lets listen!")
      print("")
      print("Carolers (singing): Kolyad-kolyad, kolyadnytsya, Dobra z medom"
            " palyanytsya, "
            "A bez medu ne taka, Dayte, dyad'ko, shostaka,A yak ne shostaka,"
            "to try hroshy, Bo ya kolyadnyk khoroshyy")
      print("")
else:
      print("That's not an option")
print("")
print("Now that the carolers are gone, lets open up presents!")
print("")
print("What was it you wanted for Christmas again? A Bike or Skates?")
skates = "Skates" or "skates"
bike = "Bike" or "bike"
present=input("")
if present == "Skates" or present == "skates":
      print("Here you go! A brand new pair of Skates!")
      print("")
elif present == "Bike" or present == "bike":
      print("Here's your brand new bike!")
      print("")
else:
      end()
print("Thanks for showing up tonight and learning how to cook with me!")
print("It was a blast, and I hope you use this recipe in the future!")
print("Good luck with your future endeavors! Sending you off with a great"
      " Dr. Seuss quote, Oh the Places You'll go!")
print("My family will now say goodbye. There are 9 of us so this may take a "
      "while")
print("")
num=0
while num<9:
      num +=1
      print("Good night!")



