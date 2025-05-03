import telebot
from HLTV import HLTV

hltv = HLTV()

class TelegramBot:
    def __init__(self, key):
        self.bot = telebot.TeleBot(key)
        self.registrar_handlers()

    def registrar_handlers(self):
        @self.bot.message_handler(commands=['start'])
        def start(msg):
            self.bot.reply_to(msg, 'Olá fã de Counter Strike! 😁😁')


        @self.bot.message_handler(commands=['help'])
        def help(msg):
            self.bot.reply_to(
                msg,
                'Comandos disponíveis:\n'
                '/start\n/help\n/motivacao\n/jogadores <time>\n/live\n/partidas\n/stats <nickname>\n/news'
            )


        @self.bot.message_handler(commands=['motivacao'])
        def motivacao(msg):
            motivacional = hltv.motivacional()
            self.bot.reply_to(msg, motivacional)


        @self.bot.message_handler(commands=['jogadores'])
        def get_players(msg):
            partes = msg.text.split(maxsplit=1)
            if len(partes) < 2:
                self.bot.reply_to(msg, "Envie o nome do time. Ex: /jogadores FURIA")

            nome_time = partes[1]
            jogadores = hltv.buscar_jogadores_por_time(nome_time)
            if not jogadores:
                self.bot.reply_to(msg, f"Nenhum jogador encontrado para '{nome_time}'.")

            resposta = "\n".join(j['fullname'] for j in jogadores)
            self.bot.reply_to(msg, f"Jogadores do time {nome_time}:\n{resposta}")


        @self.bot.message_handler(commands=['partidas'])
        def obter_partidas(msg):
            partidas = hltv.obter_partidas()
            if not partidas:
                self.bot.reply_to(msg, "Nenhuma partida encontrada.")
                return

            resposta = ""
            for partida in partidas[:5]:
                resposta += (
                    f"🕹️ Evento: {partida['name']}\n"
                    f"🕒 Horário: {partida['time']}\n"
                    f"🗺️ Mapas: {', '.join(partida['maps']) if partida['maps'] else 'Não definido'}\n"
                    f"🔫 {partida['team1']} vs {partida['team2']}\n"
                    f"{'-'*30}\n"
                )
            self.bot.reply_to(msg, resposta)

        @self.bot.message_handler(commands=['stats'])
        def status_jogador(msg):
            partes = msg.text.split(maxsplit=1)
            if len(partes) < 2:
                self.bot.reply_to(msg, "Envie o nickname. Ex: /stats s1mple")
                return

            nome = partes[1]
            stats = hltv.statusJogador(nome)
            if not stats:
                self.bot.reply_to(msg, f"Jogador '{nome}' não encontrado.")
                return

            resposta = (
                f"📊 Estatísticas de {stats['nickname']}:\n"
                f"🧩 Time: {stats['team']}\n"
                f"🔫 K/D: {stats['kd']}\n"
                f"⭐ Rating: {stats['rating']}\n"
                f"🗺️ Mapas jogados: {stats['mapsPlayed']}"
            )
            self.bot.reply_to(msg, resposta)

        @self.bot.message_handler(commands=['live'])
        def partidas_live(msg):
            partidas = hltv.obter_links_partidas_ao_vivo()
            if not partidas:
                self.bot.reply_to(msg, "❌ Nenhuma partida ao vivo.")
                return

            resposta = "🎮 Partidas Ao Vivo:\n\n"
            for p in partidas:
                resposta += f"{p['team1']} 🆚 {p['team2']}\n🔗 {p['link']}\n\n"
            self.bot.reply_to(msg, resposta)

        @self.bot.message_handler(commands=['news'])
        def noticias(msg):
            news = hltv.pegar_noticias_hltv()
            if not news:
                self.bot.reply_to(msg, "Nenhuma notícia no momento.")
                return

            resposta = "📰 Últimas Notícias HLTV:\n\n"
            for item in news[:5]:
                resposta += f"• {item['titulo']}\n🔗 {item['url']}\n\n"
            self.bot.reply_to(msg, resposta.strip())

    def run(self):
        self.bot.infinity_polling()