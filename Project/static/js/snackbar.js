 /*Snackbar functionality*/
 function show_snackbar(argument) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");
    var wait_in_ms = 3000;
    // Add the "show" class to DIV
	    switch(argument) {
	    case '1':
	        x.innerHTML = 'No more spots!';
	        x.style.background="linear-gradient(#9a0404, #871403 60%, #680303)";
	        break;
        case '2':
        	x.innerHTML = 'Rating added. Refresh page to see new average!';
        	break;
        case '3':
        	x.innerHTML = 'Successfully joined an event!';
        	x.style.background="linear-gradient(#059405, #038613 60%, #036303)";
        	wait_in_ms = 9000;
        	break;
	    default:
	        x.innerHTML = "Operation unknown!";
	        break;
	} 
	x.className = "show";
    // After number of mili-seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, wait_in_ms);
}