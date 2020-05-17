
# Operating environment
hardware
- Raspberry Pi
- mh-z19 (CO2 sensor)
- OLED (128\*32)

software
- python3
- python modules
    - mh-z19
    - adafruit-circuitpython-ssd1306
    - modules for google spreadsheet 
        - google-api-python-client 
        - google-auth-httplib2
        - google-auth-oauthlib

        `pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`


# Usage

Set `SPREADSHEET_ID` and `SLACK_URL` in `.env`.

Set up google spreadsheet.

Set up slack Incoming Webhooks.


### service setting

1. `make init-service`
