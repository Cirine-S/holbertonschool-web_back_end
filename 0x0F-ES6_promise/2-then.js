export default function handleResponseFromAPI(promise) {
  return new Promise((resolve, reject) => {
    console.log('Got a response from the API')
    if (promise) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error());
    }

  });
}
