function Animate(el, prop, opts) {
	this.el = el;
	this.prop = prop;
	this.from = opts.from;
	this.to = opts.to;
	this.time = opts.time;
	this.callback = opts.callback;
	this.animDiff = this.to - this.from;
}
// var scrollTo = function(to){
// 		$(window).scrollTo(to+"px",300,function(){
// 			if(to >= document.body.scrollHeight){}
// 			else{
// 				scrollTo(to+500);
// 				console.log("scrollTo execute...")
// 			}
// 		});
// 	};
/**
    * @public
    * begins the animation
    */
  Animate.prototype.start = function() {
  	alert('xx');
  	$(window).scrollTo("1500px",300);
  	//scrollTo(500);
    // var that = this;
    // this.startTime = new Date();

    // this.timer = setInterval(function() {
    //   that._animate.call(that);
    // }, 4);
  };

(function(){
	// var scrollTo = function(to){
	// 	$(window).scrollTo(to+"px",300,function(){
	// 		if(to >= document.body.scrollHeight){}
	// 		else{
	// 			scrollTo(to+500);
	// 			console.log("scrollTo execute...")
	// 		}
	// 	});
	// };
	// document.getElementById('click').onclick = function(e){
	// 	//new Animate('','',{time:1}).start();
	// 	alert('ff');
	// 	//var height = document.body.scrollHeight;
	// 	scrollTo(10);
	// 	//$(window).scrollTo("500px",300)
	// }

})();