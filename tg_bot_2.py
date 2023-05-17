import logging
from config import *
import random
from aiogram import Bot, Dispatcher, executor, types
import datetime
from mas import *
from JsonTool import JsonTool as jstool
#from aiogram.types import ReplyKeyboardRemove,  ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = api_token

# Configure logging 
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot)
#In several commands original text was replaced on "text" word, becouse other users couldn't understand some jokes, which had written in different commands

@dp.message_handler(commands = ["give_hug"])
async def dive_hug(message: types.Message):
    
    text = message.text.split()
    usname = "@" + message.from_user.username
    if(len(text) < 2):
        await message.reply("text")
    else:
        if(text[1] == usname):
            await message.reply("text")
            # сдесь виден премер переноса текстовой строки 
        else:
            if(text[1] == "@BanMaster228bot"):
                await message.reply("text" + message.from_user.first_name + "!❤️")
            else:
                await message.reply(text[1] + random.choice(hugs) + message.from_user.first_name + "!❤️")


@dp.message_handler(commands = ["agent"])
async def dive_hug(message: types.Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.is_chat_owner() == False and member.is_chat_admin() == False:
        await message.reply("")
    else:    
        t = str(datetime.datetime.now())
        t1 = t.split(" ")
        t2 = t1[1].split(".")
        ebanoje_chicslo= str(datetime.date.today())
        d1 = ebanoje_chicslo.split("-")
        d2 = d1[2] + "." + d1[1] + "." + d1[0]
        dolbojiob = message.reply_to_message.from_user.full_name
        # magshot = await bot.get_user_profile_photos(message.reply_to_message.from_user.id)
        getto = message.chat.title
        await bot.send_message(message.chat.id, "text" + 
        "'" + getto+ "' от " + d2 +  "text" + dolbojiob + "text")
        await bot.send_message(message.chat.id, "text" + getto+ "text")
        # await bot.send_photo(magshot.photos)
        await bot.send_message(message.chat.id, "text" +
       "" + getto+ "'.")
        await bot.send_message(message.chat.id, "text" + t2[0] + " text" +  getto+ "'.")

@dp.message_handler(commands = ['dosuicide'])
async def do_sucide(message: types.Message):
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)
    if member.is_chat_owner() == False:
        await message.reply("text")
    else:
        await bot.send_message(message.chat.id, "/suicide")



   

@dp.message_handler(commands = ["quote"])
async def gold_qoute(message: types.Message):
    sukaaaaa = message.text.split(" ")
    if len(sukaaaaa) > 1:
          if sukaaaaa[1] == 'random': 
                  await message.reply("Зололтая цитата на сегодня:" + "\n" +  random.choice(gold))      
          else : 
                  await message.reply(random.choice(errors))    
    else: 
        await message.reply("Список золотых цитат:" + "\n" + gold[0] + "\n" + gold[1] + "\n" + gold[2] + "\n" + gold[3] +
                         "\n" + gold[4] + "\n" + gold[5] + '\n' + gold[6] + "\n" + gold[7] + "\n" + gold[8]  + "\n" + gold[9])
        


@dp.message_handler(commands = ["givehug"])
async def dive_hug2(message: types.Message):
    usname = "@" + message.from_user.username # Ник того, кто написал
    message_author =  message.from_user.first_name # Имя того, кто написал
    target = "@" + message.reply_to_message.from_user.username # Цель, если ты отвечаешь на сообщение
    if(target == usname):
        await message.reply("text")
    else:
        if(target == "@BanMaster228bot"):
            await message.reply("text" + message_author + "!❤️")
        else:
            await message.reply(target + random.choice(hugs) + message_author + "!❤️")

@dp.message_handler(commands = ["birth"])
async def send_welcome(message: types.Message):
    text = message.text.split()
    date = datetime.date.today()
    d = str(date)
    d1 = d.split("-")
    d2 = d1[2] + "." + d1[1] + "." + d1[0]

    if (len(text) == 2):      
        stname = text[1]
        if(len(text)== 2):
           for c, birth in names.items():
               if(birth[stname] == d2):
                   await message.reply("text" + stname + " - " + birth[stname] + "\n" + "text")  
               else:
                   await message.reply("text" + stname + " - " + birth[stname])
    else: 
        await message.reply(random.choice(errors) + "\n" + "text") 

