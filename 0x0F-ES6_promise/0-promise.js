export default function getResponseFromAPI() {
  const myPromise = new Promise((resolve) => {
    resolve('foo');
  });
  return myPromise;
}
