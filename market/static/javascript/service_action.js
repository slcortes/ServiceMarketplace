$(document).ready(function() {

    //Datepicker widget
    $("#id_final_time_0").click(function () {
        $("#id_final_time_0").datepicker();
        $("#id_final_time_0").datepicker("show");
    });

    //Timepicker widget
    $("#id_final_time_1").click(function () {
        $("#id_final_time_1").timepicker();
        $("#id_final_time_1").timepicker("show");
    });
    
});
