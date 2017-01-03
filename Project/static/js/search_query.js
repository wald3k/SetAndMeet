// Animated search query
var input = $('input[name="q"]');


input.on("focus blur", function(evt) {
  
  if($(this).is("animated")) return;    // Do nothing while animating

  var isFocus = evt.type=="focus";      // Detect event type
  if(isFocus) this.w = $(this).width(); // On focus remember the element initial Width
  $(this).animate({width: isFocus ? 200 : this.w }); // Finally
  s
}).on("input", function() {
  
  $(this).trigger("blur");              // Trigger a blur if user selects a dropdown value
  
});