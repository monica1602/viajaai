from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# Base de dados de destinos de viagem
DESTINOS = [
    {
        "id": 1,
        "nome": "Paris, França",
        "imagem": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=400&h=300&fit=crop",
        "descricao": "A cidade luz, repleta de arte, cultura e gastronomia refinada.",
        "duracao": "media",
        "tipo": ["lazer", "estudo"],
        "temperatura": "temperado",
        "comida": ["francesa", "internacional"],
        "transporte": ["metro", "trem", "aviao"],
        "orcamento": "alto",
        "idioma": "Francês",
        "melhor_epoca": "Primavera/Verão",
        "pontos_turisticos": ["Torre Eiffel", "Louvre", "Champs-Élysées"]
    },
    {
        "id": 2,
        "nome": "Tóquio, Japão",
        "imagem": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=400&h=300&fit=crop",
        "descricao": "Uma fusão única entre tradição milenar e tecnologia de ponta.",
        "duracao": "longa",
        "tipo": ["lazer", "trabalho", "estudo"],
        "temperatura": "temperado",
        "comida": ["japonesa", "asiatica"],
        "transporte": ["metro", "trem", "aviao"],
        "orcamento": "alto",
        "idioma": "Japonês",
        "melhor_epoca": "Primavera (cerejeiras)",
        "pontos_turisticos": ["Shibuya", "Templo Senso-ji", "Monte Fuji"]
    },
    {
        "id": 3,
        "nome": "Cancún, México",
        "imagem": "https://images.unsplash.com/photo-1510097467424-192d713fd8b2?w=400&h=300&fit=crop",
        "descricao": "Praias paradisíacas com águas cristalinas e vida noturna agitada.",
        "duracao": "curta",
        "tipo": ["lazer"],
        "temperatura": "quente",
        "comida": ["mexicana", "internacional"],
        "transporte": ["aviao", "onibus"],
        "orcamento": "medio",
        "idioma": "Espanhol",
        "melhor_epoca": "Dezembro a Abril",
        "pontos_turisticos": ["Chichén Itzá", "Isla Mujeres", "Xcaret"]
    },
    {
        "id": 4,
        "nome": "Lisboa, Portugal",
        "imagem": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=400&h=300&fit=crop",
        "descricao": "Cidade histórica com clima agradável, pastéis de nata e fado.",
        "duracao": "media",
        "tipo": ["lazer", "estudo", "trabalho"],
        "temperatura": "temperado",
        "comida": ["portuguesa", "internacional"],
        "transporte": ["metro", "trem", "aviao"],
        "orcamento": "medio",
        "idioma": "Português",
        "melhor_epoca": "Primavera/Verão",
        "pontos_turisticos": ["Torre de Belém", "Alfama", "Sintra"]
    },
    {
        "id": 5,
        "nome": "Reykjavik, Islândia",
        "imagem": "https://images.unsplash.com/photo-1504829857797-ddff29c27927?w=400&h=300&fit=crop",
        "descricao": "Paisagens vulcânicas, aurora boreal e fontes termais naturais.",
        "duracao": "curta",
        "tipo": ["lazer"],
        "temperatura": "frio",
        "comida": ["nordica", "internacional"],
        "transporte": ["aviao", "carro"],
        "orcamento": "alto",
        "idioma": "Islandês",
        "melhor_epoca": "Inverno (aurora) / Verão (sol da meia-noite)",
        "pontos_turisticos": ["Blue Lagoon", "Golden Circle", "Aurora Boreal"]
    },
    {
        "id": 6,
        "nome": "Bangkok, Tailândia",
        "imagem": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?w=400&h=300&fit=crop",
        "descricao": "Templos dourados, comida de rua incrível e mercados flutuantes.",
        "duracao": "media",
        "tipo": ["lazer", "trabalho"],
        "temperatura": "quente",
        "comida": ["tailandesa", "asiatica"],
        "transporte": ["metro", "tuk-tuk", "aviao"],
        "orcamento": "baixo",
        "idioma": "Tailandês",
        "melhor_epoca": "Novembro a Fevereiro",
        "pontos_turisticos": ["Grand Palace", "Wat Arun", "Chatuchak Market"]
    },
    {
        "id": 7,
        "nome": "Nova York, EUA",
        "imagem": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=400&h=300&fit=crop",
        "descricao": "A cidade que nunca dorme, com teatros, museus e arranha-céus icônicos.",
        "duracao": "media",
        "tipo": ["lazer", "trabalho", "estudo"],
        "temperatura": "temperado",
        "comida": ["americana", "internacional"],
        "transporte": ["metro", "aviao", "taxi"],
        "orcamento": "alto",
        "idioma": "Inglês",
        "melhor_epoca": "Primavera/Outono",
        "pontos_turisticos": ["Central Park", "Estátua da Liberdade", "Times Square"]
    },
    {
        "id": 8,
        "nome": "Machu Picchu, Peru",
        "imagem": "https://images.unsplash.com/photo-1587595431973-160d0d94add1?w=400&h=300&fit=crop",
        "descricao": "Ruínas incas no alto dos Andes com vistas de tirar o fôlego.",
        "duracao": "curta",
        "tipo": ["lazer", "estudo"],
        "temperatura": "frio",
        "comida": ["peruana", "latina"],
        "transporte": ["trem", "aviao", "trilha"],
        "orcamento": "medio",
        "idioma": "Espanhol",
        "melhor_epoca": "Maio a Setembro",
        "pontos_turisticos": ["Cidadela Inca", "Huayna Picchu", "Vale Sagrado"]
    },
    {
        "id": 9,
        "nome": "Dubai, Emirados Árabes",
        "imagem": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=400&h=300&fit=crop",
        "descricao": "Luxo, arranha-céus futuristas e deserto dourado.",
        "duracao": "curta",
        "tipo": ["lazer", "trabalho"],
        "temperatura": "quente",
        "comida": ["arabe", "internacional"],
        "transporte": ["metro", "aviao", "taxi"],
        "orcamento": "alto",
        "idioma": "Árabe/Inglês",
        "melhor_epoca": "Novembro a Março",
        "pontos_turisticos": ["Burj Khalifa", "Palm Jumeirah", "Desert Safari"]
    },
    {
        "id": 10,
        "nome": "Buenos Aires, Argentina",
        "imagem": "https://images.unsplash.com/photo-1589909202802-8f4aadce1849?w=400&h=300&fit=crop",
        "descricao": "Tango, churrasco argentino e arquitetura europeia na América do Sul.",
        "duracao": "media",
        "tipo": ["lazer", "estudo"],
        "temperatura": "temperado",
        "comida": ["argentina", "latina"],
        "transporte": ["metro", "onibus", "aviao"],
        "orcamento": "baixo",
        "idioma": "Espanhol",
        "melhor_epoca": "Março a Maio / Setembro a Novembro",
        "pontos_turisticos": ["La Boca", "Recoleta", "Puerto Madero"]
    },
    {
        "id": 11,
        "nome": "Maldivas",
        "imagem": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=400&h=300&fit=crop",
        "descricao": "Ilhas paradisíacas com bangalôs sobre águas cristalinas.",
        "duracao": "curta",
        "tipo": ["lazer"],
        "temperatura": "quente",
        "comida": ["internacional", "frutos_do_mar"],
        "transporte": ["aviao", "barco"],
        "orcamento": "alto",
        "idioma": "Divehi/Inglês",
        "melhor_epoca": "Novembro a Abril",
        "pontos_turisticos": ["Resorts sobre a água", "Mergulho", "Bancos de areia"]
    },
    {
        "id": 12,
        "nome": "Berlim, Alemanha",
        "imagem": "https://images.unsplash.com/photo-1560969184-10fe8719e047?w=400&h=300&fit=crop",
        "descricao": "História, arte urbana, vida noturna vibrante e cultura alternativa.",
        "duracao": "media",
        "tipo": ["lazer", "estudo", "trabalho"],
        "temperatura": "frio",
        "comida": ["alema", "internacional"],
        "transporte": ["metro", "trem", "bicicleta"],
        "orcamento": "medio",
        "idioma": "Alemão",
        "melhor_epoca": "Maio a Setembro",
        "pontos_turisticos": ["Portão de Brandemburgo", "Muro de Berlim", "Ilha dos Museus"]
    },
    {
        "id": 13,
        "nome": "Rio de Janeiro, Brasil",
        "imagem": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=400&h=300&fit=crop",
        "descricao": "Praias famosas, samba, Cristo Redentor e energia contagiante.",
        "duracao": "media",
        "tipo": ["lazer"],
        "temperatura": "quente",
        "comida": ["brasileira", "latina"],
        "transporte": ["metro", "onibus", "aviao"],
        "orcamento": "medio",
        "idioma": "Português",
        "melhor_epoca": "Dezembro a Março",
        "pontos_turisticos": ["Cristo Redentor", "Copacabana", "Pão de Açúcar"]
    },
    {
        "id": 14,
        "nome": "Queenstown, Nova Zelândia",
        "imagem": "https://images.unsplash.com/photo-1589871973318-9ca1258faa5d?w=400&h=300&fit=crop",
        "descricao": "Capital mundial dos esportes de aventura com paisagens cinematográficas.",
        "duracao": "longa",
        "tipo": ["lazer"],
        "temperatura": "frio",
        "comida": ["internacional", "neozelandesa"],
        "transporte": ["aviao", "carro"],
        "orcamento": "alto",
        "idioma": "Inglês",
        "melhor_epoca": "Dezembro a Fevereiro",
        "pontos_turisticos": ["Bungee Jump", "Milford Sound", "Lago Wakatipu"]
    },
    {
        "id": 15,
        "nome": "Marrakech, Marrocos",
        "imagem": "https://images.unsplash.com/photo-1597212618440-806262de4f6b?w=400&h=300&fit=crop",
        "descricao": "Mercados vibrantes, palácios e o deserto do Saara como vizinho.",
        "duracao": "curta",
        "tipo": ["lazer"],
        "temperatura": "quente",
        "comida": ["marroquina", "arabe"],
        "transporte": ["aviao", "carro", "camelo"],
        "orcamento": "baixo",
        "idioma": "Árabe/Francês",
        "melhor_epoca": "Março a Maio / Setembro a Novembro",
        "pontos_turisticos": ["Medina", "Jardim Majorelle", "Deserto do Saara"]
    }
]


