<!--
Author: MANISH
License: Creative Commons Attribution 3.0 Unported
License URL: http://creativecommons.org/licenses/by/3.0/
-->
{% load staticfiles %}
<!DOCTYPE HTML>
<html>
	<head>
		<title>THE CALL 411 WEBSITE | Home :: CALL 411</title>
		<link href="{% static "css/bootstrap.css"%}" rel='stylesheet' type='text/css' />
		<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
		<script src="{% static "js/jquery.min.js"%}"></script>
		 <!-- Custom Theme files -->
		<link href="{% static "css/style.css" %}" rel='stylesheet' type='text/css' />
		<link href="{% static "css/call411.css" %}" rel='stylesheet' type='text/css' />
   		 <!-- Custom Theme files -->
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
		</script>
		 <!---- start-smoth-scrolling---->
		<script type="text/javascript" src="{% static "js/move-top.js"%}"></script>
		<script type="text/javascript" src="{% static "js/jquery.easing.min.js"%}"></script>
		
		<script type="text/javascript">
			jQuery(document).ready(function($) {
				$(".scroll").click(function(event){		
					event.preventDefault();
					$('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
				});
                var heights = $(".panel-body").map(function() {
                    return $(this).height();
                }).get(),

                maxHeight = Math.max.apply(null, heights);

                $(".panel-body").height(maxHeight);
            });
		</script>
		 <!---- start-smoth-scrolling---->
		<!----- webfonts ------>
		<link href='http://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,400,300,600,700' rel='stylesheet' type='text/css'>
		<!----- webfonts ------>
		<!----start-top-nav-script---->
		<script>
			$(function() {
				var pull 		= $('#pull');
					menu 		= $('nav ul');
					menuHeight	= menu.height();
				$(pull).on('click', function(e) {
					e.preventDefault();
					menu.slideToggle();
				});
				$(window).resize(function(){
	        		var w = $(window).width();
	        		if(w > 320 && menu.is(':hidden')) {
	        			menu.removeAttr('style');
	        		}
	    		});
			});
		</script>
		<!----//End-top-nav-script---->
	</head>
	<body>
		<!----- start-header---->
			<div id="home" class="header">
				<div class="top-header">
						<div class="logo">
							  <a href="#"><img src="{% static "images/logo.png"%}" alt="" height = 80 width = 120></a>
						</div>
						<!----start-top-nav---->
						 <nav class="top-nav">
							<ul class="top-nav">



<form id="searchThis" action="/search/" style="display: inline;" method="post">
{% csrf_token %}
<input onfocus="if(this.value==this.defaultValue)this.value='';" value="Search for Phones" type="text" id="key" onblur="if(this.value=='')this.value=this.defaultValue;" vinput="" name="q" /> <input id="searchButton" value="Go" type="submit" /></form>


								<li class="active"><a href="#home" class="scroll">Home </a></li>
								<li><a href="#about" class="scroll">about</a></li>
								<li><a href="#phones" class="scroll">phones</a></li>
							</ul>
							<a href="#" id="pull"><img src="{% static "images/menu-icon.png"%}" title="menu" /></a>
						</nav>
						<div class="clearfix"> </div>
					</div>
				</div>
		<!----- //End-header---->
		<!----- banner ---->
			<div class="banner">
				<div class="container">
					<div class="banner-info">
						<div class=" col-md-6 appp">
							 <img src="{% static "images/mbl-app.png"%}" alt="">
						</div>
						<div class="col-md-6 banner-text">
							<h1>Call 411</h1>
							<p> This website is a one-stop shop for all your phone review needs! </p>
						</div>
						<div class="clearfix"> </div>
					</div>
			</div>
		</div>

			<!----- banner ---->
			<!----- /strat-About---->
			<div id="about" class="about">
	       		<div class="container">
	       		   <div class="gallery-head text-center">
					  <h3>About Call411</h3>
                      <p>This website provides details and reviews for cell phones. Data is scraped automatically from <a href="http://www.phonearena.com">PhoneArena</a>. We provide a one stop place to find the best cell phone for you.</p>
				    </div>
	       			<div class="row text-center">
	       				<div class="col-md-3 about_grid">
	       					 <img src="{% static "images/ab-1.jpg"%}" alt="" height = 200 width = 220>
	       				</div>
	       				<div class="col-md-3 about_grid">
	       					<img src="{% static "images/ab-2.jpg"%}" alt="" height = 200 width = 220>
	       				</div>
	       				<div class="col-md-3 about_grid">
	       					<img src="{% static "images/ab-3.jpg"%}" alt="" height = 200 width = 220>
	       				</div>
	       				<div class="col-md-3 about_grid">
	       					 <img src="{% static "images/ab-4.jpg"%}" alt="" height = 200 width = 220>
	       				</div>
	       				<div class="clearfix"> </div>
	       			</div>
	       		</div>
	       	</div>
	  <!---//End-About----->

	  <!-----feature ---->
			<div id="phones" class="phones">
				<div class="container-fluid">
	       		   <div class="gallery-head text-center">
					<h3>List of Phones</h3>
</div>
                        <div class="row">
                        {% if phone_list %}
                            {% for phone in phone_list %}
                                <div class="col-md-3">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                        <center>
                                        <a href="/{{ phone.model_number }}">
                                        <img src="{{ phone.image }}" alt="phone.model_number" class="img-thumbnail img-responsive item-image"></img>
                                        </a>
                                        </center>
                                        </div>
                                      <div class="panel-body">
                                        <center>
                                        <a href="/{{ phone.model_number }}"><h3 color=#5cb85c>{{ phone.model_number }}<h3></a>
                                        </center>
                                      </div>
                                    </div>
                                </div>
                            {% endfor %}
                        {% else %}
                            <h3>No Phones</h3>
                        {% endif %}
                        </div>


                        {% if user.is_superuser %}
                        <center>
                          <form class="" action="{% url 'phones:addphone' %}">
                            <input type="submit" value="Add Phone">
                          </form>
                        <center>
                        {% endif %}	
				<nav>
			      <ul class="pagination">  
				
                    <li {% if page_prev < 1 %}class=""{% endif %}>
                        <a {% if page_prev > 0 %}href="?/page={{ page_prev }}"{% endif %}><span aria-hidden="true">&laquo;</span><span class="sr-only">Previous</span></a>
                    </li>
                    
                    {% for p in page_names %}
                        <li 
                        {% ifequal p page %}
                            class="active" 
                        {% endifequal %}
                        >
                        <a href="
                            {% ifequal p '...' %}
                            #
                            {% else %}
                            ?page={{ p }}
                            {% endifequal %}
                            ">
                            {{ p }}
                            <span class="sr-only">(current)</span>
                        </a>
                        </li>
                    {% endfor %}
                    
                    <li {% if page < 1 %}class="disabled"{% endif %}>
                        <a {% if page_next > 0 %}href="?page={{ page_next }}"{% endif %}><span aria-hidden="true">&raquo;</span><span class="sr-only">Next</span></a>
                    </li>
				
			      </ul>
                </nav>

			</div>
        </div>
     </div>
			<!-----//phones---->
			    
			    
	   <!---/start-footert----->
	   	<div class="footer">
	   		<div class="container">
				<div class="copy-right">
					<p>&copy; 2014  All rights  Reserved | Call 411</a></p>

				</div>								
			</div>

	   	</div>
	   <!---//end-footert----->
				<script type="text/javascript">
									$(document).ready(function() {
										/*
										var defaults = {
								  			containerID: 'toTop', // fading element id
											containerHoverID: 'toTopHover', // fading element hover id
											scrollSpeed: 1200,
											easingType: 'linear' 
								 		};
										*/
										
										$().UItoTop({ easingType: 'easeOutQuart' });
										
									});
								</script>

					<a href="#" id="toTop" style="display: block;"> <span id="toTopHover" style="opacity: 1;"> </span></a>
	</body>
</html>
