import keys
import summer
import pytextnow
import weather
import quotes

client = pytextnow.Client(
    keys.user,
    sid_cookie=keys.sid,
    csrf_cookie=keys.csrf 
)





def sendmessage():
    
    users = keys.lst
    for i in range(len(users)):
        person = users[i][0]
        fullmess = 'Good morning'
        fullmess = fullmess + ' ' + users[i][1] + ',' + r"\n"*2
        fullmess = fullmess +  'Senior Summer Countdown: ' + summer.getseniordays() + ' days' + r"\n"
        fullmess = fullmess +  'Summer Countdown: ' + summer.getsummerdays() + ' days' +  r"\n"
        for i in range(len(weather.getweather())):
            x = weather.getweather()
            if i == 0:
                fullmess = fullmess + r"\n"*2 + x[0][0][:32] + r"\n"*2
            else:
                fullmess = fullmess  + x[i][0] + x[i][1] + r"\n"
        fullmess = fullmess + r"\n"*2 + quotes.getrandomquote()
        client.send_sms(person, fullmess)

sendmessage()