// ============================================
// TESTE: Mensagem imediata
// ============================================
document.body.innerHTML = '<h1 style="color: blue; text-align: center;">JavaScript carregado! (teste)</h1>';

// ============================================
// Código original com logs
// ============================================
import { carregarDados } from './api.js';
import { renderEscaleta } from './renderizadores/escaleta.js';
import { renderJornalismo, attachSubAbasJornalismo } from './renderizadores/jornalismo.js';
import { renderEsportes, attachSubAbasEsportes } from './renderizadores/esportes.js';
import { renderEstudios, attachSubAbasEstudios } from './renderizadores/estudios.js';
import { renderFinanceiro } from './renderizadores/financeiro.js';

let dadosCompletos = null;
let moduloAtivo = 'escaleta';
let subAbaAtiva = null;
let loggedIn = false;

const botoesModulo = document.querySelectorAll('.modulo-btn');
const conteudoModulo = document.getElementById('conteudo-modulo');

// Verifica login
const metaLogged = document.querySelector('meta[name="logged-in"]');
if (metaLogged) {
    loggedIn = metaLogged.content === 'true';
}

function mostrarStatus(texto) {
    conteudoModulo.innerHTML = `<p style="background:#e0e0e0; padding:1rem;">${texto}</p>`;
}

function parseHash() {
    const hash = window.location.hash.slice(1);
    if (!hash) return { modulo: 'escaleta', subAba: null };
    const partes = hash.split('/');
    const modulo = partes[0] || 'escaleta';
    const subAba = partes[1] || null;
    return { modulo, subAba };
}

function updateHash(modulo, subAba = '') {
    const hash = subAba ? `#${modulo}/${subAba}` : `#${modulo}`;
    history.pushState(null, '', hash);
}

function mostrarErro(mensagem, erro, dados) {
    console.error(mensagem, erro);
    let html = `<div style="color:red; padding:1rem; background:#ffeeee; border:2px solid red; border-radius:8px; margin-bottom:1rem;">
        <strong>ERRO:</strong> ${mensagem}<br>
        <pre style="white-space: pre-wrap;">${erro.stack || erro}</pre>
    </div>`;
    if (dados) {
        html += `<pre style="background:#f4f4f4; padding:1rem; overflow:auto;">${JSON.stringify(dados, null, 2)}</pre>`;
    }
    conteudoModulo.innerHTML = html;
}

async function iniciar() {
    mostrarStatus('Iniciando... (1)');
    try {
        mostrarStatus('Chamando carregarDados()... (2)');
        dadosCompletos = await carregarDados();
        mostrarStatus('Dados recebidos! (3)');
        if (!dadosCompletos) {
            mostrarErro('Dados vazios', 'A API retornou null ou vazio', null);
            return;
        }
        mostrarStatus('Processando dados... (4)');

        const { modulo, subAba } = parseHash();
        moduloAtivo = modulo;
        subAbaAtiva = subAba;

        botoesModulo.forEach(btn => {
            btn.classList.remove('ativo');
            if (btn.dataset.modulo === moduloAtivo) {
                btn.classList.add('ativo');
            }
        });

        mostrarStatus('Renderizando módulo... (5)');
        exibirModulo(moduloAtivo, subAbaAtiva);
    } catch (e) {
        mostrarErro('Falha ao carregar dados', e, null);
    }
}

function exibirModulo(modulo, subAba = null) {
    if (!dadosCompletos) {
        mostrarErro('dadosCompletos é null', new Error('dados não carregados'), null);
        return;
    }
    try {
        let html = '';
        switch (modulo) {
            case 'escaleta':
                html = renderEscaleta(dadosCompletos.escaleta);
                break;
            case 'jornalismo':
                html = renderJornalismo(dadosCompletos.jornalismo, subAba || 'todas');
                break;
            case 'esportes':
                html = renderEsportes(dadosCompletos, subAba || 'inicio');
                break;
            case 'estudios':
                html = renderEstudios(dadosCompletos.estudios, subAba || 'equipe');
                break;
            case 'financeiro':
                html = renderFinanceiro(dadosCompletos.financeiro);
                break;
            default:
                html = '<p>Módulo não encontrado.</p>';
        }
        conteudoModulo.innerHTML = html;

        if (modulo === 'jornalismo' && dadosCompletos.jornalismo) {
            attachSubAbasJornalismo(dadosCompletos.jornalismo);
            if (subAba) {
                const btn = document.querySelector(`#sub-abas-jornalismo .sub-aba-btn[data-sub-aba="${subAba}"]`);
                if (btn) btn.click();
            }
        }
        if (modulo === 'esportes' && dadosCompletos) {
            attachSubAbasEsportes(dadosCompletos);
            if (subAba) {
                const btn = document.querySelector(`#sub-abas-esportes .sub-aba-btn[data-sub-aba="${subAba}"]`);
                if (btn) btn.click();
            }
        }
        if (modulo === 'estudios' && dadosCompletos.estudios) {
            attachSubAbasEstudios(dadosCompletos.estudios);
            if (subAba) {
                const btn = document.querySelector(`#sub-abas-estudios .sub-aba-btn[data-sub-aba="${subAba}"]`);
                if (btn) btn.click();
            }
        }
    } catch (e) {
        mostrarErro(`Erro ao renderizar módulo ${modulo}`, e, dadosCompletos);
    }
}

botoesModulo.forEach(btn => {
    btn.addEventListener('click', () => {
        botoesModulo.forEach(b => b.classList.remove('ativo'));
        btn.classList.add('ativo');
        moduloAtivo = btn.dataset.modulo;
        subAbaAtiva = null;
        updateHash(moduloAtivo);
        exibirModulo(moduloAtivo);
    });
});

window.addEventListener('popstate', () => {
    const { modulo, subAba } = parseHash();
    moduloAtivo = modulo;
    subAbaAtiva = subAba;
    botoesModulo.forEach(btn => {
        btn.classList.remove('ativo');
        if (btn.dataset.modulo === moduloAtivo) {
            btn.classList.add('ativo');
        }
    });
    exibirModulo(moduloAtivo, subAbaAtiva);
});

iniciar();
