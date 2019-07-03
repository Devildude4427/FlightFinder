// window.addEventListener("load", function(){
//     const name_input = document.getElementById('portOutbound');
//     name_input.addEventListener("keyup", function(event){hinter(event)});
//
//     window.hinterXHR = new XMLHttpRequest();
// });
//
// function hinter(event) {
//     const input = event.target;
//
//     const huge_list = document.getElementById('huge_list');
//
//     const min_characters = 1;
//
//     if (input.value.length > min_characters ) {
//         // abort any pending requests
//         window.hinterXHR.abort();
//
//         window.hinterXHR.onreadystatechange = function() {
//             if (this.readyState === 4 && this.status === 200) {
//                 // We're expecting a json response so we convert it to an object
//                 const response = JSON.parse( this.responseText );
//
//                 // clear any previously loaded options in the datalist
//                 huge_list.innerHTML = "";
//
//                 response.forEach(function(item) {
//                     // Create a new <option> element.
//                     const option = document.createElement('option');
//                     option.value = item.PlaceName;
//
//                     // attach the option to the datalist element
//                     huge_list.appendChild(option);
//                 });
//                 input.blur();
//             }
//             input.focus();
//         };
//
//         window.hinterXHR.open("GET", "https://www.skyscanner.net/g/autosuggest-flights/GB/en-GB/" + input.value +"?ccy=GBP", true);
//         window.hinterXHR.send()
//     }
// }

const input = document.getElementById('portOutbound');

new autoComplete({
    data: {                              // Data src [Array, Function, Async] | (REQUIRED)
        src: async () => {
            // Fetch External Data Source
            const source = await fetch(`https://www.skyscanner.net/g/autosuggest-flights/GB/en-GB/` + input.value + `?ccy=GBP`);
            // Format data into JSON
            const data = await source.json();
            // Return Fetched data
            let places = [];
            data.forEach(function(item) {
                places.push(item.PlaceName)
            });
            return places;
        },
        key: ["title"],
        cache: false
    },
    sort: (a, b) => {                    // Sort rendered results ascending | (Optional)
        if (a.match < b.match) return -1;
        if (a.match > b.match) return 1;
        return 0;
    },
    selector: "#portOutbound",           // Input field selector              | (Optional)
    threshold: 2,                        // Min. Chars length to start Engine | (Optional)
    debounce: 500,                       // Post duration for engine to start | (Optional)
    searchEngine: "strict",              // Search Engine type/mode           | (Optional)
    resultsList: {                       // Rendered results list object      | (Optional)
        render: true,
        container: source => {
            resultsListID = "food_List";
            return resultsListID;
        },
        destination: document.querySelector("#portOutbound"),
        position: "afterend",
        element: "ul"
    },
    maxResults: 5,                         // Max. number of rendered results | (Optional)
    highlight: true,                       // Highlight matching results      | (Optional)
    resultItem: {                          // Rendered result item            | (Optional)
        content: (data, source) => {
            source.innerHTML = data.match;
        },
        element: "li"
    },
    onSelection: feedback => {             // Action script onSelection event | (Optional)
        input.value = feedback.selection.value;
    }
});


