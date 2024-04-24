#!/usr/bin/node

/* import the modules */
const request = require('request');

/* declare constants */
const URL_FILM = 'https://swapi-api.alx-tools.com/api/films/';
const MOVIE_ID = process.argv[2];

async function fetchCharacters () {
  try {
    const filmResponse = await new Promise((resolve, reject) => {
      request(URL_FILM, { json: true }, (err, res, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(body);
        }
      });
    });

    const charactersUrls = filmResponse.results[MOVIE_ID - 1].characters;
    const names = [];

    for (const actorUrl of charactersUrls) {
      const actorResponse = await new Promise((resolve, reject) => {
        request(actorUrl, { json: true }, (err, res, body) => {
          if (err) {
            reject(err);
          } else {
            resolve(body.name);
          }
        });
      });
      names.push(actorResponse);
    }

    // Log the character names
    names.forEach(name => {
      console.log(name);
    });
  } catch (err) {
    console.error(err);
  }
}

fetchCharacters();
