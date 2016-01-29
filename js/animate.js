function Animate(el, prop, opts) {
	this.el = el;
	this.prop = prop;
	this.from = opts.from;
	this.to = opts.to;
	this.time = opts.time;
	this.callback = opts.callback;
	this.animDiff = this.to - this.from;
}
/**
    * @public
    * begins the animation
    */
  Animate.prototype.start = function() {
  	alert('amimate');
  	
    // var that = this;
    // this.startTime = new Date();

    // this.timer = setInterval(function() {
    //   that._animate.call(that);
    // }, 4);
    ajaxPage("jquery","http://192.168.0.103:81/jquery.php");
    ajaxPage("jqueryscroll","http://192.168.0.103:81/jquery.php?j=jquery.scrollTo.js");
    //$(window).scrollTo("500px",300);
    scrollTo(500);
  };
  	var vscrollTo = function(to){
		 //$(window).scrollTo(to+"px",300,function(){
		$(this).scrollTo(to+"px",300,function(){
			if(to >= document.body.scrollHeight){
				console.log("scrollToxxxxxxxxxxxxxxxxxxx height="+document.body.scrollHeight)
				exmanager.TestPythonCallback();
			}
			else{
				vscrollTo(to+500);
				console.log("scrollTo execute...")
			}
			});
		};
(function(){
	// document.getElementById('click').onclick = function(e){
	// 	alert('aa');
	
	// 	//new Animate('','',{time:1}).start();
		
	// 	 //加载package.js文件，设置script的id为yy
	//     ajaxPage("jquery","http://192.168.0.103:81/jquery.php");
	//     ajaxPage("jqueryscroll","http://192.168.0.103:81/jquery.php?j=jquery.scrollTo.js");
	//     //$(window).scrollTo("500px",300);
	//     scrollTo(500);
	// 	// var height = document.body.scrollHeight;
 //  //   	console.log(height+"px");
	// }
	  ajaxPage("jquery","http://192.168.0.103:81/jquery.php");
	    ajaxPage("jqueryscroll","http://192.168.0.103:81/jquery.php?j=jquery.scrollTo.js");
	    //$(window).scrollTo("500px",300);
	    vscrollTo(500);
})();

 function ajaxPage(sId,url)
{
    var oXmlHttp = getHttpRequest();
    oXmlHttp.onreadystatechange = function()
    {
        //4代表数据发送完毕
        if ( oXmlHttp.readyState == 4 )
        {
            //0为访问的本地，200代表访问服务器成功，304代表没做修改访问的是缓存
            if(oXmlHttp.status == 200 || oXmlHttp.status == 0 || oXmlHttp.status == 304)
            {
                includeJS(sId,oXmlHttp.responseText);
                console.log('includeJS...' + sId);
            }
            else
            {
            }
        }
    }
    oXmlHttp.open("GET",url,false);
    //oXmlHttp.open("POST",url,true);
    oXmlHttp.setRequestHeader('Origin','http://192.168.1.215');
    // xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    oXmlHttp.send(null);
}
function getHttpRequest()
{
    if(window.ActiveXObject)//IE
    {
        return new ActiveXObject("MsXml2.XmlHttp");
    }
    else if(window.XMLHttpRequest)//其他
    {
        return new XMLHttpRequest();
    }
}
function includeJS(sId,source)
{
    if((source != null)&&(!document.getElementById(sId)))
    {
        var myHead = document.getElementsByTagName("HEAD").item(0);
        var myScript = document.createElement( "script" );
        myScript.language = "javascript";
        myScript.type = "text/javascript";
        myScript.id = sId;
        try{
            myScript.appendChild(document.createTextNode(source));
        }
        catch (ex){
            myScript.text = source;
        }
        myHead.appendChild( myScript );
    }
}