## **Step 1: Set Up the Django Project**

### **1.1 Install Python and Virtual Environment**

Navigate into the project folder:

cd blog-site

Ensure you have Python installed (preferably Python 3.9+). Then, set up a virtual environment.

\# Install virtualenv if not installed

pip install virtualenv

\# Create a virtual environment

python \-m venv venv

\# Activate the virtual environment

\# On Windows:

venv\\Scripts\\activate

\# On macOS/Linux:

source venv/bin/activate

Set-ExecutionPolicy Unrestricted \-Scope Process

### **1.2 Install Django**

Once the virtual environment is activated, install Django.

pip install django

### **1.3 Start a New Django Project**

Run the following command to create a Django project named `blog_project`:

django-admin startproject blog\_site .

Run the development server to check if Django is set up correctly:

python manage.py runserver

You should see the Django welcome page at `http://127.0.0.1:8000/`.

---

## **Step 2: Create the Posts App**

Django follows the "apps" structure. Create an app named `posts` for handling blog-related functionality.

python manage.py startapp posts

Register the `blog` app in `blog_site/settings.py` under `INSTALLED_APPS`:

INSTALLED\_APPS \= \[

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'posts',  \# Add the posts app here

\]

---

## **Step 3: Define Models for the Blog**

Open `blog/models.py` and define the `Post` model:

from django.db import models

class Post(models.Model):

    title \= models.CharField(max\_length=60)

    content \= models.TextField()

    publish\_date \= models.DateField()

Run the following command to apply migrations:

python manage.py makemigrations posts

python manage.py migrate

---

## **Step 4: Register Models in the Admin Panel**

To manage blog posts via the admin panel, register the `Post` model in `blog/admin.py`:

from django.contrib import admin

from posts.models import Post

class PostAdmin(admin.ModelAdmin):

    list\_display \= ('title', 'publish\_date')

admin.site.register(Post, PostAdmin)

Create a superuser to access the admin panel:

python manage.py createsuperuser

Enter the required details (username, email, password), then run the server:

python manage.py runserver

Log in to the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

---

### **Step 5: Set Up the `templates` Folder in `BASE_DIR`**

By default, Django looks for templates inside each app’s `templates` folder. However, it's a best practice to keep all templates in a central `templates` directory at the project root.

#### **1.1 Create the `templates` Directory**

Navigate to your project root (`blog-site/`) and create a `templates` folder:

mkdir templates

#### **1.2 Configure Django to Use the Global `templates` Folder**

In `blog-site/settings.py`, update the `TEMPLATES` setting to include the `BASE_DIR / "templates"` directory:

import os

TEMPLATES \= \[

    {

        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': \[os.path.join(BASE\_DIR, "templates")\],  \# Add this line

        'APP\_DIRS': True,

        'OPTIONS': {

            'context\_processors': \[

                'django.template.context\_processors.debug',

                'django.template.context\_processors.request',

                'django.contrib.auth.context\_processors.auth',

                'django.contrib.messages.context\_processors.messages',

            \],

        },

    },

\]

---

### **Step 6: Create the Post List View**

Now, define a function-based view that retrieves and displays all blog posts.

#### **2.1 Create the View in `blog/views.py`**

Open `blog/views.py` and add the following function:

from django.shortcuts import render

from .models import Post

def post\_list\_view(request):

    posts \= Post.objects.all()

    context \= {'posts': posts}

    return render(request, 'post\_list.html', context)

---

### **Step 3: Create the Template for Post List**

Create a template file inside `templates/blog/`:

touch templates/post\_list.html

Open `post_list.html` and add the following HTML:

\<\!DOCTYPE html\>

\<html lang="en"\>

\<head\>

    \<title\>My Personal Blog\</title\>

\</head\>

\<body\>

	{% for post in data %}

		\<li\>

			\<h2\>{{ post.title }}\</h2\>

			\<p\>{{ post.content }}\</p\>

			\<p\>{{ post.publish\_date }}

		\</li\>

	{% endfor %}

\</body\>

\</html\>

---

### **Step 7: Configure URLs**

Now, add a URL pattern for the post list view.

#### **7.1 Create `urls.py` in the `blog` App (If Not Already Created)**

Open `blog_site/urls.py` and add:

from django.contrib import admin

from django.urls import path, include

from posts.views import post\_list\_view

urlpatterns \= \[

    path('admin/', admin.site.urls),

    path('post-list', post\_list\_view),

\]

---

### **Step 8: Run the Server and Test**

Start the Django development server:

python manage.py runserver

Visit `http://127.0.0.1:8000/` in your browser, and you should see a list of all blog posts.

