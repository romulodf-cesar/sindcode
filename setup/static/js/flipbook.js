// static/js/flipbook.js

document.addEventListener('DOMContentLoaded', () => {
    const pages = document.querySelectorAll('.page');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    // Todas as páginas, exceto a primeira, devem estar inicialmente "viradas" para trás
    // (ou seja, terem a classe flipped)
    for (let i = 1; i < pages.length; i++) {
        pages[i].classList.add('flipped');
    }

    let currentPage = 1; // Começa na capa (p1)

    function updatePages() {
        // Virar para a frente (navegação para trás)
        // Se a página atual é 3, e o usuário clica em 'Anterior', a página 2 vira para a frente.
        for (let i = 0; i < currentPage - 1; i++) {
            pages[i].classList.remove('flipped');
        }

        // Virar para trás (navegação para frente)
        // Se a página atual é 1, e o usuário clica em 'Próximo', a página 1 vira para trás.
        for (let i = currentPage - 1; i < pages.length; i++) {
            pages[i].classList.add('flipped');
        }

        // Habilitar/Desabilitar botões
        prevBtn.disabled = currentPage === 1;
        nextBtn.disabled = currentPage === pages.length;
    }

    prevBtn.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            updatePages();
        }
    });

    nextBtn.addEventListener('click', () => {
        if (currentPage < pages.length) {
            currentPage++;
            updatePages();
        }
    });

    updatePages(); // Inicializa o estado
});