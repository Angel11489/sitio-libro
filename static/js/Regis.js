document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const email = form.querySelector("input[type='email']");
    const password = form.querySelectorAll("input[type='password']")[0];
    const confirmPassword = form.querySelectorAll("input[type='password']")[1];

    if (form) {
        form.addEventListener("submit", function(event) {
            event.preventDefault();

            const name = form.querySelector("input[name='nombre']").value;
            const email = form.querySelector("input[name='correo']").value;
            const password = form.querySelector("input[name='contraseña']").value;
            const confirmPassword = form.querySelector("input[name='contraseña_confirm']").value;

            if (password !== confirmPassword) {
                alert("Las contraseñas no coinciden. Por favor, verifica.");
                return;
            }

            const dataToSend = {
                nombre: name,
                correo: email,
                contraseña: password
            };

            fetch('/registro/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrftoken
                    },
                    body: JSON.stringify(dataToSend)
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert("✅ ¡Registro exitoso! Redireccionando...");
                        window.location.href = '/bienvenida/';
                    } else {
                        alert("❌ Error de registro: " + data.errors.join(', '));
                    }
                })
                .catch(error => {
                    console.error('Hubo un problema con la solicitud:', error);
                    alert('Ocurrió un error de conexión.');
                });
            alert("✅ ¡Registro exitoso! Te damos la bienevenida a la comunidad de Coco_Crochet");
            form.reset();
        });
    }
});