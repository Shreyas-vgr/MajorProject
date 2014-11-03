$(document).ready(function(){
  //$('.rating').raty({ score: 3 });
  $(".rating" ).jRating({
    smallStarsPath: "static/icons/small.png",
    bigStarsPath : "static/icons/stars.png",
    rateMax: 5,
    step: true
  });
});
