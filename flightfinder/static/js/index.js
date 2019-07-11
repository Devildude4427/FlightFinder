let outboundIATACode = "";

new autoComplete({
    selector: 'input[id="port-outbound"]',
    minChars: 3,
    delay: 250,
    source: function (term, suggest) {
        const apiRequest = new Request('https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/' +
            'apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query=' + term, {
            headers: {
                    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95"
            }
        });

        fetch(apiRequest)
            .then(response => {
                if (response.ok) {
                    return response.json()
                }
            })
            .then(data => {
                let places = [];
                const {Places} = data;
                Places.forEach(location => {
                    places.push(location);
                });
                suggest(places);
            });
    },
    renderItem: function (item){
        let {PlaceId} = item;
        const {CityId, PlaceName, CountryName} = item;

        const uncutPlaceId = PlaceId;
        if (PlaceId === CityId) PlaceId = "Any";
        else PlaceId = PlaceId.slice(0, -4);

        return '<div class="autocomplete-suggestion" outbound-iata-code="' + uncutPlaceId + '" ' +
               'mocks-val="' + PlaceName + ' (' + PlaceId + ') ' + CountryName +'">' +
                    '<b>' + PlaceName + '</b>' +
                    ' (' + PlaceId + ') ' + CountryName +'' +
               '</div>'
    },
    onSelect: function (e, term, item) {
        outboundIATACode = item.getAttribute('outbound-iata-code');
    }
});

function postInputs() {
    fetch("/getQuotes", {
        method: "POST",
        body: JSON.stringify({
            portOutbound: document.getElementById("port-outbound"),
            dateOutbound: document.getElementById("date-outbound"),
            earliestTimeOutbound: document.getElementById("earliest-time-outbound"),
        })
    }).then(response => {
        document.getElementsByClassName("slide")[0].style.top = "-100vh";
        console.log("POST response: " + response)
    });
}