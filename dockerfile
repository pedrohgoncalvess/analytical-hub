# Use a imagem base do Python
FROM python:3.11

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie todos os arquivos da pasta local para o diretório de trabalho no container
COPY . /app

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que sua aplicação estará ouvindo (ajuste conforme necessário)
EXPOSE 8000

# Comando para executar sua aplicação quando o contêiner for iniciado
CMD ["python", "main.py"]