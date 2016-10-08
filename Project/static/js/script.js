//My slider
var action = "click";       //type of action like 'click','double clock','hover' etc.
var speed = "500";          //speed in ms

//use JQuery $(document).ready function
$(document).ready(function(){//when document is ready run this function
  //handler for the question
  $('li.slider-q').on(action, function(){
    //on action get the next element
    $(this).next()//refers to the '.li.slider-q' that was clicked or hovered on.
      .slideToggle(speed)
        //select all the siblings
        .siblings('li.slider-a').slideUp();
    //grab arrow image for selected question.
    var img = $(this).children('img');

    //Delete 'rotate class' for every img aparto from the active
    $('img').not(img).removeClass('rotate');

    //Toggle rotate calss
    img.toggleClass('rotate');

  });
console.log("successfully toggled!");
});
