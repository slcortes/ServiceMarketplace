$(document).ready(function() {

    //Construct final time format
    var date = new Date($('#final_time').text());
    var end_date = '';
    end_date += date.getFullYear() + '/';
    end_date += dateLengthOne((date.getMonth() + 1)) + '/';
    end_date += dateLengthOne(date.getDate()) + ' ';
    end_date += date.getHours() + ':';
    end_date += date.getMinutes() + ':';
    end_date += date.getSeconds();

    //Countdown
    $('#clock').countdown(end_date)
    .on('update.countdown', function(event) {
        var format = '';
        if(event.offset.seconds > 0) {
            format = '%Ss ' + format;
        }
        if(event.offset.minutes > 0) {
            format = '%Mm ' + format;
        }
        if(event.offset.hours > 0) {
            format = '%Hh ' + format;
        }
        if(event.offset.days > 0) {
            format = '%-Dd ' + format;
        }
        $(this).html(event.strftime(format));
    })
    .on('finish.countdown', function(event) {
        $(this).html('This offer has expired!')
        .parent().addClass('disabled');

    });

});

//Add 0 before month and date if it is one digit
function dateLengthOne(date) {
    if (date.toString().length == 1) {
        return '0' + date;
    }
    return date;
}
