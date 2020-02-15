from fortnite_python import Fortnite
from fortnite_python.domain import Mode, Platform
import fortnite_python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, ParseMode, ReplyKeyboardRemove
import logging
from emoji import emojize
import time

fort = Fortnite('fortnite Api')
platforms_list = [Platform.PC, Platform.XBOX, Platform.PSN, Platform.TOUCH, Platform.GAMEPAD, Platform.KBM]

updater = Updater(token='telegram token', use_context=True)
dispatch = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

user = {}

earth = emojize(':earth_africa:', use_aliases=True)
vi = emojize(":white_check_mark:", use_aliases=True)
mag = emojize(":mag:", use_aliases=True)
mag_right = emojize(":mag_right:", use_aliases=True)
sign_ic = emojize(":heavy_minus_sign:", use_aliases=True)
unlike = emojize(":thumbsdown:", use_aliases=True)
error = emojize(":x:", use_aliases=True)


def found_user(user):
    for platform in platforms_list:
        try:
            player = fort.player(user, platform)
            return player
        except:
            pass
    return False
