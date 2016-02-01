var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var arr =['abc','abc','bbc','ccc','abc','bbc'];
  	res.render('index', { title: 'Express',titles:arr});
});

module.exports = router;