---

### **Step 1: Create a Post Detail View**

We need a view to display a single blog post when a user clicks on its title.

#### **1.1 Define the View in `blog/views.py`**

Open `blog/views.py` and add the following function:

from django.shortcuts import render

from .models import Post

def post\_detail(request, id):

    post \= Post.objects.get(id=id)

    return render(request, 'post\_detail.html', {'post': post})

---

### **Step 2: Update URLs**

Now, add a URL pattern for the post detail view.

#### **2.1 Modify `blog_site/urls.py`**

Open `blog/urls.py` and update it:

from django.urls import path

from posts.views import post\_list, post\_detail

urlpatterns \= \[

    path('post-list', post\_list, name='post\_list'),

    path('post/\<int:post\_id\>/', post\_detail, name='post\_detail'),

\]

---

### **Step 3: Create the Post Detail Template**

Create a new file for the detail page:

touch templates/blog/post\_detail.html

Open `post_detail.html` and add the following content:

\<\!DOCTYPE html\>

\<html lang="en"\>

\<head\>

    \<meta charset="UTF-8"\>

    \<meta name="viewport" content="width=device-width, initial-scale=1.0"\>

    \<title\>{{ post.title }}\</title\>

\</head\>

\<body\>

    \<h1\>{{ post.title }}\</h1\>

    \<p\>\<strong\>Author:\</strong\> {{ post.author }}\</p\>

    \<p\>\<strong\>Published on:\</strong\> {{ post.created\_at }}\</p\>

    \<p\>{{ post.content }}\</p\>

    \<a href="{% url 'post\_list' %}"\>Back to all posts\</a\>

\</body\>

\</html\>

---

### **Step 4: Link Posts from the Post List Page**

Now, modify `templates/blog/post_list.html` to make post titles clickable:

\<\!DOCTYPE html\>

\<html lang="en"\>

\<head\>

    \<meta charset="UTF-8"\>

    \<meta name="viewport" content="width=device-width, initial-scale=1.0"\>

    \<title\>Blog Posts\</title\>

\</head\>

\<body\>

    \<h1\>All Blog Posts\</h1\>

    \<ul\>

        {% for post in posts %}

            \<li\>

                \<h2\>\<a href="{% url 'post\_detail' post.id %}"\>{{ post.title }}\</a\>\</h2\>

                \<p\>{{ post.content|truncatewords:20 }}\</p\>

                \<p\>\<strong\>Author:\</strong\> {{ post.author }}\</p\>

                \<p\>\<strong\>Published on:\</strong\> {{ post.created\_at }}\</p\>

            \</li\>

        {% empty %}

            \<p\>No posts available.\</p\>

        {% endfor %}

    \</ul\>

\</body\>

\</html\>

---

### **Step 5: Test the Post Detail Page**

1. Run the server:  
     
   python manage.py runserver  
     
2. Go to `http://127.0.0.1:8000/` and click on a post title.  
     
3. The post detail page should open, displaying the full content.

pip install django-debug-toolbar

from django.conf import settings from django.conf.urls.static import static from django.contrib import admin from django.urls import include, path

if settings.DEBUG: import debug\_toolbar

urlpatterns \+= \[path("\_\_debug\_\_/", include(debug\_toolbar.urls))\]

urlpatterns \+= static(settings.MEDIA\_URL, document\_root=settings.MEDIA\_ROOT)

urlpatterns \+= static(settings.STATIC\_URL, document\_root=settings.STATIC\_ROOT)

"debug\_toolbar.middleware.DebugToolbarMiddleware",

DEBUG\_TOOLBAR\_PANELS \= \[ "debug\_toolbar.panels.versions.VersionsPanel", "debug\_toolbar.panels.timer.TimerPanel", "debug\_toolbar.panels.settings.SettingsPanel", "debug\_toolbar.panels.headers.HeadersPanel", "debug\_toolbar.panels.request.RequestPanel", "debug\_toolbar.panels.sql.SQLPanel", "debug\_toolbar.panels.staticfiles.StaticFilesPanel", "debug\_toolbar.panels.templates.TemplatesPanel", "debug\_toolbar.panels.cache.CachePanel", "debug\_toolbar.panels.signals.SignalsPanel", "debug\_toolbar.panels.logging.LoggingPanel", "debug\_toolbar.panels.redirects.RedirectsPanel", \]

def show\_toolbar(request): return True

DEBUG\_TOOLBAR\_CONFIG \= { "INTERCEPT\_REDIRECTS": False, "SHOW\_TOOLBAR\_CALLBACK": show\_toolbar, }  
