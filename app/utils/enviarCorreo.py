import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to_email: str, body: str, subject: str):
    
    #Credenciales para que se pueda enviar el correo
    #Estos datos son el correo de la "empresa"
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    FROM_EMAIL = ""
    PASSWORD = ""
    
    #Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = FROM_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'html')) #'html' permite enlaces
    
    try:
        #Conexion con el servidor SMTP
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls() #activa la seguridad
        server.login(FROM_EMAIL, PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"Correo enviado a {to_email}")
    except Exception as e:
        print(f"Error al enviar correo: {e}")
    