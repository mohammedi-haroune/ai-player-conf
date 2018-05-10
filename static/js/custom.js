
 /* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(1000); // set duration in brackets    
});


$(document).ready(function() {

  /* Hide mobile menu after clicking on a link
    -----------------------------------------------*/
    $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });


  /* Smoothscroll js
  -----------------------------------------------*/
    $(function() {
        $('.navbar-default a').bind('click', function(event) {
            var $anchor = $(this);
            $('html, body').stop().animate({
                scrollTop: $($anchor.attr('href')).offset().top - 49
            }, 1000);
            event.preventDefault();
        });
    });




    

    /* Back to Top
    -----------------------------------------------*/
    $(window).scroll(function() {
      if ($(this).scrollTop() > 200) {
          $('.go-top').fadeIn(200);
            } else {
                $('.go-top').fadeOut(200);
           }
        });   
          // Animate the scroll to top
        $('.go-top').click(function(event) {
          event.preventDefault();
        $('html, body').animate({scrollTop: 0}, 300);
    });


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

  });

$("select")
    .map(function () {
        var value = $( this ).attr("data-value");
        for (i=0;i<14;i++){
            if (this[i].value === value){
                $("#"+this.id + " " + "option"+"["+ "value=" + '"' + this[i].value + '"' + "]").attr("selected", "selected")
            }
        }

    });

    $("a[data-toggle='collapse']").click(function () {
        if (this.text === "(SHOW)"){
            this.text = "(HIDE)"
        }
        else if (this.text === "(HIDE)") {
            this.text = "(SHOW)"
        }
    });
    $(document).ready(function () {
        var id = $('.preloader').attr("data-id");
        var ids = ['#stop', '#point1', '#point2', '#fist', '#grab'];
        $(".navbar-right a[href]")
            .map(function () {
                var href = $( this ).attr("href");
                if (href === ids[id]){
                    var $anchor = $(this);
                    $('html, body').stop().animate({
                    scrollTop: $($anchor.attr('href')).offset().top - 49
                    }, 1000);
                    $(href + " h1").append('<span class="badge badge-success">SAVED</span>')
                    $.ajax({
                         url: "./set_option",
                         type: "POST",
                   });
                }
            })
    });