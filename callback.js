const express = require('express');
const app = express();

app.use(express.json());

app.post('/callback', (req, res) => {
    console.log('Received data:', req.body);
    res.send('Data received');
});

app.listen(8080, '95.163.223.236', () => {
    console.log('Server is running on 95.163.223.236:8080');
});