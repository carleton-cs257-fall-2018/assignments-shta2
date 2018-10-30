makeTables();

function openTab(tableName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    document.getElementById(tableName).style.display = '';
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = '#e6e6e6';
    }
    document.getElementById(tableName).style.display = "block";
    document.getElementById(tableName + 'Button').style.backgroundColor = '#b3b3b3';
}

function getBaseURL() {
    //var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + 5105;
    var baseURL = "http://perlman.mathcs.carleton.edu:5105";
    return baseURL;
}

function makeTables(){
  var url = getBaseURL() + '/transactions?recipient_id=S8AZ00155'; //+ {{ id }};

  fetch(url, {method: 'get'})
  .then((response) => response.json())
  .then(function(donationsList) {
      // Build the table body.
      var tableBody = '';
      var ids = [];
      for (var k = 0; k < donationsList.length; k++) {
          tableBody += '<tr>';
          tableBody += '<td>' + donationsList[k][0] + '</td>';
          tableBody += '<td>' + donationsList[k][1] + '</td>';
          if(donationsList[k][3] = 'PAC'){
            tableBody += '<td> <a onclick="getPAC"><div class=' + donationsList[k][2] + '></div></a></td>';
          }else {
            tableBody += '<td><div class=' + donationsList[k][2] + '></div><</td>';
          }
          ids.push([donationsList[k][2], donationsList[k][3]]);
          tableBody += '<td>' + donationsList[k][3] + '</td>';
          tableBody += '</tr>' ;
      }

      // Put the table body we just built inside the table that's already on the page.
      var resultsTableElement = document.getElementById('allContributions');
      if (resultsTableElement) {
          resultsTableElement.innerHTML = tableBody;
      }
      getContributors(ids)
  })
}

function getContributors(ids){
   for (var i=0; i<ids.length; i++){
     console.log(ids[i][0] + " " + ids[i][1])
     var url = getBaseURL() + '/'
     if(ids[i][1] = 'PAC'){
       url += 'pacs'
     }
     else{
       url += 'individuals'
     }
     url += '?id=' + ids[i][0];
     console.log(url)
     var result;
     var tim = i;
     fetch(url, {method: 'get'}).then((response) => response.json()).then(function(ans) {
        console.log(ans);
        var x = document.getElementsByClassName(ans[0][0]);
        var j;
        for (j = 0; j < x.length; j++) {
           x[j].innerHTML = ans[0][1];
        }
     })
   }
}




//{{ api_port }}
