# Python Files
These are an alternative if you can't get Jupyter Notebooks to work. The Scraper must be run one command at a time, however the rest can be run normally.

## Scraper
Move the Current Working Directory to `pythonFiles` and open `scraper.py` with python's interactive shell:
```s
cd pythonFiles
```

```s
python scraper.py -i
```

After it's finished loading, log in and move to the weekly blogs section

Open the Blog List
```s
>>> openList()
```

Get the blog links
```s
>>> blogs = getBlogs()
>>> blogLinks = getLinks(blogs)
```

Get all blog text
```s
>>> blogTexts = [loadPageAndScrapeBlog(url) for url in blogLinks]
```

Save the blog data
```s
>>> saveData(blogTexts)
```

