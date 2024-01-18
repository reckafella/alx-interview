#!/usr/bin/node
const request = require('request');

const args = process.argv.slice(2);
const id = parseInt(args[0]);
const URL = `https://swapi-api.hbtn.io/api/films/${id}`;

function printCharacterNames (characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (_err, _response, body) => {
    if (_err) {
      console.log(_err);
    }
    const jsonData = JSON.parse(body);
    console.log(jsonData.name);
    printCharacterNames(characters, index + 1);
  });
}

request(URL, (_err, _response, body) => {
  if (_err) {
    console.log(_err);
  }
  const jsonData = JSON.parse(body);
  printCharacterNames(jsonData.characters, 0);
});
