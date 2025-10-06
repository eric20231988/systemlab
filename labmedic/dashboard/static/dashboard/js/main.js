// Inicialización global del dashboard
document.addEventListener("DOMContentLoaded", () => {
    console.info("✅ Dashboard inicializado");

    // Inicializar componentes de Bootstrap
    initTooltips();
    initPopovers();

    // Mensaje de bienvenida (solo la primera vez)
    mostrarBienvenida();

    // Ajustar altura del contenido principal
    ajustarAlturaContenido();
});

/**
 * Inicializa todos los tooltips de Bootstrap en la página
 */
function initTooltips() {
    const tooltipElements = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    if (tooltipElements.length) {
        tooltipElements.forEach(el => new bootstrap.Tooltip(el));
        console.debug(`🛈 Tooltips inicializados: ${tooltipElements.length}`);
    }
}

/**
 * Inicializa todos los popovers de Bootstrap en la página
 */
function initPopovers() {
    const popoverElements = document.querySelectorAll('[data-bs-toggle="popover"]');
    if (popoverElements.length) {
        popoverElements.forEach(el => new bootstrap.Popover(el));
        console.debug(`🛈 Popovers inicializados: ${popoverElements.length}`);
    }
}

/**
 * Muestra un mensaje de bienvenida en consola solo la primera vez
 */
function mostrarBienvenida() {
    if (!localStorage.getItem("bienvenidaMostrada")) {
        console.log("👋 Bienvenido al sistema de laboratorio clínico");
        localStorage.setItem("bienvenidaMostrada", "true");
    }
}

/**
 * Ajusta la altura mínima del contenido para que el footer quede al final
 */
function ajustarAlturaContenido() {
    const mainContent = document.querySelector("main");
    if (!mainContent) return;

    const recalcularAltura = () => {
        const alturaVentana = window.innerHeight;
        const alturaHeader = document.querySelector("header")?.offsetHeight || 0;
        const alturaFooter = document.querySelector("footer")?.offsetHeight || 0;
        mainContent.style.minHeight = `${alturaVentana - alturaHeader - alturaFooter}px`;
    };

    // Calcular al inicio
    recalcularAltura();

    // Recalcular en resize con requestAnimationFrame para suavidad
    window.addEventListener("resize", () => {
        window.requestAnimationFrame(recalcularAltura);
    });
}
