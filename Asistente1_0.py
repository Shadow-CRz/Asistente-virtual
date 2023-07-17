import speech_recognition as sr
import pyttsx3
import pywhatkit

# Configuración del reconocimiento de voz
r = sr.Recognizer()
mic = sr.Microphone()

# Configuración del motor de síntesis de voz
engine = pyttsx3.init()

# Variable para indicar si la asistente está en ejecución o detenida
running = True

# Función para que la asistente responda
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Función para escuchar y procesar comandos de voz
def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source)  # Ajusta el nivel de ruido del micrófono
        audio = r.listen(source)

    try:
        # Reconocimiento de voz utilizando el motor de reconocimiento de voz
        query = r.recognize_google(audio, language="es-ES")
        print("Escuchado: ", query)
        return query
    except sr.UnknownValueError:
        print("No se pudo entender el comando de voz.")
    except sr.RequestError:
        print("Error al conectarse al servicio de reconocimiento de voz.")
    return ""

# Función para procesar los comandos de voz
def process_command(command):
    global running
    command = command.lower()

    if "hola" in command:
        speak("¡Hola! ¿En qué puedo ayudarte?")
    elif "adiós" in command:
        speak("¡Hasta luego!")
        running = False  # Detiene la ejecución de la asistente
    elif "reproduce" in command:
        music= command.replace('reproduce', '')
        speak("Reproduciendo " + music)
        pywhatkit.playonyt(music)
        # Lógica para reproducir música
    elif "buscar en internet" in command:
        speak("¿Qué quieres buscar?")
        search_query = listen()
        speak("Buscando en internet: " + search_query)
        # Lógica para buscar en internet
    else:
        speak("No entendí ese comando.")

# Ciclo principal
while running:
    speak("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")
    command = listen()
    process_command(command)
