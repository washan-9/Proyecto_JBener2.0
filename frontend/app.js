/**
 * app.js - Lógica de UI (Fase 3/4)
 * Manejo del estado del layout, interacciones de modales, y sidebar.
 */

document.addEventListener('DOMContentLoaded', () => {
    console.log("Sistema de Diseño Inicializado - JBener 2.0");
    
    // Lógica para el toggle del sidebar en pantallas móviles
    const btnToggle = document.getElementById('btnToggleMenu');
    const sidebar = document.getElementById('appSidebar');

    if (btnToggle && sidebar) {
        btnToggle.addEventListener('click', () => {
            sidebar.classList.toggle('active');
        });

        // Ocultar sidebar al hacer click fuera en móviles
        document.addEventListener('click', (event) => {
            if (window.innerWidth <= 768) {
                const isClickInsideSidebar = sidebar.contains(event.target);
                const isClickOnToggle = btnToggle.contains(event.target);

                if (!isClickInsideSidebar && !isClickOnToggle && sidebar.classList.contains('active')) {
                    sidebar.classList.remove('active');
                }
            }
        });
    }
});
