# link_miner

Link Miner is a useful example showing the use of lxml XML toolkit. The code is based on: 

- XPath class in lxml.etree submodule to select relevant HTML elements.
- HTMLParser class in lxml.html submodule to parse the raw HTML.
- Functions in urllib2 and urlparse modules to work with URLs. 

Use of XPath class:

<pre>
find_links_start = lxml.etree.XPath("//ul //li //a[re:test(., '[0-9]')]",  
        namespaces=XPATH_NAMESPACES)
</pre>

Use of HTMLParser:

<pre>
xmlTree = lxml.etree.fromstring(rawhtml, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
</pre> 

In this example the page to be crawled is the one found on the Office of the Comptroller of the Currency website under Topics > Licensing > <a href="http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html" target ="_blank">Interpretations and Actions</a> 
