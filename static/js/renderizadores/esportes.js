const renderSubAbaEsportes = {
    brasileirao: (dados) => {
        if (!dados.brasileirao || dados.brasileirao.length === 0) return '<p>Sem dados do Brasileirão.</p>';
        let html = '<table class="tabela"><tr><th>Pos</th><th>Time</th><th>Pontos</th><th>Jogos</th><th>Vitórias</th></tr>';
        dados.brasileirao.forEach(time => {
            html += `<tr><td>${time.pos}</td><td>${time.time}</td><td>${time.pontos}</td><td>${time.jogos}</td><td>${time.vitorias}</td></tr>`;
        });
        html += '</table>';
        return html;
    },
    carioca: (dados) => {
        if (!dados.carioca || dados.carioca.length === 0) return '<p>Sem dados do Carioca.</p>';
        let html = '<table class="tabela"><tr><th>Pos</th><th>Time</th><th>Pontos</th></tr>';
        dados.carioca.forEach(time => {
            html += `<tr><td>${time.pos}</td><td>${time.time}</td><td>${time.pontos}</td></tr>`;
        });
        html += '</table>';
        return html;
    },
    clubes: (dados) => {
        if (!dados.esportes || dados.esportes.length === 0) return '<p>Nenhum clube encontrado.</p>';
        let html = '<div class="card-container">';
        dados.esportes.forEach(clube => {
            html += `
                <div class="card">
                    <h3>${clube.nome}</h3>
                    <p><strong>Estádio:</strong> ${clube.estadio}</p>
                    <p><strong>Técnico:</strong> ${clube.tecnico}</p>
                    <p><strong>Títulos:</strong> ${clube.titulos}</p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    }
};

export function renderEsportes(dados, abaAtiva = 'brasileirao') {
    const subAbas = [
        { id: 'brasileirao', nome: 'Brasileirão' },
        { id: 'carioca', nome: 'Carioca' },
        { id: 'clubes', nome: 'Clubes' }
    ];

    let html = '<div class="sub-abas" id="sub-abas-esportes">';
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
