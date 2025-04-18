import asyncio
from telethon import TelegramClient, events
from datetime import datetime, time
import pytz
import random

# === НАСТРОЙКИ ===
api_id = 26001916
api_hash = "f5f3ca85723b9d0ba365720e6aff1e67"
session_name = 'my_session'

# ID груп, юзернейми
TARGET_GROUPS = [
    # '💸 ЗАВДАННЯ 💸',
    'PRchatUkraine12',
    'piarr_chat_ukr',
    'doskaogolosh',
    'Ogoloshenya6996',
    'doshka_ua1',
    # 'PR_chat_Ukraine',
]

FORWARD_CHANNEL_ID = 2409928631 # або 4707019211  # Канал для пересилки відповідей (Завдання)
MESSAGES = [
"""
🔔 *Шукаєш якісну накрутку?* Маємо рішення 💼

✅ Жива українська аудиторія  
✅ Швидке виконання  
✅ Помірні ціни  
✅ Перевірено часом і відгуками!

🎯 Послуги:
- Підписки  
- Лайки  
- Коментарі  
- Перегляди  
- Репости  
- Реферали  

📌 Платформи:
Telegram • Instagram • TikTok • Facebook • YouTube • Viber

📬 Пиши 👉 @neksiix — домовимось швидко 😉
""",
    """
🔥 Хей! Є тема для просування акаунтів 😎

🎯 Живі українські користувачі  
🕐 Швидко  
📈 Ефективно  
💸 Недорого  

Наші послуги:
📌 Підписки | Лайки | Коментарі  
👁 Перегляди | Репости | Реферали  

Працюємо з:
📲 Telegram • TikTok • Instagram • YouTube • Viber • Facebook

👉 Пиши в дірект @neksiix  
""",
    """
💬 Друзі, якщо вам потрібно просування — звертайтесь!

🔹 Жива українська аудиторія  
🔹 Працюємо швидко та якісно  
🔹 Є багато задоволених клієнтів і чесних відгуків

📌 Пропоную:
1 Підписник - 1.4 грн
1 Лайк - 1 грн
1 Коментар - 1 грн
- інші послуги в діректі 

📱 Платформи: Telegram, Instagram, TikTok, YouTube, Facebook, Viber

📩 Якщо цікаво — пишіть мені @neksiix  
"""
]

TIMES = [
    time(8, 0), time(9, 30), time(10, 45),
    time(11, 30), time(12, 30), time(13, 30),
    time(14, 10), time(14, 55), time(15, 45),
    time(16, 30), time(17, 0), time(18, 0), time(19, 0)
]

TIMEZONE = pytz.timezone("Europe/Kyiv")

client = TelegramClient(session_name, api_id, api_hash)

# Збереження ID надісланих повідомлень для перевірки відповіді
sent_message_ids = set()


@client.on(events.NewMessage(incoming=True))
async def handler(event):
    # Перевіряємо, чи повідомлення є відповіддю
    if event.is_private or not event.is_reply:
        return

    try:
        original = await event.get_reply_message()

        # Якщо немає оригінального повідомлення — нічого не робимо
        if original is None:
            return

        if original.id in sent_message_ids:
            await client.send_message(
                FORWARD_CHANNEL_ID,
                f"✉️ Відповідь у {event.chat.title}:\n\n{event.message.message}"
            )
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 📩 Відповідь переслано з {event.chat.title}")
    except Exception as e:
        print(f"❌ Помилка при обробці відповіді: {e}")

async def send_scheduled_messages():
    print("Бот запущений і чекає на час розсилки...")
    while True:
        now = datetime.now(TIMEZONE).time()
        for target_time in TIMES:
            if now.hour == target_time.hour and now.minute == target_time.minute:
                message = random.choice(MESSAGES)
                for group_username in TARGET_GROUPS:
                    try:
                        group = await client.get_entity(group_username)
                        sent = await client.send_message(group, message, parse_mode="markdown")
                        sent_message_ids.add(sent.id)
                        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ✅ Надіслано до {group_username}")
                    except Exception as e:
                        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ❌ Помилка в {group_username}: {e}")
                    await asyncio.sleep(5)
                await asyncio.sleep(60)
        await asyncio.sleep(10)

async def main():
    await client.start()
    await asyncio.gather(
        send_scheduled_messages(),
        client.run_until_disconnected()
    )

if __name__ == '__main__':
    asyncio.run(main())














# import asyncio
# from telethon import TelegramClient
# from datetime import datetime, time
# import pytz
# import logging

# # === НАСТРОЙКИ ===
# api_id = 26001916
# api_hash = "f5f3ca85723b9d0ba365720e6aff1e67"
# session_name = 'my_session'

# # ID або юзернейми груп
# TARGET_GROUPS = [
#     'tiktokchatics',
#     'tiktokuachat',
#     'tiktok_aktiv2022',
#     'Tiktok_akt',
#     'chatP1arr',
#     'piaruacah',
#     'piarchatuya',
# ]

# MESSAGE_TEXT = """
# Вітаю! Пропоную свої послуги накрутки живою українською аудиторією 😎
# Підписки, лайки, коментарі, перегляди, репости, реферали - все це швидко та якісно. 
# Багато задоволених клієнтів вже оцінили наші послуги. 
# Ціни не кусаються, є багато відгуків!
# Виконуємо на такі соцмережі: 
# - Telegram 
# - Instagram 
# - tikTok 
# - viber
# - facebook
# - youTube 
# Пишіть @neksiix хто зацікавлений!
# """

# TIMES = [
#     time(8, 0), time(9, 30), time(11, 0),
#     time(12, 30), time(14, 0), time(16, 0), 
#     time(17, 0), time(18, 30), time(20, 0)
# ]

# TIMEZONE = pytz.timezone("Europe/Kyiv")

# # === ЛОГУВАННЯ ===
# logging.basicConfig(
#     filename='log.txt',
#     level=logging.INFO,
#     format='[%(asctime)s] %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )

# client = TelegramClient(session_name, api_id, api_hash)

# async def send_scheduled_messages():
#     print("Бот запущен і чекає часу...")
#     while True:
#         now = datetime.now(TIMEZONE).time()
#         for target_time in TIMES:
#             if now.hour == target_time.hour and now.minute == target_time.minute:
#                 for group in TARGET_GROUPS:
#                     try:
#                         await client.send_message(group, MESSAGE_TEXT)
#                         msg = f"✅ Успішно надіслано в {group}"
#                         print(msg)
#                         logging.info(msg)
#                     except Exception as e:
#                         err = f"❌ Помилка при надсиланні в {group}: {e}"
#                         print(err)
#                         logging.error(err)
#                 await asyncio.sleep(60)  # щоб не задублювати
#         await asyncio.sleep(10)

# async def main():
#     await client.start()
#     await send_scheduled_messages()

# if __name__ == '__main__':
#     asyncio.run(main())
