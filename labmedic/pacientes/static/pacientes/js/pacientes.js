function activarPacienteRegistrado(pacienteId) {
  const msg = document.getElementById('mensaje-paciente');
  if (msg) {
    msg.innerHTML = `
      <div class="alert alert-success d-flex align-items-center" role="alert">
        <div class="fw-semibold">Paciente encontrado. Puede registrar la orden.</div>
      </div>`;
  }
}

function activarPacienteNoRegistrado(dni) {
  const msg = document.getElementById('mensaje-paciente');
  if (msg) {
    msg.innerHTML = `
      <div class="alert alert-warning d-flex align-items-center" role="alert">
        <div>No se encontró ningún paciente con DNI <strong>${dni}</strong>.</div>
      </div>`;
  }
}

function limpiarResultadoBusqueda() {
  const msg = document.getElementById('mensaje-paciente');
  if (msg) msg.innerHTML = '';
}

document.addEventListener("htmx:afterSwap", function (evt) {
  if (evt.detail.target.id === "tabla-pacientes") {
    const wrapper = document.getElementById("tabla-pacientes-wrapper");
    const status = wrapper?.dataset.status;
    const dni = wrapper?.dataset.dni;
    const pacienteId = wrapper?.dataset.pacienteId;

    const msg = document.getElementById("mensaje-paciente");
    const btn = document.getElementById("btn-registrar-orden");

    if (status === "found") {
      msg.innerHTML = `
        <div class="alert alert-success d-flex align-items-center" role="alert">
          <i class="bi bi-check-circle-fill me-2"></i>
          Paciente con DNI <strong>${dni}</strong> encontrado.
        </div>`;
      if (btn) {
        btn.style.display = "inline-block";
        btn.disabled = false;
        const baseUrl = btn.getAttribute("data-base-url");
        btn.onclick = () => window.location.href = baseUrl.replace("/0/", `/${pacienteId}/`);
      }
    } else if (status === "not_found") {
      msg.innerHTML = `
        <div class="alert alert-warning d-flex align-items-center" role="alert">
          <i class="bi bi-exclamation-triangle-fill me-2"></i>
          No se encontró ningún paciente con DNI <strong>${dni}</strong>.
        </div>`;
      if (btn) {
        btn.style.display = "none";
        btn.disabled = true;
        btn.onclick = null;
      }
    } else {
      // status === "empty"
      msg.innerHTML = "";
      if (btn) {
        btn.style.display = "none";
        btn.disabled = true;
        btn.onclick = null;
      }
    }
  }
});
