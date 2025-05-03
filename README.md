# HLTV CS Bot 🇧🇷

Um bot de Telegram que integra informações do HLTV.org para fãs de Counter-Strike (CS:GO / CS2), com comandos para visualizar partidas ao vivo, estatísticas de jogadores, line-ups, e notícias atualizadas do cenário competitivo.

## 🚀 Funcionalidades

- 🔴 **/live** — Mostra partidas ao vivo com link direto.
- 📅 **/partidas** — Exibe os próximos confrontos com horário, mapas e times.
- 📊 **/stats `<jogador>`** — Retorna estatísticas de um jogador específico.
- 🧑‍🤝‍🧑 **/jogadores `<time>`** — Lista os jogadores de um determinado time.
- 📰 **/news** — Mostra as últimas notícias publicadas no HLTV.
- 🔥 **/motivacao** — Envia uma frase motivacional aleatória (estilo CS).
- 🆘 **/help** — Exibe todos os comandos disponíveis.
- 👋 **/start** — Saudação inicial.

## 🧠 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)
- [Telebot (pyTelegramBotAPI)](https://github.com/eternnoir/pyTelegramBotAPI)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [cloudscraper](https://pypi.org/project/cloudscraper/)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Para leitura da chave via `.env`.

## 📦 Instalação

1. Clone o repositório:

```
git clone https://github.com/Matthews1337/TelegramCSChatBot.git
```
cd TelegramCSChatBot

2. Instalação dos requisitos
```
pip install -r requirements.txt
```
## ⚙️ Utilização

1. Crie um novo bot no [BotFather](https://t.me/BotFather) no Telegram.
2. Copie o token de acesso fornecido após a criação do bot.
3. Crie um arquivo `.env` na raiz do projeto e adicione a seguinte linha: TOKEN={SEU TOKEN}
4. Execute o bot com:
```bash
python main.py
```
