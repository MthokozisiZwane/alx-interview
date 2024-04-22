#!/usr/bin/node

// Import the 'request' module for making HTTP requests
const request = require('request');

process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";

// Extract the movie ID from the command-line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided as a command-line argument
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

// Construct the API URL for fetching movie data based on the provided movie ID
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Make an HTTP GET request to the Star Wars API endpoint for the specified movie
request(apiUrl, (error, response, body) => {
  // Check for errors during the request
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check for unexpected status codes
  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  // Parse the JSON data returned by the API
  const filmData = JSON.parse(body);

  // Extract the list of characters from the movie data
  const characters = filmData.characters;

  // Iterate over the list of character URLs
  characters.forEach(characterUrl => {
    // Make an HTTP GET request to fetch character data
    request(characterUrl, (error, response, body) => {
      // Check for errors during the request
      if (error) {
        console.error('Error:', error);
        return;
      }

      // Parse the JSON data returned by the API
      const characterData = JSON.parse(body);

      // Print the name of the character to the console
      console.log(characterData.name);
    });
  });
});
