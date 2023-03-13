correct_guess: bool = False
guess: str = ""
planet: str = "Zorten"

while correct_guess is not True:
  guess = input("Louis Asked can you guess his planet's name? >>> ")

  if guess.lower() == planet.lower():
      print("Right Guess!! Louis is From Zortan ")
      correct_guess = True
  else:
      print("Wrong Choice, try again!")