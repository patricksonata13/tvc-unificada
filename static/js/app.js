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
        
        // Exibe o JSON completo como texto pré-formatado
        conteudo.innerHTML = `<pre>${JSON.stringify(dados, null, 2)}</pre>`;
    } catch (e) {
        conteudo.innerHTML = `<p style="color:red">Erro: ${e.message}</p>`;
    }
}

iniciar();
