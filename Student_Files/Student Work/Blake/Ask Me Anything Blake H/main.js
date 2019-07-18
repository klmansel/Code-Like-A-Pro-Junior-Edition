$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers = ["I Say Yes.", "It is decidedly so.", "Without a doubt.", "Yes", "You may need it.", "As I see it, yes.", "Mabey.", "The Outlook is good.", "Yes.", "Science points to yes.", "404, try again.", "I'm tired, ask again later.", "Better not tell you now.", "Cannot predict now.", "Your mind is blocked, concentrate and ask again.", "Don't count on it.", "NO", "Leave", "Outlook is not so good.", "It is very doubtful."];
 
  magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    $("#DT").effect( "shake" );
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    $("#DT").attr("src", "Blake.HEIC");

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    $("#DT").attr("src", "Blake.HEIC");
    var question = prompt("What do you want to know?");

    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});