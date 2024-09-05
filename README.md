# llm repositorio
repositorio de trabajo con modelo de lenguaje largo usando ollama

## 1. instalacion de olama

Para instalar ollama accedemos a la pagina de [ollama](https://ollama.com/download/linux), en una terminal se ejecuta el siguiente comando

````bash
curl -fsSL https://ollama.com/install.sh | sh
````
## 2. Ejecutar el servidor

una vez instalado se ejecuta el servidor ollama con el siguiente comando

````bash
$ ollama serve
````

## 3. Descargar algun modelo

El la pagina de [Modelos](https://ollama.com/library) de ollama se busca el modelo deseado y se descarga con el siguiente comando:

````bash
$ ollama pull tinyllama
````
## 4. Prueba de request a la api rest

Para realizar una peticion basica a la API de ollama se sigue la siguiente estructura

````bash
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?"
}'
````
## 4.1 Prueba de Request a la API de OLLAMA, sin streaming

````bash
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
````
## Comandos
````bash
git add .
git commit -m "Update README.md"
git push -u origin main
````
````curl
"https://api.groq.com
````
## 6. Request a groq
````bash
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${GROQ_API_KEY}" \
  -d '{
         "messages": [
           {
             "role": "user",
             "content": "¿Porque el cielo es azul?"
           }
         ],
         "model": "gemma-7b-it",
         "stream": false
       }'
````
````bash
python3 -m http.server 8080
salvadorhm@utectulancingo.edu.mx
salvadorhm@gmail.com
````