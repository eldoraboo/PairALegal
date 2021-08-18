from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Stages
FIRST,SECOND = 1,2

def start(update, context):
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [InlineKeyboardButton("Criminal Defence", callback_data='1'),
         InlineKeyboardButton("Matrimonial Matters", callback_data='2')],
         [InlineKeyboardButton("Accident & Personal Injury Claim", callback_data='3')],
         [InlineKeyboardButton("Estate Matters", callback_data='4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(
        "Hello and welcome to Pair-A-Legal!"
    )
    time.sleep(0.5)
    update.message.reply_text(
        "I am the Pair-A-Legal bot, designed to aid you in finding legal services that best suit your needs."
    )
    time.sleep(0.5)
    update.message.reply_text(
        "What services are you looking for?",
        reply_markup = reply_markup
    )
    # Tell ConversationHandler that we're in state `FIRST` now
    return FIRST


def start_over(update, context):
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # Get Bot from CallbackContext
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Criminal Defence", callback_data='1'),
         InlineKeyboardButton("Matrimonial Matters", callback_data='2')],
         [InlineKeyboardButton("Accident & Personal Injury Claim", callback_data='3')],
         [InlineKeyboardButton("Estate Matters", callback_data='4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="What services are you looking for?",
        reply_markup=reply_markup
    )
    return FIRST


def criminalDef(update, context): #1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='1.1'),
         InlineKeyboardButton("No", callback_data='1.2')],
         [InlineKeyboardButton("I don't know",callback_data = '1.3')],
         [InlineKeyboardButton("Back",callback_data = '0')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Are you eligible to receive legal aid under the criminal Legal Aid Scheme?",
        reply_markup=reply_markup
    )
    return FIRST


def c_legal_aid_yes(update, context): #1.1
    #direct to lawsocprobono to seek services from there
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""Kindly head over to https://www.lawsocprobono.org/Pages/Criminal-Legal-Aid-Scheme.aspx for your legal services.""",
    )
    time.sleep(1)
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. 
        Would you like to start over?""",
        reply_markup=reply_markup
    )
    return FIRST

def cdef_send_profiles(update, context): #1.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton(">$1200", callback_data='1.2.1')],
         [InlineKeyboardButton("$800 - $1199", callback_data='1.2.2')],
         [InlineKeyboardButton("$400 - $799", callback_data='1.2.3')],
         [InlineKeyboardButton("Back",callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Please choose based on your financial budget",
        reply_markup=reply_markup
    )
    return SECOND

def eudora_bong(update, context): #1.2.1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='1.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("female.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Eudora Bong \nCompany: Chee Chong LLP \nYears of Experience: 9""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/eudora-bong"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def angus_lim(update, context): #1.2.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='1.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Angus Lim \nCompany: Hantan LLP \nYears of Experience: 4""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/angus-lim"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST

def hana_sriram(update, context): #1.2.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='1.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("female.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Hana Sriram \nCompany: A.E.N. Law LLP \nYears of Experience: 2""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/hana-sriram"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def c_legal_aid_check(update, context): #1.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='1')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""Kindly head over to https://www.lawsocprobono.org/Pages/Criminal-Legal-Aid-Scheme.aspx to check your eligibility.""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. Would you like to start over?""",
        reply_markup=reply_markup
    )
    return FIRST

def matri_matters(update, context): #2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='2.1'),
         InlineKeyboardButton("No", callback_data='2.2')],
         [InlineKeyboardButton("I don't know",callback_data='2.3')],
         [InlineKeyboardButton("Back", callback_data='0')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Are you eligible to receive legal aid from the Legal Aid Bureau?",
        reply_markup=reply_markup
    )
    return FIRST

def mlaw_yes(update, context): #2.1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""Kindly head over to https://lab.mlaw.gov.sg/ for your legal services.""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. Would you like to start over?""",
        reply_markup=reply_markup
    )
    return FIRST

def mlaw_check(update, context): #2.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""Kindly head over to https://lab.mlaw.gov.sg/legal-services/do-i-qualify/ to check your eligibility.""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. Would you like to start over?""",
        reply_markup=reply_markup
    )
    return FIRST

