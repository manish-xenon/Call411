<form action={% url 'phones:addphone' %} method="post">
	{% csrf_token %}
	
	{{ form.as_p }}
	<input type="hidden" name="old_model_number" value="{{model_number}}" />
	<input type="submit" value="Submit" />
</form>