@dp.message_handler(commands = ["execute_order_66"])
async def ban_user(message: types.Message):
    f = open("linksworking.txt", "rt")
    author = await bot.get_chat_member(message.chat.id, message.from_user.id)
    data = f.readlines()
    members = await bot.get_chat_members_count(message.chat.id) 
    admins = await bot.get_chat_administrators(message.chat.id)

    jedi = members - len(admins)

    if author.is_chat_owner() == True:
       if( jedi > 0): 
           await bot.send_photo(message.chat.id, data[18], "That's right, my lord!" + "\n" + "Cout of jedi to kill = " + str(jedi))
       else:
           await bot.send_photo(message.chat.id, data[18], "That's right, my lord!" + "\n" + "Here are no jedies to kill ")  
       for i in range(19,len(admins)):
              await bot.send_message(message.chat.id, str(admins[i]))
    else:
        await bot.send_message(message.chat.id, "text")

# {"user": {"id": 978060088, "is_bot": false, "first_name": "Игорь", "last_name": "Князь", "username": "OlympForGods", "language_code": "en"}, 
# "status": "creator", "custom_title": "Botik", "is_anonymous": false, "can_manage_chat": true, "can_post_messages": true, "can_edit_messages": true, 
# "can_delete_messages": true, "can_manage_voice_chats": true, "can_manage_video_chats": true, 
# "can_restrict_members": true, "can_promote_members": true, "can_change_info": true, "can_invite_users": true, "can_pin_messages": true}              

@dp.message_handler(commands = ["date"])
async def send_welcome(message: types.Message):
    # text = message.text.split()
    d1 = str(datetime.date.today()).split("-")
    d2 = d1[2] + "." + d1[1] + "." + d1[0]
    t = str(datetime.datetime.now())
    t1 = t.split(" ")
    t2 = t1[1].split(".")
    await message.reply("Current date - " + d2 + "\n" + "Current time - " + t2[0])

@dp.message_handler(commands = ["stufiness"])
async def stuffiness(message: types.Message): 
    a = random.random()
    e = a/7
    b = a*5
    if(b > 1):
        c = b - 1
        d = b- c
    name = message.from_user.first_name
    if(name == "D" or name == "R"):
       if(name == "D"):
            if(d == 1):
                await message.reply(name +  "text")
            else:
                await message.reply(name +  "text" + "%.5f" % d +  "text")
       if(name == "R"):
           await message.reply(name +  "text" + "%.5f" % e)
    else:
       if (a == 1):
           await message.reply("text " + name + "text" + "[" + name + "]" + "😘😘😘")
       elif(a >= 0.8 and a < 1):
           await message.reply(name + "text" + "%.5f" % a + "text" + "👍👍👍")
       elif(a == 0):
           await message.reply(name + "text")
       elif(a > 0 and a < 0.3):
           await message.reply(name + "text" +  "%.5f" % a +  "text")
       elif(a >= 0.3 and a < 0.5):
           await message.reply(name + "text" + "%.5f" % a +   "text")
       elif(a >= 0.5 and a < 0.8):
           await message.reply(name + "text" +  "%.5f" % a +  "text")
    

@dp.message_handler(commands = ["toxicity"])
async def toxicity(message : types.Message): 
    a = random.randint(0, 100)
    name = message.from_user.full_name
    # await message.reply(message.chat.id, message.reply_to_message.from_user.id,  "Токсичность человека по имени " + message.reply_to_message.from_user.first_name + " = " + str(a) + "%")
    if(a > 80 and a < 90):
        await message.reply(name + "text " + str(a) + "text" + "👺👍👍👍")
    elif (a >= 90 and a < 100):
        await message.reply("text "+ name + "text"  + str(a) + "%"+ "👻👻👻👻🥳")
    elif ( a == 100):
        await message.reply(name + "text" + str(a) + "text" + message.from_user.first_name + "text" + "👑👑👑")
    elif ( a >= 90 and name == "text"):
        await message.reply(name + "text" +str(a) + "text")
    elif ( a < 30 and a > 0):
        await message.reply(name + "text" + str(a) + "%" + "text" + "😈😈😈")
    elif (a == 0): 
        await message.reply(name + "text" + "👎👎👎")
    elif (a > 60 and a <= 80):
        await message.reply(name + "text " + str(a) + "%"  + "\n"+ "text")
    elif(a >= 30 and a <= 60):
        await message.reply(name + "text" + str(a) + "text" + "👌👌👌")
    
       

@dp.message_handler(commands = ["write"])
async def simpleFunction(message: types.Message):
    js = jstool("birthfays")
    print("-------------")
    print(js.database)
    js.database[message.from_user.id] = message.get_args()
    js.save()