def matri_services(update, context): #2.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Contested Divorce", callback_data='2.2.0'),
         InlineKeyboardButton("Uncontested Divorce", callback_data='2.2.0')],
         [InlineKeyboardButton("Uncontested Annulment", callback_data='2.2.0'),
         InlineKeyboardButton("Deed of separation", callback_data='2.2.0'),],
         [InlineKeyboardButton("Uncontested Variation of Court Order", callback_data='2.2.0')],
         [InlineKeyboardButton("Prenuptual/Postnuptual agreement", callback_data='2.2.0')],
         [InlineKeyboardButton("Back",callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="What kind of services do you need specifically?",
        reply_markup=reply_markup
    )
    return FIRST
def matri_send_profiles(update, context): #2.2.0
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton(">$1100", callback_data='2.2.1')],
         [InlineKeyboardButton("$900 - $1099", callback_data='2.2.2')],
         [InlineKeyboardButton("$700 - $899", callback_data='2.2.3')],
         [InlineKeyboardButton("Back",callback_data='2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Please choose based on your financial budget",
        reply_markup=reply_markup
    )
    return SECOND

def janus_don(update, context): #2.2.1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='2.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Janus Don \nCompany: Balani LLC \nYears of Experience: 8""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/janus-don"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def harri_chin(update, context): #2.2.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='2.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Harri Chin \nCompany: Elle Law \nYears of Experience: 5""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/harri-chin"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def lennis_tay(update, context): #2.2.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='2.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Lennis Tay \nCompany: Faradana Legal\nYears of Experience: 14""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/lennis-tay"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST

def acc_per_injury(update, context): #3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='2.1'),
         InlineKeyboardButton("No", callback_data='3.2')],
         [InlineKeyboardButton("I don't know",callback_data='2.3')],
         [InlineKeyboardButton("Back", callback_data='0')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Are you eligible to receive legal aid from the Legal Aid Bureau?",
        reply_markup=reply_markup
    )
    return FIRST

def aci_send_profiles(update, context): #3.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton(">$1200", callback_data='3.2.1')],
         [InlineKeyboardButton("$800 - $1199", callback_data='3.2.2')],
         [InlineKeyboardButton("$400 - $799", callback_data='3.2.3')],
         [InlineKeyboardButton("Back",callback_data='3')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Please choose based on your financial budget",
        reply_markup=reply_markup
    )
    return SECOND
def amina_choo(update, context): #3.2.1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='3.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("female.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Amina Choo \nCompany: Boo and Ow LLP \nYears of Experience: 8""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/amina-choo"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST

def donshel_quek(update, context): #3.2.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='3.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Donshel Quek \nCompany: Dantil Solutions \nYears of Experience: 7""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/donshel-quek"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def jerry_rugal(update, context): #3.2.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='3.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Jerry Rugal \nCompany: Nga Law LLC \nYears of Experience: 6""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/jerry-rugal"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def estate_matters(update, context): #3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='2.1'),
         InlineKeyboardButton("No", callback_data='4.2')],
         [InlineKeyboardButton("I don't know",callback_data='2.3')],
         [InlineKeyboardButton("Back", callback_data='0')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Are you eligible to receive legal aid from the Legal Aid Bureau?",
        reply_markup=reply_markup
    )
    return FIRST

def em_services(update, context): #4.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Wills", callback_data='4.2.0'),
         InlineKeyboardButton("Lasting power of attorney", callback_data='4.2.0')],
         [InlineKeyboardButton("Probate", callback_data='4.2.0'),
         InlineKeyboardButton("Letters of Administration", callback_data='4.2.0')],
         [InlineKeyboardButton("Back",callback_data='4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="What kind of services do you need specifically?",
        reply_markup=reply_markup
    )
    return FIRST

def em_send_profiles(update, context): #4.2.0
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton(">$400", callback_data='4.2.1')],
         [InlineKeyboardButton("$300 - $399", callback_data='4.2.2')],
         [InlineKeyboardButton("$200 - $299", callback_data='4.2.3')],
         [InlineKeyboardButton("Back",callback_data='4')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Please choose based on your financial budget",
        reply_markup=reply_markup
    )
    return SECOND
    
def hairna_lim(update, context): #4.2.1
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='4.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("female.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Hairna Lim \nCompany: Saerang LLC \nYears of Experience: 16""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/hairna-lim"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST

def shieldon_goh(update, context): #4.2.2
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='4.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("male.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Shieldon Goh \nCompany: Subrani SG LLP\nYears of Experience: 3""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/shieldon-goh"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST

