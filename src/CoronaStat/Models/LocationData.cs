using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace CoronaStat.Models
{
	public class LocationData
	{
		public string Id { get; private set; }
		[Required]
		public string StateName { get; set; }
		public string CityName { get; set; }
		[DataType(DataType.Date)]
		[DisplayFormat(DataFormatString = "{yyyy-MM-dd}")]
		public DateTime StartDate { get; set; }
		[DataType(DataType.Date)]
		[DisplayFormat(DataFormatString = "{yyyy-MM-dd}")]
		public DateTime EndDate { get; set; }
		//public string ValueType { get; set; } //Obitos, casos recuperados ou casos ativos
		public string JsonData { get; set; }
		public int maxValue { get; set; }
			/*
		public List<int> Data { get; set; }
		public string getJsonData()
		{
			return JsonSerializer.Serialize(Data);
		}*/

		public LocationData()
		{
			Id = Guid.NewGuid().ToString();
		}
	}
}
