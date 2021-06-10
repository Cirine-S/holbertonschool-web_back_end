import redis from 'redis';
const client = redis.createClient();
const { promisify } = require("util");

client.on("connect", function() {
    console.log('Redis client connected to the server');
});

client.on("error", function(error) {
    console.log('Redis client not connected to the server:', error);
});

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print);


const getAsync = promisify(client.get).bind(client);
const displaySchoolValue = async(schoolName) => console.log(`${await getAsync(schoolName)}`);

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
