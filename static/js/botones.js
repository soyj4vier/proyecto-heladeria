$('#btn-save').click(function(event) {
    event.preventDefault();

    Swal.fire({
        title: "Correcto!",
        text: "El cliente fue agregado correctamente.",
        icon: "success",
        confirmButtonText: "Aceptar"
    }).then(() => {
        $('form').submit();
    });
});
