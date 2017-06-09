$(document).ready(function(){
	var counter =1;
	
    $(".buttonLevel1").click(function(){
		event.preventDefault();
		counter++;
		var nouveauLevel = jQuery('<tr><td id="td' + 
				counter + 'Level1">&bull;<input type="text" id="' + 
				counter + 'Level1Nom" name="Level1" size="20" placeholder="Level Name"><input type="text" id="' + 
				counter + 'Level1Keyword1 name="Level1" size="20" placeholer="Keyword"><input type="text" id="' +
				counter + 'Level1Action" name="Level1" size="20" placeholder="Action"><button class="buttonLevel1" type="button">add</button><button id="buttonRemLev1" type="button">remove</button>');
		jQuery("#tableLevel1").append(nouveauLevel);        
    });	
});

			