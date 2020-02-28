from fortnite_funcs import *


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"{earth}Welcome To Fortnite Bot{earth}")
    menu_1(update, context)


def menu_1(update, context):
    custom_keyboard = [[f'Search a player {mag_right}']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard, one_time_keyboard=True, resize_keyboard=True)
    user[update.message.chat_id] = {'search_state': False, "found_state": False}
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(r'./Fortnit.jpg',
                                      'rb'), reply_markup=reply_markup)


def menu_2(update, context):
    custom_keyboard = [[f'{sign_ic}Stats Solo{sign_ic}'], [f'{sign_ic}Stats Duo{sign_ic}'],
                       [f'{sign_ic}Stats Squad{sign_ic}'], [f'{mag_right} Search for another player {mag}']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(f"*The player is Found* {vi}", reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN)


def echo_text(update, context):
    try:
        if update.message.text == f'Search a player {mag_right}':
            user[update.message.chat_id] = {'search_state': True, "found_state": False}
            update.message.reply_text('*Please enter the player username*', parse_mode=ParseMode.MARKDOWN)
        elif update.message.text == f'{sign_ic}Stats Solo{sign_ic}' and user[update.message.chat_id]['found_state']:
            try:
                stats_solo = str(user[update.message.chat_id]['player'].get_stats(Mode.SOLO))
                update.message.reply_text(stats_solo)
            except:
                update.message.reply_text(f'There are no stats for the Solo playlist.{unlike}')
        elif update.message.text == f'{sign_ic}Stats Duo{sign_ic}' and user[update.message.chat_id]['found_state']:
            try:
                stats_dou = str(user[update.message.chat_id]['player'].get_stats(Mode.DUO))
                update.message.reply_text(stats_dou)
            except:
                update.message.reply_text(f'There are no stats for the Dou playlist.{unlike}')
        elif update.message.text == f'{sign_ic}Stats Squad{sign_ic}' and user[update.message.chat_id]['found_state']:
            try:
                stats_squad = str(user[update.message.chat_id]['player'].get_stats(Mode.SQUAD))
                update.message.reply_text(stats_squad)
            except:
                update.message.reply_text(f'There are no stats for the Squad playlist.{unlike}')
        elif update.message.text == f'{mag_right} Search for another player {mag}':
            user[update.message.chat_id] = {'search_state': True, "found_state": False}
            update.message.reply_text('*Please enter the player username*', parse_mode=ParseMode.MARKDOWN,
                                      reply_markup=ReplyKeyboardRemove())
        elif user[update.message.chat_id]['search_state']:
            player = found_user(update.message.text)
            if player:
                user[update.message.chat_id] = {'player': player, 'search_state': False, "found_state": True}
                menu_2(update, context)
            else:
                update.message.reply_text(f'Error "{update.message.text}" doesn\'t exist please try again.{error}')
    except KeyError:
        pass


dispatch.add_handler(CommandHandler('start', start))
dispatch.add_handler(MessageHandler(Filters.text, echo_text))
dispatch.add_handler(CommandHandler('menu_1', menu_1))

print('Running..')
updater.start_polling()
updater.idle()
