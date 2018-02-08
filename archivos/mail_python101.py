#!/usr/bin/env python3

import smtplib

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('mail@gmail.com', 'aca_pone_tu_clave_de_gmail')
server.sendmail(
        from_addr='mail@gmail.com',
        to_addrs=[
            'mail_1@gmail.com',
            'mail_2@gmail.com',
            'mail_3@gmail.com',
            'mail_4@gmail.com',
            'mail_5@gmail.com',
            ],
        msg='Hola! Les mando un mail desde Python! xD',
        )
server.close()

