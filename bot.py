import requests

print("WARNING YOU CAN GET BANNED FROM DISCORD USING A SELFBOT USE IT AT YOUR OWN RISK! ") # Line 3 - 5 : Warning alerts
print("")
print("Press Enter if you want to continue")
input("")
print("")
print("Type your Message you want to Spam.")  #Line 8 - 14: Asking for the content
print("")
Message = input("")

payload = {
    'content': Message
}

print("")                 #Line 17 - 24: Asking for the authorization-link
authorizationlinkrequest = """You neeed a authorization-link please paste it in the input.  
(If you don´t know how to get an authorization-link read it on my Github how get it!)"""
print(authorizationlinkrequest)
authorizationlink = input("")

header = {
    'authorization': authorizationlink
}
print("")
print("How many times do you wanna send the message?") # Line 26 - 28: Asking the user how many times he wants to send the message
print("")
send = int(input(""))
print("")
print("Now we only need the request-link (Please also read my Github if you don´t know how get it.) ") #Line 30 - 33 Asking for the request-link
print("")
print("")
requestlink = input("")
print("")
print("LAST WARNING DO YOU REALLY WANT TO RISK YOUR ACCOUNT? ") # Line 35 - 37 the last warning for the user
print("IF YES PRESS ENTER! ")
input("")

for i in range (send):     #Sets how many times the message should be sended
    print("Message send!") #The proof that it was sended
    r = requests.post (requestlink,data = payload, headers=header) #Where the Message will be sended and what content it contains

print("")
print("The bot had send all requested messages. ") #Line 44 - 46 Telling the user that the process was completed and the program can now be closed
print("Press enter to close the Program. ")
input("")
