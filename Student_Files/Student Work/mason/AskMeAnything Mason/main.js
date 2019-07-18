$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers = ["It isn't certain.", "It is true.", "are you dumb, its yes.", "Yes, you're wroung.", "im am not a oracle please ask later.", "As I see it, yes.", "Most likely not.", "good good.", "Yes.", "Signs point to money.", "siri is evil, try again.", "Ask again later.", "Better not tell you now  the future is a dangerous .", "Cannot predict now, the future is to unclear.", "Concentrate and ask again.", "Don't count on it.", "My reply is no to no.", "My sources say no.", "Outlook not so good.", "dougtfull the futer is."];
 
  magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    $("#8ball").attr("src", "xboxEnd.png");

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    $("#8ball").attr("src", "xboxEnd.png");
    var question = prompt("What do you want to know?");
    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});