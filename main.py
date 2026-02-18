import telebot
import time

TOKEN = "8298434438:AAHE6lsACek27uKnjnKDqjH556ojJri7y3Y"
MY_ID = 6149493827  

bot = telebot.TeleBot(TOKEN)

# রিপ্লাই দেওয়ার সময় বাড়তি টেক্সট সরিয়ে ফেলা হয়েছে
@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.chat.id == MY_ID)
def reply_to_user(message):
    try:
        reply_text = message.reply_to_message.text
        lines = reply_text.split("\n")
        user_id = ""
        for line in lines:
            if "🆔 আইডি:" in line:
                user_id = line.split("🆔 আইডি:")[1].strip()
        
        if user_id:
            # শুধু আপনার টেক্সট এবং নিচে ছোট করে টিমের নাম
            bot.send_message(user_id, f"{message.text}\n\n— [𝐓𝐙] 𝐓𝐄𝐀𝐌 💹")
            bot.reply_to(message, "✅ পাঠানো হয়েছে।")
        else:
            bot.reply_to(message, "❌ আইডি পাওয়া যায়নি।")
    except Exception as e:
        bot.reply_to(message, f"❌ সমস্যা: {str(e)}")

# মেসেজ আপনার কাছে পাঠানো
@bot.message_handler(func=lambda message: True)
def forward_to_me(message):
    bot.reply_to(message, "আপনার মেসেজটি মালিকের কাছে পাঠানো হয়েছে। ⏳")
    info = f"📩 নতুন মেসেজ!\n👤 নাম: {message.from_user.first_name}\n🆔 আইডি: {message.from_user.id}\n📝 মেসেজ: {message.text}"
    bot.send_message(MY_ID, info)

# বটটিকে সচল রাখার লুপ
def run_bot():
    print("বট সচল আছে...")
    while True:
        try:
            bot.polling(none_stop=True, interval=0, timeout=40)
        except Exception as e:
            print(f"পুনরায় চালু হচ্ছে: {e}")
            time.sleep(5)

run_bot()
