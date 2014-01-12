import urllib2
import urlparse
import lxml.html
import lxml.etree
import traceback

START_URL = "http://www.occ.gov/topics/licensing/interpretations-and-actions/index-interpretations-and-actions.html"
XPATH_NAMESPACES = dict(re='http://exslt.org/regular-expressions')
links_start = []
links_tables = []

if __name__ == '__main__':
    '''
    This example code gets html from the top level web page, converts it to an xml tree,
    and uses xpath to select and print the relevant elements
    '''
    find_links_start = lxml.etree.XPath("//ul //li //a[re:test(., '[0-9]')]",  
        namespaces=XPATH_NAMESPACES)

    # Type 1 for 1996-1998 and 1999-2004 -> links_start[2] y links_start[3]
    find_links_table_ty1 = lxml.etree.XPath("//table[re:match(@class, \
        'table_brdr')] //tr //td //div //a[re:match(@class, 'tbd')]", \
        namespaces=XPATH_NAMESPACES)
    # Type 2 for 2005-2010 -> links_start[1]
    find_links_table_ty2 = lxml.etree.XPath("//table[re:match(@class, \
        'table_brdr')] //tr //td //a[re:match(@class, 'tbd')]", \
        namespaces=XPATH_NAMESPACES)
    # Type 2 for 2011-2013 -> links_start[0]
    find_links_table_ty3 = lxml.etree.XPath("//table[re:match(@class, \
        'table_brdr')] //tr //td //a", namespaces=XPATH_NAMESPACES)
    
    try:
        # get html url and convert it to an etree
        rawhtml = urllib2.urlopen(START_URL).read()
        xmlTree = lxml.etree.fromstring(rawhtml, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
       
        # find relevant links and print them to stdout
        for link in find_links_start(xmlTree):
            href = urlparse.urljoin(START_URL, link.get("href"))
            links_start.append((href))
        rh0 = urllib2.urlopen(links_start[0]).read()
        xt0 = lxml.etree.fromstring(rh0, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
        
        for l0 in find_links_table_ty3(xt0):
            href = l0.get("href")
            links_tables.append((href))
        links_tables[31] = 'http://www.occ.gov' + links_tables[31]
        links_tables[34] = 'http://www.occ.gov' + links_tables[34]
        
        rh1 = urllib2.urlopen(links_start[1]).read()
        xt1 = lxml.etree.fromstring(rh1, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
        for l1 in find_links_table_ty2(xt1):
            href = l1.get("href")
            links_tables.append((href))
        
        rh2 = urllib2.urlopen(links_start[2]).read()
        xt2 = lxml.etree.fromstring(rh2, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
        for l2 in find_links_table_ty1(xt2):
            href = l2.get("href")
            links_tables.append((href))
            
        rh3 = urllib2.urlopen(links_start[3]).read()
        xt3 = lxml.etree.fromstring(rh3, parser = lxml.html.HTMLParser(recover=True, 
            remove_comments=True))
        for l3 in find_links_table_ty2(xt3):
            href = l3.get("href")
            links_tables.append((href))
        
        for l in links_tables:
            print l
             
    except:
        print ("Exception while parsing: %s\n" % traceback.format_exc())

