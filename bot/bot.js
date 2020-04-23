const Discord = require('discord.js');
const client = new Discord.Client();
var botID;

const getIDChannelID = "702570260242628698";
const advertChannelID = "702488700403318825";
const loggedInRole = "702877683683688449";

var nextID = 1;

client.once('ready', () => {
	console.log('Ready!');
  botID = client.user.id;
});

client.on('message', message => {
  if (message.author.id == botID) {
    console.log("recieved own message", message.content);
    return;
  }
  if (message.channel.id == getIDChannelID) {
    numToUnkey = parseInt(message.content);
    if (!isNaN(numToUnkey)) {
      if (!message.member.roles.cache.has(loggedInRole)) {
        message.author.send("Jouw code is:\n`" + ((((numToUnkey*2345945)%48355)*2342993)%56464).toString() +";"+ nextID.toString() +"`");
        message.member.roles.add(message.guild.roles.cache.get(loggedInRole))
        nextID += 1;
      } else {
        message.author.send("Je hebt al een code gekregen. Als je een nieuwe nodig hebt neem je contact op met Thijs.");
      }
    } else {
      message.author.send("Dat is geen geldige code. Stuur het getal zonder aanhalingstekens of andere tekens.");
    }
    message.delete()
  } else if (message.channel.id == advertChannelID) {
    message.delete({timeout:1000*60*60*1}); // 1 minuut
  } else if (message.guild === null) {
    message.author.send("Stuur je codes in de `#krijg-je-id`, niet in deze DM.");
  }
});

client.login(require("./auth.json").token);
