$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofpictures = ["AlbusDumbledore1.jpg","Ron1.jpg","Ginny1.jpg","Hermione1.jpg","HarryPotter1.jpg","umbridge1.jpg","greyback1.jpg","SiriusBlack1.jpg","Voldemort1.jpg","Trelawney1.jpg"];
  
  magic8Ball.getAnswer = function()
  {
    var randomNumber = Math.random();
    var randomCharacter = Math.floor(randomNumber * this.listofpictures.length);
	var response = this.listofpictures[randomCharacter];
	
	$("#8ball").attr("src",response);

	console.log("random" + response);
  };

  var onClick = function()
  {
	magic8Ball.getAnswer();
  };
  
  $("#questionButton").click( onClick );
});