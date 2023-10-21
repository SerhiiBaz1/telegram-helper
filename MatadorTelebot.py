import telebot
import json
from  telebot import types


bot = telebot.TeleBot('YOUR-TOKEN')


#admin--------------------
@bot.message_handler()
def start(message):
    if message.text.lower() == 'start':
        markup = types.ReplyKeyboardMarkup()
        sts = types.KeyboardButton('Менеджер')
        stss = types.KeyboardButton('Директор')
        markup.row(sts,stss)
        bot.send_message(message.chat.id, 'хто ви?')
    elif message.text.lower() == 'менеджер' or message.text.lower() == 'назад':

        markup = types.ReplyKeyboardMarkup()
        sts = types.KeyboardButton('Керування номерами')
        markup.row(sts)
        bot.send_message(message.chat.id, 'Доброго дня', reply_markup=markup)

    elif message.text.lower() == 'керування номерами':
        markup1 = types.ReplyKeyboardMarkup()
        cim1 = types.KeyboardButton('1')
        cim2 = types.KeyboardButton('2')
        markup1.row(cim1,cim2)
        cim3 = types.KeyboardButton('3')
        cim4 = types.KeyboardButton('4')
        markup1.row(cim3,cim4)
        cim5 = types.KeyboardButton('5')
        cim6 = types.KeyboardButton('6')
        markup1.row(cim5,cim6)
        back = types.KeyboardButton('Назад')
        markup1.row(back)
        bot.send_message(message.chat.id, 'Номера',reply_markup=markup1)


    elif message.text.lower() == '1':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('1)Зайнятий 🔴')

        b = types.KeyboardButton('1)Броньований 🟠')

        f = types.KeyboardButton('1)Свобідний 🟢')

        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim1 = data.get("cim1")
        if key_cim1 == 'free':
            a = '<b>Вільний 🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є ' + a, reply_markup=markup2,parse_mode='html')



    elif message.text.lower() == '1)зайнятий 🔴':
        with open('data.json','r') as file:
            data = json.load(file)
        data["cim1"] = 'live'
        with open('data.json','w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '1)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim1"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '1)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim1"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')


    elif message.text.lower() == '2':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('2)Зайнятий 🔴')

        b = types.KeyboardButton('2)Броньований 🟠')

        f = types.KeyboardButton('2)Свобідний 🟢')
        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim2 = data.get("cim2")
        if key_cim2 == 'free':
            a = '<b>Вільний🟢</b>'
        elif key_cim2 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim2 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є ' + a, reply_markup=markup2,parse_mode='html')



    elif message.text.lower() == '2)зайнятий 🔴':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim1"] = 'live'
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '2)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim2"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '2)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim2"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')

    elif message.text.lower() == '3':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('3)Зайнятий 🔴')

        b = types.KeyboardButton('3)Броньований 🟠')

        f = types.KeyboardButton('3)Свобідний 🟢')
        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim3 = data.get("cim3")
        if key_cim3 == 'free':
            a = '<b>Вільний 🟢</b>'
        elif key_cim3 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim3 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є...' + a, reply_markup=markup2, parse_mode='html')



    elif message.text.lower() == '3)зайнятий 🔴':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim1"] = 'live'
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '3)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim3"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '3)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim3"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')


    elif message.text.lower() == '4':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('4)Зайнятий 🔴')

        b = types.KeyboardButton('4)Броньований 🟠')

        f = types.KeyboardButton('4)Свобідний 🟢')

        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim1 = data.get("cim4")
        if key_cim1 == 'free':
            a = '<b>Вільний 🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є ' + a, reply_markup=markup2,parse_mode='html')



    elif message.text.lower() == '4)зайнятий 🔴':
        with open('data.json','r') as file:
            data = json.load(file)
        data["cim4"] = 'live'
        with open('data.json','w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '4)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim4"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '4)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim4"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')






    elif message.text.lower() == '5':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('5)Зайнятий 🔴')

        b = types.KeyboardButton('5)Броньований 🟠')

        f = types.KeyboardButton('5)Свобідний 🟢')

        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim1 = data.get("cim5")
        if key_cim1 == 'free':
            a = '<b>Вільний 🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є ' + a, reply_markup=markup2,parse_mode='html')



    elif message.text.lower() == '5)зайнятий 🔴':
        with open('data.json','r') as file:
            data = json.load(file)
        data["cim5"] = 'live'
        with open('data.json','w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '5)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim5"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '5)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim5"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')


    elif message.text.lower() == '6':
        markup2 = types.ReplyKeyboardMarkup()
        y = types.KeyboardButton('6)Зайнятий 🔴')

        b = types.KeyboardButton('6)Броньований 🟠')

        f = types.KeyboardButton('6)Свобідний 🟢')
        markup2.row(y, b, f)
        back = types.KeyboardButton('Назад')
        markup2.row(back)
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim2 = data.get("cim6")
        if key_cim2 == 'free':
            a = '<b>Вільний🟢</b>'
        elif key_cim2 == 'reserv':
            a = '<b>Броньований 🟠</b>'
        elif key_cim2 == 'live':
            a = '<b>Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, 'Номер є ' + a, reply_markup=markup2,parse_mode='html')



    elif message.text.lower() == '6)зайнятий 🔴':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim6"] = 'live'
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '6)броньований 🟠':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim6"] = "reserv"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')



    elif message.text.lower() == '6)свобідний 🟢':
        with open('data.json', 'r') as file:
            data = json.load(file)
        data["cim6"] = "free"
        with open('data.json', 'w') as file:
            json.dump(data, file)
        bot.send_message(message.chat.id, 'все готово')













    if message.text.lower() == 'директор':
        markup4 = types.ReplyKeyboardMarkup()
        sts = types.KeyboardButton('статус номерів')
        markup4.row(sts)
        bot.send_message(message.chat.id, 'Доброго дня', reply_markup=markup4)

    elif message.text.lower() == 'статус номерів':
        with open('data.json', 'r') as file:
            data = json.load(file)
        key_cim1 = data.get("cim1")
        if key_cim1 == 'free':
            a = '<b>Номер 1 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 1 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 1 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a ,parse_mode='html')
        key_cim1 = data.get("cim2")
        if key_cim1 == 'free':
            a = '<b>Номер 2 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 2 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 2 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a,parse_mode='html')
        key_cim1 = data.get("cim3")
        if key_cim1 == 'free':
            a = '<b>Номер 3 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 3 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 3 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a,parse_mode='html')
        key_cim1 = data.get("cim4") 
        if key_cim1 == 'free':
            a = '<b>Номер 4 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 4 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 4 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a, parse_mode='html')
        key_cim1 = data.get("cim5")
        if key_cim1 == 'free':
            a = '<b>Номер 5 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 5 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 5 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a, parse_mode='html')
        key_cim1 = data.get("cim6")
        if key_cim1 == 'free':
            a = '<b>Номер 6 - Вільний🟢</b>'
        elif key_cim1 == 'reserv':
            a = '<b>Номер 6 - Броньований🟠</b>'
        elif key_cim1 == 'live':
            a = '<b>Номер 6 - Зайнятий 🔴</b>'
        bot.send_message(message.chat.id, a, parse_mode='html')






bot.polling(none_stop=True)


