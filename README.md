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
  <img src="https://img.shields.io/badge/Status-Online-brightgreen" alt="Status">
</p>

<p align="center">
  🌐 <a href="https://viajaai-x8q9.onrender.com"><strong>Acessar o site ao vivo</strong></a>
</p>

---

## 📋 Sobre o Projeto

Planejar uma viagem pode ser desafiador com tantas opções disponíveis. **ViajaAI** resolve esse problema oferecendo recomendações personalizadas de destinos com base no perfil e nas preferências de cada viajante.

O usuário responde algumas perguntas simples — quanto tempo tem, que tipo de viagem busca, qual clima prefere, que tipo de comida gosta — e o sistema retorna os destinos mais compatíveis, ranqueados por um score de afinidade calculado em tempo real.

---

## 🎯 Como Funciona

### A Experiência do Usuário

1. O viajante acessa o site e encontra um formulário visual com 6 filtros
2. Seleciona suas preferências (pode preencher todos ou apenas alguns)
3. Clica em "Buscar Destinos"
4. Os resultados aparecem como cards com fotos, tags e porcentagem de compatibilidade
5. Ao clicar em um destino, um modal exibe informações completas: idioma local, melhor época para visitar, tipo de transporte disponível e pontos turísticos imperdíveis

### O Algoritmo de Recomendação

O sistema utiliza um **algoritmo de scoring ponderado** que analisa até 6 critérios com pesos diferentes:

| Critério | Peso | Justificativa |
|----------|------|---------------|
| Duração | 3 | Fator decisivo (define se a viagem é viável) |
| Tipo de viagem | 3 | Define o propósito e expectativa |
| Temperatura | 2 | Conforto e preferência climática |
| Gastronomia | 2 | Experiência cultural importante |
| Orçamento | 2 | Limitação prática |
| Transporte | 1 | Preferência logística |

O score final é calculado como:

```
compatibilidade = (pontos_obtidos / pontos_máximos) × 100%
```

Destinos com **70%+** são exibidos como alta compatibilidade (verde), **40-69%** como média (amarelo), e abaixo como baixa (vermelho).

---

## 🌍 Destinos no Catálogo

O sistema conta com **15 destinos internacionais** cuidadosamente selecionados para cobrir diferentes perfis de viajante:

| Destino | Clima | Tipo | Orçamento | Destaque |
|---------|-------|------|-----------|----------|
| 🇫🇷 Paris | Temperado | Lazer, Estudo | Luxo | Arte e gastronomia |
| 🇯🇵 Tóquio | Temperado | Lazer, Trabalho, Estudo | Luxo | Tradição + tecnologia |
| 🇲🇽 Cancún | Quente | Lazer | Moderado | Praias paradisíacas |
| 🇵🇹 Lisboa | Temperado | Lazer, Estudo, Trabalho | Moderado | Cultura e pastéis de nata |
| 🇮🇸 Reykjavik | Frio | Lazer | Luxo | Aurora boreal |
| 🇹🇭 Bangkok | Quente | Lazer, Trabalho | Econômico | Templos e street food |
| 🇺🇸 Nova York | Temperado | Lazer, Trabalho, Estudo | Luxo | Cidade que nunca dorme |
| 🇵🇪 Machu Picchu | Frio | Lazer, Estudo | Moderado | Ruínas incas |
| 🇦🇪 Dubai | Quente | Lazer, Trabalho | Luxo | Luxo e arquitetura |
| 🇦🇷 Buenos Aires | Temperado | Lazer, Estudo | Econômico | Tango e churrasco |
| 🇲🇻 Maldivas | Quente | Lazer | Luxo | Bangalôs sobre a água |
| 🇩🇪 Berlim | Frio | Lazer, Estudo, Trabalho | Moderado | História e vida noturna |
| 🇧🇷 Rio de Janeiro | Quente | Lazer | Moderado | Praias e samba |
| 🇳🇿 Queenstown | Frio | Lazer | Luxo | Esportes de aventura |
| 🇲🇦 Marrakech | Quente | Lazer | Econômico | Mercados e deserto |

---

## 🎨 Interface

A interface foi construída com foco em **experiência visual** e **facilidade de uso**:

