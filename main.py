# main.py
import preguntas_respuestas as pr

def obtener_respuesta(pregunta):
    # Buscar la pregunta en el diccionario de preguntas
    if pregunta in pr.qa_pairs:
        return pr.qa_pairs[pregunta]
    else:
        # Buscar la pregunta en las variantes de preguntas
        for key, variants in pr.question_variants.items():
            if pregunta in variants:
                return pr.qa_pairs[key]
        return "Lo siento, no tengo una respuesta para esa pregunta."

def chatbot():
    print("¡Hola! Soy el chatbot del ITLA. ¿En qué puedo ayudarte hoy?")
    while True:
        pregunta = input("Tú: ")
        if pregunta.lower() in ["salir", "adios"]:
            print("Chatbot: ¡Hasta luego!")
            break
        respuesta = obtener_respuesta(pregunta)
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    chatbot()

