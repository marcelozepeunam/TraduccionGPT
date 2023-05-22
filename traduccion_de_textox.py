#Revisa que no subir a git el archivo .env
import os 
import openai
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("OPENAI_API_KEY")
openai.api_key=api_key

#Funcion que traduce el texto
def traducir_texto(texto, idioma):
    prompt=(f"Traduce el texto '{texto}' al '{idioma}'")
    response=openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1, 
        temperature=0.5,
        max_tokens=100
    )
    return response.choices[0].text.strip()

#Dinámica del programa
mi_texto=input("\nEscribe el texto que deseas traducir: ")
mi_idioma=input("\n¿A qué idioma deseas traducirlo?: ")
traduccion=traducir_texto(mi_texto, mi_idioma)

print(f"\nTraducción: {traduccion}\n")

