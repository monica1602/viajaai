// ViajaAI - App Principal
document.addEventListener('DOMContentLoaded', () => {
    carregarDestinos();
    configurarEventos();
});

// Configura os event listeners
function configurarEventos() {
    const form = document.getElementById('filtros-form');
    const btnLimpar = document.getElementById('btn-limpar');
    const modalOverlay = document.getElementById('modal-overlay');
    const modalFechar = document.getElementById('modal-fechar');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        buscarRecomendacoes();
    });

    btnLimpar.addEventListener('click', () => {
        form.reset();
        carregarDestinos();
    });

    modalFechar.addEventListener('click', fecharModal);
    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            fecharModal();
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') fecharModal();
    });
}


// Carrega todos os destinos (sem filtro)
async function carregarDestinos() {
    mostrarLoading();
    try {
        const response = await fetch('/api/destinos');
        const destinos = await response.json();
        exibirDestinos(destinos, false);
    } catch (error) {
        console.error('Erro ao carregar destinos:', error);
        exibirErro();
    }
}

// Busca recomendações com base nos filtros
async function buscarRecomendacoes() {
    const filtros = obterFiltros();
    
    // Se não há filtros selecionados, carrega todos
    const temFiltro = Object.values(filtros).some(v => v !== '' && v !== null);
    if (!temFiltro) {
        carregarDestinos();
        return;
    }

    mostrarLoading();
    try {
        const response = await fetch('/api/recomendar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(filtros)
        });
        const destinos = await response.json();
        exibirDestinos(destinos, true);
    } catch (error) {
        console.error('Erro ao buscar recomendações:', error);
        exibirErro();
    }
}

// Obtém os valores dos filtros do formulário
function obterFiltros() {
    return {
        duracao: document.getElementById('duracao').value || null,
        tipo: document.getElementById('tipo').value || null,
        temperatura: document.getElementById('temperatura').value || null,
        comida: document.getElementById('comida').value || null,
        transporte: document.getElementById('transporte').value || null,
        orcamento: document.getElementById('orcamento').value || null
    };
}


// Exibe os destinos no grid
function exibirDestinos(destinos, comScore) {
    const grid = document.getElementById('destinos-grid');
    const semResultados = document.getElementById('sem-resultados');
    const contagem = document.getElementById('contagem-resultados');

    if (destinos.length === 0) {
        grid.innerHTML = '';
        semResultados.style.display = 'block';
        contagem.textContent = '';
        return;
    }

    semResultados.style.display = 'none';
    contagem.textContent = `${destinos.length} destino${destinos.length > 1 ? 's' : ''} encontrado${destinos.length > 1 ? 's' : ''}`;

    grid.innerHTML = destinos.map(destino => criarCardHTML(destino, comScore)).join('');

    // Adiciona eventos de clique nos cards
    grid.querySelectorAll('.destino-card').forEach(card => {
        card.addEventListener('click', () => {
            const id = parseInt(card.dataset.id);
            const destino = destinos.find(d => d.id === id);
            if (destino) abrirModal(destino);
        });
    });
}

// Cria o HTML de um card de destino
function criarCardHTML(destino, comScore) {
    const temperaturaLabel = {
        'quente': '☀️ Quente',
        'temperado': '🌤️ Temperado',
        'frio': '❄️ Frio'
    };

    const duracaoLabel = {
        'curta': '⚡ Curta',
        'media': '📅 Média',
        'longa': '🗓️ Longa'
    };

    const orcamentoLabel = {
        'baixo': '💰 Econômico',
        'medio': '💳 Moderado',
        'alto': '💎 Luxo'
    };

    let compatibilidadeHTML = '';
    if (comScore && destino.compatibilidade !== undefined) {
        let classe = 'compatibilidade-baixa';
        if (destino.compatibilidade >= 70) classe = 'compatibilidade-alta';
        else if (destino.compatibilidade >= 40) classe = 'compatibilidade-media';
        
        compatibilidadeHTML = `
            <span class="destino-compatibilidade ${classe}">
                ${destino.compatibilidade}% compatível
            </span>`;
    }

    return `
        <article class="destino-card" data-id="${destino.id}" tabindex="0" role="button" 
                 aria-label="Ver detalhes de ${destino.nome}">
            <div class="destino-imagem-wrapper">
                <img src="${destino.imagem}" alt="${destino.nome}" class="destino-imagem" loading="lazy">
                ${compatibilidadeHTML}
            </div>
            <div class="destino-info">
                <h4 class="destino-nome">${destino.nome}</h4>
                <p class="destino-descricao">${destino.descricao}</p>
                <div class="destino-tags">
                    <span class="tag tag-temperatura">${temperaturaLabel[destino.temperatura] || destino.temperatura}</span>
                    <span class="tag tag-duracao">${duracaoLabel[destino.duracao] || destino.duracao}</span>
                    <span class="tag tag-orcamento">${orcamentoLabel[destino.orcamento] || destino.orcamento}</span>
                </div>
            </div>
        </article>
    `;
}


