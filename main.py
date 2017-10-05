from database import Database
from cal_interface import Cal
from tvdb_api import Tvdb
from get_data import get_data


from config import SHOWS


def main():
    cal = Cal()
    database = Database()
    tvdb = Tvdb()

    for key in SHOWS.keys():
        data = get_data(tvdb, SHOWS[key])
        if data is None:
            continue
        for episode, air_time, name in data:
            if not database.is_uploaded(key, air_time):
                cal.add_all_day_event(get_summary(key, episode), get_description(key, name), air_time)
                database.add_uploaded(key, air_time)
                database.commit()
            else:
                print("Already there")

    database.close()


def get_summary(key, episode): return key + " - " + str(episode)


def get_description(key, name): return "New episode of " + str(key) + ", named " + str(name) + " is here. Enjoy!"


if __name__ == "__main__":
    main()
