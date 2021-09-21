from telegram.messanger import *
from base.base import get_card_token, app

app.add_url_rule(
    '/{Some secret url}',
    view_func=TelegramMessanger.as_view('telegram_messanger')
)
