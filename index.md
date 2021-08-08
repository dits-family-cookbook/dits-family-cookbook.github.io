---
layout: default
---

# Baking & Desserts

## Bars
<hr />

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "bars" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}


## Cakes
<hr />

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cakes" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}

## Cookies
<hr />

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "cookies" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}


## Desserts
<hr />

{% for page in site.pages %}
{% if page.url contains "baking" and page.url contains "/desserts" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}

# Breads
<hr />

{% for page in site.pages %}
{% if page.url contains "breads" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}


# Candies
<hr />

{% for page in site.pages %}
{% if page.url contains "candies" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}


# Canning
<hr />

{% for page in site.pages %}
{% if page.url contains "canning" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}



# Main Dishes
<hr />

{% for page in site.pages %}
{% if page.url contains "main-dishes" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}

# Miscellaneous
<hr />

{% for page in site.pages %}
{% if page.url contains "miscellaneous" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}



# Salads
<hr />

{% for page in site.pages %}
{% if page.url contains "salads" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}



# Soups and Stews
<hr />

{% for page in site.pages %}
{% if page.url contains "soups" and page.title %}
[{{ page.title }}]({{ page.url }})
<hr />
{% endif %}
{% endfor %}
