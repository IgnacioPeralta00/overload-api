const exercisesEN = require('../data/exercises_en.json');
const exercisesES = require('../data/exercises_es.json');

module.exports = (req, res) => {

    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');

    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }


    const lang = req.query.lang === 'es' ? 'es' : 'en';
    const responseData = lang === 'es' ? exercisesES : exercisesEN;

    res.status(200).json(responseData);
};