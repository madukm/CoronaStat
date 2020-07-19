// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your Javascript code.
function get_cities_from_state(state_name) {
    let begin_string = "<datalist id=\"city_locations\">"
    let end_string = "</datalist>"
   
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            //console.log(this.responseText);
            let ret_cities = JSON.parse(this.responseText);
            //console.log(ret_cities);
            function city_list() {
                let avail_options = begin_string;
                for (let cityName of ret_cities) {
                    console.log(cityName);
                    avail_options += "<option value=\"" + cityName + "\" />";
                }
                avail_options += end_string;
                return avail_options;
            }
            document.getElementById("city_input_options").innerHTML = city_list();
        }
    };
    xmlhttp.open("GET", "http://127.0.0.1:5000/api/nomes/cidade?state=" + state_name, true);
    xmlhttp.send();
}
