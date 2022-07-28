import tank
import sys


def main():
    """
    Main Programme
    """

    #
    isaac_tank = tank.Tank('german', 'tiger')
    tim_tank = tank.Tank('american', 'sherman')
    harry_tank = tank.Tank('british', 'churchill')

    # game begins
    isaac_tank.accell(49)
    tim_tank.accell(41)
    harry_tank.rotate_left(289)
    harry_tank.accell(29)

    isaac_tank.take_damage(53)
    print(isaac_tank._health)

    isaac_tank._health = 100
    print(isaac_tank._health)

    isaac_tank.set_health(101)
    print(isaac_tank._health)

    # print Object issue
    print(isaac_tank)

    print(f"health of Isaacs + Tims Tank = {isaac_tank + tim_tank}")


    return None


if __name__ == "__main__":
    main()
    sys.exit(0)
