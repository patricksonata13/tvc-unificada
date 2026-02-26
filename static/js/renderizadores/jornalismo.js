const renderCategoria = {
    todas: (noticias) => {
        if (!noticias || noticias.length === 0) return '<p>Nenhuma notícia.</p>';
        let html = '<div class="card-container">';
        noticias.forEach(not => {
            html += `
                <div class="card">
                    <h3>${not.titulo}</h3>
                    <p><strong>Categoria:</strong> ${not.categoria}</p>
                    <p><strong>Data:</strong> ${not.data}</p>
                    <p><strong>Autor:</strong> ${not.autor}</p>
                    <p>${not.conteudo}</p>
                    <p><small>Visualizações: ${not.views}</small></p>
                </div>
            `;
        });
        html += '</div>';
        return html;
    },
    cidade: (noticias) => {
        const filtradas = noticias.filter(n => n.categoria === 'Cidade');
        return renderCategoria.todas(filtradas);
    },
    cultura: (noticias) => {
        const filtradas = noticias.filter(n => n.categoria === 'Cultura');
        return renderCategoria.todas(filtradas);
    },
    esportes: (noticias) => {
        const filtradas = noticias.filter(n => n.categoria === 'Esportes');
        return renderCategoria.todas(filtradas);
    },
    comunidade: (noticias) => {
        const filtradas = noticias.filter(n => n.categoria === 'Comunidade');
        return renderCategoria.todas(filtradas);
    }
};

export function renderJornalismo(noticias, abaAtiva = 'todas') {
    const subAbas = [
        { id: 'todas', nome: 'Todas' },
        { id: 'cidade', nome: 'Cidade' },
        { id: 'cultura', nome: 'Cultura' },
        { id: 'esportes', nome: 'Esportes' },
        { id: 'comunidade', nome: 'Comunidade' }
    ];

    let html = '<div class="sub-abas" id="sub-abas-jornalismo">';
    subAbas.forEach(aba => {
        const ativo = (aba.id === abaAtiva) ? 'ativo' : '';
        html += `<button class="sub-aba-btn ${ativo}" data-sub-aba="${aba.id}">${aba.nome}</button>`;
    });
    html += '</div>';
    html += '<div id="conteudo-sub-aba-jornalismo" class="conteudo-sub-aba">';
    html += renderCategoria[abaAtiva](noticias);
    html += '</div>';

    return html;
}

export function attachSubAbasJornalismo(noticias) {
    const botoes = document.querySelectorAll('#sub-abas-jornalismo .sub-aba-btn');
    const conteudoSub = document.getElementById('conteudo-sub-aba-jornalismo');

    botoes.forEach(btn => {
        btn.addEventListener('click', () => {
            botoes.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            const aba = btn.dataset.subAba;
            conteudoSub.innerHTML = renderCategoria[aba](noticias);
        });
    });
}
