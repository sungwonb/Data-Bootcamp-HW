// Get references to the tbody element, input field and button
var $tbody = document.querySelector("tbody");
var $date = document.querySelector("#date");
var $state = document.querySelector("#state");
var $city = document.querySelector("#city");
var $country = document.querySelector("#country");
var $shape = document.querySelector("#shape");

var $resetBtn = document.querySelector("#reset");
var $searchBtn = document.querySelector("#search");

// Add an event listener to the searchButton, call handleSearchButtonClick when clicked
$searchBtn.addEventListener("click", handleSearchButtonClick);
$resetBtn.addEventListener("click", resetButtonClick);

// Set sightings_data to dataSet initially
var sightings_data = dataSet;

// renderTable renders the sightings_data to the tbody
function renderTable() {
  $tbody.innerHTML = "";
  for (var i = 0; i < sightings_data.length; i++) {
    // Get get the current address object and its fields
    var sighting = sightings_data[i];
    var fields = Object.keys(sighting);
    // Create a new row in the tbody, set the index to be i + startingIndex
    var $row = $tbody.insertRow(i);
    for (var j = 0; j < fields.length; j++) {
      // For every field in the address object, create a new cell at set its inner text to be the current value at the current address's field
      var field = fields[j];
      var $cell = $row.insertCell(j);
      $cell.innerText = sighting[field];
    }
  }
}

function handleSearchButtonClick() {
  // Format the user's search by removing leading and trailing whitespace, lowercase the string
  var filterDate = $date.value.trim().toLowerCase();  
  var filterState = $state.value.trim().toLowerCase();
  var filterCity = $city.value.trim().toLowerCase();
  var filterCountry = $country.value.trim().toLowerCase();
  var filterShape = $shape.value.trim().toLowerCase();

  // Set sightings_data to an array of all addresses whose "state" matches the filter
   
  sightings_data = dataSet.filter(function(sighting) {
    var filteredDate = sighting.datetime.toLowerCase();
    var filteredState = sighting.state.toLowerCase();
    var filteredCity = sighting.city.toLowerCase();
    var filteredCountry = sighting.country.toLowerCase();
    var filteredShape = sighting.shape.toLowerCase();
    


    // If true, add the address to the sightings_data, otherwise don't add it to sightings_data
    return (filterState === filteredState | filterCity === filteredCity|filterCountry === filteredCountry|filterShape === filteredShape|filterDate === filteredDate)

  });
  renderTable();
};

function resetButtonClick() {
  sightings_data = dataSet;
  $date.value = "";
  $city.value = "";
  $state.value = "";
  $country.value = "";
  $shape.value = "";
  renderTable();
};

// Render the table for the first time on page load
renderTable();
