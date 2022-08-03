from datetime import datetime

AUTHOR = 'Julio Melanda'
SITENAME = 'Programe em Python'
SITEURL = 'http://localhost:8000'
SITELOGO = 'images/logo.png'

SUBTITLE = 'Um pouco de tudo sobre programação em Python'

PATH = 'content'

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = []

ROBOTS = "index, follow"

COPYRIGHT_YEAR = datetime.today().year
COPYRIGHT = f'©{COPYRIGHT_YEAR} {AUTHOR}'

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True


MENUITEMS = (
    ("Arquivo", "/archives.html"),
    ("Categorias", "/categories.html"),
    ("Tags", "/tags.html"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TYPOGRIFY = True


# path-specific metadata
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    }

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/CNAME',
    'extra/favicon.ico',
    ]

THEME = 'themes/Flex'
THEME_STATIC_PATHS = ['static']
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['post_stats', 'search', 'related_posts', 'pelican-toc']

# Site search plugin
SEARCH_MODE = "output"
SEARCH_HTML_SELECTOR = "main"
# Table of Content Plugin
TOC = {
    'TOC_HEADERS'       : '^h[1-3]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression
    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated
    'TOC_INCLUDE_TITLE': 'false',    # If 'true' include title in toc
}


DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (('index', 'search', 'tags', 'categories', 'archives',))
PAGINATED_TEMPLATES = {'index':None,'tag':None,'category':None,'author':None,'archives':24,}


THEME_COLOR_ENABLE_USER_OVERRIDE = True

DATE_FORMATS = {
    "en": "%m-%d-%Y",
    "pt_BR": "%d-%m-%Y",
}
BROWSER_COLOR = "#666666"
PYGMENTS_STYLE = "github"
PYGMENTS_STYLE_DARK = "one-dark"


SOCIAL = (
    ("github", "https://github.com/jcemelanda"),
    ("linkedin", "https://www.linkedin.com/in/jcemelanda"),
    ("twitter", "https://twitter.com/jcemelanda"),
)
