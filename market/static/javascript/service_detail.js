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
        $.ajax({
            method: "GET",
            url: "/service/end/" + window.location.pathname.split("/")[2],
            dataType: "json",
            error: function(msg) {
                console.log(msg)
            }
        });
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
    function checkAndPushBid() {

        if ($("#clock").text() == "This offer has expired!") {
            return;
        }

        //If 0, push bid and close service
        if (parseFloat($('#bidInput').val()) == 0) {

            //Create and save new bid object
            $.ajax({
                method: "GET",
                url: "/bid/?bid=" + 0 + "&pk=" +
                window.location.pathname.split("/")[2],
                dataType: "json",
                error: function(msg) {
                    console.log(msg)
                }
            });

            //End bidding
            $.ajax({
                method: "GET",
                url: "/service/end/" + window.location.pathname.split("/")[2],
                dataType: "json",
                error: function(msg) {
                    console.log(msg)
                }
            });

            var end_date = new Date;
            var date = new Date(end_date.toISOString());
            end_date = '';
            end_date += date.getFullYear() + '/';
            end_date += dateLengthOne((date.getMonth() + 1)) + '/';
            end_date += dateLengthOne(date.getDate()) + ' ';
            end_date += date.getHours() + ':';
            end_date += date.getMinutes() + ':';
            end_date += date.getSeconds();
            $('#clock').countdown(end_date)
            .on('finish.countdown', function(event) {
                $(this).html('This offer has expired!')
                .parent().addClass('disabled');
            });

            myDataRef.push({bid: 0});
            return;
        }

        var invalid_format = false

        var submitted_bid = $('#bidInput').val();
        var submitted_bid_split = submitted_bid.split(".");
        if (submitted_bid_split.length == 2) {
            submitted_bid = submitted_bid_split[0] + "." +
            submitted_bid_split[1].substring(0,2);
        } else if (submitted_bid_split.length != 1) {
            invalid_format = true;
        }

        var current_bid = $('#current_bid').text();
        current_bid = parseFloat(current_bid, 10);
        submitted_bid = parseFloat(submitted_bid, 10);

        if ((submitted_bid < current_bid) && submitted_bid > 0 &&
        !invalid_format) {

            //Check if a zero needs to be added to the end
            submitted_bid_split = String(submitted_bid).split(".");
            if (submitted_bid_split.length != 1 &&
                submitted_bid_split[1].length == 1) {
                    submitted_bid = submitted_bid_split[0] + "." +
                    addZeroToEnd(submitted_bid_split[1]);
                }

                //Send bid
                myDataRef.push({bid: submitted_bid});

                $('#bidInput').val('');
                $("#error_bid").text('');

                //Add permission that they can review
                $.ajax({
                    method: "GET",
                    url: "/bidded/?username=" + $("#owner").text(),
                    dataType: "json",
                    error: function(msg) {
                        console.log(msg)
                    }
                });

                //Create and save new bid object
                $.ajax({
                    method: "GET",
                    url: "/bid/?bid=" + submitted_bid + "&pk=" +
                    window.location.pathname.split("/")[2],
                    dataType: "json",
                    error: function(msg) {
                        console.log(msg)
                    }
                });
            } else if (submitted_bid < 0){
                $("#error_bid").text('Enter a bid greater than $0!');
            } else if (invalid_format){
                $("#error_bid").text('Invalid Format!');
            } else {
                $("#error_bid").text('Enter a bid lower than ' + current_bid + '!');
            }
        }

        //Display new bids
        function displayBid(bid) {
            $('#current_bid').text(bid);
        };

        //Add zero to .x
        function addZeroToEnd(decimal) {
            return decimal + '0';
        }

    }
