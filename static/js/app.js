import { carregarDados } from './api.js';

async function iniciar() {
    const conteudo = document.getElementById('conteudo-modulo');
    conteudo.innerHTML = '<p>Carregando...</p>';
    
    try {
        const dados = await carregarDados();
        if (!dados) {
            conteudo.innerHTML = '<p>Erro: dados vazios</p>';
            return;
        }
        
        // Exibe apenas os títulos da escaleta como exemplo
        let html = '<h2>Projetos da Escaleta</h2><ul>';
        if (dados.escaleta && dados.escaleta.length) {
            dados.escaleta.forEach(p => {
                html += `<li><strong>${p.nome}</strong> – ${p.descricao.substring(0, 50)}…</li>`;
            });
        } else {
            html += '<li>Nenhum projeto</li>';
        }
        html += '</ul>';
        
        conteudo.innerHTML = html;
    } catch (e) {
        conteudo.innerHTML = `<p style="color:red">Erro: ${e.message}</p>`;
    }
}

iniciar();
