$(document).ready(function() {
	

$("#pd").datepicker({
  dateFormat: "yy-mm-dd",
  changeMonth: true,
  changeYear: true
}).datepicker("setDate", new Date());
$("#md").datepicker({
  dateFormat: "yy-mm-dd",
  changeMonth: true,
  changeYear: true
})

	$("#btn-verrecep").click(function(){
		alert("hola");
	
    alert($('#hl').val()); 
  });


});
