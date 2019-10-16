#!/usr/bin/env python3

# Created by : Mariam Hemdan
# Created on : October 2019
# This program check whether an entered character is lowercase or uppercase


def main():
    # this program check whether an entered character is lowercase or uppercase

    # input
    character = (input("Enter your character: "))
    print("")

    # process and output
    if (character >= "a" and character <= "z"):
        print(" This character is a Lowercase character ")
    elif(character >= "A" and character <= "Z"):
        print("This character is an Uppercase character ")
    else:
        print(" This is not a character ")


if __name__ == '__main__':
    main()
