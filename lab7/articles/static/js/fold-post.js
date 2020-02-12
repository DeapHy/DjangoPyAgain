var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++)
{ 
	foldBtns[i].addEventListener("click", function(e) { 
		if (e.target.className == "fold-button folded")
		{
			e.target.innerHTML = "свернуть"; 
			e.target.className = "fold-button"; 
			event.target
				.parentElement
				.className = "one-post";
		}
		else
		{
			e.target.innerHTML = "развернуть"; 
			e.target.className = "fold-button folded"; 
			e.className = "one-post-folded";
			event.target
				.parentElement
				.className = "one-post-folded";
		}
		
	});
}
