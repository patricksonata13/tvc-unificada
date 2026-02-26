export async function carregarDados() {
    try {
        const resposta = await fetch('/api/tudo');
        return await resposta.json();
    } catch (erro) {
        console.error('Erro ao carregar dados:', erro);
        return null;
    }
}
