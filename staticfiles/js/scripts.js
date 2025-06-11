<script>
  document.addEventListener('DOMContentLoaded', () => {
    // Scroll Reveal com IntersectionObserver
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('show');
        }
      });
    }, {
      threshold: 0.1
    });

    const hiddenElements = document.querySelectorAll('.hidden');
    hiddenElements.forEach(el => observer.observe(el));

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
      if (window.scrollY > 50) {
        header.style.boxShadow = '0 4px 12px rgba(58, 74, 20, 0.3)';
        header.style.padding = '1rem 2rem';
      } else {
        header.style.boxShadow = 'var(--sombra)';
        header.style.padding = '1.5rem 2rem';
      }
    });
    // Observador de interseção para animações
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.hidden').forEach(el => {
            observer.observe(el);
        });
    });
     // Ativa animações quando o elemento aparece na tela
    document.addEventListener('DOMContentLoaded', function() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, { threshold: 0.1 });
        
        document.querySelectorAll('.hidden').forEach(el => {
            observer.observe(el);
        });
    });
=======

      // Mostrar ou esconder botão "Voltar ao Topo"
      const topBtn = document.querySelector('#scrollToTopBtn');
      if (topBtn) {
        topBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
      }
    });
