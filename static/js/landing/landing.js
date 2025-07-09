document.addEventListener('DOMContentLoaded', () => {
            const carouselInner = document.querySelector('.banner-carousel .carousel-inner');
            const carouselItems = document.querySelectorAll('.banner-carousel .carousel-item');
            const prevBtn = document.querySelector('.banner-carousel .carousel-control.prev');
            const nextBtn = document.querySelector('.banner-carousel .carousel-control.next');
            let currentIndex = 0;
            const totalItems = carouselItems.length;

            function updateCarousel() {
                const offset = -currentIndex * 100;
                carouselInner.style.transform = `translateX(${offset}%)`;
            }

            if (prevBtn && nextBtn) { // Verifica se os botões existem para evitar erros
                prevBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex > 0) ? currentIndex - 1 : totalItems - 1;
                    updateCarousel();
                });

                nextBtn.addEventListener('click', () => {
                    currentIndex = (currentIndex < totalItems - 1) ? currentIndex + 1 : 0;
                    updateCarousel();
                });
            }


            // Auto-play (opcional)
            setInterval(() => {
                currentIndex = (currentIndex < totalItems - 1) ? currentIndex + 1 : 0;
                updateCarousel();
            }, 5000); // Muda a cada 5 segundos
        });

        // Controle de Quantidade
        document.addEventListener('DOMContentLoaded', () => {
            const quantityControls = document.querySelectorAll('.quantity-control');

            quantityControls.forEach(control => {
                const minusBtn = control.querySelector('.minus');
                const plusBtn = control.querySelector('.plus');
                const quantityInput = control.querySelector('.quantity-input');

                minusBtn.addEventListener('click', () => {
                    let currentValue = parseInt(quantityInput.value);
                    if (currentValue > 1) {
                        quantityInput.value = currentValue - 1;
                    }
                });

                plusBtn.addEventListener('click', () => {
                    let currentValue = parseInt(quantityInput.value);
                    quantityInput.value = currentValue + 1;
                });
            });
        });

        // Carrosséis de Produtos e Marcas
        document.addEventListener('DOMContentLoaded', () => {
            function initializeCarousel(containerSelector, itemSelector, prevBtnSelector, nextBtnSelector) {
                const container = document.querySelector(containerSelector);
                if (!container) return; // Exit if container doesn't exist

                const prevBtn = container.closest('.carousel-container').querySelector(prevBtnSelector);
                const nextBtn = container.closest('.carousel-container').querySelector(nextBtnSelector);
                let scrollAmount = 0;
                const scrollStep = 300; // Ajuste conforme a largura dos itens e espaçamento

                if (prevBtn && nextBtn) { // Verifica se os botões existem
                    prevBtn.addEventListener('click', () => {
                        scrollAmount -= scrollStep;
                        if (scrollAmount < 0) scrollAmount = 0;
                        container.scroll({
                            left: scrollAmount,
                            behavior: 'smooth'
                        });
                    });

                    nextBtn.addEventListener('click', () => {
                        scrollAmount += scrollStep;
                        // Previne scroll excessivo
                        const maxScroll = container.scrollWidth - container.clientWidth;
                        if (scrollAmount > maxScroll) scrollAmount = maxScroll;

                        container.scroll({
                            left: scrollAmount,
                            behavior: 'smooth'
                        });
                    });
                }
            }

            // Inicializa os carrosséis de produtos individualmente
            document.querySelectorAll('.product-carousel-section').forEach(section => {
                const productCarousel = section.querySelector('.product-carousel');
                if (productCarousel) {
                    initializeCarousel(
                        `.${productCarousel.classList[0]}`, // Usar a classe do próprio carrossel para o seletor
                        '.product-card',
                        '.prev-product-carousel',
                        '.next-product-carousel'
                    );
                }
            });

            // Inicializa o carrossel de marcas
            initializeCarousel('.brands-carousel', '.brand-item', '.prev-brand-carousel', '.next-brand-carousel');
        });


        // Funcionalidade "Ver Mais/Ver Menos" para Depoimentos