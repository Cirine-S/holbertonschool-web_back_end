import redis from 'redis';
const client = redis.createClient();

client.on("connect", function() {
    console.log('Redis client connected to the server');
});

client.on("error", function(error) {
    console.log('Redis client not connected to the server:', error);
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '10');
displaySchoolValue('HolbertonSanFrancisco');
