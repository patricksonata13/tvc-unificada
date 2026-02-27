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

function parseHash() {
    try {
        const hash = window.location.hash.slice(1);
        if (!hash) return { modulo: 'escaleta', subAba: null };
        const partes = hash.split('/');
        const modulo = partes[0] || 'escaleta';
        const subAba = partes[1] || null;
        return { modulo, subAba };
    } catch (e) {
        mostrarErro('Erro no parseHash: ' + e.message);
        return { modulo: 'escaleta', subAba: null };
    }
}

function updateHash(modulo, subAba = '') {
    try {
        const hash = subAba ? `#${modulo}/${subAba}` : `#${modulo}`;
        history.pushState(null, '', hash);
    } catch (e) {
        mostrarErro('Erro no updateHash: ' + e.message);
    }
}

function mostrarErro(msg) {
    console.error(msg);
    conteudoModulo.innerHTML = `<div style="color:red; padding:2rem; background:#ffeeee; border:2px solid red; border-radius:8px;">
        <strong>ERRO:</strong> ${msg}
    </div>`;
}

async function iniciar() {
    try {
        console.log('Iniciando...');
        dadosCompletos = await carregarDados();
        console.log('Dados recebidos:', dadosCompletos);
        if (!dadosCompletos) {
            conteudoModulo.innerHTML = '<p class="loading">Erro ao carregar dados (resposta vazia).</p>';
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
    } catch (e) {
        mostrarErro('Erro no iniciar: ' + e.message + ' - Stack: ' + e.stack);
    }
}

function exibirModulo(modulo, subAba = null) {
    try {
        console.log('Exibindo módulo:', modulo, 'subAba:', subAba);
        if (!dadosCompletos) {
            mostrarErro('dadosCompletos é null');
            return;
        }

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
        console.log('HTML injetado para', modulo);

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
        mostrarErro('Erro em exibirModulo: ' + e.message + ' - Stack: ' + e.stack);
    }
}

botoesModulo.forEach(btn => {
    btn.addEventListener('click', () => {
        try {
            botoesModulo.forEach(b => b.classList.remove('ativo'));
            btn.classList.add('ativo');
            moduloAtivo = btn.dataset.modulo;
            subAbaAtiva = null;
            updateHash(moduloAtivo);
            exibirModulo(moduloAtivo);
        } catch (e) {
            mostrarErro('Erro no clique: ' + e.message);
        }
    });
});

window.addEventListener('popstate', () => {
    try {
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
    } catch (e) {
        mostrarErro('Erro no popstate: ' + e.message);
    }
});

iniciar();
