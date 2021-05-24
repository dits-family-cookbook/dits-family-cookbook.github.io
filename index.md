---
layout: default
---

# Baking & Desserts

## Bars

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "bars" %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


## Cakes

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cakes" %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}

## Cookies

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cookies" %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


## Desserts

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "/desserts" %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}

# Breads

# Main Dishes

{% for page in site.pages %}
{% if page.url contains "main-dishes"  %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


# Salads

# Soups and Stews

{% for page in site.pages %}
{% if page.url contains "soups"  %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}
