from config import *
from send_emails import send_email
from sms import send_sms
import webbrowser
import telegram_send

def send_alerts(flats):
    if SOUND_ALERTS:
        print('\a')
    if SEND_EMAILS:
        send_email_alert(flats)
    if SEND_SMS:
        send_sms_alert(flats)
    if OPEN_WEBBROWSER:
        open_webbrowser(flats)
    if SEND_TELEGRAM:
        send_telegram_alert(flats)


def alert_summary(flats):
    return f'Flatchecker has found {len(flats)} new flats'


def alert_detail(flats):
    out=alert_summary(flats)
    for flat in flats:
        out += '\n\n'+flat.alert()
    return out


def open_webbrowser(flats):
    for flat in flats:
        webbrowser.open(flat.link)


def send_email_alert(flats):
    send_email(alert_summary(flats),alert_detail(flats))


def send_sms_alert(flats):
    if len(flats) == 1:
        send_sms(flats[0].alert())
    else:
        send_sms(alert_summary(flats))

def send_telegram_alert(flats):
    telegram_send.send(messages=[flat.alert() for flat in flats])

