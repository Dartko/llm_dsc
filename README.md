# llm repositorio
repositorio de trabajo con modelo de lenguaje largo usando ollama

## 1. instalacion de olama

Para instalar ollama accedemos a la pagina de [ollama](https://ollama.com/download/linux), en una terminal se ejecuta el siguiente comando

````bash
curl -fsSL https://ollama.com/install.sh | sh
````
##2. Ejecutar el servidor

una vez instalado se ejecuta el servidor ollama con el siguiente comando

````bash
$ ollama serve
````

##3. Descargar algun modelo

El la pagina de [Modelos](https://ollama.com/library) de ollama se busca el modelo deseado y se descarga con el siguiente comando:

````bash
$ ollama pull tinyllama
````
