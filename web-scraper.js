const request = require('request-promise');
const cheerio = require('cheerio');

request('https://gameranx.com/news/')
if(!error && response.statusCode == 200){
    const $ = cheerio.load(html);
}

const data = $('.entries-wrap')