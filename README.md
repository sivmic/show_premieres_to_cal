Just install the dependencies from the `dependencies.txt` file, and you're almost good to go.

There's just one little thing. You have to create a file called `config.py` in the root of the project and create this variables in it. Then you're good to go.

```python
# cal_id to your cal
CAL_ID = "your cal id"

# google cal informations
SCOPES = "scopes you are giving permissions"
CLIENT_SECRET_FILE = "client_secret.json"
APPLICATION_NAME = "Google Calendar to adding premieres of favourite shows"

# for better usability (some shows do not have nice names in tvdb_api)
SHOWS = {
    "name of show": "name of show in tvdb_api"
}
```

Before using you also need to add `client_secret.json`. Instructions here: (step 1):

`https://developers.google.com/google-apps/calendar/quickstart/python#step_1_turn_on_the_api_name`


Also: this script add everything from Season 1, so, add this events to stand-alone cal, not your main cal.
(specified in `CAL_ID` in `config.py`)


If you want to use deploy script, create `deploy.sh`. Here is example:

```
zip -r output.zip * -x "uploaded.db" -x "output.zip"
scp -i <path_to_your_aws_pem_file> output.zip <username>@<ip>:~/show_premieres_to_cal.zip
ssh -i <path_to_your_aws_pem_file> <username>@<ip> "cp ~/show_premieres_to_cal/uploaded.db ~/uploaded.db; rm -rf ~/show_premieres_to_cal; mkdir ~/show_premieres_to_cal; unzip show_premieres_to_cal.zip -d ~/show_premieres_to_cal; cp ~/uploaded.db ~/show_premieres_to_cal/uploaded.db;"
```

When you are done, the best way to use this script is with cron. Just run `main.py` every day and you are good.