@dp.message_handler(commands = ["compatibility"])
async def simpleFunction(message: types.Message):
    name = message.from_user.first_name
    text = message.text.split()
    i = 0
    second = text[i+1]
    a = random.randint(0, 100)
    if(len(text) <= 3):
        if (a ==0):
           await message.reply(name + "text" + second + "text " + str(a) + "%" + "\n" + "text")
        else:
            await message.reply(name + "text " + second + "text" + str(a) + "%")
    if(len(text)> 3):
        if (a ==0):
           await message.reply(name + "text" + second + "text" + str(a) + "%" + "\n" + "text")
        else:
            await message.reply(name + "text " + second + "text" + str(a) + "%")
        

@dp.message_handler(commands=['ban'])
async def kick_user(message: types.Message):
        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        message_author = await bot.get_chat_member(message.chat.id, message.reply_to_message.from_user.id);
    # if member.is_chat_owner() == False:
    #     await message.reply("Команда закрыта на доработку и переработку")
    # else:
    #    if member.is_chat_owner() == False and member.is_chat_admin() == False:
    #       await message.reply("Пашёл нахуй, у тебя нет прав)))")
        if (member.is_chat_owner() == False and member.is_chat_admin() == False and message_author.is_chat_owner() == True) or (member.is_chat_owner() == False and member.is_chat_admin() == False and message_author.is_chat_admin() == True): # Если создателя или пробует банить плебей
           await message.reply("@" + message.reply_to_message.from_user.username + "text" + message.from_user.username)
        elif member.is_chat_owner() == True and message_author.is_chat_admin() == True: # Если создатель хочет забанить админа
            await message.reply(f"@{message.reply_to_message.from_user.username}, text")
        elif member.is_chat_owner() == False and message_author.is_chat_owner() == True: # Если создателя пробует банить админ
           await message.reply("@" + message.reply_to_message.from_user.username + "text" + message.from_user.username + "!")
        elif member.is_chat_admin() == True and message_author.is_chat_admin() == True: # Если админ покушается на админа
           if(message_author == 'BanMaster228'):
               await message.reply("@" + message.from_user.username + "text")
           else:
               await message.reply("@" + message.from_user.username + "text" + message.reply_to_message.from_user.username + "text")
        else:
            await message.reply("@" + message.reply_to_message.from_user.username + "text" + message.from_user.username)
            await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
       #await bot.send_message(message.reply_to_message.from_user.id,"https://t.me/+kW9tI6kAKfBhYjJk")

@dp.message_handler(commands = ['kanye'])
async def send_welcome(message: types.Message):
        f = open("linksworking.txt", "rt")
        data = f.readlines()
        await bot.send_photo(message.chat.id, random.choice(data))

@dp.message_handler(commands = ['command1'])
async def simpleFunction(message: types.Message):
    text = message.text.split()
    i = 1
    us ="@"+ message.from_user.username
    us2 = message.from_user.full_name.split()
    if(len(text) <= 1):
        await message.reply("Вtext")
    elif(text[i] == us):
        await message.reply("text")
    elif(text[i] == "text"):
        await message.reply("text")
    else:
        await message.reply(us2[0] + "text" + text[i])

@dp.message_handler(commands = ["mom"])
async def simpleFunction(message: types.Message):
    text = message.text.split()
    i = 0
    if(len(text) == 2):
        await message.reply("Мать " + text[i+1] + random.choice(mom) + "\n" + "text")
    else:
        await message.reply(random.choice(errors) + "\n" + "text")

@dp.message_handler(commands = ["mobilization"])
async def kick_user(message: types.Message):
    a =  random.randint(0, 100)
    if(a > 90):
         await message.reply("text" + str(a)  + "%😍" + "\n" 
         + "text")
    elif( a < 30):
        await message.reply("text" + str(a)  + "%😍" + "\n" 
         + "text")
    else:
        await message.reply("text" + str(a)  + "%😍" + "\n" 
         + "text")


@dp.message_handler(commands = ["wakeupneo"])
async def simpleFunction(message: types.Message):
    f = open("linksworking.txt", "rt")
    data = f.readlines()
    a = data[17]
    await bot.send_photo(message.chat.id, a,  "text")


@dp.message_handler(commands = ["kill"])
async def simpleFunction(message: types.Message):
    text = message.text.split()
    if(text[1] == "@BanMaster228bot"):
        await message.reply("text")
    else:
        await message.reply(text[1] + "\t" + random.choice(deaths)) #message.chat.id,

@dp.message_handler(commands = ["suicide"])
async def simpleFunction(message: types.Message):
     text = message.from_user.full_name.split()
     name = text[0]
     await message.reply( name + "\t" + random.choice(suicide))

