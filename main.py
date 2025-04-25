# Torino Financial Advisor Main Entry Point

from dotenv import load_dotenv
# Carrega o arquivo de variáveis de ambiente
load_dotenv()

from web_app.app import run_app

if __name__ == "__main__":
    run_app()