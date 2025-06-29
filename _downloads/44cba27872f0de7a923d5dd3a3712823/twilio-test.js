#!/usr/bin/env node
// From: http://twilio.github.io/twilio-node/
// Twilio Credentials 
var accountSid = ''; 
var authToken = ''; 
 
//require the Twilio module and create a REST client 
var client = require('twilio')(accountSid, authToken); 
 
client.messages.create({ 
	to: "812555121", 
	from: "+2605551212", 
	body: "This is a test",   
}, function(err, message) { 
	console.log(message.sid); 
});

// https://github.com/twilio/twilio-node/blob/master/LICENSE