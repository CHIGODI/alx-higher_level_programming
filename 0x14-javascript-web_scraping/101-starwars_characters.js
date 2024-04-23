#!/usr/bin/node

/* import the modules */
const request = require('request');

/* declare constants */
const URL_FILM = 'https://swapi-api.alx-tools.com/api/films/';
const MOVIE_ID = process.argv[2];

request(URL_FILM, { json: true }, (err, res, body) => {
  if (err) {
    throw err;
  }
  const charactersUrls = body.results[MOVIE_ID - 1].characters;
  charactersUrls.forEach((actorUrl) => {
    request(actorUrl, { json: true }, (err, res, body) => {
      if (err) {
        throw err;
      }
      console.log(body.name);
    });
  });
});
