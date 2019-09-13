$(document).ready(function() {
  //alert("jola ajax")
	//$('#dataTable').DataTable();//de la tabla responsive
//alert("reporte");
 /***** PARA LLENAR LA LISTA***/
cod=$("#codigo").val()
 $.ajax({
    type: 'POST',
   
    url: '/ejemplar/listartipoe',
  //data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
    data:{csrfmiddlewaretoken: cod},
    success: function(data, textStatus ){
     
     // $('#dataTable tbody > tr').remove();
      
      contenido="";
      for (var i = 0; i < data.length; i++) {

        contenido=contenido +'<option value="'+data[i].nombre+'">'+data[i].nombre+'</option>';
                
      }
      $("#lista").append(contenido);
      //alert(contenido);
     
     
    },
    fail: function(xhr, textStatus, errorThrown){
       alert('request failed');
    }

})
 /***** PARA LLENAR LA LISTA***/
/***** PARA LLENAR LA TABLA***/





//cabecera="<thead><tr><th>Nombre</th><th>Año</th><th>&nbsp</th><th>&nbsp</th></tr></thead><tfoot><th>&nbsp</th><th>&nbsp</th><th>&nbsp</th><th>&nbsp</th></tfoot>";
cabecera="<thead><tr><th>Siglo</th><th>Fecha</th><th>Descripción</th></tr></thead> <tfoot><th>&nbsp</th><th>&nbsp</th><th>&nbsp</th></tfoot>";
$("#dataTable").append(cabecera);                


var vartipo = "La aurora";
 $.ajax({
    //type: 'GET',
      type: 'POST',
    url: '/ejemplar/listarfiltroe',
    data: {'tipo': vartipo,
            csrfmiddlewaretoken: cod
          },
   // timeout: 5000,
    success: function(data, textStatus ){
      //alert(data);
     // alert(data.length);
      //var objeto = JSON.parse(data);//lo convierte de json a objeto de js
      
     // alert(data[1].nombre);
     
      /*for (var i = 0; i < data.length; i++) {
        
        alert("Nombre: "+data[i].nombre + "Año: "+data[i].anio  + "id: "+data[i].id);
      }*/
      //$("#dataTable").remove();
      //$('#dataTable tbody > tr').remove();


      // $("#dataTable").reset();
      //$("#dataTable tbody").empty();

      /*contenido="";
      for (var i = 0; i < data.length; i++) {
        contenido = contenido + "<tr>  <td>"+ data[i].nombre +"</td><td>"+ data[i].anio
         +"<td> <a href='/foto/actualiza/"+data[i].id
         +"'>modificar</a> </td> <td> <a href='/foto/elimina/"+data[i].id+"'>eliminar</a> </td>";
        
      }*/
      //alert(contenido);
      //$("#dataTable").append(contenido);
      table =$('#dataTable').DataTable({

        

        language: {
        "decimal": "",
        "emptyTable": "No hay información",
        "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
        "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
        "infoFiltered": "(Filtrado de _MAX_ total registros)",
        "infoPostFix": "",
        "thousands": ",",
        "lengthMenu": "Mostrar _MENU_ Registros",
        "loadingRecords": "Cargando...",
        "processing": "Procesando...",
        "search": "Buscar:",
        "zeroRecords": "Sin resultados encontrados",
        "paginate": {
            "first": "Primero",
            "last": "Ultimo",
            "next": "Siguiente",
            "previous": "Anterior"
                  }
         },
      
      data: data, // aqui inicializo el datatable con la data.
      columns: [{
          data: 'siglo'
        },
        {
          data: 'fecha'
        },
        {
          data: 'descripcion'
        },
        
       

      ],

    });//fin datatable

     

      //$('#dataTable').DataTable();
     
     // $('#dataTable').DataTable();//de la tabla responsive
    },
    fail: function(xhr, textStatus, errorThrown){
       alert('request failed');
    }

})
 /***** PARA LLENAR LA TABLA***/
 
$("#lista").change(function () {
 //table.destroy();
            
        //alert("hola5");
      var vartipo = $(this).val();
        //alert(vartipo);

            
      /*$.ajax({
          url: '/foto/listarfiltro/',
          
          data: {tipo: vartipo},
          success: function (data) {
             alert("kkk");
          }

      });*/



      /*$.ajax({
              url: '/foto/listarfiltro',
              data: {'tipo': vartipo, 'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()},
              // la verdad no recuerdo el nombre de el input con el token, pero verificalo
              //csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
              //$('csrfmiddlewaretoken').val()
              type: 'POST',
              processData:false,
              contentType:false,

              success: function(data) {
                  alert("que");
              },
          fail: function(xhr, textStatus, errorThrown){
             alert('request failed');
          }
          })*/
      /***** PARA LLENAR LA TABLA***/
       $.ajax({
          //type: 'GET',
            type:'POST',
          url: '/ejemplar/listarfiltroe',
          
          data: {'tipo': vartipo,
            csrfmiddlewaretoken: cod
          },
         // timeout: 5000,
          success: function(data, textStatus ){
            //alert(data);
           // alert(data.length);
            //var objeto = JSON.parse(data);//lo convierte de json a objeto de js
            
           // alert(data[1].nombre);
           
            /*for (var i = 0; i < data.length; i++) {
              
              alert("Nombre: "+data[i].nombre + "Año: "+data[i].anio  + "id: "+data[i].id);
            }*/
            //$("#dataTable").remove();
            //$('#dataTable tbody > tr').remove();
           //$("#dataTable").empty();
      //cabecera="<thead><tr><th>Nombre</th><th>Año</th><th>&nbsp</th><th>&nbsp</th></tr></thead><tfoot><th>&nbsp</th><th>&nbsp</th><th>&nbsp</th><th>&nbsp</th></tfoot>";
      //$("#dataTable").append(cabecera); 
            //$("#dataTable tbody").empty();

            /*contenido="";
            for (var i = 0; i < data.length; i++) {
              contenido = contenido + "<tr>  <td>"+ data[i].nombre +"</td><td>"+ data[i].anio
               +"<td> <a href='/foto/actualiza/"+data[i].id
               +"'>modificar</a> </td> <td> <a href='/foto/elimina/"+data[i].id+"'>eliminar</a> </td>";
              
            }*/
            //alert(contenido);
          
           table.clear().draw();//borramos la data anterior
          
           for (var i = 0; i < data.length; i++) {

              table.row.add( {"siglo": data[i].siglo, "fecha":  data[i].fecha, "descripcion":   data[i].descripcion } ).draw();//cargamos nueva data por filas
              
            }
             // Add new data


            /*table = $('#dataTable').DataTable({
            
            language: {
            "decimal": "",
            "emptyTable": "No hay información",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ Entradas",
            "infoEmpty": "Mostrando 0 to 0 of 0 Entradas",
            "infoFiltered": "(Filtrado de _MAX_ total entradas)",
            "infoPostFix": "",
            "thousands": ",",
            "lengthMenu": "Mostrar _MENU_ Entradas",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar:",
            "zeroRecords": "Sin resultados encontrados",
            "paginate": {
                "first": "Primero",
                "last": "Ultimo",
                "next": "Siguiente",
                "previous": "Anterior"
                      }
             },
            data: data, // aqui inicializo el datatable con la data.
            columns: [{
                data: 'nombre'
              },
              {
                data: 'anio'
              },
              {
                              data: null,
                              defaultContent: '<a href="#" class="edit">Edit</a> / <a href="#" class="remove">Delete</a>'
                          },
             
             

            ],

          });*///fin datatable

           
          },//success

          fail: function(xhr, textStatus, errorThrown){
             alert('request failed');
          }

      })
       /***** PARA LLENAR LA TABLA***/


      //alert("ojo");


      /*$.ajax({

          url: "/foto/listarfiltro"

      }).done( function() {

          alert( 'Success!!' );

      }).fail( function() {

          alert( "Error" );

      }).always( function() {

          alert( 'Always' );

      });*/
      //alert('jjj1');


      /*
      contenido="";
      for (var i = 0; i < data.length; i++) {
        contenido = contenido + "<tr>  <td>"+ data[i].nombre +"</td><td>"+ data[i].anio +"</td> <td> </td>    <td>  </td>  </tr>";
         
        }
      alert("hola");

      $('#dataTable').append*/



          
  

});//lista


$("#btn1").click(function(){
 
  //window.location.href = "/foto/reportepdf/"+$("#lista").val();
   window.open("/ejemplar/reportepdf/"+$("#lista").val(),'_blank');

 });
$("#btn2").click(function(){
  //alert("boton7");
  //window.open("/foto/reporte_fotos_excel/");
  // window.location.href = "/foto/reporte_fotos_excel/";
  alert($("#lista").val());
   //window.location.href = "/foto/reporte_fotos_excel/"+$("#lista").val();


 });




});//ready
