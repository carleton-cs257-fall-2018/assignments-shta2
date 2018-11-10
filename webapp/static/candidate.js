makeTables();
document.getElementById("allButton").click();

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

//build three tables for the candidate based on transactions to that candidate
function makeTables(){
  var url = getBaseURL() + '/transactions?recipient_id=' + id

  fetch(url, {method: 'get'})
  .then((response) => response.json())
  .then(function(donationsList) {
      var tables = {'allContributions': '', 'contributionsFromPACs': '', 'contributionsFromIndividuals': ''}
      for(table in tables){
          tables[table] = '<tr><th>Date</th><th>Amount</th><th>Contributor</th><th>Contributor Type</th></tr>';
          var ids = [];
          for (var k = 0; k < donationsList.length; k++) {
              //Skip this entry when building Donations from PACs table
              if(table == 'contributionsFromPACs' && donationsList[k][3] == 'Individual'){
                  continue
              }
              //Skip this entry when building Individual Donations table
              if(table == 'contributionsFromIndividuals' && donationsList[k][3] == 'PAC'){
                  continue
              }
              tables[table] += '<tr>';
              tables[table] += '<td>' + donationsList[k][0] + '</td>';
              tables[table] += '<td>' + donationsList[k][1] + '</td>';
              //checks contributor type
              if(donationsList[k][3] == 'PAC'){
                tables[table] += '<td> <a onclick="getPAC"><div class=' + donationsList[k][2] + '></div></a></td>';
              }else {
    	        tables[table] += '<td><div class=' + donationsList[k][2] + '></div><l/td>';
              }
              ids.push([donationsList[k][2], donationsList[k][3]]);
              tables[table] += '<td>' + donationsList[k][3] + '</td>';
              tables[table] += '</tr>' ;
          }
          var resultsTableElement = document.getElementById(table);
          if (resultsTableElement) {
              console.log('hello paul and conor');
              resultsTableElement.innerHTML = tables[table];
          }
      }
      getContributors(ids)
  })
}

//gets the string of the contributor name based on the inputted list of [id, contributor_type] pairs
function getContributors(ids){
   for (var i=0; i<ids.length; i++){
     var url = getBaseURL() + '/'
     if(ids[i][1] == 'PAC'){
       url += 'pacs';
     }
     else{
       url += 'individuals';
     }
     url += '?id=' + ids[i][0];
     url = url.replace(' ', '%20');
     
     fetch(url, {method: 'get'}).then((response) => response.json()).then(function(result) {
        var tableCell = document.getElementsByClassName(result[0][0]);
        for (var j = 0; j < tableCell.length; j++) {
           tableCell[j].innerHTML = result[0][1];
        }
     })
   }
}

function makeHeader(){
   document.getElementById('name').innerHTML()
}
