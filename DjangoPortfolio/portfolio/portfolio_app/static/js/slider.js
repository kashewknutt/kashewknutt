document.addEventListener('DOMContentLoaded', function() {
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    // Show the initial slide
    showSlide(currentSlide);

    // Event listeners for slide buttons
    document.querySelector('.prev-slide').addEventListener('click', function() {
        currentSlide = (currentSlide - 1 + slides.length) % slides.length;
        showSlide(currentSlide);
    });

    document.querySelector('.next-slide').addEventListener('click', function() {
        currentSlide = (currentSlide + 1) % slides.length;
        showSlide(currentSlide);
    });

    // Function to show a specific slide
    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }
});
