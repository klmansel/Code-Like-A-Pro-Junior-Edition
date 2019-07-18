$(document).ready(function(){
  
  var magic8Ball = {};
   magic8Ball.listofanswers = ["Feed me paper.", "the magic 8 ball is a scam", "i am muche better than any 8 ball.", "hotdog.", "pineapple.", "EEEEEEEEA SPORTS", "markas brownley", ".emit ruoy gnitsiaw era ouy siht gnidaer era uoy fI", "If you are reading this you are wasting your time.", "meme review."];
 
  magic8Ball.getAnswer = function(question)
  {
    var randomNumber = Math.random();
    var randomAnswer = Math.floor(randomNumber * this.listofanswers.length);
    var answer = this.listofanswers[randomAnswer];
    
    $("#8ball").effect( "shake" );
    $("#answer").text( answer );
    $("#answer").fadeIn(3000);
    $("#8ball").attr("src", "https://s3.amazonaws.com/media.skillcrush.com/skillcrush/wp-content/uploads/2016/09/answerside.png");

    console.log(question);
    console.log(answer);
  };
  $("#answer").hide();

  var onClick = function()
  {
    $("#answer").hide();
    $("#8ball").attr("src", "https://s3.amazonaws.com/media.skillcrush.com/skillcrush/wp-content/uploads/2016/09/magic8ballQuestion.png");
    var question = prompt("What do you want to know?");
    magic8Ball.getAnswer(question);
  };
  
  $("#questionButton").click( onClick );
});