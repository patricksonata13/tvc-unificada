export function renderFinanceiro(financeiro) {
    if (!financeiro || Object.keys(financeiro).length === 0) {
        return '<p>Dados financeiros não disponíveis.</p>';
    }
    let html = '<table class="tabela"><tr><th>Chave</th><th>Valor</th></tr>';
    for (let [chave, valor] of Object.entries(financeiro)) {
        html += `<tr><td>${chave}</td><td>${JSON.stringify(valor)}</td></tr>`;
    }
    html += '</table>';
    return html;
}
