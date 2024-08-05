import smtplib

MY_EMAIL = "shirgaonkarsaif2786@gmail.com"
PASSWORD = "dugmvsmzlvzajpvx"


class NotificationManager:

    def send_mail(self,emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            for email in emails:
                print(email)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
