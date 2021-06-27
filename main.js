const fs = require("fs");


// console.log(file)

var newIMDb

fs.readFile("./imdb.json", "utf8", (err, jsonString) => {
    if (err) {
        console.log("Error reading file from disk:", err);
        return;
    }
    try {
        const imdb = JSON.parse(jsonString);

        newIMDb = imdb.map(item => {
            item.genres = item['genre'];
            delete item['genre'];
            return item;
        })

        const jsonString2 = JSON.stringify(newIMDb)
        fs.writeFile('./imdb.json', jsonString2, err => {
            if (err) {
                console.log('Error writing file', err)
            } else {
                jsonString
                console.log('Successfully wrote file')
            }
        })

// console.log("Customer address is:", newIMDb)
    } catch (err) {
        console.log("Error parsing JSON string:", err);
    }
});


