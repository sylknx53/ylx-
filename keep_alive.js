const keepAlive = require('./keep_alive.js');
keepAlive();
   
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send("Bot 7/24 Aktif ve Calisiyor!");
});

function keepAlive() {
    
    const port = process.env.PORT || 10000;
    
    app.listen(port, '0.0.0.0', () => {
        console.log(`Keep-alive sunucusu ${port} portunda başlatıldı.`);
    });
}


module.exports = keepAlive;