// app.js
var express = require('express');
var path = require("path");
var bodyParser = require('body-parser');
var app = express();
var products = [
    { id:1,name:'Bhavesh' },
    { id:2,name:'Jane'},
    { id:3,name:'Smith'},
    { id:4,name:'Bruce'}
];

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname,'./public')));
app.get('/', function(req,res){
    res.sendFile(path.join(__dirname,'./public'));
  });

  app.get('/api/all', (req, res) => {
    res.send(products);
})
app.post('/api/get', (req, res) => {
    const product = products.find(({ id }) => id == req.body.id);

    if (!product)
        res.status(404).send('<h2 style="font-family: Malgun Gothic; color: darkred;">Ooops... Cant find what you are looking for!</h2>');
    res.send(product);
});

app.post('/api/students', (req, res) => {
 var product = {
        id: req.body.id,
        name: req.body.name,
        
    };
    products.push(product);
    res.send(product);
});

app.post('/api/put', (req, res) => {
 var product = products.find(({ id }) => id == req.body.id);
    if (!product) res.status(404).send('<h2 style="font-family: Malgun Gothic; color: darkred;">Not Found!! </h2>');
    product.name = req.body.name;
    res.send(product);
});

app.post('/api/delete', (req, res) => {

 const product = products.find(({ id }) => id == req.body.id);
    if (!product) res.status(404).send('<h2 style="font-family: Malgun Gothic; color: darkred;"> Not Found!! </h2>');

    const index = products.indexOf(product);
    products.splice(index, 1);

    res.send(product);
});
app.listen(8080);


  