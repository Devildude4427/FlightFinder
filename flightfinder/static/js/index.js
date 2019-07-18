let locale = () => { return document.getElementById("select-locale").value; };
let country = () => { return locale().slice(3); };
let currency = () => { return document.getElementById("select-currency").value; };

let outboundIATACode = "";
let dateOutbound = "";

datepicker("#date-outbound", {
    minDate: new Date(),
    onSelect: (instance) => dateOutbound = dateFormatter((instance.dateSelected).toISOString())
});

AutoComplete({
    selector: "input[id='port-outbound']",
    minChars: 3,
    delay: 250,
    source: function (term, suggest) {
        const apiRequest = new Request("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/" +
            "apiservices/autosuggest/v1.0/" + country() + "/" + currency() + "/" + locale() + "/?query=" + term, {
            headers: {
                    "X-RapidAPI-Host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
                    "X-RapidAPI-Key": "70f8ad8a68mshf3eb22144cd2fbbp1c6840jsn4efbf8230f95"
            }
        });

        fetch(apiRequest)
            .then((response) => {
                if (response.ok) {
                    return response.json();
                }
            })
            .then((data) => {
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
        if (PlaceId === CityId) {
            PlaceId = "Any";
        }
        else {
            PlaceId = PlaceId.slice(0, -4);
        }

        return `<div class='autocomplete-suggestion' outbound-iata-code="${uncutPlaceId}" ` +
            `data-val="${PlaceName} (${PlaceId}) ${CountryName}">` +
            `<b>${PlaceName}</b> (${PlaceId}) ${CountryName}</div>`;
    },
    onSelect: function (e, term, item) {
        outboundIATACode = item.getAttribute("outbound-iata-code");
    }
});

function postInputs() {
    if(formValidated()) {
        fetch("/getQuotes", {
            method: "POST",
            headers: new Headers({
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }),
            body: JSON.stringify({
                portOutbound: outboundIATACode,
                dateOutbound: dateOutbound,
                earliestTimeOutbound: document.getElementById("earliest-time-outbound").value,
                locale: locale(),
                country: country(),
                currency: currency(),
            })
            }).then(response => {
                if (response.ok) {
                    return response.json();
                }
            }).then(data => {
                clearQuotes();
                slidePaneUp();
                populateQuoteList(data);
            });
    }
}

let formValidated = () => {
    const errorMessage = document.getElementById("error-message");
   if (!outboundIATACode || outboundIATACode.indexOf('-sky') === -1) {
       errorMessage.style.opacity= "1";
       return false;
   }
   errorMessage.style.opacity= "0";
   return true;
};

function dateFormatter(date) {
    return date.split("T")[0];
}

function slidePaneUp() {
    document.getElementsByClassName("slide")[0].style.top = "-100vh";
}

function clearQuotes() {
    const quoteList = document.getElementById("quote-list");
    while (quoteList.firstChild) {
        quoteList.removeChild(quoteList.firstChild);
    }
}

function currencySymbol() {
    return (currency() === "USD" ? " $" : " £");
}

function populateQuoteList(jsonResponse) {
    const quoteParent = document.getElementById("quote-list");
    if (!jsonResponse.hasOwnProperty("errorMessage")) {
        (jsonResponse.quotes).forEach((quote) => {
            const quoteElement = document.createElement("div");
            quoteElement.classList.add("quote");
            quoteParent.appendChild(quoteElement);

            const destinationPrice = document.createElement("h3");
            destinationPrice.innerHTML = quote["destination"] + ", " + quote["country"] + currencySymbol() + quote["price"];
            quoteElement.appendChild(destinationPrice);

            const carrierDates = document.createElement("h4");
            carrierDates.innerHTML = quote["carrierOutbound"] + " " + dateFormatter(quote["dateOutbound"]) + " - " +
                dateFormatter(quote["dateInbound"]) + " " + quote["carrierInbound"];
            quoteElement.appendChild(carrierDates);
        });
    }
    else {
        const quoteElement = document.createElement("div");
        quoteElement.classList.add("quote");
        quoteParent.appendChild(quoteElement);

        const destinationPrice = document.createElement("h3");
        destinationPrice.innerHTML = jsonResponse["errorMessage"];
        quoteElement.appendChild(destinationPrice);
    }

}