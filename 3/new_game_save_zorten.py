from typing import Final

IRONMAN_ATTACK_POWER: Final[int] = 250
BLACKWIDOW_ATTACK_POWER: Final[int] = 180
SPIDERMAN_ATTACK_POWER: Final[int] = 190
HULK_ATTACK_POWER: Final[int] = 300

thanos_life: int = 1500
choice = 0

choice = int(input("Enter Your Pair no >>> "))

if choice == 1:
    print("Ironman And blaclwidow Are Attacking Thanos...")
elif choice == 2:
    print("Blackwidow And Spiderman Attacking Thanos...")
elif choice == 3:
    print("Spiderman And Hulk Are Attacking Thanos...")
elif choice == 4:
    print("Hulk And Ironman Attacling Thanos...")