@dp.message_handler(commands = ["wedding"])
async def simpleFunction(message: types.Message):
    text = message.text.split()
    i = 1
    if(text[i+1] == "и" or text[i+1] == "and"or text[i+1] == "+"):
        if(text[i] == text[i + 2]):
             await message.reply("text") 
        else: 
             await message.reply(text[i] + " и "  + text[i + 2]  + "text" + "\n" + random.choice(wedding))
    else:
         await message.reply(random.choice(errors))
    
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):     
    await message.reply(random.choice(replays))

@dp.message_handler(commands=['R'])
async def send_welcome(message: types.Message):    
    a = random.randint(0, 1000)
    if(a < 100):
        await message.reply("text" + str(a) + "Ω" + "\n" 
        +"text")
    if(a > 850):
        await message.reply("text" + str(a) + "Ω" + "\n" 
        +"text")
    elif(a >= 100 and a <= 850):
         await message.reply("text " + str(a) + "Ω")
    
@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):    
    await message.reply(random.choice(help))

@dp.message_handler(commands=['hromosom'])
async def send_welcome(message: types.Message):
    text = message.from_user.first_name
    a = random.randint(46,47) 
    if(text == "Kiruhwa"):
        await bot.send_photo(message.chat.id, open("daun.jpg", "rb"))
        await message.reply("text" + "\t" + "text")
    else:
        if( a == 47):
            await bot.send_photo(message.chat.id, open("daun.jpg", "rb"))
            await message.reply("text" + "\t" + "text")
        elif(a == 46):
            await message.reply("text" + "\n" + "text")



@dp.message_handler(commands=['size'])
async def kick_user(message: types.Message):
    a = random.randint(0, 163)
    if(message.from_user.username == "OlympForGods"):
        b = random.randint(150, 178)
        await message.reply(f"text " + str(b) + "см" + "\n" + "text")
    else:
      if ( a == 0):
          await message.reply(f"text")
      if (a > 140 and  a < 163):
          await message.reply(f"text" + str(a) + "см" + "\n" + "text")
      elif(a > 0 and a < 15):
          await message.reply(f"text " + str(a) + "см" + "\n" + "text")
      elif ( a >= 15 and a <= 30):
          await message.reply(f"text" + str(a) + "см" + "\n" + "text")
      elif ( a > 30 and a <= 60):
          await message.reply(f"text " + str(a) + "см" + "\n" + "text")
      elif ( a > 60 and a <= 99):
          await message.reply(f"text " + str(a) + "см" + "\n" + "text")
      elif ( a > 99 and a <= 140):
          await message.reply(f"Тtext" + str(a) + "см" + "\n" + "text")
      elif(a == 163):
          await message.reply(f"text" + str(a) + "см" + "\n" + "text")


@dp.message_handler(commands=['iq'])
async def kick_user(message: types.Message):   
     a = random.randint(0,200)
     if(a == 7):
        await message.reply(f"text" + str(a) + "\n" + "text")
     if(a == 37):
        await bot.send_photo(message.chat.id, open("IQ.jpeg", "rb"))
     if( a == 0):
        await message.reply(f"Ваш iq = " + str(a))
     if(a == 173):
        b = a*2
        await message.reply(f"Ваш iq = " + str(b)  + "text" + "\n" + "text!")
     elif(a > 0 and  a < 7):
        await message.reply(f"Твой iq = " + str(a) + "\n" + "Пtext")
     elif(a > 7 and a < 37):
        await message.reply(f"Твой iq = " + str(a) + "\n" + "text")
     elif(a > 37 and a < 50):
        await message.reply(f"Твой iq = " + str(a) + "\n" + "text")
     elif(a >= 50 and a <= 190):
        await message.reply(f"Твой iq = " + str(a))
     elif(a > 190):
        await message.reply(f"Твой IQ = " + str(a) + "\n" + "text")


@dp.message_handler(commands = ["announce"])
async def one_hundred(message: types.Message):
      member = await bot.get_chat_member(message.chat.id, message.from_user.id)
      print(member.is_chat_owner())
      if member.is_chat_creator() == True:
         await bot.send_photo(message.chat.id, open("ass.jpg", "rb"))
         await bot.send_message(message.chat.id, f'❤️❤️❤️')
      else: 
         await bot.send_message(message.chat.id, "a")
     

@dp.message_handler(content_types=types.ContentTypes.NEW_CHAT_MEMBERS)
async def new_member_member(message: types.Message):
    user = message.new_chat_members[0]
    await bot.send_photo(message.chat.id, open("helloFace.jpg", "rb"))
    if (user.username is None):
        await bot.send_message(message.chat.id, 
        f'{user.full_name} , от лица нашей компании "{message.chat.title}" ')
    else:   
        await bot.send_message(message.chat.id, 
        f'@{user.username} , text"{message.chat.title}"text')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
