#group 有些问题捏
db.test.group({
key:{age:true},
initial:{num:0},
$reduce:function(doc,prev)
{
prev.num++
},
condition:{age:{$gt:2}}
});