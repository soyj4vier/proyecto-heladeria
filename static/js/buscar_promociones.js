$(document).ready(function () {
    $('#search-btn').click(function () {
        const query = $('#search-input').val(); // Obtener el valor del campo de búsqueda

        // Realizar la solicitud AJAX
        $.ajax({
            url: '/buscar_promociones/', // URL del endpoint de búsqueda
            type: 'GET',
            data: { q: query }, // Enviar el término de búsqueda como parámetro
            success: function (data) {
                // Actualizar la tabla con los resultados
                let tbody = '';
                if (data.promociones.length > 0) {
                    data.promociones.forEach(promo => {
                        tbody += `
                            <tr>
                                <td>${promo.id}</td>
                                <td>${promo.nombre}</td>
                                <td>${promo.descripcion}</td>
                                <td>${promo.fecha_inicio}</td>
                                <td>${promo.fecha_fin}</td>
                                <td>${promo.activo ? 'Sí' : 'No'}</td>
                                <td>
                                    <a href="/promocionesmodificado/${promo.id}" class="btn btn-info">Modificar</a>
                                    <a href="/promocioneseliminar/${promo.id}" class="btn btn-danger" onclick="return confirm('¿Estás seguro de que deseas eliminar esta promoción?');">Eliminar</a>
                                </td>
                            </tr>
                        `;
                    });
                } else {
                    tbody = `
                        <tr>
                            <td colspan="7" class="text-center">No se encontraron promociones.</td>
                        </tr>
                    `;
                }
                $('tbody').html(tbody); // Actualizar el contenido de la tabla
            },
            error: function () {
                alert('Error al buscar promociones.');
            }
        });
    });
});