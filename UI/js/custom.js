$(document).ready(function(){
  //$('.rating').raty({ score: 3 });
  $(".rating" ).jRating({
    smallStarsPath: "icons/small.png",
    bigStarsPath : "icons/stars.png",
    rateMax: 5,
    step: true
  });
});
