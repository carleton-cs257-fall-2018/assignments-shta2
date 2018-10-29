function getBaseURL() {
    //var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + 5105;
    var baseURL = "http://perlman.mathcs.carleton.edu:5105";
    return baseURL;
}


function candidate_search(){
    var resultsTableElement = document.getElementById('results_table');
    resultsTableElement.innerHTML = "you submitted a thing!!";
}

function getFormData(formName) {
    var form = document.getElementById(formName);
    var dictionary = {};
    for (var i = 0; i < form.length; i++){
        dictionary[form[i].name] = form[i].value;
    }
    return dictionary;
}

function candidateSearchClicked() {
    var url = getBaseURL() + '/candidates';
    var parameters = getFormData('candidateForm');
    var first = true;
    for (var parameter in parameters){
        if (parameters[parameter] != ''){
            if(first){
                url += '?';
            } else{
                url += '&';
                first = false;
            }
            url += parameter + '=' + parameters[parameter]
        }
    }

    // Send the request to the Books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(candidatesList) {
        // Build the table body.
        var tableBody = '';
        for (var k = 0; k < candidatesList.length; k++) {
            tableBody += '<tr>';

            tableBody += '<td> <a onclick="getCandidate(' + candidatesList[k]['id'] + ")\">"
                            + candidatesList[k][2] + ', '
                            + candidatesList[k][1] + '</a> </td>';
            tableBody += '<td>' + candidatesList[k][3] + '</td>';
            tableBody += '<td>' + candidatesList[k][4]+ '</td>';
            tableBody += '<td>' + candidatesList[k][5] + '</td>';
            tableBody += '</tr>' ;
        }

        // Put the table body we just built inside the table that's already on the page.
        var resultsTableElement = document.getElementById('results_table');
        if (resultsTableElement) {
            resultsTableElement.innerHTML = tableBody;
        }
    })
}