// Abre o modal de detalhes
function abrirModal(destino) {
    const overlay = document.getElementById('modal-overlay');
    const conteudo = document.getElementById('modal-conteudo');

    const transporteIcons = {
        'aviao': 'fa-plane',
        'trem': 'fa-train',
        'metro': 'fa-subway',
        'onibus': 'fa-bus',
        'carro': 'fa-car',
        'barco': 'fa-ship',
        'bicicleta': 'fa-bicycle',
        'tuk-tuk': 'fa-motorcycle',
        'taxi': 'fa-taxi',
        'trilha': 'fa-hiking',
        'camelo': 'fa-horse'
    };

    const tipoLabels = {
        'lazer': 'Lazer',
        'trabalho': 'Trabalho',
        'estudo': 'Estudo'
    };

    const duracaoLabels = {
        'curta': 'Curta (até 5 dias)',
        'media': 'Média (6-14 dias)',
        'longa': 'Longa (15+ dias)'
    };

    const orcamentoLabels = {
        'baixo': 'Econômico',
        'medio': 'Moderado',
        'alto': 'Luxo'
    };

    const tipos = destino.tipo.map(t => tipoLabels[t] || t).join(', ');
    const transportes = destino.transporte.map(t => {
        const icon = transporteIcons[t] || 'fa-route';
        return `<i class="fas ${icon}" title="${t}"></i>`;
    }).join(' ');

    conteudo.innerHTML = `
        <img src="${destino.imagem}" alt="${destino.nome}" class="modal-imagem">
        <div class="modal-body">
            <h2 class="modal-nome">${destino.nome}</h2>
            <p class="modal-descricao">${destino.descricao}</p>
            
            <div class="modal-detalhes">
                <div class="modal-detalhe-item">
                    <i class="fas fa-calendar-alt"></i>
                    <span>${duracaoLabels[destino.duracao]}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-suitcase"></i>
                    <span>${tipos}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-thermometer-half"></i>
                    <span>${destino.temperatura.charAt(0).toUpperCase() + destino.temperatura.slice(1)}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-wallet"></i>
                    <span>${orcamentoLabels[destino.orcamento]}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-language"></i>
                    <span>${destino.idioma}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-sun"></i>
                    <span>${destino.melhor_epoca}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-utensils"></i>
                    <span>${destino.comida.join(', ')}</span>
                </div>
                <div class="modal-detalhe-item">
                    <i class="fas fa-route"></i>
                    <span>${destino.transporte.join(', ')}</span>
                </div>
            </div>

            <div class="modal-pontos">
                <h4><i class="fas fa-star"></i> Pontos Turísticos</h4>
                <ul>
                    ${destino.pontos_turisticos.map(p => `<li>${p}</li>`).join('')}
                </ul>
            </div>
        </div>
    `;

    overlay.classList.add('ativo');
    document.body.style.overflow = 'hidden';
}

// Fecha o modal
function fecharModal() {
    const overlay = document.getElementById('modal-overlay');
    overlay.classList.remove('ativo');
    document.body.style.overflow = '';
}

// Mostra loading
function mostrarLoading() {
    const grid = document.getElementById('destinos-grid');
    grid.innerHTML = `
        <div class="loading" style="grid-column: 1 / -1;">
            <div class="loading-spinner"></div>
        </div>
    `;
    document.getElementById('sem-resultados').style.display = 'none';
    document.getElementById('contagem-resultados').textContent = '';
}

// Exibe mensagem de erro
function exibirErro() {
    const grid = document.getElementById('destinos-grid');
    grid.innerHTML = `
        <div class="sem-resultados" style="grid-column: 1 / -1;">
            <i class="fas fa-exclamation-triangle"></i>
            <h4>Erro ao carregar destinos</h4>
            <p>Tente novamente em alguns instantes.</p>
        </div>
    `;
}
