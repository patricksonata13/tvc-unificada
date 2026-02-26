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

// Verifica se o usuário está logado via meta tag
const metaLogged = document.querySelector('meta[name="logged-in"]');
if (metaLogged) {
    loggedIn = metaLogged.content === 'true';
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

async function iniciar() {
    dadosCompletos = await carregarDados();
    if (!dadosCompletos) {
        conteudoModulo.innerHTML = '<p class="loading">Erro ao carregar dados.</p>';
        return;
    }

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
}

function exibirModulo(modulo, subAba = null) {
    if (!dadosCompletos) return;

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

    // Anexa eventos de sub-aba (apenas para módulos que têm sub-abas)
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
