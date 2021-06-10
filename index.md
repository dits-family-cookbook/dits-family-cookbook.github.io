---
layout: default
---

# Baking & Desserts

## Bars

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "bars" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


## Cakes

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cakes" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}

## Cookies

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cookies" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


## Desserts

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "/desserts" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}

# Breads

{% for page in site.pages %}
{% if page.url contains "breads" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


# Canning

{% for page in site.pages %}
{% if page.url contains "canning" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}



# Main Dishes

{% for page in site.pages %}
{% if page.url contains "main-dishes" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}

# Salads

# Soups and Stews

{% for page in site.pages %}
{% if page.url contains "soups" and page.title != blank %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}
