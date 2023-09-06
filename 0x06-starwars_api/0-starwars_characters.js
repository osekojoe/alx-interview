#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const movieId = process.argv[2];

async function StarWarsCharacters(movieId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieId;
  let response = await (await request(endpoint)).body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const characterUrl = characters[i];
    let character = await (await request(characterUrl)).body;
    character = JSON.parse(character);
    console.log(character.name);
  }
}

StarWarsCharacters(movieId);