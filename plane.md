# GEOINFO.UZ 


## Moduls
- Category
- Post

## CategoryModel
- id
- name
- photo
- description
- slug
- date
- posts

## PostModel 
- id
- title
- photo
- content
- slug
- date
- category_id


## Pages
### Home page
    @url: /
    @method GET
    @desc   Web layout last 10 and top 5 posts, category
    @access Public 

### Category page
    @url: /category
    @method GET
    @desc   Category page
    @access Public

### Category create
    @url: /category/create
    @method GET, POST
    @desc   Category page
    @access Public  



  <link rel="stylesheet" href="{{ url_for('static', filename='assets/css/blog.css') }}">


  <a class="nav-link btn btn-success text-light" href="{{ url_for('post.post_create')}}"> <i
                  class="fa fa-plus" aria-hidden="true"></i> Maqola yozish</a>

### Block
{% block content %} 

{% endblock %}


### If
{% if messages %} 

{% endif %}

### For
{% for message in messages %}

{% endfor %}

### With
{% with messages = get_flashed_messages() %}

 {% endwith %}

### Include
 {% include 'layouts/pagination.html' %}

### Extends
 {% extends 'layouts/base.html' %}