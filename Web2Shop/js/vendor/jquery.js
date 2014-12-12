$(document).ready(function()
{
  $('.button').click(function()
  {
  	//if($("#").val() == '') DROPDOWN MENU MOET HIERIN KOMEN ZODAT WEET WELKE COMPONENT .JSON BESTAND GEBRUIKT MOET WORDEN!
    	$.ajax(
    	{
      		url: "json_data.json",
      		dataType: "text",
      		success: function(data)
      		{
        		var json = $.parseJSON(data);
        		if($("#searchBar").val() == 'Thierry')
        		{
        			$('#results').html('Name: '+ json.p1.name + '<br />'
        				+ 'Age: ' + json.p1.age + '<br />'
        				+ 'Company: ' + json.p1.company);
        		}
        		else if($("#searchBar").val() == 'Wen')
        		{	
        			$('#results').html('Name: '+ json.p3.name + '<br />'
        				+ 'Age: ' + json.p3.age + '<br />'
        				+ 'Company: '+ json.p3.company);
        		}
        		else
        		{
        			$('#results').html('We could not find any people with the input: ' + $("#searchBar").val());
        		}

     		}
   		});
  });
});