- **Cards com fotos reais** dos destinos (via Unsplash)
- **Tags coloridas** para identificação rápida (clima, duração, orçamento)
- **Badge de compatibilidade** com código de cores no canto de cada card
- **Modal interativo** com grid de informações detalhadas
- **Animações suaves** em hover e transições
- **100% responsivo** — adapta-se a qualquer tamanho de tela

---

## 🔍 Filtros Disponíveis

| Filtro | Opções | O que influencia |
|--------|--------|------------------|
| **Duração** | Curta (até 5 dias), Média (6-14 dias), Longa (15+ dias) | Viabilidade da viagem |
| **Tipo** | Lazer, Trabalho, Estudo | Propósito e infraestrutura |
| **Temperatura** | Quente (25°C+), Temperado (15-25°C), Frio (<15°C) | Conforto climático |
| **Gastronomia** | 17 culinárias (japonesa, mexicana, árabe, etc.) | Experiência cultural |
| **Transporte** | Avião, Trem, Metrô, Ônibus, Carro, Barco, Bicicleta | Acessibilidade |
| **Orçamento** | Econômico, Moderado, Luxo | Planejamento financeiro |

---

## 🛠️ Tecnologias Utilizadas

| Camada | Tecnologia | Função |
|--------|-----------|--------|
| **Backend** | Python 3.10, Flask | API REST, lógica de recomendação |
| **Frontend** | HTML5, CSS3, JavaScript ES6+ | Interface interativa |
| **Layout** | CSS Grid, Flexbox | Design responsivo |
| **Tipografia** | Google Fonts (Poppins) | Visual moderno |
| **Ícones** | Font Awesome 6 | Iconografia consistente |
| **Imagens** | Unsplash | Fotos de alta qualidade |
| **Servidor** | Gunicorn | Produção (WSGI) |
| **Hospedagem** | Render | Deploy automático via GitHub |

---

## 📁 Estrutura do Projeto

```
viajaai/
├── app.py                 # Backend Flask — API + algoritmo de recomendação
├── static/
│   ├── index.html         # Frontend principal (servido pelo Flask)
│   ├── styles.css         # Design completo da aplicação
│   └── app.js             # Lógica: chamadas à API, renderização, modal
├── index.html             # Versão standalone (abre sem servidor)
├── requirements.txt       # flask, gunicorn
├── Procfile               # Comando de start para o Render
├── render.yaml            # Blueprint de deploy
└── .gitignore             # Ignora __pycache__, venv, .env
```

---

## 🔗 API REST

| Método | Endpoint | Descrição | Retorno |
|--------|----------|-----------|---------|
| `GET` | `/api/destinos` | Todos os 15 destinos | Array de objetos |
| `GET` | `/api/filtros` | Opções de cada filtro | Objeto com categorias |
| `POST` | `/api/recomendar` | Destinos ranqueados | Array ordenado por score |

### Exemplo de uso:

```json
// POST /api/recomendar
// Request:
{
  "duracao": "curta",
  "tipo": "lazer",
  "temperatura": "quente",
  "orcamento": "medio"
}

// Response:
[
  { "nome": "Cancún, México", "compatibilidade": 100, ... },
  { "nome": "Rio de Janeiro, Brasil", "compatibilidade": 75, ... },
  { "nome": "Bangkok, Tailândia", "compatibilidade": 50, ... }
]
```

---

## 🚀 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/monica1602/viajaai.git
cd viajaai

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
python app.py
```

Acesse https://viajaai-x8q9.onrender.com/

---

## 🌐 Site Online

O projeto está publicado e acessível em:

**🔗 https://viajaai-x8q9.onrender.com**

> O Render pode levar alguns segundos para iniciar na primeira visita (free tier). Após o carregamento inicial, a navegação é instantânea.

---

## 💡 Possíveis Melhorias Futuras

- [ ] Adicionar mais destinos ao catálogo
- [ ] Integração com APIs de passagens aéreas (Skyscanner, Google Flights)
- [ ] Sistema de favoritos com localStorage
- [ ] Filtro por continente/região
- [ ] Modo escuro
- [ ] Login e perfil do viajante
- [ ] Avaliações e comentários de outros viajantes

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b feature/minha-feature`
3. Commit: `git commit -m 'Adiciona nova feature'`
4. Push: `git push origin feature/minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT.

---

<p align="center">
  Feito com ❤️ por <a href="https://github.com/monica1602">monica1602</a>
</p>
