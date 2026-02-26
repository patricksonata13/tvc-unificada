export function renderEscaleta(projetos) {
    if (!projetos || projetos.length === 0) return '<p>Nenhum projeto encontrado.</p>';

    let html = '<div class="card-container">';
    projetos.forEach(proj => {
        html += `
            <div class="card">
                <h3>${proj.nome}</h3>
                <p><strong>Tipo:</strong> ${proj.tipo}</p>
                <p><strong>Status:</strong> ${proj.status}</p>
                <p><strong>Progresso:</strong> ${proj.progresso}%</p>
                <p><strong>Responsável:</strong> ${proj.responsavel}</p>
                <p><strong>Visão:</strong> ${proj.visao}</p>
                <p><strong>Orçamento:</strong> R$ ${proj.orcamento?.toLocaleString()}</p>
                <p><em>${proj.descricao}</em></p>
                ${window.USER_LOGGED_IN ? `<div style="margin-top: 1rem; text-align: right;"><a href="/admin/escaleta/${proj.id}/editar" class="btn-editar-card" style="background: #ff9800; color: white; padding: 0.25rem 0.5rem; border-radius: 4px; text-decoration: none;">✏️ Editar</a></div>` : ''}
            </div>
        `;
    });
    html += '</div>';
    return html;
}
