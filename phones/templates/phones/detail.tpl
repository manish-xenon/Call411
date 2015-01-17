<!--
Author: MANISH
-->
{% load staticfiles %}
<!DOCTYPE HTML>
<html>
<head>
	<title> Detail Page | Home :: CALL 411</title>
	<link href="{% static "css/bootstrap.css"%}" rel='stylesheet' type='text/css' />
	<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
	<script src="{% static "js/jquery.min.js"%}"></script>
	<!-- Custom Theme files -->
	<link href="{% static "css/style.css"%}" rel='stylesheet' type='text/css' />
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

	<!----- /strat-Reviews---->
	<div id="reviews" class="reviews">
		<div class="container">
			<div class="text-center well">
                <div class="panel panel-default">
                <div class="panel-header review-head">
				    <h3>Phone Details</h3>
                </div>
                <div class="panel-body">
                    <div class=" col-md-6 feature-text">
                    <table align='center' class="table" padding='30px'>
                        <tr>
                            <td>Model Number</td>
                            <td>{{phone.model_number}}</td>
                        </tr>
                        <tr class="table-striped">
                            <td>RAM</td>
                            {% if phone.ram > 0%}
                            <td>{{phone.ram}} MB</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr>
                            <td>Processor</td>
                            <td>{{phone.processor}}</td>
                        </tr>
                        <tr class="table-striped">
                            <td>Manufacturer</td>
                            <td>{{phone.manufacturer}}</td>
                        </tr>
                        <tr>
                            <td>Operating System</td>
                            <td>{{phone.system}}</td>
                        </tr>
                        <tr class="table-striped">
                            <td>Screen Size</td>
                            {% if phone.screen_size > 0%}
                            <td>{{phone.screen_size}} inches</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr>
                            <td>Screen Resolution</td>
                            <td>{{phone.screen_resolution}}</td>
                        </tr>
                        <tr class="table-striped">
                            <td>Battery Capacity</td>
                            {% if phone.battery_capacity > 0%}
                            <td>{{phone.battery_capacity}} mAh</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr>
                            <td>Talk Time</td>
                            {% if phone.talk_time > 0%}
                            <td>{{phone.talk_time}} minutes</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr class="table-striped">
                            <td>Camera Megapixels</td>
                            {% if phone.camera_megapixels > 0%}
                            <td>{{phone.camera_megapixels}} MP</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr>
                            <td>Price</td>
                            {% if phone.price > 0%}
                            <td>${{phone.price}}</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr class="table-striped">
                            <td>Weight</td>
                            {% if phone.weight > 0%}
                            <td>{{phone.weight}} oz</td>
                            {% else %}
                            <td>No data available</td>
                            {% endif %}
                        </tr>
                        <tr>
                            <td>Storage Options</td>
                            <td>{{phone.storage_options}}</td>
                        </tr>
                        <tr>
                            <td>Dimensions</td>
                            <td>{{phone.dimensions}}</td>
                        </tr>
                    </table>
                    </div>
                    <div class="col-md-6 hand-app">
                                 <img src="{{phone.image}}" alt="" class="img-responsive img-thumbnail">
                    </div>
                </div>
                </div>
				
				{% if user.is_superuser %}
				<form action="edit/">
					<input class="btn btn-default"type="submit" value="Edit">
				</form>
				<form action="del/">
					<input class="btn btn-default" type="submit" value="Delete">
				</form>
                {% endif %}

                <div class="review-head">
                <h3>Similar Phones</h3>
                </div>
                {% for suggest in suggest_phones %}
                    <div class="panel panel-default">
                        <a href="/{{ suggest.model_number }}">{{ suggest.model_number }}</a>
                    </div>
                {% endfor %}

                <div>
                <div class="review-head">
                <h3> Text Reviews </h3>
                </div>
                    {% for review in text_reviews %}
                       <div class="panel panel-default">
                         <div class="panel-heading">
                           <h3 class="panel-title">
                            {{review.reviewer}}
                            <span class="badge">{{review.rating}}</span> 
                           </h3>
                         </div>
                         <div class="panel-body">
                           {{review.review_text}}
                         </div>
                       </div>
                    {% endfor %}
                </div> 

                <div>
                <div class="review-head">
                <h3> Video Reviews </h3>
                </div>
                    {% for review in video_reviews %}
                           <div class="panel panel-default"> 
                             <div class="panel-heading">
                               <h3 class="panel-title">
                                {{review.reviewer}}
                                <span class="badge">{{review.rating | stringformat:".1f"}}</span> 
                               </h3>
                             </div>
                             <div class="panel-body" height=600px>
                             <iframe
                               width=100%
                               height=600px
                               src="{{review.media_content}}"
                             />
                             </div>
                           </div>
                    {% endfor %}
                </div>


			</div>
			
		</div>
	</div>
	<!---//End-Reviews-----> <!---/start-footer----->
	   	<div class="footer">
	   		<div class="container">
				<div class="copy-right">
					<p>&copy; 2014  All rights  Reserved | Call 411</a></p>

				</div>								
			</div>

	   	</div>
	<!---//end-footer----->

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
