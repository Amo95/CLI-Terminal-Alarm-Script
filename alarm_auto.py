from datetime import datetime, date
from playsound import playsound
import os, time, calendar, random
from textwrap import dedent

# farg, sarg = sys.argv

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
colors = [BLUE, RED, YELLOW, MAGENTA, GREEN]


def quit():
    print(RED + "\n\nThank for using this cli app\n" + END)
    exit(1)


def weekdays(num):
    try:
        l_time = []

        while len(l_time) < 2:
            ctime = datetime.now()
            current_time = ctime.strftime("%H:%M:%S")
            n_time = current_time.split(":")

            for i in range(0, 100):
                if str(n_time) == str(num):

                    os.system("clear")

                    print(colors[random.randint(0, len(colors) - 1)] + dedent(f"""
                        ███╗██╗███╗    ██╗    ██╗ █████╗ ██╗  ██╗███████╗██╗   ██╗██████╗ ██╗██╗    ███████╗████████╗██╗   ██╗██████╗ ██╗   ██╗██╗██╗
                        ██╔╝██║╚██║    ██║    ██║██╔══██╗██║ ██╔╝██╔════╝██║   ██║██╔══██╗██║██║    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗╚██╗ ██╔╝██║██║
                        ██║ ██║ ██║    ██║ █╗ ██║███████║█████╔╝ █████╗  ██║   ██║██████╔╝██║██║    ███████╗   ██║   ██║   ██║██║  ██║ ╚████╔╝ ██║██║
                        ██║ ╚═╝ ██║    ██║███╗██║██╔══██║██╔═██╗ ██╔══╝  ██║   ██║██╔═══╝ ╚═╝╚═╝    ╚════██║   ██║   ██║   ██║██║  ██║  ╚██╔╝  ╚═╝╚═╝
                        ███╗██╗███║    ╚███╔███╔╝██║  ██║██║  ██╗███████╗╚██████╔╝██║     ██╗██╗    ███████║   ██║   ╚██████╔╝██████╔╝   ██║   ██╗██╗
                        ╚══╝╚═╝╚══╝     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝    ╚═╝   ╚═╝╚═╝
                        """ + END))
                    time.sleep(1)
                    playsound('alarm_3.mp3')

                    l_time.append(i)

    except KeyboardInterrupt:
        quit()

    except EOFError:
        quit()


def weekends():
    weekdays("10")


if __name__ == '__main__':
    os.system("clear")
    while True:
        my_date = date.today()
        day = calendar.day_name[my_date.weekday()]
        l_day = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"
        ]

        if day in l_day[0:5]:
            try:
                enter = input("Set time [format::HH.MM.SS]>>> ")
                split_entry = enter.split(".")
                weekdays(split_entry)
            except KeyboardInterrupt:
                quit()

        elif day in l_day[5:7]:
            weekends()
