  document.addEventListener('DOMContentLoaded', () => {
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

      // Mostrar ou esconder botão "Voltar ao Topo"
      const topBtn = document.querySelector('#scrollToTopBtn');
      if (topBtn) {
        topBtn.style.display = window.scrollY > 300 ? 'block' : 'none';
      }
    });

    // Botão voltar ao topo
    const topBtn = document.createElement('button');
    topBtn.id = 'scrollToTopBtn';
    topBtn.innerHTML = '⬆';
    document.body.appendChild(topBtn);
    Object.assign(topBtn.style, {
      position: 'fixed',
      bottom: '20px',
      right: '20px',
      padding: '10px 15px',
      background: 'var(--cor-escura)',
      color: 'var(--cor-clara)',
      border: 'none',
      borderRadius: '50%',
      fontSize: '1.2rem',
      cursor: 'pointer',
      display: 'none',
      zIndex: 1000,
      transition: 'opacity 0.3s ease',
    });

    topBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Animação extra para imagens com classe .zoom-on-scroll
    const zoomElements = document.querySelectorAll('.zoom-on-scroll');
    zoomElements.forEach(img => {
      observer.observe(img);
      img.classList.add('zoom-hidden');
    });
  });
