window.addEventListener("load", function(){
    const name_input = document.getElementById('portOutbound');
    name_input.addEventListener("keyup", function(event){hinter(event)});

    window.hinterXHR = new XMLHttpRequest();
});

function hinter(event) {
    const input = event.target;

    const huge_list = document.getElementById('huge_list');

    const min_characters = 1;

    if (input.value.length > min_characters ) {
        // abort any pending requests
        window.hinterXHR.abort();

        window.hinterXHR.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                // We're expecting a json response so we convert it to an object
                const response = JSON.parse( this.responseText );

                // clear any previously loaded options in the datalist
                huge_list.innerHTML = "";

                response.forEach(function(item) {
                    // Create a new <option> element.
                    const option = document.createElement('option');
                    option.value = item.PlaceName;

                    // attach the option to the datalist element
                    huge_list.appendChild(option);
                });
                input.blur();
            }
            input.focus();
        };

        window.hinterXHR.open("GET", "https://www.skyscanner.net/g/autosuggest-flights/GB/en-GB/" + input.value +"?ccy=GBP", true);
        window.hinterXHR.send()
    }
}
