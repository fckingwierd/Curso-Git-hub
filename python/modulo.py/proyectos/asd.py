from twilio.rest import Client

client = Client("AC797717ba16b7be56a0c17f75e30bada0", "8cd2c929f75c3c7bc2596d4f04bda7d3")
from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:543548408310"
client.messages.create(body = "Que onda gay",
                       from_ = from_whatsapp_number,
                       to = to_whatsapp_number)