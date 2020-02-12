$(document).ready(function(){    
	$('.one-post').hover(function(event)
	{     
		$(event.currentTarget).find(".one-post-shadow").animate({opacity: 0.1}, 300)   
	}, 
	function(event)
	{       
		$(event.currentTarget).find(".one-post-shadow").animate({opacity: 0}, 300)     
	}); 
}); 

$(document).ready(function(){    
	$('#navbar-center').hover(function(event)
	{     
		pic_width = Number.parseInt($('.logo').css('width'));
		pic_height = Number.parseInt($('.logo').css('height'));
		$(event.currentTarget).find(".logo").animate(
		{
			width: pic_width+20,
			height: (pic_width+20)/pic_width * pic_height
		}, 100)  
	}, 
	function(event)
	{
		pic_width = Number.parseInt($('.logo').css('width'));
		pic_height = Number.parseInt($('.logo').css('height'));     
		$(event.currentTarget).find(".logo").animate(
		{
			width: pic_width - 20,
			height: (pic_width - 20)/pic_width * pic_height
		}, 100)      
	}); 
});