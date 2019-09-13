  $(document).ready(function() {

          alert("hola87");
          /*$('#YOUR_FORM').submit(function() { // catch the form's submit event
            $.ajax({ // create an AJAX call...
                data: $(this).serialize(), // get the form data
                type: $(this).attr('method'), // GET or POST
                url: $(this).attr('action'), // the file to call
                success: function(response) { // on success..
                    $('#DIV_CONTAINING_FORM').html(response); // update the DIV 
                }
            });
            return false;
        });*/
    });

//MODAL CON DIALOG DE JQUERY
      var modal;

function abrir_dialog(url, titulo)
{
    
    modal = $('#popup').dialog(
    {
        title: titulo,
        modal: true,
        //width: 1000,
        //width:'auto',
        position:['middle',30],
        //position: [500,0],
        width: "75%",
        maxWidth: "768px",
        resizable: false
    }).dialog('open').load(url)
}

function cerrar_dialog()
{
    modal.dialog("close");
}

//MODAL CON MODAL DE BOOTSTRAP      
function abrir_modal(url)
{
        //alert(url);
       
        $('#popup1').load(url, function()
        {
                $(this).modal('show');
                //$(this).draggable({handle: ".modal-header"});//movible
        });
        return false;
}

function cerrar_modal()
{
        $('#popup1').modal('hide');
        return false;
}


 
