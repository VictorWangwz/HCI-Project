

var textbox = document.getElementById("textbox");
var txtButton = document.getElementById("txtButton");
var vidButton = document.getElementById("vidButton");

txtButton.addEventListener("click", function(){
   
   var x = document.createElement("P");                        // Create a <p> node
	var t = document.createTextNode(textbox.value);    // Create a text node
	x.appendChild(t);                                           // Append the text to <p>
	document.body.appendChild(x);     
   
     textbox.value = "";
});

vidButton.addEventListener("click", function() {
/*	var x = document.createElement("IMG");
  x.setAttribute("src", "tonimorrison.jpg");
  x.setAttribute("width", "304");
  x.setAttribute("height", "228");
  document.body.appendChild(x);
	*/
	var vidFrame = document.createElement("IFRAME");
	/**var x = document.createElement("VIDEO");
	x.src = "https://www.youtube.com/embed/eH3giaIzONA";
	x.setAttribute("width", "304");
    x.setAttribute("height", "228");
    x.controls = true;
	vidFrame.appendChild(x);*/
	
	vidFrame.src = "MuhammadAli.mp4";
	vidFrame.width=304;
    vidFrame.height = 228;
	vidFrame.allow="accelerometer; autoplay;encrypted-media;"
    document.body.appendChild(vidFrame);
	
});