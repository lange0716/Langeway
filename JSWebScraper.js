const axios = require('axios');
const cheerio = require('cheerio');

const getFeedTitles = async () => {
    try {
        const {data} = await axios.get(
            'https://time.com/'
        );
        const $ = cheerio.load(data);
        const postTitles = [];

        $('ul > li.most-popular-feed__item').each((_idx, el) => {
            const postTitle = $(el).text()
            postTitles.push(postTitle)
        });

        return postTitles;
    }
    catch (error) {
        throw error;
    }
};

getFeedTitles()
.then((postTitles) => console.log(postTitles));