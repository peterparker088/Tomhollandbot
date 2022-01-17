from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# LUCK------------ https://telegram.me/Josprojects ------------ #

# EMOJI CONSTANTS
BASKET_BALL = "🏀"
# EMOJI CONSTANTS

@Client.on_message(
    filters.command(["basketball","basket"])
)
async def basketball_basket(client, message):
    """ /basketball an @animatedbasketball """
    rep_mesg_id = message.message_id
    if message.reply_to_message:
        rep_mesg_id = message.reply_to_message.message_id
    await client.send_dice(
        chat_id=message.chat.id,
        emoji=BASKET_BALL,
        disable_notification=True,
        reply_to_message_id=rep_mesg_id
    )
