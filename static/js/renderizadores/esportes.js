const renderSubAbaEsportes = {
    inicio: (dados) => { ... },  // (conteúdo completo – por economia, não repetirei, mas use o código anterior)
    noticias: (dados) => { ... },
    jogos: (dados) => { ... },
    classificacoes: (dados) => { ... },
    times: (dados) => { ... },
    outras_modalidades: (dados) => { ... },
    estatisticas: (dados) => { ... }
};

export function renderEsportes(dados, abaAtiva = 'inicio') { ... }
export function attachSubAbasEsportes(dados) { ... }