def calcular_score(destino, filtros):
    """Calcula um score de compatibilidade entre o destino e os filtros do usuário."""
    score = 0
    max_score = 0

    # Duração
    if filtros.get("duracao"):
        max_score += 3
        if destino["duracao"] == filtros["duracao"]:
            score += 3

    # Tipo de viagem
    if filtros.get("tipo"):
        max_score += 3
        if filtros["tipo"] in destino["tipo"]:
            score += 3

    # Temperatura
    if filtros.get("temperatura"):
        max_score += 2
        if destino["temperatura"] == filtros["temperatura"]:
            score += 2

    # Comida
    if filtros.get("comida"):
        max_score += 2
        comidas_filtro = filtros["comida"] if isinstance(filtros["comida"], list) else [filtros["comida"]]
        for c in comidas_filtro:
            if c in destino["comida"]:
                score += 2
                break

    # Transporte
    if filtros.get("transporte"):
        max_score += 1
        transportes_filtro = filtros["transporte"] if isinstance(filtros["transporte"], list) else [filtros["transporte"]]
        for t in transportes_filtro:
            if t in destino["transporte"]:
                score += 1
                break

    # Orçamento
    if filtros.get("orcamento"):
        max_score += 2
        if destino["orcamento"] == filtros["orcamento"]:
            score += 2

    if max_score == 0:
        return 100  # Sem filtros, todos são compatíveis

    return round((score / max_score) * 100)


