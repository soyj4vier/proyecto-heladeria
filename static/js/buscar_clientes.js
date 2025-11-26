$(document).ready(function () {
    $('#search-btn').click(function () {
        const query = $('#search-input').val(); // Obtener el valor del campo de búsqueda

        // Realizar la solicitud AJAX
        $.ajax({
            url: '/buscar_clientes/', // URL del endpoint de búsqueda
            type: 'GET',
            data: { q: query }, // Enviar el término de búsqueda como parámetro
            success: function (data) {
                // Actualizar la tabla con los resultados
                let tbody = '';
                if (data.clientes.length > 0) {
                    data.clientes.forEach(cliente => {
                        tbody += `
                            <tr>
                                <td>${cliente.run}</td>
                                <td>${cliente.nombre}</td>
                                <td>${cliente.apellido_paterno}</td>
                                <td>${cliente.apellido_materno}</td>
                                <td>${cliente.puntos}</td>
                                <td>
                                    <a href="/modificarcliente/${cliente.run}" class="btn btn-info">Modificar</a>
                                    <a href="/eliminarcliente/${cliente.run}" class="btn btn-danger" onclick="return confirm('¿Estás seguro de que deseas eliminar este cliente?');">Eliminar</a>
                                </td>
                            </tr>
                        `;
                    });
                } else {
                    tbody = `
                        <tr>
                            <td colspan="6" class="text-center">No se encontraron clientes.</td>
                        </tr>
                    `;
                }
                $('tbody').html(tbody); // Actualizar el contenido de la tabla
            },
            error: function () {
                alert('Error al buscar clientes.');
            }
        });
    });
});