const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
    res.setHeader('Access-Control-Allow-Credentials', true);
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS');
    res.setHeader('Content-Type', 'application/json');

    if (req.method === 'OPTIONS') {
        res.status(200).end();
        return;
    }

    try {
        const lang = req.query.lang === 'es' ? 'es' : 'en';
        const fileName = lang === 'es' ? 'exercises-es.json' : 'exercises-en.json';
        const filePath = path.join(process.cwd(), 'data', fileName);
        
        const fileContent = fs.readFileSync(filePath, 'utf8');
        const responseData = JSON.parse(fileContent);

        res.status(200).json(responseData);
    } catch (error) {
        console.error('Error:', error);
        res.status(500).json({ 
            error: 'Internal Server Error',
            message: error.message 
        });
    }
};
