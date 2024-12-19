# Keylogger Simples

Este repositório contém um projeto de um keylogger simples, desenvolvido como parte de uma atividade de segurança da informação. O objetivo do projeto é educacional, para demonstrar como funcionam os keyloggers.

## **Aviso Importante**

Este projeto é destinado apenas para fins educacionais e de pesquisa. O uso indevido deste software para atividades maliciosas ou ilegais é estritamente proibido. Os autores não se responsabilizam pelo uso indevido do código.

---

## **Conteúdo do Repositório**

- `src/` : Contém o código-fonte do keylogger e do servidor.
- `demo/keylogger.mp4` : Um vídeo de demonstração que mostra o funcionamento do keylogger.
- `requirements.txt` : Arquivo de dependências do projeto.
- `README.md` : Este arquivo.

---

## **Funcionalidades**

- Captura de teclas digitadas no teclado.
- Armazenamento das teclas capturadas em um arquivo.

---

## **Como Executar**

1. Clone este repositório:
   ```bash
   git clone https://github.com/NatalioLeandro/simple-keylogger.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd simple-keylogger
   ```

3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script do servidor:
   ```bash
   python src/server.py
   ```

5. Execute o script do keylogger:
   ```bash
   python src/keylogger.py
   ```

---

## **Demonstração**

Veja o vídeo de demonstração na pasta `demo/keylogger.mp4` para entender como o keylogger funciona na prática.

---

## **Como Prevenir-se de Keyloggers**

- Utilize um antivírus atualizado.
- Evite baixar programas de fontes não confiáveis.
- Ative a autenticação em dois fatores sempre que possível.
- Monitore regularmente os processos em execução no seu sistema.