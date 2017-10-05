def get_data(tvdb, serial_name: str):
    try:
        data = []

        show = tvdb[serial_name]
        for season in show.keys():
            if season == 0:
                continue
            for episode in show[season].keys():
                name = show[season][episode]['episodename']
                air_time = show[season][episode]['firstaired']
                episode = "Season " + str(season) + ": Episode " + str(episode)
                data.append([episode, air_time, name])

        return data
    except:
        return None
