import os

API_KEY = os.getenv("API_KEY")


def conectar():
    if API_KEY is None:
        print("No existe API_KEY en el entorno. Por favor, configúralo antes de ejecutar.")
    else:
        print("API_KEY cargada correctamente desde variable de entorno")


if __name__ == "__main__":
    conectar()


# API_KEY = "demo_api_key_no_real_1234567890"

# def conectar():
#     print("Conectando con API usando: ", API_KEY)

# if __name__ == "__main__":
#     conectar()