def tamfan_niu(update, context): #4.2.3
    """Show new choice of buttons"""
    query = update.callback_query
    bot = context.bot
    keyboard = [
        [InlineKeyboardButton("Yes", callback_data='0'),
         InlineKeyboardButton("No", callback_data='00')],
         [InlineKeyboardButton("Back",callback_data='4.2')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="""We have found a lawyer that suits your needs!""",
    )
    bot.send_photo(
        chat_id=query.message.chat_id,
        photo = open("female.jpg",'rb')
        )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Name: Tamfan Niu \nCompany: Guan & Kai \nYears of Experience: 2""",
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """See more on our website: https://eldoraboo.github.io/PairALegal/tamfan-niu"""
    )
    bot.send_message(
        chat_id=query.message.chat_id,
        text = """Thank you for using Pair-A-Legal bot. \nWould you like to restart?""",
        reply_markup = reply_markup
    )
    return FIRST
def end(update, context):
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over"""
    query = update.callback_query
    bot = context.bot
    bot.edit_message_text(
        chat_id=query.message.chat_id,
        message_id=query.message.message_id,
        text="Goodbye!"
    )
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater('ENTER_TOKEN_HERE', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Setup conversation handler with the states FIRST 
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [CallbackQueryHandler(criminalDef, pattern='^' + '1' + '$'),
                    CallbackQueryHandler(c_legal_aid_yes, pattern='^' + '1.1' + '$'),
                    CallbackQueryHandler(c_legal_aid_check, pattern='^' + '1.3' + '$'),
                    CallbackQueryHandler(cdef_send_profiles, pattern='^' + '1.2' + '$'),
                    CallbackQueryHandler(matri_matters, pattern='^' + '2' + '$'),
                    CallbackQueryHandler(mlaw_yes, pattern='^' + '2.1' + '$'),
                    CallbackQueryHandler(mlaw_check, pattern='^' + '2.3' + '$'),
                    CallbackQueryHandler(matri_services, pattern='^' + '2.2' + '$'),
                    CallbackQueryHandler(matri_send_profiles, pattern='^' + '2.2.0' + '$'),
                    CallbackQueryHandler(acc_per_injury, pattern='^' + '3' + '$'),
                    CallbackQueryHandler(aci_send_profiles, pattern='^' + '3.2' + '$'),
                    CallbackQueryHandler(estate_matters, pattern='^' + '4' + '$'),
                    CallbackQueryHandler(em_services, pattern='^' + '4.2' + '$'),
                    CallbackQueryHandler(em_send_profiles, pattern='^' + '4.2.0' + '$'),
                    CallbackQueryHandler(start_over, pattern='^' + '0' + '$'),
                    CallbackQueryHandler(end, pattern='^' + '00' + '$')],
            SECOND: [CallbackQueryHandler(criminalDef, pattern='^' + '1' + '$'),
                    CallbackQueryHandler(eudora_bong, pattern='^' + '1.2.1' + '$'),
                    CallbackQueryHandler(angus_lim, pattern='^' + '1.2.2' + '$'),
                    CallbackQueryHandler(hana_sriram, pattern='^' + '1.2.3' + '$'),
                    CallbackQueryHandler(matri_matters, pattern='^' + '2' + '$'),
                    CallbackQueryHandler(janus_don, pattern='^' + '2.2.1' + '$'),
                    CallbackQueryHandler(harri_chin, pattern='^' + '2.2.2' + '$'),
                    CallbackQueryHandler(lennis_tay, pattern='^' + '2.2.3' + '$'),
                    CallbackQueryHandler(acc_per_injury, pattern='^' + '3' + '$'),
                    CallbackQueryHandler(amina_choo, pattern='^' + '3.2.1' + '$'),
                    CallbackQueryHandler(donshel_quek, pattern='^' + '3.2.2' + '$'),
                    CallbackQueryHandler(jerry_rugal, pattern='^' + '3.2.3' + '$'),
                    CallbackQueryHandler(estate_matters, pattern='^' + '4' + '$'),
                    CallbackQueryHandler(hairna_lim, pattern='^' + '4.2.1' + '$'),
                    CallbackQueryHandler(shieldon_goh, pattern='^' + '4.2.2' + '$'),
                    CallbackQueryHandler(tamfan_niu, pattern='^' + '4.2.3' + '$')
                    ]

        },
        fallbacks=[CommandHandler('start', start)]
    )

    # Add ConversationHandler to dispatcher that will be used for handling
    # updates
    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
