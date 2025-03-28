import telebot

TOKEN = "8189191443:AAG2JVIYUssa-yZKdVONSacrNJF5EYJK_Y8"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")


# Command handler
@bot.message_handler(commands=['sanjar_belgila'])
def tag_all(message):
    chat_id = message.chat.id
    members = bot.get_chat_administrators(chat_id)
    all_members = []

    try:
        for i in range(1, 500):
            user = bot.get_chat_member(chat_id, i)
            if user.status in ['member', 'administrator', 'creator'] and not user.user.is_bot:
                all_members.append(
                    f"@{user.user.username}" if user.user.username else f"<a href='tg://user?id={user.user.id}'>{user.user.full_name}</a>")
    except Exception:
        pass

    if all_members:
        tag_message = " ".join(all_members)
        bot.send_message(chat_id, f"🔔 {tag_message}")
    else:
        bot.send_message(chat_id,
                         " ")


# Text message handler
@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text.strip()  # Bo'shliqlarni olib tashlash

    # So'z va sonlarni tekshirish
    if text == "311":
        bot.send_message(chat_id, "@MRF_03 @Abduraimov_Sanjarbek @AbdurahimSalox @SpencerCOF @S_R_B_13 @JaysonKhan @javohirilyosbekov @Dedas123 @IsomovBakhodir @akbarovmuhammadali777 @ahmadali_gulomov @Raximjon_R7 @al1_lion @asror10122003 @dastur_2021 @Ilhomjonmuqimov2002 @Mvare2 @MahmudovMurodil04 @theshadowmonarch1 @lifeofsanjar @Abdurasulov_02 @Zafarbek1009 @I1_Alex")
    elif text == "Bot":
        bot.send_message(chat_id, "Bot qaravor @Abduraimov_Sanjarbek")

    #else:
       # bot.send_message(chat_id, f"Siz yozgan matn: {text}. Men bunga javob bera olmadim.")


print("Bot ishga tushdi...")
bot.polling()