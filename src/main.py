import telebot
from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener el token desde las variables de entorno
TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)

# Comando de bienvenida
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hola, Este bot es sobre la web Navi Esplore, Software, que te ayudará encontrar mejores lugares en las ciudades del mundo.")

# Comando de ayuda general
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = ("Comandos disponibles:\n"
                 "/start - Bienvenida y descripción del bot.\n"
                 "/get_started - Guía para comenzar a usar la app.\n"
                 "/using_maps - Cómo usar los mapas en la app.\n"
                 "/finding_events - Cómo encontrar eventos.\n"
                 "/booking_tips - Consejos para hacer reservaciones.\n"
                 "/feedback_howto - Cómo dejar feedback en la app.\n"
                 "/profile_settings - Cómo configurar tu perfil.")
    bot.reply_to(message, help_text)

# Comandos específicos para funciones de la app
@bot.message_handler(commands=['get_started', 'using_maps', 'finding_events', 'booking_tips', 'feedback_howto', 'profile_settings'])
def send_specific_help(message):
    if message.text == '/get_started':
        response = ("Bienvenido a Navi Esplore! Aquí te explicamos cómo empezar:\n"
                    "1. Crea tu perfil.\n"
                    "2. Selecciona tus intereses para recibir recomendaciones personalizadas.\n"
                    "3. Usa el mapa interactivo para ver puntos de interés.\n"
                    "4. Accede al calendario de eventos para no perderte nada.\n"
                    "Si necesitas más ayuda, usa el comando /help.")
    elif message.text == '/using_maps':
        response = ("Usar los mapas en Navi Esplore es fácil:\n"
                    "• Zoom in/out para ver más o menos detalle.\n"
                    "• Toca los iconos en el mapa para obtener información de lugares.\n"
                    "• Usa la búsqueda para encontrar lugares específicos.")
    elif message.text == '/finding_events':
        response = ("Encontrar eventos en Navi Esplore:\n"
                    "• Ve a la sección 'Eventos' en el menú.\n"
                    "• Puedes buscar eventos por fecha o categoría.\n"
                    "• Inscríbete o guarda eventos de tu interés.")
    elif message.text == '/booking_tips':
        response = ("Hacer reservaciones con Navi Esplore:\n"
                    "• Accede a la sección de 'Reservaciones'.\n"
                    "• Elige hoteles o actividades y selecciona tus fechas.\n"
                    "• Sigue los pasos para confirmar tu reserva.")
    elif message.text == '/feedback_howto':
        response = ("Dejar feedback en Navi Esplore es importante:\n"
                    "• Ve a la sección 'Feedback'.\n"
                    "• Elige 'Dejar reseña' para compartir tu experiencia sobre un lugar o servicio.\n"
                    "• Tu opinión ayudará a otros usuarios y a mejorar la app.")
    elif message.text == '/profile_settings':
        response = ("Configurar tu perfil en Navi Esplore:\n"
                    "• En el menú, selecciona 'Mi Perfil'.\n"
                    "• Aquí puedes editar tu información personal, cambiar tu foto, y ajustar tus preferencias.")
    bot.reply_to(message, response)

# Manejador genérico para cualquier otro mensaje
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True)
