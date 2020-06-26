using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace CoronaStat.Models
{
	public class LocationData
	{
		public string Id { get; private set; }
		[Required]
		public string Name { get; set; }

		public DateTime StartDate { get; set; }
		public DateTime EndDate { get; set; }
		//public string ValueType { get; set; } //Obitos, casos recuperados ou casos ativos
		public string JsonData { get; set; }

		public LocationData()
		{
			Id = Guid.NewGuid().ToString();
		}
	}
}
