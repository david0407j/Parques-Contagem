document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal com IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('show');
                entry.target.classList.add('visible');
                
                // Tratamento especial para imagens com zoom
                if (entry.target.classList.contains('zoom-on-scroll')) {
                    entry.target.classList.remove('zoom-hidden');
                }
            }
        });
    }, {
        threshold: 0.1
    });

    // Observar todos os elementos com classes relevantes
    document.querySelectorAll('.hidden, .zoom-on-scroll').forEach(el => {
        if (el.classList.contains('zoom-on-scroll')) {
            el.classList.add('zoom-hidden');
        }
        observer.observe(el);
    });

    // Scroll suave para âncoras
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Efeito no header ao rolar
    window.addEventListener('scroll', () => {
        const header = document.querySelector('header');
        if (header) {
            if (window.scrollY > 50) {
                header.style.boxShadow = '0 4px 12px rgba(58, 74, 20, 0.3)';
                header.style.padding = '1rem 2rem';
            } else {
                header.style.boxShadow = 'var(--sombra)';
                header.style.padding = '1.5rem 2rem';
            }
        }
    });
});