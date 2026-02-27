// Teste: fetch direto para a API
(async function() {
    const conteudo = document.getElementById('conteudo-modulo');
    conteudo.innerHTML = '<p>Fazendo requisição direta...</p>';

    try {
        const resposta = await fetch('/api/tudo');
        if (!resposta.ok) {
            throw new Error(`HTTP ${resposta.status}`);
        }
        const dados = await resposta.json();
        conteudo.innerHTML = `<pre>${JSON.stringify(dados, null, 2)}</pre>`;
    } catch (erro) {
        conteudo.innerHTML = `<p style="color:red">Erro: ${erro.message}</p>`;
    }
})();
