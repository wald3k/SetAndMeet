
$(function(){
    var is_rated = false;
    var clicked_button = 0;
    $('.event_rating-select .btn').on('mouseover', function(){
        $(this).removeClass('btn-default').addClass('btn-warning');
        $(this).prevAll().removeClass('btn-default').addClass('btn-warning'); //for all previous siblings of selected button
        $(this).nextAll().removeClass('btn-warning').addClass('btn-default'); //for all next siblings of selected button
    });

    $('.event_rating-select').on('mouseleave', function(){
        active = $(this).parent().find('.selected');
        if(active.length) {
            active.removeClass('btn-default').addClass('btn-warning');
            active.prevAll().removeClass('btn-default').addClass('btn-warning');
            active.nextAll().removeClass('btn-warning').addClass('btn-default');
        } else {
            $(this).find('.btn').removeClass('btn-warning').addClass('btn-default');
        }
    });

    $('.event_rating-select .btn').click(function(){
        if($(this).hasClass('selected')) {
            $('.rating-select .selected').removeClass('selected');
            is_rated = false;
        } else {
            $('.rating-select .selected').removeClass('selected');
            $(this).addClass('selected');
            is_rated = true;
            clicked_button = $('.selected').index() + 1;//indexes start at 0!
        }
    });
//My additional functions
    $('.event_rev-btn-submit .btn').click(function(){
        if(is_rated == true) {
            var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
            var author = $('#user_info').attr('request_user_id');
            send_event_rating(rated_event,author,clicked_button);//call to function
        } else {
            alert("Cannot send review!");
        }
    });
});

//Global function existing to serve everyone
function send_event_rating(myevent, author, rating) {         
    //alert("Sending ajax query for event with id: " + myevent + ". Your rating is: " + rating + ". Your user id: " + author);  
    //Sending actual AJAX QUERY TO DB HERE..........
    $.ajax({
        type:'POST',
        url:'/add_event_review/' + myevent + '/' + author + '/' + rating + '/',
        data: {
            event_pk:myevent,
            author_pk: author,
            rating: rating,
            csrfmiddlewaretoken: getCookie("csrftoken")
        },
        success:function(json_response){
            var success = json_response['message']; //saving message to variable
            if(success == true){
                alert("Rating successfully added!");
            }
            else{
                alert("You have already rated this event!");
            }
        }
    });
}

//getCookie function retrieves csrf token from cookies.http://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django
function getCookie(c_name)
{
    console.log("Zwacam crsf");
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }