 /*Snackbar functionality*/
 function show_snackbar(argument) {
    // Get the snackbar DIV
    var x = document.getElementById("snackbar");

    // Add the "show" class to DIV
    
    
	    switch(argument) {
	    case '1':
	        x.innerHTML = 'No more spots!';
	        x.style.background="linear-gradient(#9a0404, #871403 60%, #680303)";
	        break;
        case '2':
        	x.innerHTML = 'Rating added. Refresh page to see new average!';
        	break;
	    default:
	        x.innerHTML = "Operation unknown!";
	        break;
	} 
	x.className = "show";
    // After 3 seconds, remove the show class from DIV
    setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
}