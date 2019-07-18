$(document).ready(function(){
  
  var magic8Ball = {};
  magic8Ball.listofanswers =
  ["It will hapen","Yes","No","It won`t hapen","Outlook amazing","Sourses Say no","Sourses Say yes",
	"Outlook bad","Cannot predict now"]; magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    $("#8ball").attr("src", "cristel.jpg");

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    $("#8ball").attr("src","cristel.jpg");
    var question = prompt("What do you want to know");
    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});