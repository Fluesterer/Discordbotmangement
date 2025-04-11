const express = require('express');
const bodyParser = require('body-parser');
const { Client } = require('discord.js');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(express.static('public'));

let botClient;

app.post('/login', async (req, res) => {
    const token = req.body.token;
    
    try {
        botClient = new Client();
        await botClient.login(token);
        res.status(200).send('Erfolgreich eingeloggt');
    } catch (error) {
        res.status(400).send('Ungültiges Token');
    }
});

app.get('/dashboard', (req, res) => {
    if (!botClient) {
        return res.redirect('/');
    }
    // Gebe die Dashboard-Seite zurück
    res.sendFile(__dirname + '/public/dashboard.html');
});

app.listen(port, () => {
    console.log(`Server läuft auf http://localhost:${port}`);
});
