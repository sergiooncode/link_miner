# link_miner

Link Miner is a useful example showing the use of lxml XML toolkit.

Use of XPath class:

<pre>
find_links_start = lxml.etree.XPath("//ul //li //a[re:test(., '[0-9]')]",  
        namespaces=XPATH_NAMESPACES)
</pre>
