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

    bidding();

});

//Add 0 before month and date if it is one digit
function dateLengthOne(date) {
    if (date.toString().length == 1) {
        return '0' + date;
    }
    return date;
}

function bidding() {

    //Construct Firebase url
    var myDataRef = new Firebase('https://torrid-inferno-5445.firebaseio.com/' + window.location.pathname);

    //Get entered bid
    $('#submit').click(function (e) {
        checkAndPushBid();
    });
    $('#bidInput').keypress(function (e) {
      if (e.keyCode == 13) {
        checkAndPushBid();
      }
    });

    //Watch for bids and display new bid
    myDataRef.on('child_added', function(snapshot) {
      var message = snapshot.val();
      displayBid(message.bid);
    });

    //Check and push bid
    function checkAndPushBid(bid) {
        var submitted_bid = $('#bidInput').val();
        submitted_bid = parseFloat(submitted_bid, 10);
        
        var current_bid = $('#current_bid').text();
        current_bid = parseFloat(current_bid, 10);

        if ((submitted_bid < current_bid) && submitted_bid > 0) {
            myDataRef.push({bid: submitted_bid});
            $('#bidInput').val('');
            $("#error_bid").text('');
        } else if (submitted_bid < 0){
            $("#error_bid").text('Enter a bid greater than $0!');
        } else {
            $("#error_bid").text('Enter a bid lower than ' + current_bid + '!');
        }
    }

    //Display new bids
    function displayBid(bid) {
      $('#current_bid').text(bid);
    };

}
