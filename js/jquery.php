<?php

// We'll be granting access to only the arunranga.com domain which we think is safe to access this resource as application/xml

if($_SERVER['HTTP_ORIGIN'] == "file://")
{
 
    header('Access-Control-Allow-Origin: file://');
    header('Content-type: application/xml');
    parse_str($_SERVER['QUERY_STRING'], $get);
   	if(count($get)==0){
   		readfile('jquery.js');
   	}else{
   		readfile($get['j']);
    }
}
else
{    
header('Content-Type: text/html');
echo "<html>";
echo "<head>";
echo "   <title>Another Resource</title>";
echo "</head>";
echo "<body>",
    "<p>This resource behaves two-fold:";
echo "<ul>",
        "<li>If accessed from <code>http://arunranga.com</code> it returns an XML document</li>";
echo " <li>If accessed from any other origin including from simply typing in the URL into the browser's address bar,";
echo "you get this HTML document</li>", 
    "</ul>",
"</body>",
"</html>";
}
?>