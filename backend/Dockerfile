# Use a imagem base oficial do Python
FROM python:3.13

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta que o servidor usará
EXPOSE 8000

# Comando para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]