module.exports = (req, res) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Content-Type', 'application/json');
    
    res.status(200).json({
        message: 'Welcome to Overload API',
        endpoints: {
            exercises: '/api/exercises?lang=en',
            exercisesES: '/api/exercises?lang=es'
        }
    });
};
