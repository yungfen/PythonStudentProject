import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "tiffanyliu.contact@gmail.com"
password = "pmcvskjwtyquwfjb"

receiver = "tiff2021any@gmail.com"
context = ssl.create_default_context()

message = """
Hi!
How are you today?
Bye!!!:)"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
