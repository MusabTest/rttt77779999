import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# تكوين سجلات الوحدة النمطية
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# تعريف المعالج الذي سيتم استدعاؤه عند تنفيذ الأمر /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('ادخل كود التفعيل.')

# تعريف المعالج الذي سيتم استدعاؤه عند استلام رسالة نصية
def process_message(update: Update, context: CallbackContext) -> None:
    user_name = update.message.text

    # احصل على مسار الملف النصي
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # قم بفتح ملف النص
    with open(file_path, 'r') as file:
        words = file.read().splitlines()

    if user_name in words:
        update.message.reply_text('تم التفعيل')
        context.bot.stop()
    else:
        update.message.reply_text('كود التفعيل خاطئ اعد المحاولة! .')

def main() -> None:
    # قم بإعداد Updater واحصل على التوكن الخاص بك من @BotFather
    updater = Updater('6081907607:AAESpGdusikUfxqadmoFyCpu4TZ9eW_XitY')

    # احصل على المساعد من التحديثات
    dispatcher = updater.dispatcher

    # تعريف معالجات الأوامر
    dispatcher.add_handler(CommandHandler('start', start))

    # تعريف معالج الرسائل النصية
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_message))

    # ابدأ البوت
    updater.start_polling()

    # انتظر حتى يتم إيقاف البوت
    updater.idle()

if __name__ == '__main__':
    main()
