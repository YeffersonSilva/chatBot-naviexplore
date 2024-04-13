# Navi Explore Bot

Navi Explore Bot es un asistente virtual desarrollado para Telegram que ayuda a turistas y residentes a encontrar los mejores lugares en ciudades de todo el mundo. Este bot es parte del proyecto Navi Esplore, una aplicación móvil que consolida información crucial sobre eventos locales, atracciones, alojamiento, transporte y otros servicios.

## Características

- **Exploración de Atracciones**: Proporciona listados de atracciones turísticas y lugares de interés cerca de la ubicación del usuario.
- **Información de Eventos**: Informa sobre eventos locales próximos, permitiendo a los usuarios planificar su participación.
- **Recomendaciones Personalizadas**: Ofrece recomendaciones basadas en las preferencias y el historial de navegación del usuario.
- **Asistencia de Transporte**: Detalla opciones de transporte disponibles en la ubicación del usuario.
- **Reservas Directas**: Permite a los usuarios hacer reservaciones en hoteles y restaurantes directamente desde el chat.
- **Feedback y Reseñas**: Facilita a los usuarios la opción de dejar comentarios y valoraciones sobre lugares y servicios utilizados.

## Comandos Disponibles

- `/start`: Inicia la interacción con el bot proporcionando una breve descripción de sus funciones.
- `/help`: Muestra todos los comandos disponibles y cómo usarlos.
- `/explore`: Busca atracciones cercanas basadas en la ubicación actual del usuario.
- `/events`: Lista eventos próximos en la zona seleccionada.
- `/book`: Ofrece opciones de reservación para alojamientos y actividades.
- `/feedback`: Permite al usuario dejar comentarios sobre experiencias específicas.
- `/settings`: Acceso a configuraciones del perfil del usuario y preferencias del bot.

## Configuración

Para ejecutar este bot localmente o desplegarlo en un servidor, necesitas seguir estos pasos:

1. Clona el repositorio a tu máquina local o servidor.
2. Asegúrate de tener Python instalado y luego instala las dependencias utilizando:

   ```bash
   pip install pyTelegramBotAPI python-dotenv
# chatBot-naviexplore

## Crea un archivo .env en la raíz del directorio del proyecto y añade tu token de bot de Telegram:
   ```bash

TELEGRAM_TOKEN=your_telegram_bot_token_here
