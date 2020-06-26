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

namespace CoronaStat.Pages
{
    public class StatsModel : PageModel
    {
        private readonly CovidLocationDbContext _db;

        public StatsModel(CovidLocationDbContext _dbContext)
        {
            _db = _dbContext;
        }

        [BindProperty]
        public LocationData Location { get; set; }

        public string testnamestring { get; set; }
        public string teststartstring { get; set; }
        public string testendstring { get; set; }

        public List<LocationData> Locations { get; private set; } = new List<LocationData>();

        public List<int> test_data { get; private set; } = new List<int>();
        public List<int> data_span { get; set; } = new List<int>();

        //Here it may contain the data to be displayed.
        public async Task OnPostAsync()
        {
            LocationData ChartLocation = new LocationData();

            testnamestring = ChartLocation.Name = Location.Name;
            ChartLocation.StartDate = Location.StartDate;
            ChartLocation.EndDate = Location.EndDate;
            teststartstring = ChartLocation.StartDate.ToString();
            testendstring = ChartLocation.EndDate.ToString();

            var builder = new UriBuilder("http://127.0.0.1:5000/api/dados/estado");
            var query = HttpUtility.ParseQueryString(builder.Query);
            query["q"] = ChartLocation.Name;
            query["startdate"] = ChartLocation.StartDate.Date.ToString("yyyy/MM/dd");
            query["enddate"] = ChartLocation.EndDate.Date.ToString("yyyy/MM/dd");
            builder.Query = query.ToString();
            string url = builder.ToString();

            testnamestring = url;

            //Here we must wait for API to answer
            HttpClient httpClient = new HttpClient();
            var res = await httpClient.GetStringAsync(url);
            List<int> a_list = JsonSerializer.Deserialize<List<int>>(res.ToString());
            ChartLocation.JsonData = JsonSerializer.Serialize(a_list);
            data_span = Enumerable.Range(0, a_list.Count).ToList();

            //Adding new location to db context.
            _db.LocationDataStorage.Add(ChartLocation);
            await _db.SaveChangesAsync();
            Locations = await _db.LocationDataStorage.AsNoTracking().ToListAsync();
            RedirectToPage();
        }
    }
}
