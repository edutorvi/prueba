$(document).ready(function() {
//$('#text-finicio').datetimepicker();
$( "#text-finicio" ).datepicker({
  dateFormat: "dd/mm/yy",
  changeMonth: true,
  changeYear: true
}).datepicker("setDate", new Date());

$( "#text-ffin" ).datepicker({
  dateFormat: "dd/mm/yy",
  changeMonth: true,
  changeYear: true
}).datepicker("setDate",new Date());

/*$('#text-ffin').timepicker();
$('#text-ffin').timepicker('setTime', '18:00');*/


//abrir reporte en una ventana popup
/*$("#btn-verrecep").click(function(){
    alert($('#idarea').val() +'--'+$('#text-finicio').val()+'--'+$('#text-ffin').val());
    
            var caracteristicas = "height=760,width=1024,scrollTo,resizable=1,scrollbars=1,location=0";
            varhref="MPDF7/report/report01.php?codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
            nueva=window.open(varhref, 'Popup', caracteristicas);
             
            return false;
        });*/

//abrir reporte en una ventana popup

$("#btn-verrecep").click(function(){
    //alert($('#idarea').val() +'--'+$('#text-hinicio').val()+'--'+$('#text-hfin').val());
   //varhref="MPDF7/report/recepcionadosmpdfver.php?codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
            
       /* $.post("MPDF7/report/tramitados.php",
                {
                    tipo:1,
                    codarea: $('#idarea').val(),
                    fechaini: $('#text-finicio').val(),
                    fechafin: $('#text-ffin').val(),
                    
                    
                },
            function(data, status){

                $('#rptarecep').html(data);
            });
                     */
            //return false;
  });

$("#btn-recepexcel").click(function(){
   // alert($('#idarea').val() +'--'+$('#text-finicio').val()+'--'+$('#text-ffin').val());
  /* var caracteristicas = "height=760,width=1024,scrollTo,resizable=1,scrollbars=1,location=0";
   //varhref="report/reporteexcel1.php?finicio=1&ffin=50";
   varhref="MPDF7/report/tramitados.php?tipo=2&codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
   nueva=window.open(varhref, '_top', caracteristicas);
   return false;*/
 });



$("#btn-receppdf").click(function(){
   //alert($('#idarea').val() +'--'+$('#text-finicio').val()+'--'+$('#text-ffin').val());
  /*  
            var caracteristicas = "height=760,width=1024,scrollTo,resizable=1,scrollbars=1,location=0";
            varhref="MPDF7/report/tramitados.php?tipo=3&codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
             //varhref="MPDF7/report/datawindow1.pdf"
            //varhref="MPDF7/report/reportempdf.php?finicio=1&ffin=10";
            
            //varhref="core/modules/index/view/reportes/widget-default.php?codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
            //varhref="index.php?view=reportes?codarea=" + $('#idarea').val() + "&fechaini=" + $('#text-finicio').val() + "&fechafin="+$('#text-ffin').val();
            nueva=window.open(varhref, 'Popup', caracteristicas);
                           
            //nueva=window.open(varhref,"_parent","width=760,height=1024");
            return false;*/
  });

$("#btn-imprime").click(function(){
   /* $("#rptarecep").print();
    return (false);*/
});

});