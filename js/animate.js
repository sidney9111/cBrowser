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
  	alert('xx');
    // var that = this;
    // this.startTime = new Date();

    // this.timer = setInterval(function() {
    //   that._animate.call(that);
    // }, 4);
  };
(function(){
	document.getElementById('click').onclick = function(e){
		//new Animate('','',{time:1}).start();
		alert('ff');
		$(...).scrollTo(100,200);
	}})();