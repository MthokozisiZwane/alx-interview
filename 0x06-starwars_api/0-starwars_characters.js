#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as the chars list in the /films/ endpoint
 */

const request = require('request');
const movieId = process.argv[2] + '/';
const apiURL = 'https://swapi-api.hbtn.io/api/films/';
// Makes API request, sets async to allow await promise
request(apiURL + movieId, async (err, res, body) => {
  if (err) return console.error(err);

  // finds URL of each character in the film
  const  filmData = JSON.parse(body).characters;

  // Use URL list to make requests
  // await queues requests until they resolve
  for (const characterUrl of  filmData) {
    await new Promise((resolve, reject) => {
      request(characterUrl, (err, res, body) => {
        if (err) return console.error(err);

        // finds each character name and prints in URL order
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
