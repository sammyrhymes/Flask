# JINJA2

In this section we will be going through template design with jinja2 so buckle up.

A Jinja template is simply a text file. Jinja can generate any text-based format (HTML, XML, CSV, LaTeX, etc.). A Jinja template doesn’t need to have a specific extension: .html, .xml, or any other extension is just fine.

A template contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template. The template syntax is heavily inspired by Django and Python.

Below is a minimal template that illustrates a few basics using the default Jinja configuration. We will cover the details later in this document:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <title>My Webpage</title>
</head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>

    <h1>My Webpage</h1>
    {{ a_variable }}

    {# a comment #}
</body>
</html>
```

The following example shows the default configuration settings. An application developer can change the syntax configuration from {% foo %} to <% foo %>, or something similar.

There are a few kinds of delimiters. The default Jinja delimiters are configured as follows:

    **{% ... %}** for Statements

    **{{ ... }}** for Expressions to print to the template output

    **{# ... #}** for Comments not included in the template output

Line Statements and Comments are also possible, though they don’t have default prefix characters. To use them, set line_statement_prefix and line_comment_prefix when creating the Environment.