import time
import subprocess
import os

import settings 
from spreadsheet import Spreadsheet
import co2_monitor 
from monitor import Monitor
import slack_nortification


if __name__ == '__main__':
    settings.init()
    spreadsheet = Spreadsheet()
    monitor = Monitor()
    status_list = ["normal", "warning", "alart"] 
    status = status_list[0]

    while True:
        cmd = "hostname -I | cut -d' ' -f1"
        IP = subprocess.check_output(cmd, shell=True).decode("utf-8")

        # read sensor values
        co2, tem, hu = co2_monitor.read_all()

        monitor.display(co2, tem, hu, IP)

        # push data to google spreadsheet
        spreadsheet.appendValue([[time.time(), co2, tem, hu]], range_='log!A1')

        # notification to slack
        if co2 >= 2000: 
            if status == status_list[2]:
                continue
            status = status_list[2]
            url = os.environ.get("SLACK_URL") 
            message = {
                'text': 'Alart!!!\nCO2 concentration is over 2000,',
            }
            res = slack_nortification.post_slack(url, message)
        elif co2 >= 1500:
            if status == status_list[1]: 
                continue
            status = status_list[1]
            url = os.environ.get("SLACK_URL") 
            message = {
                'text': 'Warning!\nCO2 concentration is over 1500,',
            }
            res = slack_nortification.post_slack(url, message)
        else:
            status = status_list[0]

        time.sleep(10)
