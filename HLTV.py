import requests
import cloudscraper
import random
from bs4 import BeautifulSoup

class HLTV:
    def __init__(self):
        pass

    def __fetch(self,url = None):
        url = url
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()  
            # print((data))
        else:
            print(f"Erro ao fazer requisição: {response.status_code}")
        return data

    def __get_matches(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/matches.json")
        return matches

    def __get_results(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/results.json")
        return matches

    def __get_match(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/matchesByEvent.json")
        return matches

    def __get_stats(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/match.json")
        return matches

    def __get_topTeams(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/teams.json")
        return matches


    def __get_TeamPlayers(self,):
        matches = self.__fetch(url = "https://hltv-api.vercel.app/api/player.json")
        return matches
    

    def buscar_jogadores_por_time(self, nome_time)->"list":
        times = self.__get_TeamPlayers()
        try:
            for time in times:
                if time.get('name', '').lower() == nome_time.lower():
                    return [
                    {
                        'fullname': jogador.get('fullname'),
                        'image': jogador.get('image')
                    }
                    for jogador in time.get('players', [])
                ]
                else:
                    # raise Exception("[ERRO]: Time não encontrado!")
                    pass
        except Exception as e:
            print(e)
            return []  # Retorna lista vazia se time não for encontrado
        
    def obter_partidas(self)-> "list":
        matches = self.__get_matches()
        lista_partidas = []
        for match in matches:
            partida = {
                "name": match.get("event", {}).get("name"),
                "time": match.get("time"),
                "maps": match.get("maps"),
                "team1": match.get("teams", [{}])[0].get("name"),
                "team2": match.get("teams", [{}, {}])[1].get("name"),
            }
            lista_partidas.append(partida)
        return lista_partidas
    

    def statusJogador(self, nome_busca)->"dict":
        jogadores = self.__get_stats()
        for jogador in jogadores:
            if jogador.get('nickname', '').lower() == nome_busca.lower():
                return {
                    'nickname': jogador.get('nickname'),
                    'kd': jogador.get('kd'),
                    'rating': jogador.get('rating'),
                    'mapsPlayed': jogador.get('mapsPlayed'),
                    'team': jogador.get('team')
                }
        return None  
    
    def pegar_noticias_hltv(self):
        url = 'https://www.hltv.org/'
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        h2 = soup.find('h2', class_='newsheader', string="Today's news")
        if not h2:
            return []
        news_container = h2.find_next_sibling('div', class_='standard-box standard-list')
        if not news_container:
            return []

        links = news_container.find_all('a', class_='newsline article')
        noticias = [
            {
                'titulo': link.get_text(strip=True),
                'url': 'https://www.hltv.org' + link['href']
            }
            for link in links
        ]
        return noticias


    def obter_links_partidas_ao_vivo(self):
        url = 'https://www.hltv.org/matches'
        scraper = cloudscraper.create_scraper()
        r = scraper.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        live_matches_container = soup.find('div', class_='liveMatches')
        if not live_matches_container:
            return []

        partidas = live_matches_container.find_all('div', class_='match-wrapper live-match-container')

        links_partidas = []
        for partida in partidas:
            a_tag = partida.find('a', class_='match-top')
            if not a_tag:
                continue

            link = 'https://www.hltv.org' + a_tag['href']

            team_names = partida.select('div.match-teamname')
            if len(team_names) >= 2:
                team1 = team_names[0].get_text(strip=True)
                team2 = team_names[1].get_text(strip=True)
            else:
                team1, team2 = "Time 1", "Time 2"

            links_partidas.append({
                'link': link,
                'team1': team1,
                'team2': team2
            })

        return links_partidas
    

    def motivacional(self):
        frases = [
            "Você é bom, acredite no seu potencial!\nEntre no bomb direto sem granadas!\nAbra pixel sem strafe!\nAtire pulando achando que tu é o Coldzera!\nDá say no chat no início do round!",
            "Você é bom!\nSó te falta movimentação, posicionamento de mira, noção de jogo, comunicação...",
            "A vida é igual clutch: às vezes parece perdida, mas dá pra virar.",
            "Seja o bait que seu time merece... e deixe eles fazerem a kill.",
            "Lembre-se: até o Taco já errava HS. Tá tudo certo errar também!",
            "Confia no spray... mesmo quando ele não confia em você.",
            "Se você não sabe o que está fazendo, o inimigo também não sabe como te counterar."
        ]
        return random.choice(frases)
