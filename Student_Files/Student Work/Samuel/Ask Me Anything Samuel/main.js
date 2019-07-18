$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers = ["You look great today", "You're a smart cookie.", "I bet you make babies smile.", "You have impeccable manners.", "I like your style.", "You have the best laugh.", "I appreciate you.", "You are the most perfect you there is.", "You're strong.", "Your perspective is refreshing.", "You're an awesome friend.", "You light up the room.", "You deserve a hug right now.", "You should be proud of yourself.", "You're more helpful than you realize.", "You have a great sense of humor.", "You've got all the right moves!", "You're awesome!"];
 
  magic8Ball.getAnswer = function()
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
	$("#answer").text( answer );
    $("#answer").fadeIn(1000);
    $("#8ball").attr("src", "mouth.gif");

    console.log(answer);

  };
  
  $("#answer").hide();
 

  var onClick = function()
  {
    $("#answer").hide();
	$("#answer").text( answer );
	magic8Ball.getAnswer();

  };
  
  $("#questionButton").click( onClick );
});