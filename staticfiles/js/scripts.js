 // Scroll Animation
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

      // Smooth scroll for anchor links
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
    });

    // Header scroll effect
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