$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers = ["NAAAAAH MAN.", "i mean i guess.", "duh.", "Yes, definitely.", "*lies* sure.", "not a chance.", "Most likely.", "Outlook good...NOT.", "Yes.", "Signs point to yes.", "idk ask later dude.", "Ask again later.", "Better not tell you now.", "dont want to predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is... no.", "My sources say no.", "Outlook ur screwed.", "Very doubtful."];
 
  magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    $("#8ball").effect( "shake" );
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    $("#8ball").attr("src", "kangchenjunga.jpg");

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    $("#8ball").attr("src", "kangchenjunga.jpg");
    var question = prompt("What do you want to know?");
    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});