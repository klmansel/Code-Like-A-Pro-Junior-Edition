$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers = ["I want it to be successful", "I want it to be okay.", "I think it's gonna suck.", "I'm not sure."];
 
  magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    $("#8ball").effect( "shake" );
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    
    var question = prompt("What do you want your future to be like?");
    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});