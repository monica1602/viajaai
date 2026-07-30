# ✈️ ViajaAI - Recomendação Inteligente de Viagens

<p align="center">
  <img src="https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&h=300&fit=crop" alt="ViajaAI Banner" width="100%">
</p>

<p align="center">
  <strong>Descubra seu destino ideal com base nas suas preferências pessoais</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-3.x-green?logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Deploy-Render-purple?logo=render&logoColor=white" alt="Render">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>

---

## 📋 Sobre o Projeto

**ViajaAI** é uma aplicação web que recomenda destinos de viagem com base nas preferências do usuário. O sistema utiliza um algoritmo de pontuação por compatibilidade para ranquear os melhores destinos de acordo com os filtros selecionados.

### Funcionalidades

- 🔍 **Filtros inteligentes** — Duração, tipo de viagem, temperatura, gastronomia, transporte e orçamento
- 📊 **Score de compatibilidade** — Cada destino recebe uma porcentagem de match com suas preferências
- 🗺️ **15 destinos internacionais** — De Paris a Marrakech, com informações detalhadas
- 📱 **Design responsivo** — Funciona perfeitamente em desktop, tablet e celular
- 🖼️ **Modal de detalhes** — Idioma, melhor época, pontos turísticos e mais

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes)

### Instalação

```bash
# Clone o repositório
git clone https://github.com/monica1602/viajaai.git
cd viajaai

# Instale as dependências
pip install -r requirements.txt

# Rode a aplicação
python app.py
```

Acesse **http://localhost:5000** no navegador.

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | Python, Flask |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Estilo** | CSS Grid, Flexbox, Poppins Font |
| **Ícones** | Font Awesome 6 |
| **Deploy** | Render, Gunicorn |

---

## 📁 Estrutura do Projeto

```
viajaai/
├── app.py                 # Backend Flask (API + servidor)
├── Procfile               # Comando de inicialização (Render)
├── render.yaml            # Configuração de deploy
├── requirements.txt       # Dependências Python
├── index.html             # Versão standalone (sem servidor)
├── .gitignore
└── static/
    ├── index.html         # Frontend principal
    ├── styles.css         # Estilos da aplicação
    └── app.js             # Lógica do frontend
```

---

## 🔗 API Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/` | Página principal |
| `GET` | `/api/destinos` | Lista todos os destinos |
| `GET` | `/api/filtros` | Retorna opções de filtros |
| `POST` | `/api/recomendar` | Retorna destinos ranqueados |

### Exemplo de Requisição

```json
POST /api/recomendar
{
  "duracao": "curta",
  "tipo": "lazer",
  "temperatura": "quente",
  "comida": "mexicana",
  "transporte": "aviao",
  "orcamento": "medio"
}
```

---

## 🎯 Filtros Disponíveis

| Filtro | Opções |
|--------|--------|
| **Duração** | Curta (até 5 dias), Média (6-14 dias), Longa (15+ dias) |
| **Tipo** | Lazer, Trabalho, Estudo |
| **Temperatura** | Quente, Temperado, Frio |
| **Gastronomia** | 17 tipos de culinária |
| **Transporte** | Avião, Trem, Metrô, Ônibus, Carro, Barco, Bicicleta |
| **Orçamento** | Econômico, Moderado, Luxo |

---

## 🌍 Destinos Disponíveis

| Destino | Temperatura | Orçamento |
|---------|-------------|-----------|
| Paris, França | Temperado | Luxo |
| Tóquio, Japão | Temperado | Luxo |
| Cancún, México | Quente | Moderado |
| Lisboa, Portugal | Temperado | Moderado |
| Reykjavik, Islândia | Frio | Luxo |
| Bangkok, Tailândia | Quente | Econômico |
| Nova York, EUA | Temperado | Luxo |
| Machu Picchu, Peru | Frio | Moderado |
| Dubai, Emirados Árabes | Quente | Luxo |
| Buenos Aires, Argentina | Temperado | Econômico |
| Maldivas | Quente | Luxo |
| Berlim, Alemanha | Frio | Moderado |
| Rio de Janeiro, Brasil | Quente | Moderado |
| Queenstown, Nova Zelândia | Frio | Luxo |
| Marrakech, Marrocos | Quente | Econômico |

---

## 📦 Deploy no Render

1. Faça fork ou conecte este repositório ao [Render](https://render.com)
2. Crie um **Web Service** conectado ao repo
3. As configurações serão detectadas automaticamente via `render.yaml`
4. Aguarde o build e acesse sua URL pública

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch (`git checkout -b feature/novo-destino`)
3. Commit suas mudanças (`git commit -m 'Adiciona novo destino'`)
4. Push para a branch (`git push origin feature/novo-destino`)
5. Abrir um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Feito com ❤️ por <a href="https://github.com/monica1602">monica1602</a>
</p>
