# Configurações básicas
DEBUG = False
SECRET_KEY = '5b98ed2a030a8b2cc0c68e4f19a8063e'

# Configuração do diretório estático
STATIC_FOLDER = 'static'

# Configuração do diretório de templates
TEMPLATE_FOLDER = 'templates'


class Config:
    # Configurações de segurança do e-mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'mustaqueestandarjunior@gmail.com'
    MAIL_PASSWORD = 'kexkyfowogynsrmy'
