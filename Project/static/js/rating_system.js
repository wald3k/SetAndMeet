/*Handling Event RATINGS START*/
$(function(){
    var is_rated = false;
    var clicked_button = 0;
    $('.event-rating-select .btn').on('mouseover', function(){
        $(this).removeClass('btn-default').addClass('btn-warning');
        $(this).prevAll().removeClass('btn-default').addClass('btn-warning'); //for all previous siblings of selected button
        $(this).nextAll().removeClass('btn-warning').addClass('btn-default'); //for all next siblings of selected button
    });

    $('.event-rating-select').on('mouseleave', function(){
        active = $(this).parent().find('.selected');
        if(active.length) {
            active.removeClass('btn-default').addClass('btn-warning');
            active.prevAll().removeClass('btn-default').addClass('btn-warning');
            active.nextAll().removeClass('btn-warning').addClass('btn-default');
        } else {
            $(this).find('.btn').removeClass('btn-warning').addClass('btn-default');
        }
    });

    $('.event-rating-select .btn').click(function(){
        if($(this).hasClass('selected')) {
            $('.event-rating-select .selected').removeClass('selected');
            is_rated = false;
        } else {
            $('.event-rating-select .selected').removeClass('selected');
            $(this).addClass('selected');
            is_rated = true;
            clicked_button = $('.selected').index() + 1;//indexes start at 0!
        }
    });
//My additional functions
    $('.event-rev-btn-submit .btn').click(function(){
        if(is_rated == true) {
            var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
            var author = $('#user_info').attr('request_user_id');
            send_event_rating(rated_event,author,clicked_button);//call to function
        } else {
            alert("Cannot send review!");
        }
    });
});
/*Handling Event RATINGS STOP*/

/*Handling Profile RATINGS START*/
$(function(){
    //set green color on buttons if profile was rated DISCLAIMER:(In this version it always sets 5 stars!!)
    // $( ".profile-rating-select .btn-sm" ).each(function() {
    //     if($(this).parent().parent().attr('already_rated') == 'True'){
    //         $( this ).removeClass( "btn-warning" );
    //         $( this ).addClass( "btn-success" );
    //     }      
    // });

    var  already_rated = true;
    $('.profile-rev-btn-submit .btn').click(function(){
        var rated_profile = $(this).parent('div').parent('div').attr('user_id'); //get profile_id
        var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
        var author = $('#wydarzenie').attr('logged_user_pk');  //gets author.id
        var rating = 3;
        console.log( rated_event);
        alert(rated_profile);
        already_rated = has_been_rated(rated_event, author, rated_profile, rating );//ajax request to check if author already rated this profile
        console.log( already_rated);
    });
    ///////////////////////////////////////////////////////////////////////////////////
       
     $('.profile-rating-select .btn-sm').on('mouseover', function(){
            var rated_profile = $(this).parent().parent().attr('user_id'); //get profile_id
            var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
            var author = $('#wydarzenie').attr('logged_user_pk');  //gets author.id
            var rating = 3;
            var rated = $(this).parent().parent().attr('already_rated');//takes it from html (it was sent to html from view)
            if(rated == "False"){//this will affect buttons only if Profile was not rated before!
                $(this).removeClass('btn-default').addClass('btn-success');
                $(this).prevAll().removeClass('btn-default').addClass('btn-success'); //for all previous siblings of selected button
                $(this).nextAll().removeClass('btn-success').addClass('btn-default'); //for all next siblings of selected button
            }
        });


  $('.profile-rating-select .btn-sm').on('mouseleave', function(){
    var rated_profile = $(this).parent().parent().attr('user_id'); //get profile_id
    var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
    var author = $('#wydarzenie').attr('logged_user_pk');  //gets author.id
    var rating = 3;
    var rated = $(this).parent().parent().attr('already_rated');//takes it from html (it was sent to html from view)
    if(rated == "False"){
        active = $(this).parent().find('.selected');
        if(active.length) {
            active.removeClass('btn-default').addClass('btn-success');
            active.prevAll().removeClass('btn-default').addClass('btn-success');
            active.nextAll().removeClass('btn-success').addClass('btn-default');
        } else {
            $(this).parent().find('.btn').removeClass('btn-success').addClass('btn-default');
        }
    }
    });

    $('.profile-rating-select .btn-sm').click(function(){
        var rated_profile = $(this).parent().parent().attr('user_id'); //get profile_id
        var rated_event = $('#wydarzenie').attr('numer_wydarzenia');  //gets event.id
        var author = $('#wydarzenie').attr('logged_user_pk');  //gets author.id
        var rating = 0;
        var rated = $(this).parent().parent().attr('already_rated');//takes it from html (it was sent to html from view)
        console.log(rated + " click");
        if(rated == "False"){
                $('.profile-rating-select .selected').removeClass('selected');
                $(this).addClass('selected');
                //set different color to show that rating has just been made
                $(this).prevAll().removeClass('btn-default').addClass('btn-danger');
                $(this).removeClass('btn-default').addClass('btn-danger');
                //end of color manipulation
                $(this).parent().parent().attr('already_rated','True');
                rating = $('.selected').index() + 1;//indexes start at 0!
                rate_target_profile(rated_event,author,rated_profile,rating);
                show_snackbar("Rating added. Refresh page to see new average!");
        }
        else{
            alert("You've already reviewed this Profile!");
        }
    });
});
/*Handling Profile RATINGS STOP*/




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
/*Check if this user has already been rated by logged user. Returns true if profile was already rated*/
function has_been_rated(rated_event, author, rated_profile, rating ) {        
    //alert("Sending ajax query for event with id: " + myevent + ". Your rating is: " + rating + ". Your user id: " + author);  
    //Sending actual AJAX QUERY TO DB HERE..........
    $.ajax({
        type:'POST',
        url:'/has_been_rated/',
        data: {
            event_pk:rated_event,
            author_pk: author,
            target_pk: rated_profile,
            rating: rating,
            csrfmiddlewaretoken: getCookie("csrftoken")
        },
        success:function(json_response){
            console.log("Profile already rated?: " + json_response['profile_was_rated']);
        }
    });
}
/*Sends AJAX query for selected profile in selected event TO add a new rating*/
function rate_target_profile(rated_event, author, rated_profile, rating ) {    
    //alert("Sending ajax query for event with id: " + myevent + ". Your rating is: " + rating + ". Your user id: " + author);  
    //Sending actual AJAX QUERY TO DB HERE..........
    $.ajax({
        type:'POST',
        url:'/rate_target_profile/',
        data: {
            event_pk:rated_event,
            author_pk: author,
            target_pk: rated_profile,
            rating: rating,
            csrfmiddlewaretoken: getCookie("csrftoken")
        },
        success:function(json_response){
            console.log("Profile rated successfully?: " + json_response['rating_added']);
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


 /*Snackbar functionality*/
 function show_snackbar(text) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar")

    // Add the "show" class to DIV
    x.className = "show";
    x.innerHTML = text;
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}