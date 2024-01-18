#!/usr/bin/node
const request = require('request');
const args = process.argv.slice(2);
const id = parseInt(args[0]);

function returnCharacters () {
  return new Promise((resolve, reject) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

    request(url, (_err, _response, body) => {
      const jsonData = JSON.parse(body);
      try {
        resolve(jsonData.characters);
      } catch (err) {
        reject(err);
      }
    });
  });
}

returnCharacters().then((characters) => {
  for (const character of characters) {
    request(character, (_err, _response, body) => {
      const jsonData = JSON.parse(body);
      console.log(jsonData.name);
    });
  }
});
