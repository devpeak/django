<!DOCTYPE html>
<html>
<head>       
</head>
<body>
    <h2> Django</h2>
    <pre>-----Linux Commands-----
    <b>source</b>: source is a shell built-in command which is used to <em>read</em> and<em> execute </em>the content of a file(generally set of commands).
    </pre>
    <h3>django Virtual Environment Setup</h3>
    
<ul>
    <li>The virtual environment is an environment which is used by Django to <strong>execute</strong> an application.</li>
    <li>It is recommended to create and execute a Django application in a <em>separate environment</em>.</li>
    <li>Python provides a tool <b>virtualenv</b> to create an isolated Python environment.</li>
    <li>We will use this tool to create a virtual environment for our Django application.</li>
</ul>
    
<h3>Commands in Python </h3>
    <pre><ol>
    <li><b>python -m venv virt </b>▶ This will create the virt directory if it doesn’t exist,and also 
    create directories inside it containing a copy of the Python interpreter and various supporting files.</li>
    <li><b>pip freeze </b>▶ This commands allows you to see what modules you have <em>installed</em> and its <em>version with</em> the pip install command to this point.</li>
    <li><b>python -m pip list </b>▶ display all of the packages installed in the virtual environment.</li>
    <li><b>deactivate </b>▶ To deactivate a virtual environment.</li>
    <li><b>django-admin startproject myclub_website </b>▶ This will create a mysite directory in your current directory.</li>
    </ol></pre>

<h4>what startproject created ?</h4>
        <pre>myclub_website/
                    manage.py
                    db.sqlite3
                    myclub_website/
                        __init__.py
                        setting.py
                        urls.py
                        asgi.py
                        wsgi.py
                        __pycache__
</pre>
    <ul>
     <li>The outer <b>myclub_website/</b> root directory is a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.</li>

<li><b>manage.py</b>: A command-line utility that lets you interact with this Django project in various ways.</li>

<li>The inner <b>myclub_website/</b> directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. myclub_website.urls).
</li>

<li><b>myclub_website/__init__.py</b>: An empty file that tells Python that this directory should be considered a Python package.</li>

<li><b>myclub_website/settings.py</b>: Settings/configuration for this Django project.</li>

<li><b>myclub_website/urls.py</b>: The URL declarations for this Django project; a “table of contents” of your Django-powered site.
 </li>

<li>myclub_website/asgi.py: An entry-point for ASGI-compatible web servers to serve your project</li>

<li><b>myclub_website/wsgi.py</b>: An entry-point for WSGI-compatible web servers to serve your project.</li>
</ul>

<h4>The development server</h4>
    <pre>python manage.py runserver</pre>
    <p>You’ll see the following output on the command line:</p>
    <pre>Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    November 29, 2022 - 20:02:28
    Django version 4.1.3, using settings 'myclub_website.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK
</pre>

</body>
</html>