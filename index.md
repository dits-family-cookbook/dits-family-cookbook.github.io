---
layout: default
---

# Breads

# Desserts

{% for page in site.pages %}
{% if page.url contains "desserts"  %}
[{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


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


# Vegetables and Sides
