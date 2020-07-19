using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Net.Http;
using System.Text.Json;
using System.Text.Json.Serialization;
using System.Web;

using CoronaStat.Models;
using Microsoft.EntityFrameworkCore;
using System.Runtime.InteropServices;
using System.Globalization;

namespace CoronaStat.Pages
{
    public class StatsModel : PageModel
    {
        private readonly CovidLocationDbContext _db;
        public Random randgen;
        public StatsModel(CovidLocationDbContext _dbContext) //Constructor.
        {
            _db = _dbContext;
            randgen = new Random();
        }
        public List<int> data_span { get; set; } = new List<int>();

        public class Date
        {
            public DateTime StartDate;
            public DateTime EndDate;
        };

        public Date date { get; private set; } = new Date();

        //Location......
        [BindProperty]
        public LocationData Location { get; set; }

        public List<LocationData> Locations { get; private set; } = new List<LocationData>();
        //public List<string> AvailableLocations { get; } = new List<string>();//

        public List<string> AvailableStates { get; private set; }

        private async Task<List<string>> GetDateRange()
        {
            var builder = new UriBuilder("http://127.0.0.1:5000/api/datas");
            string url = builder.ToString();

            HttpClient httpClient = new HttpClient();
            var res = await httpClient.GetStringAsync(url);
            List<string> a_list = JsonSerializer.Deserialize<List<string>>(res.ToString());

            return a_list;
        }

        private async Task<List<string>> GetStateNames()
        {
            var builder = new UriBuilder("http://127.0.0.1:5000/api/nomes/estado");
            string url = builder.ToString();

            HttpClient httpClient = new HttpClient();
            var res = await httpClient.GetStringAsync(url);
            List<string> a_list = JsonSerializer.Deserialize<List<string>>(res.ToString());

            return a_list;
        }

        public async Task LoadPage()
        {   
            //Make a request to API, asking for locations.
            //First, get state locations.
            //Get available states from api.
            AvailableStates = await GetStateNames();

            //Get date range from api.
            List<string> dates = await GetDateRange();
            date.StartDate =
                DateTime.ParseExact(dates.ElementAt(0), "yyyy/MM/dd", CultureInfo.InvariantCulture);
            date.EndDate =
                DateTime.ParseExact(dates.ElementAt(1), "yyyy/MM/dd", CultureInfo.InvariantCulture);
        }

        public async Task OnGetAsync()
        {
            await LoadPage();
            RedirectToPage();
        }


        //Here it may contain the data to be displayed.
        public async Task OnPostAsync()
        {
            await LoadPage();
            LocationData ChartLocation = new LocationData();

            ChartLocation.CityName = Location.CityName;
            ChartLocation.StateName = Location.StateName;
            ChartLocation.StartDate = Location.StartDate;
            ChartLocation.EndDate = Location.EndDate;
            ChartLocation.StartDate.ToString();
            ChartLocation.EndDate.ToString();

            var builder = new UriBuilder("http://127.0.0.1:5000/api/casos");
            var query = HttpUtility.ParseQueryString(builder.Query);

            query["state"] = ChartLocation.StateName;
            query["city"] = ChartLocation.CityName;
            query["startdate"] = ChartLocation.StartDate.Date.ToString("yyyy/MM/dd");
            query["enddate"] = ChartLocation.EndDate.Date.ToString("yyyy/MM/dd");

            builder.Query = query.ToString();
            string url = builder.ToString();

            //Here we must wait for API to answer
            HttpClient httpClient = new HttpClient();
            var res = await httpClient.GetStringAsync(url);
            List<int> a_list = JsonSerializer.Deserialize<List<int>>(res.ToString());
            ChartLocation.JsonData = JsonSerializer.Serialize(a_list);
            ChartLocation.maxValue = a_list.Max();
            data_span = Enumerable.Range(0, a_list.Count).ToList();

            //Adding new location to db context.
            _db.LocationDataStorage.Add(ChartLocation);
            await _db.SaveChangesAsync();
            Locations = await _db.LocationDataStorage.AsNoTracking().ToListAsync();
            RedirectToPage();
        }
    }
}
