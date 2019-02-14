#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys
import traceback
from telegram import ParseMode

from . import keyboards
from ..sources import wf
from ..utils import utils
from ..utils.logging import logger
from ..utils.loadconfig import config

warframe = wf.Warframe()


def error(update, context):
    trace = ''.join(traceback.format_tb(sys.exc_info()[2]))
    text = f'The error <code>{context.error}</code> happened. The full traceback:\n\n<code>{trace}</code>'
    context.bot.send_message(config['admin_id'], text, parse_mode=ParseMode.HTML)
    logger.error(f'Update: {update}')
    raise context.error


def start(update, context):
    utils.update_user_data(update.message.from_user, context.user_data)
    update.message.reply_text('Please choose:', reply_markup=keyboards.main_menu_keyboard())


def invasions(update, context):
    utils.update_user_data(update.message.from_user, context.user_data)
    text = wf.get_invasions(update.message.from_user.id, True, False)
    update.message.reply_text(text=text, parse_mode=ParseMode.MARKDOWN)