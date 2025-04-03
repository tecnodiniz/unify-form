// Script para o sistema de formulários unificados

document.addEventListener('DOMContentLoaded', function() {
    // Animações para elementos da página
    const animateElements = document.querySelectorAll('.card, .hero-section, .feature-card');
    animateElements.forEach(function(element, index) {
        setTimeout(function() {
            element.classList.add('fade-in');
        }, index * 100);
    });

    // Efeito de hover nos botões
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(function(button) {
        button.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 5px 12px rgba(0, 0, 0, 0.15)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 3px 6px rgba(0, 0, 0, 0.1)';
        });
    });

    // Animar cards ao passar o mouse
    const cards = document.querySelectorAll('.card, .feature-card');
    cards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 1rem 2rem rgba(0, 0, 0, 0.15)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 0.5rem 1rem rgba(0, 0, 0, 0.15)';
        });
    });
});
