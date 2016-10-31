setInterval(get_all_shouts, 6000); //60000 MS == 1 minute
//setInterval(scroll_shoutbox, 6000); //60000 MS == 1 minute

$(document).ready(function(){//when document is ready run this function
  $('#submit').on('click', function(e){
    var message = $('#shout').val(); //grab value of an input
    $('#shout').val('');//clear input box
    //alert($('#shout').val());
    var profile_avatar = $('.avatar-medium').html();
    console.log("Testuje console");
    var wydarzenie = $('#wydarzenie').attr('numer_wydarzenia');
    console.log(wydarzenie);
    //alert( {{ event.id }} );
    e.preventDefault();//prevent page from being refreshed.
    //Make ajax call to specified URL
    $.ajax({
      type:'POST',
      url:'/shout_add/',
      data:{
        text:message,
        event_id: wydarzenie,
        avatar: profile_avatar,
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
      },
      success:function(json_response){
        var new_html = "";
        var len = json_response.length;       //check length of json_response array
        console.log(json_response)
        // new_html += "<ul>";
        // //console.log(json_response);
        jQuery.each(json_response, function(index, item) {
                    //now you can access properties using dot notation
                    //console.log(JSON.stringify(item.fields.text));
                    // new_html+= "\n<li>\n";
                    // new_html += profile_avatar;
                    // new_html+= JSON.stringify(item.fields.text);
                    // new_html+= "\n</li>";
                    if(index == len - 1){
                      var message_text = JSON.stringify(item.fields.text);
                      message_text = message_text.replace(/\"/g, ""); //replacy any " to nothing
                      console.log("Enter this if only once!");
                        new_html = profile_avatar + message_text;
                    }
        });
        // new_html += "\n</ul>";
        var old_html = $('#shouts').html();
        $('#shouts').html(old_html +"</br>" + new_html);//replacing content of id shouts with new html!
        scroll_shoutbox();//scroll to the bottom
      }
    })

  });
});


//Get send this query as set in interval. Retrieve all shouts!
// function get_all_shouts() {
//   var profile_avatar = $('.avatar-medium').html();
//   var wydarzenie = $('#wydarzenie').attr('numer_wydarzenia');
//   console.log("hi");
//   $.ajax({
//     type:'POST',
//     url:'/shout_list/',
//     data:{
//       event_id: wydarzenie,
//       csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
//     },
//     success:function(json_response){
//       var new_html = "";
//       var len = json_response.length;       //check length of json_response array
//       jQuery.each(json_response, function(index, item) {
//                   new_html+= "<br><li>";
//                   new_html += profile_avatar;
//                   new_html+= JSON.stringify(item.fields.text);
//                   new_html+= "</li>";
//                   console.log(new_html);
//       });
//       $('#shouts').html(new_html);//replacing content of id shouts with new html!
//     }
//   })
// }
function get_all_shouts() {
  var profile_avatar = $('.avatar-medium').html();
  var wydarzenie = $('#wydarzenie').attr('numer_wydarzenia');
  console.log("hi");
  $.ajax({
    type:'POST',
    url:'/shout_list/',
    data:{
      event_id: wydarzenie,
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
    },
    success:function(response){
      $('#shouts').html(response);//replacing content of id shouts with new html!
      scroll_shoutbox();//scroll to the bottom
    }
  })
}

function scroll_shoutbox() {
  console.log("Scrolling down")
  $("#shouts").scrollTop($("#shouts").scrollTop() + 9999999999);
}
