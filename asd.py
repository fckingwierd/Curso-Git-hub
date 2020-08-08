from twilio.rest import Client

client = Client("AC797717ba16b7be56a0c17f75e30bada0", "280491f399cb15fb04ff90e72bdca645")
from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:+543548408310"
client.messages.create(body = "Que onda gay",
                       from_ = from_whatsapp_number,
                       to = to_whatsapp_number)