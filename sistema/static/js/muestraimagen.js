
$(document).ready(function() {

          

          function readURL(input) {
              if (input.files && input.files[0]) {
                
              var reader = new FileReader();
            reader.onload = function(e) {
                     $("#bla").attr("src", e.target.result);
             }
            reader.readAsDataURL(input.files[0]);
           }
          }

          //$("#id_{{form.ruta.name}}").change(function() {//captura el change del boton que busca la imagen
          $($("#rutaimagen").val()).change(function() {//captura el change del boton que busca la imagen
            //alert($("#rutaimagen").val());
            //alert("{{form.ruta.name}}");
           readURL(this);
           $("#bla").show();
           });

});
     
$("#guarda1").click(function(){
        //alert("hola5");
        cod=$("#codigo").val()
        var frm = $('#FORM-ID');
        //alert(frm.serialize());
  // frm.submit(function () {



        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                //$('#popup1').html(data);
                alert("bien");
                alert(data);
                //$("#popup1").html(data);
                //alert(data[0][0]);

                $('#popup1').modal('hide');
                 window.location.href = "/serie/listar";
                
            },
            error: function(data) {
                alert("mal");
                //var objeto = JSON.parse(data);//lo convierte de json a objeto de js
                alert(data);
                 alert(data['status']);
                 alert(data.responseText)

                //errors = $.parseJSON(data.responseText);
                var error = JSON.parse(data.responseText);//lo convierte de json a objeto de js
               alert(error);/*
                        error_msg = '';

                        $.each(errors, function (key, data) {
                            $.each(data, function (key_array, data) {
                                error_msg += '<div class="row"><div class="col-md-4">'+ key + 
                                            '(' + data['code'] + ')</div><div class="col-md-8">' 
                                            + data['message'] + '</div></div>';
                            });
                        });
                 alert(data['code']);
                alert(data['message']);


                alert(error_msg);*/
                 //$('#popup1').remove();
      //  $('#popup1 .modal-dialog .modal-content .modal-body').prepend(
            //'<div id="id_save_dialog_message" class="alert alert-danger">' + error_msg + '</div>');
                 //var objeto = JSON.parse(data);//lo convierte de json a objeto de js
                 //alert(objeto);
                 /*var strErr = data.uno + '';  //make json object as string
                strErr = strErr.split(",").pop();
                alert(strErr);*/
                $("#popup1").html(data.responseText);
                $('#popup1').modal('show');
                //$('#popup1').html(data);
                 //$('#popup1').modal('show');
                //$("#MESSAGE-DIV").html("Something went wrong!");
            },
            fail: function(xhr, textStatus, errorThrown){
       alert('request failed');
    }
        });
        return false;
    //});
  
  });  

/*$("#guarda").click(function(){
  alert("hokk");

        var frm = $('#FORM-ID');
        //alert(frm.serialize());
  frm.submit(function () {



        $.ajax({
            type: frm.attr('method'),
            url: frm.attr('action'),
            data: frm.serialize(),
            success: function (data) {
                $('#popup1').html(data);
                alert("bien");

                $('#popup1').modal('show');
                //$("#SOME-DIV").html(data);
            },
            error: function(data) {
                alert("mal");
                //$("#MESSAGE-DIV").html("Something went wrong!");
            },
            fail: function(xhr, textStatus, errorThrown){
       alert('request failed');
    }
        });
        return false;
})

})*/