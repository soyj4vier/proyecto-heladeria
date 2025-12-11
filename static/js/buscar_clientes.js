$(document).ready(function () {
    $('#search-btn').click(function () {
        const query = $('#search-input').val(); // Obtener el valor del campo de búsqueda
        console.log('Buscando clientes con el término:', query); // Log para verificar el término de búsqueda

        // Realizar la solicitud AJAX
        $.ajax({
            url: '/buscar_clientes/', // URL del endpoint de búsqueda
            type: 'GET',
            data: { q: query }, // Enviar el término de búsqueda como parámetro
            success: function (data) {
                console.log('Datos recibidos del servidor:', data); // Log para verificar los datos recibidos
                let tbody = '';
                if (data.clientes.length > 0) {
                    data.clientes.forEach(cliente => {
                        const modificarUrl = `/clientemodificado/${cliente.run}`; // URL corregida
                        const eliminarUrl = `/clienteeliminar/${cliente.run}`;
                        console.log('Generando URLs:', { modificarUrl, eliminarUrl }); // Log para verificar las URLs generadas

                        tbody += `
                            <tr>
                                <td>${cliente.run}</td>
                                <td>${cliente.nombre}</td>
                                <td>${cliente.apellido_paterno}</td>
                                <td>${cliente.apellido_materno}</td>
                                <td>${cliente.puntos}</td>
                                <td>
                                    <a href="${modificarUrl}" class="btn btn-info">Modificar</a>
                                    <a href="${eliminarUrl}" class="btn btn-danger" onclick="return confirm('¿Estás seguro de que deseas eliminar este cliente?');">Eliminar</a>
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
                console.error('Error al buscar clientes.'); // Log para errores en la solicitud AJAX
                alert('Error al buscar clientes.');
            }
        });
    });
});