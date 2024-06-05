document.addEventListener('DOMContentLoaded', function() {
    const sliders = document.querySelectorAll('.slider');
    
    sliders.forEach(slider => {
        const slides = slider.querySelectorAll('.slide');
        let currentSlide = 0;

        // Show the initial slide
        showSlide(slides, currentSlide);

        // Event listeners for slide buttons
        slider.querySelector('.prev-slide').addEventListener('click', function() {
            currentSlide = (currentSlide - 1 + slides.length) % slides.length;
            showSlide(slides, currentSlide);
        });

        slider.querySelector('.next-slide').addEventListener('click', function() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(slides, currentSlide);
        });
    });

    // Function to show a specific slide
    function showSlide(slides, index) {
        slides.forEach((slide, i) => {
            slide.classList.remove('active');
            if (i === index) {
                slide.classList.add('active');
            }
        });
    }
});
