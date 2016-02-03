var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	var MongoClient = require('mongodb').MongoClient;
	var assert = require('assert');
	var url = 'mongodb://localhost:27017/test';
	var findRestaurants = function(db, callback) {
	   var cursor =db.collection('jian').find( );
	   var list = [];
	   for(var i=0;i<7;i++){
	   	for(var j=0;j<24;j++){
	   		list[i*24+j]=[i,j,0];	
	   	}
	   }
	   // console.log(list[7][2]);
	   // list[7].count+=1;
	   // console.log(list[7].count);
	   cursor.each(function(err, doc) {
	      assert.equal(err, null);
	      if (doc != null) {
	      	var date = new Date(doc.date);
	      	// console.log(doc.date);
      		// console.log(date.getDay());
      		// console.log(date.getHours());
      		list[date.getDay()*24+date.getHours()][2]+=1;

	        //console.dir(doc);
	        //console.log(list[date.getDay()*24+date.getHours()][2]);
	      } else {
	      	//var ret = new Object();
	      	//ret.seriesData = list;
	      	var arr =['abc','abc','bbc','ccc','abc','bbc'];
  	   		res.render('index', { data: list,titles:arr,ret:list});
  	   		console.log(list);
	        callback();
	      }
	   });
	  
	};

	MongoClient.connect(url, function(err, db) {
	  assert.equal(null, err);
	  findRestaurants(db,function(){
	  	db.close();	
	  })
	  
	});

	
});

module.exports = router;
