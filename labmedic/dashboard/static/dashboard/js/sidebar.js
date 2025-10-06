document.addEventListener("DOMContentLoaded", function () {
    const sidebar = document.getElementById("sidebarMenu");
    const toggleBtn = document.getElementById("sidebarToggle");

    if (!sidebar || !toggleBtn) return; // Evita errores si no existen

    // Función para alternar colapsado/expandido
    function toggleSidebar() {
        const isMobile = window.innerWidth <= 768;

        if (isMobile) {
            // En móvil, mostrar/ocultar completamente
            sidebar.classList.toggle("show");
        } else {
            // En escritorio, colapsar/expandir
            sidebar.classList.toggle("collapsed");
            localStorage.setItem(
                "sidebar-collapsed",
                sidebar.classList.contains("collapsed")
            );
        }
    }

    // Evento click en el botón
    toggleBtn.addEventListener("click", toggleSidebar);

    // Restaurar estado en escritorio
    if (window.innerWidth > 768 && localStorage.getItem("sidebar-collapsed") === "true") {
        sidebar.classList.add("collapsed");
    }

    // Ajustar al cambiar tamaño de ventana
    window.addEventListener("resize", function () {
        if (window.innerWidth <= 768) {
            sidebar.classList.remove("collapsed");
            localStorage.removeItem("sidebar-collapsed");
        }
    });
});
