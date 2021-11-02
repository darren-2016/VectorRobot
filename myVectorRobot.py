#!/usr/bin/env python3

# Copyright (c) 2021 Darren Draper
#

import anki_vector

from anki_vector import audio


def main():
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:
            robot.audio.set_master_volume(audio.RobotVolumeLevel.LOW)

            robot.behavior.say_text("Hello there!")

            robot.motors.stop_all_motors()

            #if robot.status.is_being_held:
                #print("Vector is being held.")

if __name__ == "__main__":
    main()
