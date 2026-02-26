const renderSubAba = {
    equipe: (dados) => {
        if (!dados.equipe || dados.equipe.length === 0) return '<p>Nenhum membro da equipe.</p>';
        let html = '<div class="card-container">';
        dados.equipe.forEach(p => {
            html += `
                <div class="card">
                    <h3>${p.nome}</h3>
                    <p><strong>Função:</strong> ${p.funcao}</p>
                    <p><strong>Área:</strong> ${p.area}</p>
                    <p><strong>Disponibilidade:</strong> ${p.disponibilidade}</p>
                    <p><strong>Projetos:</strong> ${p.projetos?.join(', ')}</p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    },
    equipamentos: (dados) => {
        if (!dados.equipamentos || dados.equipamentos.length === 0) return '<p>Nenhum equipamento.</p>';
        let html = '<div class="card-container">';
        dados.equipamentos.forEach(eq => {
            html += `
                <div class="card">
                    <h3>${eq.nome}</h3>
                    <p><strong>Tipo:</strong> ${eq.tipo}</p>
                    <p><strong>Quantidade:</strong> ${eq.quantidade} (disponíveis: ${eq.disponiveis})</p>
                    <p><strong>Status:</strong> ${eq.status}</p>
                    <p><strong>Localização:</strong> ${eq.localizacao}</p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    },
    materiais: (dados) => {
        if (!dados.materiais || dados.materiais.length === 0) return '<p>Nenhum material.</p>';
        let html = '<div class="card-container">';
        dados.materiais.forEach(mat => {
            html += `
                <div class="card">
                    <h3>${mat.nome}</h3>
                    <p><strong>Tipo:</strong> ${mat.tipo}</p>
                    <p><strong>Quantidade:</strong> ${mat.quantidade} (disponíveis: ${mat.disponiveis})</p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    },
    fluxo: (dados) => {
        if (!dados.fluxo || dados.fluxo.length === 0) return '<p>Nenhum fluxo de trabalho.</p>';
        let html = '<table class="tabela"><tr><th>Projeto</th><th>Tarefa</th><th>Responsável</th><th>Prazo</th><th>Status</th><th>Prioridade</th></tr>';
        dados.fluxo.forEach(item => {
            html += `<tr><td>${item.projeto}</td><td>${item.tarefa}</td><td>${item.responsavel}</td><td>${item.prazo}</td><td>${item.status}</td><td>${item.prioridade}</td></tr>`;
        });
        html += '</table>';
        return html;
    },
    agenda: (dados) => {
        if (!dados.agenda || dados.agenda.length === 0) return '<p>Nenhum item na agenda.</p>';
        let html = '<table class="tabela"><tr><th>Data</th><th>Evento</th><th>Local</th><th>Responsável</th></tr>';
        dados.agenda.forEach(item => {
            html += `<tr><td>${item.data}</td><td>${item.evento}</td><td>${item.local}</td><td>${item.responsavel}</td></tr>`;
        });
        html += '</table>';
        return html;
    },
    escalas: (dados) => {
        if (!dados.escalas || dados.escalas.length === 0) return '<p>Nenhuma escala.</p>';
        let html = '<table class="tabela"><tr><th>Data</th><th>Função</th><th>Membro</th><th>Local</th></tr>';
        dados.escalas.forEach(item => {
            html += `<tr><td>${item.data}</td><td>${item.funcao}</td><td>${item.membro}</td><td>${item.local}</td></tr>`;
        });
        html += '</table>';
        return html;
    }
};

export function renderEstudios(estudios, abaAtiva = 'equipe') {
    const subAbas = [
        { id: 'equipe', nome: 'Equipe' },
        { id: 'equipamentos', nome: 'Equipamentos' },
        { id: 'materiais', nome: 'Materiais' },
        { id: 'fluxo', nome: 'Fluxo' },
        { id: 'agenda', nome: 'Agenda' },
        { id: 'escalas', nome: 'Escalas' }
    ];

    let html = '<div class="sub-abas" id="sub-abas-estudios">';
    subAbas.forEach(aba => {
        const ativo = (aba.id === abaAtiva) ? 'ativo' : '';
        html += `<button class="sub-aba-btn ${ativo}" data-sub-aba="${aba.id}">${aba.nome}</button>`;
    });
    html += '</div>';
    html += '<div id="conteudo-sub-aba-estudios" class="conteudo-sub-aba">';
    html += renderSubAba[abaAtiva](estudios);
    html += '</div>';

    return html;
}

export function attachSubAbasEstudios(estudios) {
    const botoes = document.querySelectorAll('#sub-abas-estudios .sub-aba-btn');
    const conteudoSub = document.getElementById('conteudo-sub-aba-estudios');

    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            const aba = btn.dataset.subAba;
            conteudoSub.innerHTML = renderSubAba[aba](estudios);
        });
    });
}
