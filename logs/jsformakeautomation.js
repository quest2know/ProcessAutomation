// Input: HTML passed from previous module
let html = inputData.html;
 // Use DOMParser-like behavior via JSDOM substitute 
const cheerio = require('cheerio');
const $ = cheerio.load(html);
 // Extract all <a> tags 
let links = []; 
$('a').each((i, el) => { const href = $(el).attr('href');
// Only keep product links
if (href && href.includes('/products/')) 
{ 
// Convert relative URLs to absolute
    let fullUrl = href.startsWith('http') ? href : `https://doreefashions.com${href}`;
    links.push(fullUrl);
} });
println(`Extracted ${links.length} product links.`);   
for (let link of links) {
    println(link);
}
return links;
// Return array to Make.com output = { productLinks: links };