@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)


@app.route('/api/destinos', methods=['GET'])
def listar_destinos():
    """Retorna todos os destinos disponíveis."""
    return jsonify(DESTINOS)


@app.route('/api/recomendar', methods=['POST'])
def recomendar():
    """Retorna destinos recomendados com base nos filtros do usuário."""
    filtros = request.get_json()

    resultados = []
    for destino in DESTINOS:
        score = calcular_score(destino, filtros)
        if score > 0:
            resultado = destino.copy()
            resultado["compatibilidade"] = score
            resultados.append(resultado)

    # Ordena por compatibilidade (maior primeiro)
    resultados.sort(key=lambda x: x["compatibilidade"], reverse=True)

    return jsonify(resultados)


@app.route('/api/filtros', methods=['GET'])
def listar_filtros():
    """Retorna as opções disponíveis para os filtros."""
    filtros = {
        "duracao": [
            {"valor": "curta", "label": "Curta (até 5 dias)"},
            {"valor": "media", "label": "Média (6-14 dias)"},
            {"valor": "longa", "label": "Longa (15+ dias)"}
        ],
        "tipo": [
            {"valor": "lazer", "label": "Lazer"},
            {"valor": "trabalho", "label": "Trabalho"},
            {"valor": "estudo", "label": "Estudo"}
        ],
        "temperatura": [
            {"valor": "quente", "label": "Quente (25°C+)"},
            {"valor": "temperado", "label": "Temperado (15-25°C)"},
            {"valor": "frio", "label": "Frio (abaixo de 15°C)"}
        ],
        "comida": [
            {"valor": "internacional", "label": "Internacional"},
            {"valor": "japonesa", "label": "Japonesa"},
            {"valor": "italiana", "label": "Italiana"},
            {"valor": "mexicana", "label": "Mexicana"},
            {"valor": "francesa", "label": "Francesa"},
            {"valor": "tailandesa", "label": "Tailandesa"},
            {"valor": "brasileira", "label": "Brasileira"},
            {"valor": "arabe", "label": "Árabe"},
            {"valor": "asiatica", "label": "Asiática"},
            {"valor": "latina", "label": "Latina"},
            {"valor": "portuguesa", "label": "Portuguesa"},
            {"valor": "americana", "label": "Americana"},
            {"valor": "nordica", "label": "Nórdica"},
            {"valor": "alema", "label": "Alemã"},
            {"valor": "peruana", "label": "Peruana"},
            {"valor": "argentina", "label": "Argentina"},
            {"valor": "marroquina", "label": "Marroquina"},
            {"valor": "frutos_do_mar", "label": "Frutos do Mar"}
        ],
        "transporte": [
            {"valor": "aviao", "label": "Avião"},
            {"valor": "trem", "label": "Trem"},
            {"valor": "metro", "label": "Metrô"},
            {"valor": "onibus", "label": "Ônibus"},
            {"valor": "carro", "label": "Carro"},
            {"valor": "barco", "label": "Barco"},
            {"valor": "bicicleta", "label": "Bicicleta"}
        ],
        "orcamento": [
            {"valor": "baixo", "label": "Econômico"},
            {"valor": "medio", "label": "Moderado"},
            {"valor": "alto", "label": "Luxo"}
        ]
    }
    return jsonify(filtros)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
