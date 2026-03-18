document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Reset all buttons
            filterButtons.forEach(btn => {
                btn.classList.remove('active', 'bg-blue-600', 'text-white');
                btn.classList.add('bg-gray-200', 'hover:bg-gray-300');
            });
            
            // Set active state on clicked button
            this.classList.add('active', 'bg-blue-600', 'text-white');
            this.classList.remove('bg-gray-200', 'hover:bg-gray-300');
            
            // Get filter value and filter cards
            const filterValue = this.getAttribute('data-filter');
            console.log('Filtering by:', filterValue);
            
            projectCards.forEach(card => {
                const tags = card.getAttribute('data-tags').toLowerCase().split(' ');
                const isVisible = filterValue === 'all' || tags.includes(filterValue);
                card.style.display = isVisible ? 'block' : 'none';
                if (isVisible) card.classList.add('animate-fade-in');
            });
        });
    });

    // Intersection Observer for scroll animations
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    // Observe all project cards
    projectCards.forEach(card => observer.observe(card));
    
    console.log('Portfolio initialization complete');
});