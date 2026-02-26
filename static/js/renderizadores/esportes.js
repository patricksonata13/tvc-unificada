// Funções auxiliares para formatar data
function formatarData(dataISO) {
    const d = new Date(dataISO);
    return d.toLocaleDateString('pt-BR');
}

// Dados simulados para jogos (enquanto não temos no backend)
const jogosSimulados = [
    { data: '2026-03-01', hora: '16:00', time1: 'Flamengo', time2: 'Fluminense', placar: null, modalidade: 'Futebol' },
    { data: '2026-03-02', hora: '19:00', time1: 'Vasco', time2: 'Botafogo', placar: null, modalidade: 'Futebol' },
    { data: '2026-03-03', hora: '20:30', time1: 'Sesc-RJ', time2: 'Fluminense Vôlei', placar: null, modalidade: 'Vôlei' },
];

// Dados simulados para notícias (puxadas do jornalismo)
function getNoticiasEsportes(dados) {
    if (dados.jornalismo) {
        return dados.jornalismo.filter(n => n.categoria === 'Esportes');
    }
    return [];
}

const renderSubAbaEsportes = {
    inicio: (dados) => {
        let html = '<div class="dashboard-esportes">';
        
        // Últimas notícias
        const noticias = getNoticiasEsportes(dados).slice(0, 3);
        html += '<section><h3>📰 Últimas notícias</h3>';
        if (noticias.length) {
            html += '<ul>';
            noticias.forEach(n => {
                html += `<li><a href="/noticia/${n.id}" style="text-decoration: none; color: var(--cor-texto);"><strong>${n.titulo}</strong> <small>(${n.data})</small></a></li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>Nenhuma notícia recente.</p>';
        }
        html += '</section>';

        // Próximos jogos
        html += '<section><h3>📅 Próximos jogos</h3>';
        const proximos = jogosSimulados.filter(j => !j.placar).slice(0, 3);
        if (proximos.length) {
            html += '<ul>';
            proximos.forEach(j => {
                html += `<li><strong>${j.time1} x ${j.time2}</strong> - ${formatarData(j.data)} às ${j.hora} (${j.modalidade})</li>`;
            });
            html += '</ul>';
        } else {
            html += '<p>Nenhum jogo agendado.</p>';
        }
        html += '</section>';

        // Classificação resumida (top 4 do Brasileirão)
        html += '<section><h3>🏆 Brasileirão (top 4)</h3>';
        if (dados.brasileirao && dados.brasileirao.length) {
            html += '<table class="tabela"><tr><th>Pos</th><th>Time</th><th>Pontos</th></tr>';
            dados.brasileirao.slice(0, 4).forEach(t => {
                html += `<tr><td>${t.pos}</td><td>${t.time}</td><td>${t.pontos}</td></tr>`;
            });
            html += '</table>';
        } else {
            html += '<p>Sem dados.</p>';
        }
        html += '</section>';

        html += '</div>';
        return html;
    },

    noticias: (dados) => {
        const noticias = getNoticiasEsportes(dados);
        if (noticias.length === 0) return '<p>Nenhuma notícia esportiva encontrada.</p>';
        let html = '<div class="card-container">';
        noticias.forEach(n => {
            html += `
                <div class="card">
                    <h3>${n.titulo}</h3>
                    <p><strong>${n.data}</strong> - ${n.autor}</p>
                    <p>${n.conteudo}</p>
                    <p><small>👁️ ${n.views} visualizações</small></p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    },

    jogos: (dados) => {
        let html = '<h3>📅 Próximos jogos</h3>';
        html += '<table class="tabela"><tr><th>Data</th><th>Hora</th><th>Time 1</th><th>Time 2</th><th>Placar</th><th>Modalidade</th></tr>';
        jogosSimulados.forEach(j => {
            const placar = j.placar ? `${j.placar.time1} x ${j.placar.time2}` : 'a definir';
            html += `<tr><td>${formatarData(j.data)}</td><td>${j.hora}</td><td>${j.time1}</td><td>${j.time2}</td><td>${placar}</td><td>${j.modalidade}</td></tr>`;
        });
        html += '</table>';
        return html;
    },

    classificacoes: (dados) => {
        let html = '<h3>🇧🇷 Brasileirão</h3>';
        if (dados.brasileirao && dados.brasileirao.length) {
            html += '<table class="tabela"><tr><th>Pos</th><th>Time</th><th>Pontos</th><th>Jogos</th><th>Vitórias</th></tr>';
            dados.brasileirao.forEach(t => {
                html += `<tr><td>${t.pos}</td><td>${t.time}</td><td>${t.pontos}</td><td>${t.jogos}</td><td>${t.vitorias}</td></tr>`;
            });
            html += '</table>';
        } else {
            html += '<p>Sem dados.</p>';
        }

        html += '<h3 style="margin-top:2rem;">🏆 Carioca</h3>';
        if (dados.carioca && dados.carioca.length) {
            html += '<table class="tabela"><tr><th>Pos</th><th>Time</th><th>Pontos</th></tr>';
            dados.carioca.forEach(t => {
                html += `<tr><td>${t.pos}</td><td>${t.time}</td><td>${t.pontos}</td></tr>`;
            });
            html += '</table>';
        } else {
            html += '<p>Sem dados.</p>';
        }
        return html;
    },

    times: (dados) => {
        let html = '<h3>⚽ Grandes Clubes</h3>';
        if (dados.esportes && dados.esportes.length) {
            html += '<div class="card-container">';
            dados.esportes.forEach(clube => {
                html += `
                    <div class="card">
                        <h3>${clube.nome}</h3>
                        <p><strong>🏟️ Estádio:</strong> ${clube.estadio}</p>
                        <p><strong>🧑‍🏫 Técnico:</strong> ${clube.tecnico}</p>
                        <p><strong>🏆 Títulos:</strong> ${clube.titulos}</p>
                    </div>
                `;
            });
            html += '</div>';
        } else {
            html += '<p>Sem dados.</p>';
        }

        html += '<h3 style="margin-top:2rem;">🔹 Outros Times</h3>';
        if (dados.outros_times && dados.outros_times.length) {
            html += '<div class="card-container">';
            dados.outros_times.forEach(time => {
                html += `
                    <div class="card">
                        <h3>${time.nome}</h3>
                        <p><strong>🏟️ Estádio:</strong> ${time.estadio}</p>
                        <p><strong>🧑‍🏫 Técnico:</strong> ${time.tecnico}</p>
                        <p><strong>🏆 Títulos:</strong> ${time.titulos}</p>
                    </div>
                `;
            });
            html += '</div>';
        } else {
            html += '<p>Sem dados.</p>';
        }
        return html;
    },

    outras_modalidades: (dados) => {
        let html = '<h3>🏐 Vôlei</h3>';
        if (dados.volei && dados.volei.length) {
            html += '<div class="card-container">';
            dados.volei.forEach(v => {
                html += `
                    <div class="card">
                        <h3>${v.nome}</h3>
                        <p><strong>🏟️ Ginásio:</strong> ${v.ginasio}</p>
                        <p><strong>🏆 Títulos:</strong> ${v.titulos}</p>
                    </div>
                `;
            });
            html += '</div>';
        } else {
            html += '<p>Sem dados.</p>';
        }

        html += '<h3 style="margin-top:2rem;">🤾 Handebol</h3>';
        if (dados.handebol && dados.handebol.length) {
            html += '<div class="card-container">';
            dados.handebol.forEach(h => {
                html += `
                    <div class="card">
                        <h3>${h.nome}</h3>
                        <p><strong>🏟️ Ginásio:</strong> ${h.ginasio}</p>
                        <p><strong>🏆 Títulos:</strong> ${h.titulos}</p>
                    </div>
                `;
            });
            html += '</div>';
        } else {
            html += '<p>Sem dados.</p>';
        }

        // Futuramente: basquete, futsal, etc.
        return html;
    },

    estatisticas: (dados) => {
        return '<p>📊 Estatísticas em breve (artilheiros, cartões, etc.)</p>';
    }
};

export function renderEsportes(dados, abaAtiva = 'inicio') {
    const subAbas = [
        { id: 'inicio', nome: '🏠 Início' },
        { id: 'noticias', nome: '📰 Notícias' },
        { id: 'jogos', nome: '📅 Jogos' },
        { id: 'classificacoes', nome: '🏆 Classificações' },
        { id: 'times', nome: '⚽ Times' },
        { id: 'outras_modalidades', nome: '🤾 Outras Modalidades' },
        { id: 'estatisticas', nome: '📊 Estatísticas' }
    ];

    let html = '<div style="text-align: center; margin-bottom: 1.5rem;">';
    html += '<h2 style="font-size: 2rem; margin-bottom: 0.5rem;">🏖️ Esportes no Rio de Janeiro 🏟️</h2>';
    html += '<p style="color: var(--cor-texto-secundario);">A paixão do carioca pelo esporte em um só lugar</p>';
    html += '</div>';

    html += '<div class="sub-abas" id="sub-abas-esportes">';
    subAbas.forEach(aba => {
        const ativo = (aba.id === abaAtiva) ? 'ativo' : '';
        html += `<button class="sub-aba-btn ${ativo}" data-sub-aba="${aba.id}">${aba.nome}</button>`;
    });
    html += '</div>';
    html += '<div id="conteudo-sub-aba-esportes" class="conteudo-sub-aba">';
    html += renderSubAbaEsportes[abaAtiva](dados);
    html += '</div>';

    return html;
}

export function attachSubAbasEsportes(dados) {
    const botoes = document.querySelectorAll('#sub-abas-esportes .sub-aba-btn');
    const conteudoSub = document.getElementById('conteudo-sub-aba-esportes');

    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            const aba = btn.dataset.subAba;
            conteudoSub.innerHTML = renderSubAbaEsportes[aba](dados);
        });
    });
}
