#  UNUQUE URL AND REDIRECTIONS

### relevant codes

```
# format 1 (cononical url)
@app.route('/project/')
def project():
    return 'this is the project page'
# format 2
@app.route('/about')
def project():
    return 'this is the about page'

```
From the above codes we can see two ways of creating urls. From our stand point both these are ok, and lead to the same address whether you add the trailspace or not. This is not true on the browser side i.e the browser will identify 127.0.0.1:5000/about and 127.0.0.1:5000/about/ as two separate addresses. Due to SEO and avoiding double indexing by the browser, this standard was introduced.

##### In simple terms #####

The first one with 127.0.0.1:5000/project/ is what we call a cononical url. This is because no matter how you spell *(with or without trailing slash)* it successfully opens the project page. 
![project page](../static/unique_url%26redirections/project.png)

Opening the about page the way it was defined in the route decorator, it succesfully opens the about page. 

![about page](../static/unique_url%26redirections/about.png)

However; when you try opening it as 127.0.0.1:5000/about/ *with a trailing slash* it will lead to a rediection error stating **page not found** error 404.

![404 error page](../static/unique_url%26redirections/404.png)


Best advice is to choose one and stick to one format for the whole project. The first one has a layer of redirection error protection so it would be available to use that one.
